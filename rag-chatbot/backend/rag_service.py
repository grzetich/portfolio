import os
from typing import Dict, List, Any
from anthropic import AsyncAnthropic
try:
    from database import VectorDatabase
except ImportError:
    from simple_database import SimpleVectorDatabase as VectorDatabase
from document_processor import DocumentProcessor

class RAGService:
    def __init__(self):
        self.db = VectorDatabase()
        self.processor = DocumentProcessor()
        self.anthropic_client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.resume_path = "../../docs/_data/resume.json"
    
    async def initialize(self):
        await self.db.connect()
    
    async def ingest_resume(self) -> int:
        # Clear existing chunks
        await self.db.clear_chunks()
        
        # Load and process resume
        resume_data = self.processor.load_resume_json(self.resume_path)
        chunks = self.processor.chunk_resume(resume_data)
        
        # Embed chunks
        embedded_chunks = self.processor.embed_chunks(chunks)
        
        # Store in database
        await self.db.insert_chunks(embedded_chunks)
        
        return len(embedded_chunks)
    
    async def query(self, user_query: str) -> Dict[str, Any]:
        # Embed the query
        query_embedding = self.processor.embed_query(user_query)
        
        # Retrieve relevant chunks
        similar_chunks = await self.db.similarity_search(query_embedding, k=3)
        
        # Prepare context for LLM
        context = "\n\n".join([
            f"Resume Section: {chunk['content']}"
            for chunk in similar_chunks
        ])
        
        # Generate response using Claude
        prompt = f"""
        You are a helpful assistant that answers questions about Ed Grzetich's resume. 
        Use only the information provided in the resume context below to answer the user's question.
        If the information needed to answer the question is not in the resume context, 
        politely say that the information is not available in the resume.
        
        Resume Context:
        {context}
        
        User Question: {user_query}
        
        Answer:"""
        
        response = await self.anthropic_client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        return {
            "answer": response.content[0].text,
            "sources": [chunk['content'][:200] + "..." for chunk in similar_chunks]
        }