---
layout: posts
title: "How I Built a Contamination-Free API to Test AI Doc Formats"
description: "Testing how AI reads documentation requires controlling for training data. I built two custom APIs that have never existed on the public internet to isolate what actually matters."
date: 2026-03-02
categories: [AI, API, Research, Side Projects]
---

If you test how well AI tools use Stripe's API docs, how do you know what you're measuring? The AI might be reading your docs, or it might be drawing on patterns it already learned. You can't tell. That's the contamination problem, and it almost killed this research before it started.

## The problem with popular APIs

When I set out to test whether documentation format affects AI code generation, the obvious approach was to use a well-known API. Stripe, Twilio, GitHub. Pick one, document it in different formats, generate code, compare the results.

Then I thought about it for five minutes and realized the whole thing was flawed.

Every popular API is everywhere. GitHub repos, Stack Overflow answers, blog tutorials, coding bootcamp projects, YouTube walkthroughs. All of that is in the training data for every major AI model. When you ask Claude or GPT-4o to generate Stripe integration code, some unknown percentage of its output comes from memorized patterns, not from reading the documentation you gave it.

That means you can't isolate the variable. You're not measuring "how well does the AI read this documentation format." You're measuring some unknowable mix of documentation comprehension and training data recall. The results would be meaningless.

## The solution: build something that doesn't exist

The fix was straightforward in concept: build APIs that have never existed on the public internet. No GitHub repos. No Stack Overflow questions. No tutorials. No training data exposure of any kind.

I built two of them.

The first is **BookClub**, a book club management API with 6 endpoints. Members, books, meetings, notes. Simple enough that even a small model should be able to generate working integration code, but with enough structure to test real patterns like nested resources and input validation.

The second is **EventForge**, an event management API with 10 endpoints. This one is intentionally more complex: HMAC webhook verification, cursor-based pagination, PATCH operations for partial updates. The kind of patterns that stress-test whether a model truly understands the documentation or is just pattern-matching.

Two APIs at different complexity levels let me ask a question that one API alone can't answer: does the relationship between format and code generation change as the API gets harder?

## Why two complexity levels matter

If I'd only built BookClub, I might have concluded that documentation format doesn't matter much. The simple API is forgiving. Most models, most formats, most of the time, it works.

EventForge tells a different story. When you push the complexity up, the cracks in certain formats become visible. Patterns that were fine for a 6-endpoint API fall apart on a 10-endpoint API with authentication, pagination, and partial updates. The interaction between format and complexity is where the most important findings live.

## Same information, four formats

With the APIs built, I documented each one in four formats: YAML, OpenAPI 3.0, a novel format I created called DON (Documentation-Optimized Notation), and Markdown. Every format describes the exact same endpoints with the exact same parameters and the exact same constraints. The only thing that changes is how the information is structured.

This is critical. If the formats contained different information, you couldn't attribute differences in code generation to format. The four docs are informationally identical. They differ only in structure, verbosity, and notation.

## The test harness

For each combination of API, format, and model, I ran integration tests. Give the model a documentation spec and a task ("write a function that adds a book to the club"), capture the generated code, and test whether it actually works against the live API.

Temperature set to 0.0 across all runs to minimize randomness. Multiple runs per combination to check for consistency. Over 21,000 total test executions across four AI models, from local models you can run on a laptop to frontier cloud APIs.

The result is a dataset where every variable is controlled except the one I'm testing. When the generated code differs between formats, I know the format caused it.

## What contamination-free data lets you see

With clean data, patterns emerge that would be invisible in a contaminated test. You can see exactly how a model responds to the documentation in front of it, without the noise of prior training on the same API.

Some of those patterns were surprising. Some confirmed what I expected. All of them required contamination-free data to be credible.

The full findings are in the book. But the methodology point stands on its own: if you're testing how AI tools interact with documentation, you need to control for training data contamination. Otherwise you're measuring the model's memory, not its comprehension.

---

**The full results, including what those patterns actually are, are coming in *Tokens Not Jokin'*, out this month.**

[Try the free Docs Cost Calculator →](https://doc-cost.vercel.app/)

[Learn more about the book →](https://tokensnotjokin.com)

[Get the book on Leanpub →](https://leanpub.com/tokensnotjokin)
