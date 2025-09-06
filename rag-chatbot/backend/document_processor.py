import json
from typing import List, Dict, Any
import numpy as np
from pathlib import Path
from portfolio_processor import PortfolioProcessor
try:
    from sentence_transformers import SentenceTransformer
    USE_REAL_EMBEDDINGS = True
except ImportError:
    from mock_embeddings import MockEmbeddingModel
    USE_REAL_EMBEDDINGS = False

class DocumentProcessor:
    def __init__(self):
        if USE_REAL_EMBEDDINGS:
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        else:
            self.embedding_model = MockEmbeddingModel()
        self.embedding_dimension = 384
        self.portfolio_processor = PortfolioProcessor()
    
    def load_resume_json(self, file_path: str) -> Dict[str, Any]:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def chunk_resume(self, resume_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        chunks = []
        
        # Process contact info
        if 'contactinfo' in resume_data:
            contact = resume_data['contactinfo']
            contact_text = f"""
            Contact Information:
            Name: {contact.get('name', {}).get('first', '')} {contact.get('name', {}).get('last', '')}
            Email: {contact.get('email', '')}
            Location: {contact.get('city', '')}, {contact.get('state', '')}
            Phone: {contact.get('phonenumber', '')}
            Website: {contact.get('url', '')}
            """.strip()
            
            chunks.append({
                'content': contact_text,
                'metadata': {'section': 'contact_info'}
            })
        
        # Process objective
        if 'objective' in resume_data:
            objective_text = f"Professional Objective: {resume_data['objective']}"
            chunks.append({
                'content': objective_text,
                'metadata': {'section': 'objective'}
            })
        
        # Process experience
        if 'experience' in resume_data:
            for i, exp in enumerate(resume_data['experience']):
                exp_text = f"""
                Work Experience at {exp.get('company', 'Unknown Company')}:
                Title: {exp.get('title', 'Unknown Title')}
                Duration: {exp.get('date_start', 'Unknown')} - {exp.get('date_end', 'Present')}
                Responsibilities: {exp.get('duties', 'No description available')}
                """.strip()
                
                chunks.append({
                    'content': exp_text,
                    'metadata': {
                        'section': 'experience',
                        'company': exp.get('company', ''),
                        'title': exp.get('title', ''),
                        'index': i
                    }
                })
        
        # Process education
        if 'education' in resume_data:
            edu = resume_data['education']
            edu_text = f"""
            Education:
            School: {edu.get('school', 'Unknown School')}
            Degree: {edu.get('degree', 'Unknown Degree')}
            """.strip()
            
            chunks.append({
                'content': edu_text,
                'metadata': {'section': 'education'}
            })
        
        return chunks
    
    def chunk_all_content(self) -> List[Dict[str, Any]]:
        """Process both resume and portfolio content into chunks"""
        all_chunks = []
        
        # Load and chunk resume data
        resume_data = self.load_resume_json("../../docs/_data/resume.json")
        resume_chunks = self.chunk_resume(resume_data)
        all_chunks.extend(resume_chunks)
        
        # Load and chunk portfolio content
        portfolio_content = self.portfolio_processor.load_all_portfolio_content()
        
        # Convert portfolio content to the same format as resume chunks
        for item in portfolio_content:
            chunk = {
                'content': f"{item['title']}: {item['content']}" if item.get('title') else item['content'],
                'metadata': {
                    'section': item['metadata']['section'],
                    'content_type': item['type'],
                    'source': item['source'],
                    **item['metadata']
                }
            }
            all_chunks.append(chunk)
        
        return all_chunks
    
    def embed_chunks(self, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        texts = [chunk['content'] for chunk in chunks]
        embeddings = self.embedding_model.encode(texts)
        
        for i, chunk in enumerate(chunks):
            chunk['embedding'] = embeddings[i].tolist()
        
        return chunks
    
    def embed_query(self, query: str) -> np.ndarray:
        return self.embedding_model.encode([query])[0]