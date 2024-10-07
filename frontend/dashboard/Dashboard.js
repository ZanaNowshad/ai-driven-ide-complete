
import React, { useState } from 'react';
import './Dashboard.css';

const Dashboard = () => {
    const [widgets, setWidgets] = useState(["Project Overview", "Quick Actions", "AI Integration Shortcuts"]);

    const addWidget = (widgetName) => {
        setWidgets([...widgets, widgetName]);
    };

    return (
        <div className="dashboard">
            <h1>Dashboard Homepage</h1>
            <div className="widgets">
                {widgets.map((widget, index) => (
                    <div key={index} className="widget">
                        {widget}
                    </div>
                ))}
            </div>
            <button onClick={() => addWidget("New Widget")}>Add Widget</button>
        </div>
    );
};

export default Dashboard;
