"""
Utility functions for book processing and embedding generation
"""

import os
import re
import json
import numpy as np
import google.generativeai as genai
from typing import List, Dict, Tuple


def read_markdown_files(book_dir: str = '../book_content') -> List[Dict[str, str]]:
    """
    Read all markdown files from the book_content directory.
    
    Args:
        book_dir (str): Path to the directory containing markdown files
        
    Returns:
        List[Dict]: List of dictionaries with chapter info and content
    """
    chapters = []
    md_files = sorted([f for f in os.listdir(book_dir) if f.endswith('.md')])
    
    for filename in md_files:
        filepath = os.path.join(book_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract chapter number and title
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = match.group(1) if match else filename
        
        chapters.append({
            'filename': filename,
            'title': title,
            'content': content
        })
    
    return chapters


def chunk_text(text: str, chunk_size: int = 600, overlap: int = 100) -> List[str]:
    """
    Split text into overlapping chunks by words.
    
    Args:
        text (str): Text to chunk
        chunk_size (int): Target number of words per chunk
        overlap (int): Number of words to overlap between chunks
        
    Returns:
        List[str]: List of text chunks
    """
    # Clean the text
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    
    words = text.split()
    chunks = []
    
    i = 0
    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunks.append(' '.join(chunk_words))
        i += chunk_size - overlap
        
        if i + chunk_size >= len(words) and i < len(words):
            # Add remaining words as last chunk
            chunks.append(' '.join(words[i:]))
            break
    
    return chunks


def create_embeddings(texts: List[str], api_key: str) -> np.ndarray:
    """
    Generate embeddings for a list of texts using Gemini API.
    
    Args:
        texts (List[str]): List of text chunks to embed
        api_key (str): Gemini API key
        
    Returns:
        np.ndarray: Array of embeddings
    """
    genai.configure(api_key=api_key)
    
    embeddings = []
    for i, text in enumerate(texts):
        print(f"Creating embedding {i+1}/{len(texts)}...")
        
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_document"
        )
        embeddings.append(result['embedding'])
    
    return np.array(embeddings)


def process_book_and_create_embeddings(
    book_dir: str = '../book_content',
    output_dir: str = '.',
    chunk_size: int = 600,
    overlap: int = 100
) -> Tuple[np.ndarray, List[Dict]]:
    """
    Process entire book: read, chunk, and create embeddings.
    
    Args:
        book_dir (str): Directory containing markdown files
        output_dir (str): Directory to save embeddings and metadata
        chunk_size (int): Words per chunk
        overlap (int): Overlapping words between chunks
        
    Returns:
        Tuple[np.ndarray, List[Dict]]: Embeddings array and metadata list
    """
    print("=" * 80)
    print("PROCESSING BOOK AND CREATING EMBEDDINGS")
    print("=" * 80)
    
    # Read all chapters
    print("\n1. Reading markdown files...")
    chapters = read_markdown_files(book_dir)
    print(f"   Found {len(chapters)} chapters")
    
    # Chunk all content
    print("\n2. Chunking content...")
    all_chunks = []
    metadata = []
    
    for chapter in chapters:
        chunks = chunk_text(chapter['content'], chunk_size, overlap)
        print(f"   {chapter['title']}: {len(chunks)} chunks")
        
        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            metadata.append({
                'chunk_id': len(all_chunks) - 1,
                'chapter': chapter['title'],
                'filename': chapter['filename'],
                'chunk_index': i,
                'content': chunk
            })
    
    print(f"\n   Total chunks: {len(all_chunks)}")
    
    # Create embeddings
    print("\n3. Creating embeddings with Gemini...")
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment")
    
    embeddings = create_embeddings(all_chunks, api_key)
    
    # Save to disk
    print("\n4. Saving to disk...")
    embeddings_path = os.path.join(output_dir, 'embeddings.npy')
    metadata_path = os.path.join(output_dir, 'metadata.json')
    
    np.save(embeddings_path, embeddings)
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"   Embeddings saved to: {embeddings_path}")
    print(f"   Metadata saved to: {metadata_path}")
    print("\n✅ Processing complete!")
    
    return embeddings, metadata
