
const express = require('express');
const router = express.Router();
const { Pool } = require('pg');
const pool = new Pool();
const jwt = require('jsonwebtoken');

// Middleware to check authentication and roles
const authenticate = (req, res, next) => {
    const token = req.header('Authorization')?.replace('Bearer ', '');
    if (!token) {
        return res.status(401).send('Access denied. No token provided.');
    }

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded;
        next();
    } catch (err) {
        res.status(400).send('Invalid token.');
    }
};

const authorize = (roles) => (req, res, next) => {
    if (!roles.includes(req.user.role)) {
        return res.status(403).send('Access denied. You do not have the required permissions.');
    }
    next();
};

// Create a new task (restricted to admins and project managers)
router.post('/tasks', authenticate, authorize(['admin', 'project_manager']), async (req, res) => {
    try {
        const { title, description, assignedTo, priority, status } = req.body;
        const result = await pool.query(
            'INSERT INTO tasks (title, description, assigned_to, priority, status) VALUES ($1, $2, $3, $4, $5) RETURNING *',
            [title, description, assignedTo, priority, status]
        );
        res.status(201).json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

// Get all tasks (restricted to authenticated users)
router.get('/tasks', authenticate, async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM tasks');
        res.status(200).json(result.rows);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

// Update a task (restricted to admins and project managers)
router.put('/tasks/:id', authenticate, authorize(['admin', 'project_manager']), async (req, res) => {
    try {
        const { id } = req.params;
        const { title, description, assignedTo, priority, status } = req.body;
        const result = await pool.query(
            'UPDATE tasks SET title = $1, description = $2, assigned_to = $3, priority = $4, status = $5 WHERE id = $6 RETURNING *',
            [title, description, assignedTo, priority, status, id]
        );
        if (result.rows.length === 0) {
            return res.status(404).send('Task not found');
        }
        res.status(200).json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

// Delete a task (restricted to admins only)
router.delete('/tasks/:id', authenticate, authorize(['admin']), async (req, res) => {
    try {
        const { id } = req.params;
        const result = await pool.query('DELETE FROM tasks WHERE id = $1 RETURNING *', [id]);
        if (result.rows.length === 0) {
            return res.status(404).send('Task not found');
        }
        res.status(200).json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

module.exports = router;
