# RAG Resume Chatbot

An interactive chatbot that allows users to ask questions about Ed Grzetich's resume using Retrieval-Augmented Generation (RAG) technology.

## Features

- **Document Ingestion**: Processes resume data from JSON format
- **Vector Search**: Uses pgvector for semantic similarity search
- **AI-Powered Responses**: Leverages Claude 3 Sonnet for natural language generation
- **Web Interface**: Simple, responsive chat interface
- **RESTful API**: FastAPI backend with CORS support

## Architecture

### Backend (FastAPI)
- **Framework**: FastAPI with Python 3.8+
- **Database**: PostgreSQL with pgvector extension
- **Embedding Model**: sentence-transformers (all-MiniLM-L6-v2)
- **LLM**: Claude 3 Sonnet via Anthropic API

### Frontend
- **Technology**: Vanilla HTML, CSS, JavaScript
- **Hosting**: Can be deployed to GitHub Pages
- **Responsive Design**: Mobile-friendly interface

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL with pgvector extension
- Anthropic API key

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd rag-chatbot/backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database URL and Anthropic API key
   ```

5. Run the application:
   ```bash
   python main.py
   ```

### Database Setup

Ensure PostgreSQL is running and create a database with pgvector extension:

```sql
CREATE DATABASE resume_chatbot;
\c resume_chatbot;
CREATE EXTENSION vector;
```

### Frontend Setup

1. Open `rag-chatbot/frontend/index.html` in a web browser, or
2. Serve it using a local web server:
   ```bash
   cd rag-chatbot/frontend
   python -m http.server 8080
   ```

## API Endpoints

- `POST /chat` - Send a message to the chatbot
- `GET /health` - Health check endpoint
- `POST /ingest` - Ingest resume data into the vector database

## Deployment

### Backend (Render)
The backend is designed to be deployed on Render with the following configuration:
- Build Command: `pip install -r requirements.txt`
- Start Command: `python main.py`
- Environment variables: `DATABASE_URL`, `ANTHROPIC_API_KEY`

### Frontend (GitHub Pages)
The frontend can be deployed to GitHub Pages as a static site.

## Usage Examples

Ask questions like:
- "What is Ed's experience with AWS?"
- "Tell me about Ed's role at Mastercard"
- "What technologies has Ed worked with?"
- "What is Ed's educational background?"

## Technical Details

### Document Processing
- Resume data is chunked by sections (contact info, objective, experience, education)
- Each chunk is embedded using sentence-transformers
- Embeddings are stored in PostgreSQL with pgvector

### RAG Pipeline
1. User query is embedded using the same model
2. Similarity search retrieves top-k relevant chunks
3. Context and query are sent to Claude 3 Sonnet
4. Response is generated based only on resume content

## Future Enhancements

- MCP (Model Context Protocol) integration
- Multi-document support
- Automated resume upload interface
- Enhanced conversation history