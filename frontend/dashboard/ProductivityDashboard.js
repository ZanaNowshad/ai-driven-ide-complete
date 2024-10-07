
import React, { useState, useEffect } from 'react';
import './Dashboard.css';

const ProductivityDashboard = () => {
    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        // Fetch productivity metrics from the backend AI
        async function fetchMetrics() {
            const response = await fetch('/api/productivity_metrics');
            const data = await response.json();
            setMetrics(data.metrics);
        }
        fetchMetrics();
    }, []);

    return (
        <div className="dashboard">
            <h1>Productivity Dashboard</h1>
            <div className="metrics">
                {metrics.map((metric, index) => (
                    <div key={index} className="metric">
                        <h2>{metric.title}</h2>
                        <p>{metric.value}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ProductivityDashboard;
