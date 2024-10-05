
const express = require('express');
const router = express.Router();
const { Pool } = require('pg');
const pool = new Pool();

// Create a new risk item
router.post('/risks', async (req, res) => {
    try {
        const { title, description, level, owner, mitigationPlan } = req.body;
        const result = await pool.query(
            'INSERT INTO risks (title, description, level, owner, mitigation_plan) VALUES ($1, $2, $3, $4, $5) RETURNING *',
            [title, description, level, owner, mitigationPlan]
        );
        res.status(201).json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

// Get all risks
router.get('/risks', async (req, res) => {
    try {
        const result = await pool.query('SELECT * FROM risks');
        res.status(200).json(result.rows);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

// Update a risk item
router.put('/risks/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const { title, description, level, owner, mitigationPlan } = req.body;
        const result = await pool.query(
            'UPDATE risks SET title = $1, description = $2, level = $3, owner = $4, mitigation_plan = $5 WHERE id = $6 RETURNING *',
            [title, description, level, owner, mitigationPlan, id]
        );
        if (result.rows.length === 0) {
            return res.status(404).send('Risk item not found');
        }
        res.status(200).json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

// Delete a risk item
router.delete('/risks/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const result = await pool.query('DELETE FROM risks WHERE id = $1 RETURNING *', [id]);
        if (result.rows.length === 0) {
            return res.status(404).send('Risk item not found');
        }
        res.status(200).json(result.rows[0]);
    } catch (err) {
        console.error(err);
        res.status(500).send('Server error');
    }
});

module.exports = router;
