import os
from typing import Dict, List, Any
import google.generativeai as genai
try:
    from database import VectorDatabase
except ImportError:
    from simple_database import SimpleVectorDatabase as VectorDatabase
from document_processor import DocumentProcessor

class RAGServiceGemini:
    def __init__(self):
        self.db = VectorDatabase()
        self.processor = DocumentProcessor()
        
        # Configure Google Gemini
        api_key = os.getenv("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        
        # Use Gemini 1.5 Flash - fast and cost-effective for RAG
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.resume_path = "../../docs/_data/resume.json"
    
    async def initialize(self):
        await self.db.connect()
    
    async def ingest_all_content(self) -> int:
        # Clear existing chunks
        await self.db.clear_chunks()
        
        # Load and process all content (resume + portfolio)
        chunks = self.processor.chunk_all_content()
        
        # Embed chunks
        embedded_chunks = self.processor.embed_chunks(chunks)
        
        # Store in database
        await self.db.insert_chunks(embedded_chunks)
        
        return len(embedded_chunks)
    
    # Keep backward compatibility
    async def ingest_resume(self) -> int:
        return await self.ingest_all_content()
    
    async def query(self, user_query: str) -> Dict[str, Any]:
        # Embed the query
        query_embedding = self.processor.embed_query(user_query)
        
        # Retrieve relevant chunks (increased for richer context)
        similar_chunks = await self.db.similarity_search(query_embedding, k=5)
        
        # Prepare context for LLM with better labeling
        context_parts = []
        for chunk in similar_chunks:
            content_type = chunk.get('metadata', {}).get('content_type', 'resume')
            section = chunk.get('metadata', {}).get('section', 'general')
            
            if content_type == 'project':
                label = f"Portfolio Project"
            elif content_type == 'blog_post':
                label = f"Blog Article"
            elif content_type == 'about':
                label = f"About Ed"
            elif content_type == 'github_repository':
                repo_name = chunk.get('metadata', {}).get('repo_name', 'Repository')
                label = f"GitHub Repository: {repo_name}"
            else:
                label = f"Resume - {section.title()}"
                
            context_parts.append(f"{label}: {chunk['content']}")
        
        context = "\n\n".join(context_parts)
        
        # Generate response using Gemini
        prompt = f"""You are a knowledgeable assistant helping people learn about Ed Grzetich's professional background and portfolio. You have access to information from his resume, portfolio projects, blog posts, and career experience.

RESPONSE GUIDELINES:
- Provide engaging, conversational responses that tell a story about Ed's work
- Use ONLY the information from the context below - never make up details
- When discussing projects, explain not just what Ed did, but why it mattered and what problems it solved
- Include specific outcomes, metrics, or achievements when available
- Connect different aspects of Ed's experience when relevant (e.g., how his writing skills helped with technical projects)
- If information isn't available in the context, say so politely but suggest what might be found in Ed's portfolio
- Write in a warm, professional tone that reflects Ed's expertise and problem-solving approach

CONTEXT ABOUT ED:
{context}

USER QUESTION: {user_query}

Please provide a thoughtful, informative response:"""
        
        try:
            response = self.model.generate_content(prompt)
            return {
                "answer": response.text,
                "sources": [chunk['content'][:200] + "..." for chunk in similar_chunks]
            }
        except Exception as e:
            # Fallback for testing without API key
            return {
                "answer": f"Mock response based on retrieved context about: {user_query}. Found {len(similar_chunks)} relevant resume sections.",
                "sources": [chunk['content'][:200] + "..." for chunk in similar_chunks]
            }