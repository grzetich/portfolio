import os
import json
import re
from typing import List, Dict, Any
from pathlib import Path
import yaml
from github_processor import GitHubProcessor

class PortfolioProcessor:
    """Comprehensive processor for all portfolio content types"""
    
    def __init__(self):
        self.portfolio_root = "../../docs"
        github_token = os.getenv("GITHUB_TOKEN")
        self.github_processor = GitHubProcessor(username="grzetich", github_token=github_token)
        
    def load_markdown_with_frontmatter(self, file_path: str) -> Dict[str, Any]:
        """Load markdown file with YAML frontmatter"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1]) if parts[1].strip() else {}
                markdown_content = parts[2].strip()
            else:
                frontmatter = {}
                markdown_content = content
        else:
            frontmatter = {}
            markdown_content = content
            
        return {
            'frontmatter': frontmatter,
            'content': markdown_content,
            'raw': content
        }
    
    def extract_projects_from_index(self) -> List[Dict[str, Any]]:
        """Extract individual projects from index.md"""
        index_path = os.path.join(self.portfolio_root, "index.md")
        data = self.load_markdown_with_frontmatter(index_path)
        
        projects = []
        content = data['content']
        
        # Split by project-card divs
        project_sections = re.split(r'<div class="project-card"[^>]*>', content)
        
        for i, section in enumerate(project_sections[1:], 1):  # Skip first empty section
            # Extract content until closing div
            project_content = section.split('</div>')[0].strip()
            
            # Extract project title (first ### heading)
            title_match = re.search(r'###\s*(.+)', project_content)
            title = title_match.group(1) if title_match else f"Project {i}"
            
            # Clean up markdown and extract text
            clean_content = re.sub(r'[*_`]', '', project_content)  # Remove markdown formatting
            clean_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', clean_content)  # Convert links to "text (url)"
            clean_content = re.sub(r'\n+', ' ', clean_content)  # Normalize whitespace
            
            projects.append({
                'type': 'project',
                'title': title,
                'content': clean_content,
                'source': 'index.md',
                'metadata': {
                    'section': 'portfolio_projects',
                    'project_index': i
                }
            })
        
        return projects
    
    def load_blog_posts(self) -> List[Dict[str, Any]]:
        """Load all blog posts from _posts directory"""
        posts_dir = os.path.join(self.portfolio_root, "_posts")
        posts = []
        
        if os.path.exists(posts_dir):
            for filename in os.listdir(posts_dir):
                if filename.endswith('.md'):
                    post_path = os.path.join(posts_dir, filename)
                    data = self.load_markdown_with_frontmatter(post_path)
                    
                    # Clean content for better chunking while preserving links
                    clean_content = re.sub(r'[*_`]', '', data['content'])
                    # Convert markdown links to "text (url)" format to preserve both
                    clean_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', clean_content)
                    clean_content = re.sub(r'\n+', ' ', clean_content)
                    
                    posts.append({
                        'type': 'blog_post',
                        'title': data['frontmatter'].get('title', filename),
                        'content': clean_content,
                        'source': filename,
                        'metadata': {
                            'section': 'blog_posts',
                            'date': data['frontmatter'].get('date'),
                            'categories': data['frontmatter'].get('categories', []),
                            'description': data['frontmatter'].get('description', '')
                        }
                    })
        
        return posts
    
    def load_about_page(self) -> Dict[str, Any]:
        """Load about page content"""
        about_path = os.path.join(self.portfolio_root, "about.md")
        data = self.load_markdown_with_frontmatter(about_path)
        
        # Clean content
        clean_content = re.sub(r'[*_`]', '', data['content'])
        clean_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', clean_content)
        clean_content = re.sub(r'<[^>]+>', '', clean_content)  # Remove HTML tags
        clean_content = re.sub(r'\n+', ' ', clean_content)
        
        return {
            'type': 'about',
            'title': 'About Ed Grzetich',
            'content': clean_content,
            'source': 'about.md',
            'metadata': {
                'section': 'about',
                'description': data['frontmatter'].get('description', '')
            }
        }
    
    def chunk_large_content(self, item: Dict[str, Any], max_chunk_size: int = 1500) -> List[Dict[str, Any]]:
        """Split large content into smaller chunks for better retrieval"""
        content = item['content']
        if len(content) <= max_chunk_size:
            return [item]
        
        # Split by sentences for better chunking
        sentences = re.split(r'[.!?]+', content)
        chunks = []
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk + sentence) <= max_chunk_size:
                current_chunk += sentence + ". "
            else:
                if current_chunk.strip():
                    chunk_item = item.copy()
                    chunk_item['content'] = current_chunk.strip()
                    chunk_item['metadata'] = item['metadata'].copy()
                    chunk_item['metadata']['chunk_index'] = len(chunks)
                    chunks.append(chunk_item)
                current_chunk = sentence + ". "
        
        # Add remaining content
        if current_chunk.strip():
            chunk_item = item.copy()
            chunk_item['content'] = current_chunk.strip()
            chunk_item['metadata'] = item['metadata'].copy()
            chunk_item['metadata']['chunk_index'] = len(chunks)
            chunks.append(chunk_item)
        
        return chunks
    
    def load_github_repositories(self) -> List[Dict[str, Any]]:
        """Load GitHub repositories"""
        try:
            return self.github_processor.process_repositories()
        except Exception as e:
            print(f"Error loading GitHub repositories: {e}")
            return []
    
    def load_all_portfolio_content(self, include_github: bool = True) -> List[Dict[str, Any]]:
        """Load and process all portfolio content"""
        all_content = []
        
        # Load projects from index
        projects = self.extract_projects_from_index()
        for project in projects:
            chunks = self.chunk_large_content(project)
            all_content.extend(chunks)
        
        # Load blog posts
        blog_posts = self.load_blog_posts()
        for post in blog_posts:
            chunks = self.chunk_large_content(post)
            all_content.extend(chunks)
        
        # Load about page
        about = self.load_about_page()
        chunks = self.chunk_large_content(about)
        all_content.extend(chunks)
        
        # Load GitHub repositories
        if include_github:
            github_repos = self.load_github_repositories()
            for repo in github_repos:
                chunks = self.chunk_large_content(repo)
                all_content.extend(chunks)
        
        return all_content