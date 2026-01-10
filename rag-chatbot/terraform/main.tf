terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.0"
    }
  }
}

provider "render" {}

# PostgreSQL Database
resource "render_postgres" "resume_chatbot_db" {
  name   = "resume-chatbot-db"
  plan   = "free"
  region = "oregon"
}

# Web Service
resource "render_web_service" "resume_chatbot_api" {
  name = "resume-chatbot-api"
  plan = "free"
  
  runtime = "python3"
  
  github_repo = {
    repo_url = "https://github.com/your-username/your-repo"
    branch   = "main"
  }
  
  root_directory = "rag-chatbot/backend"
  
  build_command = "pip install -r requirements.txt"
  start_command = "python main.py"
  
  environment_variables = {
    DATABASE_URL      = render_postgres.resume_chatbot_db.internal_connection_string
    ANTHROPIC_API_KEY = var.anthropic_api_key
  }
  
  disk_size_gb = 1
}

# Variable for API key
variable "anthropic_api_key" {
  description = "Anthropic API key for Claude access"
  type        = string
  sensitive   = true
}

# Outputs
output "database_url" {
  value     = render_postgres.resume_chatbot_db.external_connection_string
  sensitive = true
}

output "web_service_url" {
  value = render_web_service.resume_chatbot_api.url
}