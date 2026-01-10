#!/usr/bin/env python3
"""
Simple test script to verify the RAG chatbot works locally with mock responses
"""
import asyncio
import sys
import os
from rag_service import RAGService

async def test_local_rag():
    print("Testing RAG chatbot locally...")
    
    # Create RAG service
    rag = RAGService()
    
    # Initialize (connects to simple database)
    print("Initializing database...")
    await rag.initialize()
    
    # Ingest resume data
    print("Ingesting resume data...")
    chunks_count = await rag.ingest_resume()
    print(f"Successfully ingested {chunks_count} chunks from resume")
    
    # Test queries without calling Anthropic API
    test_queries = [
        "What is Ed's experience with AWS?",
        "Tell me about Ed's education",
        "What companies has Ed worked for?",
        "What is Ed's role at Mastercard?"
    ]
    
    print("\nTesting similarity search (without LLM calls)...")
    for query in test_queries:
        print(f"\nQuery: {query}")
        
        # Just test the embedding and search part
        query_embedding = rag.processor.embed_query(query)
        similar_chunks = await rag.db.similarity_search(query_embedding, k=2)
        
        print(f"Found {len(similar_chunks)} relevant chunks:")
        for i, chunk in enumerate(similar_chunks, 1):
            content_preview = chunk['content'][:150] + "..." if len(chunk['content']) > 150 else chunk['content']
            print(f"   {i}. {content_preview}")
            print(f"      Similarity: {chunk['similarity']:.3f}")
    
    print("\nLocal RAG test completed successfully!")
    print("\nTo test with real Claude API:")
    print("   1. Set ANTHROPIC_API_KEY in .env file")
    print("   2. Use the /chat endpoint via frontend or curl")

if __name__ == "__main__":
    asyncio.run(test_local_rag())