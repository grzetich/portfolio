import requests
import base64
import re
from typing import List, Dict, Any, Optional
import time

class GitHubProcessor:
    """Process GitHub repositories to extract project information"""
    
    def __init__(self, username: str = "grzetich", github_token: Optional[str] = None):
        self.username = username
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": f"RAG-Portfolio-Bot-{username}"
        }
        
        # Add authentication if token provided
        if github_token:
            self.headers["Authorization"] = f"token {github_token}"
            
        # Rate limiting
        self.last_request = 0
        self.min_interval = 1  # Minimum seconds between requests
    
    def _make_request(self, url: str) -> Optional[Dict]:
        """Make rate-limited GitHub API request"""
        # Simple rate limiting
        current_time = time.time()
        time_since_last = current_time - self.last_request
        if time_since_last < self.min_interval:
            time.sleep(self.min_interval - time_since_last)
        
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            self.last_request = time.time()
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"GitHub API: Resource not found - {url}")
                return None
            elif response.status_code == 403:
                print(f"GitHub API: Rate limited or forbidden - {url}")
                return None
            else:
                print(f"GitHub API: Error {response.status_code} - {url}")
                return None
                
        except requests.RequestException as e:
            print(f"GitHub API: Request failed - {e}")
            return None
    
    def get_specific_repository(self, repo_name: str) -> Optional[Dict[str, Any]]:
        """Fetch a specific repository by name"""
        url = f"{self.base_url}/repos/{self.username}/{repo_name}"
        repo_data = self._make_request(url)
        return repo_data

    def get_repositories(self, include_forks: bool = False) -> List[Dict[str, Any]]:
        """Fetch user's repositories"""
        url = f"{self.base_url}/users/{self.username}/repos"
        params = "?sort=updated&per_page=50"
        
        repos_data = self._make_request(f"{url}{params}")
        if not repos_data:
            return []
        
        repos = []
        for repo in repos_data:
            # Skip forks unless requested
            if repo.get('fork') and not include_forks:
                continue
                
            # Skip if no description and no README
            if not repo.get('description') and not repo.get('has_wiki'):
                continue
            
            repos.append({
                'name': repo['name'],
                'full_name': repo['full_name'],
                'description': repo.get('description', ''),
                'html_url': repo['html_url'],
                'language': repo.get('language'),
                'languages_url': repo['languages_url'],
                'topics': repo.get('topics', []),
                'created_at': repo['created_at'],
                'updated_at': repo['updated_at'],
                'size': repo['size'],
                'stargazers_count': repo['stargazers_count'],
                'forks_count': repo['forks_count'],
                'default_branch': repo['default_branch']
            })
        
        return repos
    
    def get_repository_languages(self, repo_full_name: str) -> Dict[str, int]:
        """Get languages used in a repository"""
        url = f"{self.base_url}/repos/{repo_full_name}/languages"
        languages_data = self._make_request(url)
        return languages_data or {}
    
    def get_readme_content(self, repo_full_name: str) -> Optional[str]:
        """Fetch README content from repository"""
        # Try common README filenames
        readme_files = ['README.md', 'README.rst', 'README.txt', 'README']
        
        for filename in readme_files:
            url = f"{self.base_url}/repos/{repo_full_name}/contents/{filename}"
            content_data = self._make_request(url)
            
            if content_data and content_data.get('content'):
                try:
                    # Decode base64 content
                    content = base64.b64decode(content_data['content']).decode('utf-8')
                    return content
                except Exception as e:
                    print(f"Error decoding README for {repo_full_name}: {e}")
                    continue
        
        return None
    
    def process_readme_content(self, readme_content: str) -> str:
        """Clean and process README content for RAG ingestion"""
        if not readme_content:
            return ""
        
        # Remove excessive whitespace and normalize
        content = re.sub(r'\n{3,}', '\n\n', readme_content)
        
        # Convert markdown headers to simple text
        content = re.sub(r'^#{1,6}\s*(.+)$', r'\1:', content, flags=re.MULTILINE)
        
        # Preserve markdown links in "text (url)" format
        content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', content)
        
        # Remove code blocks but preserve inline code context
        content = re.sub(r'```[\s\S]*?```', '[Code example omitted]', content)
        content = re.sub(r'`([^`]+)`', r'"\1"', content)
        
        # Clean up extra whitespace
        content = re.sub(r'\s+', ' ', content)
        content = content.strip()
        
        return content
    
    def process_repositories(self) -> List[Dict[str, Any]]:
        """Process all repositories into RAG-ready format"""
        repos = self.get_repositories()
        
        # Add specific repository if not already included
        amplify_repo = self.get_specific_repository("amplify-ui-help-panel")
        if amplify_repo:
            # Check if it's already in repos list
            repo_names = [r['name'] for r in repos]
            if 'amplify-ui-help-panel' not in repo_names:
                repos.append({
                    'name': amplify_repo['name'],
                    'full_name': amplify_repo['full_name'],
                    'description': amplify_repo.get('description', ''),
                    'html_url': amplify_repo['html_url'],
                    'language': amplify_repo.get('language'),
                    'languages_url': amplify_repo['languages_url'],
                    'topics': amplify_repo.get('topics', []),
                    'created_at': amplify_repo['created_at'],
                    'updated_at': amplify_repo['updated_at'],
                    'size': amplify_repo['size'],
                    'stargazers_count': amplify_repo['stargazers_count'],
                    'forks_count': amplify_repo['forks_count'],
                    'default_branch': amplify_repo['default_branch']
                })
        
        processed_repos = []
        
        print(f"Processing {len(repos)} repositories for {self.username}...")
        
        for repo in repos:
            print(f"Processing: {repo['name']}")
            
            # Get languages
            languages = self.get_repository_languages(repo['full_name'])
            
            # Get README
            readme_content = self.get_readme_content(repo['full_name'])
            processed_readme = self.process_readme_content(readme_content) if readme_content else ""
            
            # Combine description and README
            full_description = []
            if repo['description']:
                full_description.append(f"Description: {repo['description']}")
            
            if processed_readme:
                full_description.append(f"Documentation: {processed_readme}")
            
            # Add technical details
            tech_details = []
            if repo['language']:
                tech_details.append(f"Primary language: {repo['language']}")
            
            if languages:
                lang_list = list(languages.keys())
                if len(lang_list) > 1:
                    tech_details.append(f"Technologies used: {', '.join(lang_list)}")
            
            if repo['topics']:
                tech_details.append(f"Topics: {', '.join(repo['topics'])}")
            
            if tech_details:
                full_description.append("Technical details: " + "; ".join(tech_details))
            
            # Create repository entry
            repo_content = {
                'type': 'github_repository',
                'title': f"GitHub Repository: {repo['name']}",
                'content': " | ".join(full_description) if full_description else f"Repository: {repo['name']}",
                'source': f"github:{repo['full_name']}",
                'metadata': {
                    'section': 'github_repositories',
                    'repo_name': repo['name'],
                    'repo_url': repo['html_url'],
                    'language': repo['language'],
                    'languages': list(languages.keys()),
                    'topics': repo['topics'],
                    'stars': repo['stargazers_count'],
                    'updated_at': repo['updated_at']
                }
            }
            
            processed_repos.append(repo_content)
        
        print(f"Successfully processed {len(processed_repos)} repositories")
        return processed_repos