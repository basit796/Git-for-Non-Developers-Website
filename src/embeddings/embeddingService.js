// Simple embedding service using text similarity
// In a production environment, you would use actual embeddings with OpenAI or similar services

const gitKnowledge = require('./gitKnowledge');

class EmbeddingService {
    constructor() {
        this.knowledge = gitKnowledge;
    }

    // Simple keyword-based similarity (cosine similarity would be used with real embeddings)
    calculateSimilarity(query, content) {
        const queryWords = query.toLowerCase().split(/\s+/);
        const contentWords = content.toLowerCase().split(/\s+/);
        
        let matches = 0;
        queryWords.forEach(word => {
            if (contentWords.includes(word)) {
                matches++;
            }
        });
        
        return matches / Math.max(queryWords.length, 1);
    }

    // Find relevant context based on user query
    findRelevantContext(query, topK = 3) {
        // Calculate similarity scores for all knowledge items
        const scoredItems = this.knowledge.map(item => ({
            ...item,
            score: this.calculateSimilarity(query, item.topic + ' ' + item.content)
        }));

        // Sort by score and return top K results
        const topResults = scoredItems
            .sort((a, b) => b.score - a.score)
            .slice(0, topK);

        // Only return items with meaningful similarity
        return topResults.filter(item => item.score > 0);
    }

    // Get context string to provide to the agent
    getContextForQuery(query) {
        const relevantItems = this.findRelevantContext(query);
        
        if (relevantItems.length === 0) {
            return "No specific context found. Provide a general helpful response about Git.";
        }

        let context = "Relevant information from knowledge base:\n\n";
        relevantItems.forEach((item, index) => {
            context += `${index + 1}. ${item.topic}:\n${item.content}\n\n`;
        });

        return context;
    }

    // Get all knowledge items (for testing/admin purposes)
    getAllKnowledge() {
        return this.knowledge;
    }
}

module.exports = EmbeddingService;
