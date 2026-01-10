import asyncpg
import os
from typing import List, Dict, Any
import numpy as np
from pgvector.asyncpg import register_vector

class VectorDatabase:
    def __init__(self):
        self.pool = None
        self.database_url = os.getenv("DATABASE_URL")
    
    async def connect(self):
        self.pool = await asyncpg.create_pool(self.database_url)
        
        async with self.pool.acquire() as conn:
            await register_vector(conn)
            
            await conn.execute("""
                CREATE EXTENSION IF NOT EXISTS vector;
            """)
            
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS resume_chunks (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    embedding VECTOR(384),
                    metadata JSONB,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)
            
            await conn.execute("""
                CREATE INDEX IF NOT EXISTS resume_chunks_embedding_idx 
                ON resume_chunks USING ivfflat (embedding vector_cosine_ops)
                WITH (lists = 100);
            """)
    
    async def insert_chunks(self, chunks: List[Dict[str, Any]]):
        if not self.pool:
            await self.connect()
        
        async with self.pool.acquire() as conn:
            await conn.executemany("""
                INSERT INTO resume_chunks (content, embedding, metadata) 
                VALUES ($1, $2, $3)
            """, [
                (chunk['content'], chunk['embedding'], chunk.get('metadata', {}))
                for chunk in chunks
            ])
    
    async def similarity_search(self, query_embedding: np.ndarray, k: int = 5) -> List[Dict[str, Any]]:
        if not self.pool:
            await self.connect()
        
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("""
                SELECT content, metadata, 1 - (embedding <=> $1) as similarity
                FROM resume_chunks
                ORDER BY embedding <=> $1
                LIMIT $2
            """, query_embedding, k)
        
        return [
            {
                'content': row['content'],
                'metadata': row['metadata'],
                'similarity': row['similarity']
            }
            for row in rows
        ]
    
    async def clear_chunks(self):
        if not self.pool:
            await self.connect()
        
        async with self.pool.acquire() as conn:
            await conn.execute("DELETE FROM resume_chunks")
    
    async def close(self):
        if self.pool:
            await self.pool.close()