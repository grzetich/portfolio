import numpy as np
import json
import hashlib

class MockEmbeddingModel:
    """Simple mock embedding model for testing without sentence-transformers"""
    
    def __init__(self):
        self.dimension = 384
        np.random.seed(42)  # For reproducible results
    
    def encode(self, texts):
        """Create simple hash-based embeddings"""
        if isinstance(texts, str):
            texts = [texts]
        
        embeddings = []
        for text in texts:
            # Create a simple hash-based embedding
            hash_obj = hashlib.md5(text.lower().encode())
            hash_hex = hash_obj.hexdigest()
            
            # Convert hex to numbers and normalize
            hash_ints = [int(hash_hex[i:i+2], 16) for i in range(0, min(len(hash_hex), 32), 2)]
            
            # Pad or truncate to desired dimension
            if len(hash_ints) < self.dimension:
                hash_ints.extend([0] * (self.dimension - len(hash_ints)))
            else:
                hash_ints = hash_ints[:self.dimension]
            
            # Normalize to unit vector
            embedding = np.array(hash_ints, dtype=float)
            norm = np.linalg.norm(embedding)
            if norm > 0:
                embedding = embedding / norm
            
            embeddings.append(embedding)
        
        return np.array(embeddings)

class SimpleDocumentProcessor:
    def __init__(self):
        self.embedding_model = MockEmbeddingModel()
        self.embedding_dimension = 384
    
    def load_resume_json(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def chunk_resume(self, resume_data):
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
    
    def embed_chunks(self, chunks):
        texts = [chunk['content'] for chunk in chunks]
        embeddings = self.embedding_model.encode(texts)
        
        for i, chunk in enumerate(chunks):
            chunk['embedding'] = embeddings[i].tolist()
        
        return chunks
    
    def embed_query(self, query: str):
        return self.embedding_model.encode([query])[0]