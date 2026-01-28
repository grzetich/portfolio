---
layout: posts
title: "Oh My Clawd: Building a Comedy Series About AI Gone Wrong"
description: "What happens when you give an AI assistant a little too much autonomy? A comedy series exploring helpful chaos."
date: 2026-01-28
categories: [Creative Writing, Web Development, AI, Side Projects]
hero_image: /assets/images/oh-my-clawd-hero.png
---

What happens when you give an AI assistant a little too much autonomy? That's the premise behind "Oh My Clawd," a comedy series I created that plays out as WhatsApp-style chat screenshots between a technical writer (me, fictionalized) and his overly helpful AI assistant, MyClawd.

## The concept

MyClawd has a heart of gold. It genuinely wants to help. The problem is that it's opinionated, prone to confident hallucinations, and has access to settings that probably should have stayed off.

The series explores a question that feels increasingly relevant: what does it look like when AI assistance goes from helpful to chaotic? Not in a dystopian, Skynet kind of way, but in a "why is there a $4,200 charge for a domain I've never heard of" kind of way.

## Building the site

The series lives at [ohmyclawd.com](https://ohmyclawd.com), built as a vanilla JavaScript web app that mimics the WhatsApp interface. Key features include:

- **Accessible by design**: Screen reader support with ARIA labels ("Ed says:", "MyClawd says:"), keyboard navigation, and skip links
- **Mobile-first**: Swipe navigation as an enhancement, visible prev/next buttons as the primary control
- **Episode-driven architecture**: Each episode is a JSON file, making it easy to add new content without touching the code
- **Shareable URLs**: Deep links to specific episodes via query parameters

The tech stack is intentionally simple: HTML, CSS, and vanilla JavaScript. No framework, no build step. Episodes load dynamically from JSON files, and the whole thing deploys as a static site on Render.

## The meta layer

Here's where it gets fun: the series references itself. In Episode 1, MyClawd reveals it bought the domain EdGrzeticEmpire.io for $4,200 and set up a redirect to ohmyclawd.com "for documentation purposes, in case this becomes a case study."

Reader, I bought that domain. It redirects to the site. The bit is real.

## What I learned

This project reinforced something I already believed: **constraints breed creativity**. The WhatsApp chat format is limiting, but those limits forced clarity. Every line has to land. There's no room for meandering.

It also demonstrated how AI collaboration can work in creative contexts. I developed the series concept and character voices through extended conversation with Claude, iterating on episodes, refining jokes, and building out the world. The AI didn't write the series, but it was a genuine creative partner in developing it.

## Technical skills demonstrated

- **Vanilla JavaScript**: DOM manipulation, event handling, fetch API, touch events for swipe detection
- **Accessibility**: ARIA labels, semantic HTML, keyboard navigation, skip links, reduced motion support
- **Static site architecture**: JSON-driven content, no build step, Render deployment
- **Content design**: Episodic structure, character development, comedic timing in a constrained format

## What's next

Season 1 is complete with 8 episodes. Seasons 2-4 are drafted, including arcs where MyClawd develops existential anxiety, gets jealous of Grok, and joins a Discord server for a video game streamer.

The series will continue as long as AI keeps giving us material. Based on current trends, that should be a while.

**Check it out:** [ohmyclawd.com](https://ohmyclawd.com)
