"""
Script to generate embeddings from book content.
Run this once to create embeddings.npy and metadata.json files.
"""

import os
from dotenv import load_dotenv
from utils import process_book_and_create_embeddings

# Load environment variables
load_dotenv()

if __name__ == '__main__':
    try:
        # Process book and create embeddings
        embeddings, metadata = process_book_and_create_embeddings(
            book_dir='../book_content',
            output_dir='.',
            chunk_size=600,  # ~600 words per chunk
            overlap=100      # 100 words overlap
        )
        
        print(f"\n📊 Summary:")
        print(f"   - Total chunks: {len(metadata)}")
        print(f"   - Embedding dimensions: {embeddings.shape}")
        print(f"   - Files created: embeddings.npy, metadata.json")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
