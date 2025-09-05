from typing import List, Dict, Any
import numpy as np
import json

class SimpleVectorDatabase:
    def __init__(self):
        self.chunks = []
    
    async def connect(self):
        pass
    
    async def insert_chunks(self, chunks: List[Dict[str, Any]]):
        self.chunks.extend(chunks)
    
    async def similarity_search(self, query_embedding: np.ndarray, k: int = 5) -> List[Dict[str, Any]]:
        if not self.chunks:
            return []
        
        similarities = []
        for chunk in self.chunks:
            chunk_embedding = np.array(chunk['embedding'])
            similarity = np.dot(query_embedding, chunk_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(chunk_embedding)
            )
            similarities.append({
                'content': chunk['content'],
                'metadata': chunk.get('metadata', {}),
                'similarity': float(similarity)
            })
        
        similarities.sort(key=lambda x: x['similarity'], reverse=True)
        return similarities[:k]
    
    async def clear_chunks(self):
        self.chunks.clear()
    
    async def close(self):
        pass