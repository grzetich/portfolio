---
layout: posts
title: "Claude Context Analysis: What 500 CLAUDE.md Files Reveal About How Developers Use Claude"
description: "I built a tool that scrapes CLAUDE.md files from GitHub and runs topic modeling to surface patterns in how developers configure Claude Code."
date: 2026-02-06
categories: [Web Development, AI, Data Science, Side Projects]
---

Every day at 3 AM GMT, a Flask app I built wakes up, scrapes 500 CLAUDE.md files from public GitHub repositories, runs topic modeling on them, and publishes the results. The goal: figure out what developers are actually putting in their CLAUDE.md files and how those patterns change over time.

**Check it out:** [analyze-claude-md.onrender.com](https://analyze-claude-md.onrender.com/)

## Why this exists

CLAUDE.md files are how developers tell Claude Code how to work with their project. They contain coding standards, build commands, architecture decisions, and behavioral instructions. But there's no official guidance on what makes a good one. Everyone's figuring it out independently.

I wanted to answer a simple question: what are the common patterns? If 500 repos all mention "typescript" and "npm" in their CLAUDE.md files, that tells you something about the ecosystem. If "agent" is trending upward over 30 days, that tells you something about where things are headed.

## How it works

The pipeline has four stages:

1. **Collection:** The GitHub Code Search API finds files named `claude.md` across public repos. The app downloads up to 500 per run, handling pagination and rate limits.

2. **Preprocessing:** NLTK tokenizes the text, removes stopwords, and lemmatizes words down to root forms. "Running" becomes "run," "configurations" becomes "configuration."

3. **Topic modeling:** NMF (Non-negative Matrix Factorization) discovers 5 topics, each a weighted distribution over words. The model uses TF-IDF weighting, which downweights common terms and highlights distinctive ones.

4. **Visualization:** Results are saved to JSON and rendered as horizontal bar charts on the homepage, with word weights shown proportionally.

The whole thing runs on Render's free tier with no database. Analysis history is stored as JSON files committed to the repo so data survives redeploys.

## Choosing NMF over LDA

The project originally used LDA (Latent Dirichlet Allocation), which is the textbook approach for topic modeling. It was brittle for this use case.

LDA topics shifted significantly between runs, even with a fixed random seed, because the input data changes daily (GitHub returns different repos each time). The topics were often incoherent, mixing unrelated terms. And because LDA uses raw word counts, common words dominated even when they weren't distinctive.

NMF paired with TF-IDF solved all three problems. Topics are more coherent (the top words within each topic clearly relate to each other), more stable across runs, and better at surfacing distinctive terms rather than just frequent ones. The swap was nearly drop-in since both models are in scikit-learn with the same API.

BERTopic would produce even better results using transformer embeddings for semantic understanding, but it requires 80-400MB for the sentence-transformers model, which won't fit on Render's free tier.

## What the data shows

After 30 daily runs, some clear patterns emerge:

- **"npm" is the most consistently dominant term**, appearing with high weight in nearly every run. Frontend tooling dominates CLAUDE.md files.
- **"typescript," "react," and "server"** form a stable cluster. The JavaScript/TypeScript ecosystem is where most Claude Code usage lives.
- **"agent" has been trending upward** over the past month, reflecting the growing use of agentic patterns.
- **"python," "database," and "api"** are consistently present but with more variance, suggesting they're concentrated in specific project types rather than being universal.

The term trends page lets you toggle individual terms on and off, with both absolute weight and normalized (0-100%) views for comparing terms with different baselines.

## The label generation problem

One interesting challenge: how do you name a topic? LDA and NMF produce distributions over words, not labels. The current approach is a heuristic function that checks if the top 5 words contain keywords from hardcoded lists:

```python
if any(word in top_5_words for word in ['npm', 'typescript', 'react']):
    return "Frontend Development"
```

This is the weakest part of the system. If "react" happens to be the 6th word instead of top 5, a clearly frontend topic gets a generic fallback label. It's why the term trends page tracks individual words rather than relying on topic labels. The words are the stable data; the labels are cosmetic.

## Technical details

- **Stack:** Flask, scikit-learn, NLTK, Chart.js, Jinja2
- **Hosting:** Render free tier (512MB RAM, cold starts)
- **Storage:** JSON files in a `data/` directory committed to the repo
- **Scheduling:** Background daemon thread checks hourly, runs analysis at 3 AM GMT
- **Data:** 500 files per run, 30-day rolling history, 15 terms tracked in trends

The app has no database. Historical data is an array of JSON objects appended to a file. Topic evolution tracking uses cosine similarity to match topics across runs despite label changes. The whole codebase is a single `app.py` file with Jinja2 templates.

## What I learned

**NMF is underrated.** Most topic modeling tutorials teach LDA first, but for short documents with noisy input, NMF with TF-IDF produces noticeably better results with less tuning.

**Track words, not topics.** Topic-level tracking across runs is fragile because the groupings shift. Term-level tracking is rock solid and often more useful.

**Commit your data.** Storing analysis history as committed JSON files instead of relying on ephemeral server storage was a simple decision that saved the project's 30-day history from being wiped on every deploy.

**Check it out:** [analyze-claude-md.onrender.com](https://analyze-claude-md.onrender.com/)

**Source code:** [github.com/grzetich/analyzeclaudemd](https://github.com/grzetich/analyzeclaudemd)
