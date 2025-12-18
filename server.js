// Main server file
const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const agentRoutes = require('./src/routes/agentRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from public directory
app.use(express.static(path.join(__dirname, 'public')));

// API routes
app.use('/api', agentRoutes);

// Serve index.html for root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// 404 handler
app.use((req, res) => {
    res.status(404).json({
        success: false,
        error: 'Route not found'
    });
});

// Error handler
app.use((err, req, res, next) => {
    console.error('Server error:', err);
    res.status(500).json({
        success: false,
        error: 'Internal server error',
        message: err.message
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`
🚀 Git for Non-Developers Website is running!
📍 Server: http://localhost:${PORT}
🤖 Agent API: http://localhost:${PORT}/api/agent
📚 Topics: http://localhost:${PORT}/api/topics
💚 Health: http://localhost:${PORT}/api/health
    `);
});

module.exports = app;
