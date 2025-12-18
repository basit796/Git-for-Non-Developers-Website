// Simple embedding service using text similarity
// In a production environment, you would use actual embeddings with OpenAI or similar services

const gitKnowledge = require('./gitKnowledge');

class EmbeddingService {
    constructor() {
        this.knowledge = gitKnowledge;
    }

    // Simple keyword-based similarity using Jaccard similarity coefficient
    calculateSimilarity(query, content) {
        const queryWords = new Set(query.toLowerCase().split(/\s+/).filter(w => w.length > 0));
        const contentWords = new Set(content.toLowerCase().split(/\s+/).filter(w => w.length > 0));
        
        // Calculate intersection and union
        const intersection = new Set([...queryWords].filter(word => contentWords.has(word)));
        const union = new Set([...queryWords, ...contentWords]);
        
        // Jaccard similarity: |intersection| / |union|
        return union.size > 0 ? intersection.size / union.size : 0;
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

    // Get structured context data to provide to the agent
    getContextForQuery(query) {
        const relevantItems = this.findRelevantContext(query);
        
        if (relevantItems.length === 0) {
            return {
                hasContext: false,
                items: []
            };
        }

        return {
            hasContext: true,
            items: relevantItems.map(item => ({
                topic: item.topic,
                content: item.content,
                score: item.score
            }))
        };
    }

    // Get all knowledge items (for testing/admin purposes)
    getAllKnowledge() {
        return this.knowledge;
    }
}

module.exports = EmbeddingService;
