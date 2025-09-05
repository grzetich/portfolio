#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from document_processor import DocumentProcessor
from simple_database import SimpleVectorDatabase
import json
import asyncio

async def test_basic_functionality():
    print("Testing basic RAG functionality...")
    
    # Initialize components
    processor = DocumentProcessor()
    db = SimpleVectorDatabase()
    
    print("✓ Components initialized")
    
    # Load resume data
    try:
        resume_data = processor.load_resume_json("../../docs/_data/resume.json")
        print("✓ Resume data loaded")
        print(f"  - Contact: {resume_data['contactinfo']['name']['first']} {resume_data['contactinfo']['name']['last']}")
        print(f"  - Experience entries: {len(resume_data['experience'])}")
    except Exception as e:
        print(f"✗ Failed to load resume: {e}")
        return
    
    # Chunk the resume
    try:
        chunks = processor.chunk_resume(resume_data)
        print(f"✓ Resume chunked into {len(chunks)} pieces")
        for i, chunk in enumerate(chunks[:3]):
            print(f"  - Chunk {i+1}: {chunk['content'][:100]}...")
    except Exception as e:
        print(f"✗ Failed to chunk resume: {e}")
        return
    
    # Embed chunks
    try:
        print("Embedding chunks (this may take a moment)...")
        embedded_chunks = processor.embed_chunks(chunks)
        print(f"✓ {len(embedded_chunks)} chunks embedded")
        print(f"  - Embedding dimension: {len(embedded_chunks[0]['embedding'])}")
    except Exception as e:
        print(f"✗ Failed to embed chunks: {e}")
        return
    
    # Store in database
    try:
        await db.connect()
        await db.insert_chunks(embedded_chunks)
        print("✓ Chunks stored in database")
    except Exception as e:
        print(f"✗ Failed to store chunks: {e}")
        return
    
    # Test query
    try:
        test_queries = [
            "What is Ed's experience with AWS?",
            "Tell me about Ed's education",
            "What companies has Ed worked for?"
        ]
        
        for query in test_queries:
            print(f"\nTesting query: '{query}'")
            query_embedding = processor.embed_query(query)
            results = await db.similarity_search(query_embedding, k=2)
            
            print(f"  Found {len(results)} relevant chunks:")
            for i, result in enumerate(results):
                print(f"    {i+1}. Similarity: {result['similarity']:.3f}")
                print(f"       Content: {result['content'][:100]}...")
                
    except Exception as e:
        print(f"✗ Failed to test queries: {e}")
        return
    
    print("\n🎉 Basic RAG functionality test completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_basic_functionality())