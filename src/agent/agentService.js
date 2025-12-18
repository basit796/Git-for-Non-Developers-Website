// Agent service that processes user queries with context from embeddings
const EmbeddingService = require('../embeddings/embeddingService');

class AgentService {
    constructor() {
        this.embeddingService = new EmbeddingService();
    }

    // Generate a response based on user query and context
    async generateResponse(query) {
        try {
            // Get relevant context from embeddings
            const context = this.embeddingService.getContextForQuery(query);
            
            // For demo purposes, we'll create a simple rule-based response system
            // In production, this would call an AI service like OpenAI with the context
            const response = this.createContextualResponse(query, context);
            
            return {
                success: true,
                response: response,
                context: context
            };
        } catch (error) {
            console.error('Error generating response:', error);
            return {
                success: false,
                response: "I'm sorry, I encountered an error processing your question. Please try again.",
                error: error.message
            };
        }
    }

    // Create a contextual response based on query and retrieved context
    createContextualResponse(query, contextData) {
        const queryLower = query.toLowerCase();
        
        // Check if we have relevant context
        if (!contextData.hasContext || contextData.items.length === 0) {
            return this.generateGeneralResponse(query);
        }

        // Build response from the most relevant sections
        let response = "";
        
        if (contextData.items.length >= 1) {
            const firstItem = contextData.items[0];
            response += firstItem.content;
        }
        
        if (contextData.items.length >= 2) {
            const secondItem = contextData.items[1];
            response += "\n\n" + secondItem.content;
        }
        
        response += "\n\nIs there anything specific about this you'd like me to explain further?";
        
        return response;
    }

    // Generate general response when no specific context is found
    generateGeneralResponse(query) {
        const queryLower = query.toLowerCase();
        
        // Basic keyword matching for common questions
        if (queryLower.includes('help') || queryLower.includes('start')) {
            return "I'm here to help you learn Git! You can ask me about:\n\n" +
                   "- Basic concepts (repository, commit, branch)\n" +
                   "- Common commands (add, commit, push, pull)\n" +
                   "- Workflows (branching, merging)\n" +
                   "- Best practices\n\n" +
                   "What would you like to learn about?";
        }
        
        if (queryLower.includes('thank')) {
            return "You're welcome! Feel free to ask if you have more questions about Git. I'm here to help!";
        }
        
        return "I understand you're asking about Git, but I don't have specific information about that topic in my knowledge base. " +
               "Could you rephrase your question or ask about basic Git concepts like commits, branches, or repositories?";
    }

    // Get all available topics (for reference)
    getAvailableTopics() {
        return this.embeddingService.getAllKnowledge().map(item => item.topic);
    }
}

module.exports = AgentService;
