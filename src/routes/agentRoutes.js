// API routes for the agent
const express = require('express');
const AgentService = require('../agent/agentService');

const router = express.Router();
const agentService = new AgentService();

// POST /api/agent - Handle user queries
router.post('/agent', async (req, res) => {
    try {
        const { query } = req.body;
        
        if (!query || typeof query !== 'string' || query.trim().length === 0) {
            return res.status(400).json({
                success: false,
                error: 'Query is required and must be a non-empty string'
            });
        }

        // Generate response using the agent
        const result = await agentService.generateResponse(query);
        
        res.json({
            success: result.success,
            response: result.response,
            timestamp: new Date().toISOString()
        });
        
    } catch (error) {
        console.error('Error in agent route:', error);
        res.status(500).json({
            success: false,
            error: 'Internal server error',
            message: error.message
        });
    }
});

// GET /api/topics - Get available topics (for reference)
router.get('/topics', (req, res) => {
    try {
        const topics = agentService.getAvailableTopics();
        res.json({
            success: true,
            topics: topics,
            count: topics.length
        });
    } catch (error) {
        console.error('Error getting topics:', error);
        res.status(500).json({
            success: false,
            error: 'Internal server error'
        });
    }
});

// GET /api/health - Health check
router.get('/health', (req, res) => {
    res.json({
        success: true,
        status: 'healthy',
        timestamp: new Date().toISOString()
    });
});

module.exports = router;
