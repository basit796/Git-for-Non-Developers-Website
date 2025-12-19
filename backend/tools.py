"""
Tools for Git Book ADK Agent
Contains all tool functions for RAG search and book content retrieval
"""

import numpy as np
import json
from typing import List, Dict, Any
import google.generativeai as genai
import os


def search_book_content(query: str) -> str:
    """
    Search the book content using RAG (Retrieval Augmented Generation).
    This tool finds relevant book chunks based on user query using semantic search.
    
    Args:
        query (str): User's question or search query
        
    Returns:
        str: Relevant book content chunks with metadata
    """
    try:
        # Load embeddings and metadata
        embeddings = np.load('embeddings.npy')
        with open('metadata.json', 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Configure Gemini API
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        
        # Generate query embedding using Gemini
        query_embedding = genai.embed_content(
            model="models/text-embedding-004",
            content=query,
            task_type="retrieval_query"
        )['embedding']
        
        # Calculate cosine similarity
        query_vec = np.array(query_embedding)
        similarities = np.dot(embeddings, query_vec) / (
            np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_vec)
        )
        
        # Get top 3 most relevant chunks
        top_indices = np.argsort(similarities)[-3:][::-1]
        
        # Build context from top chunks
        context_parts = []
        for idx in top_indices:
            chunk_meta = metadata[int(idx)]
            context_parts.append(
                f"[Chapter: {chunk_meta['chapter']}]\n{chunk_meta['content']}\n"
            )
        
        return "\n---\n".join(context_parts)
        
    except FileNotFoundError:
        return "Error: Embeddings not found. Please run the embedding creation script first."
    except Exception as e:
        return f"Error searching book content: {str(e)}"


def get_chapter_list() -> str:
    """
    Get a list of all available chapters in the book.
    
    Returns:
        str: Formatted list of chapters
    """
    chapters = [
        "Chapter 1: The Chaos of 'Final_v2_REAL.docx'",
        "Chapter 2: The Anatomy of Git",
        "Chapter 3: Your First Time Machine",
        "Chapter 4: Branching: Parallel Universes",
        "Chapter 5: The Cloud: GitHub & Beyond",
        "Chapter 6: Git in the Real World"
    ]
    return "\n".join(f"{i+1}. {ch}" for i, ch in enumerate(chapters))


# Tool declarations for ADK Agent
TOOLS = [
    {
        "name": "search_book_content",
        "description": "Search the Git book content using semantic search. Use this when user asks questions about Git, version control, GitHub, or any topic covered in the book.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The user's question or search query"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "get_chapter_list",
        "description": "Get a list of all chapters in the book. Use this when user asks about book structure or wants to know what topics are covered.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
]


# Tool function mapping
TOOL_FUNCTIONS = {
    "search_book_content": search_book_content,
    "get_chapter_list": get_chapter_list
}
