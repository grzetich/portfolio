Resume API interface

Construct an API interface to run on GitHub Pages taking in _data/resume.json as the input and providing sample functionality like in _includes/api_demo.html. 

Example backend code:
``
resume_api.py - A Flask API to serve resume data, fetched from GitHub

from flask import Flask, jsonify, request
import requests # Import the requests library
import os # For environment variables, good practice for URLs
from flask_cors import CORS # Import Flask-CORS

app = Flask(__name__)
CORS(app) # Enable CORS for your Flask app. IMPORTANT for frontend!

# --- Configuration ---
# IMPORTANT: Replace this with the actual raw URL from your GitHub repo!
# Example: "https://https://raw.githubusercontent.com/Grzetich/portfolio/main/resume.json"
# It's even better practice to use environment variables for sensitive or changing URLs.
GITHUB_RESUME_URL = os.environ.get(
    "GITHUB_RESUME_URL", 
    "YOUR_RAW_GITHUB_RESUME_JSON_URL_HERE" # <--- REPLACE THIS PLACEHOLDER!
)

# --- Global variable to store resume data after fetching ---
resume_data = None

# --- Function to load resume data from GitHub ---
def load_resume_data():
    global resume_data # Declare that we are modifying the global variable
    try:
        response = requests.get(GITHUB_RESUME_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        resume_data = response.json()
        print("Resume data loaded successfully from GitHub!")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching resume data from GitHub: {e}")
        resume_data = {"error": "Failed to load resume data from external source."}
    except ValueError as e: # Catch JSON decoding errors
        print(f"Error decoding JSON from GitHub response: {e}")
        resume_data = {"error": "Invalid JSON data from external source."}

# --- Load data when the app starts ---
load_resume_data()

# --- API Endpoints ---

@app.route('/')
def home():
    """
    Root endpoint: Provides a simple welcome message and instructions.
    """
    if resume_data and "error" not in resume_data:
        return jsonify({
            "message": "Welcome to Ed Grzetich's Resume API!",
            "status": "Resume data loaded.",
            "endpoints": {
                "/resume": "Get the full resume.",
                "/resume/contact": "Get contact information.",
                "/resume/objective": "Get the objective statement.",
                "/resume/experience": "Get all experience entries.",
                "/resume/experience/<company_name>": "Get a specific experience entry by company name (e.g., /resume/experience/aws).",
                "/resume/education": "Get education information."
            }
        })
    else:
        return jsonify({"message": "API initializing or encountered an error loading resume data.", "details": resume_data}), 500


@app.route('/resume', methods=['GET'])
def get_full_resume():
    """
    GET /resume: Returns the entire resume data.
    """
    if resume_data and "error" not in resume_data:
        return jsonify(resume_data)
    return jsonify({"error": "Resume data not available or failed to load."}), 500

@app.route('/resume/contact', methods=['GET'])
def get_contact_info():
    """
    GET /resume/contact: Returns the contact information.
    """
    if resume_data and "error" not in resume_data and "contactinfo" in resume_data:
        return jsonify(resume_data["contactinfo"])
    return jsonify({"error": "Contact information not found or resume data unavailable"}), 404

@app.route('/resume/objective', methods=['GET'])
def get_objective():
    """
    GET /resume/objective: Returns the objective statement.
    """
    if resume_data and "error" not in resume_data and "objective" in resume_data:
        return jsonify({"objective": resume_data["objective"]})
    return jsonify({"error": "Objective not found or resume data unavailable"}), 404

@app.route('/resume/experience', methods=['GET'])
def get_all_experience():
    """
    GET /resume/experience: Returns all experience entries.
    """
    if resume_data and "error" not in resume_data and "experience" in resume_data:
        return jsonify(resume_data["experience"])
    return jsonify({"error": "Experience entries not found or resume data unavailable"}), 404

@app.route('/resume/experience/<company_name>', methods=['GET'])
def get_experience_by_company(company_name):
    """
    GET /resume/experience/{company_name}: Returns a specific experience entry.
    Company name is case-insensitive.
    Example: /resume/experience/aws or /resume/experience/general%20dynamics
    """
    if resume_data and "error" not in resume_data and \
       "experience" in resume_data and isinstance(resume_data["experience"], list):
        
        # Normalize company name for comparison (lowercase, no spaces)
        normalized_query_name = company_name.replace(" ", "").lower()
        
        for job in resume_data["experience"]:
            if "company" in job:
                normalized_job_name = job["company"].replace(" ", "").lower()
                if normalized_job_name == normalized_query_name:
                    return jsonify(job)
    
    return jsonify({"error": f"Experience for company '{company_name}' not found or resume data unavailable"}), 404

@app.route('/resume/education', methods=['GET'])
def get_education_info():
    """
    GET /resume/education: Returns education information.
    """
    if resume_data and "error" not in resume_data and "education" in resume_data:
        return jsonify(resume_data["education"])
    return jsonify({"error": "Education information not found or resume data unavailable"}), 404

# --- Run the Flask app ---
if __name__ == '__main__':
    # Flask will automatically use the PORT environment variable provided by Replit.
    # We use 0.0.0.0 to make it accessible externally in containers/VMs.
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)

Write a GEMINI.md file if you need to. Add it and this file to .gitignore