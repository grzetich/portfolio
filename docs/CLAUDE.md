# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based portfolio website showcasing technical writing, content design projects, and a blog. The site includes an interactive resume API demo that serves JSON data from a local file.

## Architecture

- **Jekyll Static Site**: Built with Jekyll using the minima theme with custom CSS overrides
- **Resume API Demo**: JavaScript-based simulation of a REST API using local JSON data (`resume.json`)
- **Resume Data**: Structured JSON following JSON Schema (`_data/resume_schema.json`)
- **Python Flask API**: Experimental Flask API (`resume_api.py`) for serving resume data from GitHub
- **Content Structure**:
  - `_posts/`: Blog posts in Markdown
  - `_layouts/`: Jekyll layout templates
  - `_includes/`: Reusable components (like `api_demo.html`)
  - `_data/`: Structured data files
  - `assets/`: Static assets (CSS, images, PDFs)

## Development Commands

Since Ruby/Jekyll tools are not installed in this environment:

- **Local Development**: Requires Jekyll installation (`bundle install`, `bundle exec jekyll serve`)
- **Python API Testing**: `python resume_api.py` (requires Flask and flask-cors)
- **Content Updates**: Edit Markdown files directly; Jekyll will rebuild automatically

## Key Files

- `_config.yml`: Jekyll configuration, site settings, and plugins
- `resume.json`: Main resume data file (duplicates `_data/resume.json`)
- `_includes/api_demo.html`: Interactive resume API demonstration component
- `Gemfile`: Ruby dependencies (Jekyll)
- `_sass/`: Custom SCSS files for styling

## Content Guidelines

- Blog posts go in `_posts/` with YYYY-MM-DD-title.md format
- Resume updates require changes to both `resume.json` and `_data/resume.json`
- Custom styling is in `_sass/` and `assets/css/style.css`
- All external links and PDFs are in `assets/other/`

## API Demo

The resume API demo simulates REST endpoints:
- `/api/resume` - Full resume data
- `/api/contactinfo` - Contact information
- `/api/objective` - Professional objective
- `/api/experience` - Work experience array
- `/api/education` - Education details

The demo loads data from `resume.json` and provides interactive buttons to "fetch" different endpoints.