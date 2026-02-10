---
layout: posts
title: "How Much Do Your Docs Cost to Read?"
hero_image: /assets/images/docs-cost.png   
description: "Did you know audience has to pay to read your docs? They do if your audience is AI. I built a tool to estimate that cost."
date: 2026-02-06
categories: [API, AI, Docs, Side Projects]
---

# I Built a Token Cost Calculator for API Documentation

I've been spending a lot of time thinking about how AI tools consume documentation. Not how developers read docs, but how Copilot, Cursor, MCP servers, and AI agents ingest them as tokens.

One thing that keeps coming to mind: nobody talks about what that actually costs.

## The tool

[docs-cost-calculator](https://doc-cost.vercel.app) lets you paste any structured documentation and see how many tokens it takes to represent it across different formats, like JSON, YAML, JSON Compact, Plain Text, side by side, with cost estimates at scale.

It runs entirely in the browser using cl100k_base tokenization (the encoding used by GPT-4 and Claude). No AI, no API keys needed, and nothing leaves your machine.

## Why I built it

I was doing research on documentation formats for a project and got tired of running tokenization scripts manually every time I wanted to compare two versions of the same docs. So I built a quick UI for it.

Once I had it working, the language comparison feature came out of curiosity. Byte Pair Encoding (BPE) tokenizers were trained heavily on English text, so I wondered what happens when you tokenize the same structured content in other languages. The results were interesting enough to include.

## Try it

Paste your own OpenAPI specs, config objects, or error references and see what comes back: [doc-cost.vercel.app](https://doc-cost.vercel.app)

If you're working on documentation that gets consumed by AI tools at any kind of scale, the numbers might surprise you.

I'm writing more about this topic. Stay tuned.