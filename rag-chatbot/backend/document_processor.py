import json
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
import numpy as np
from pathlib import Path

class DocumentProcessor:
    def __init__(self):
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embedding_dimension = 384
    
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
    
    def embed_chunks(self, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        texts = [chunk['content'] for chunk in chunks]
        embeddings = self.embedding_model.encode(texts)
        
        for i, chunk in enumerate(chunks):
            chunk['embedding'] = embeddings[i].tolist()
        
        return chunks
    
    def embed_query(self, query: str) -> np.ndarray:
        return self.embedding_model.encode([query])[0]