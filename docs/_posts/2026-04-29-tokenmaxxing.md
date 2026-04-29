---
layout: posts
title: "Tokenmaxxing Is Visible. Doc Format Waste Isn't."
date: 2026-04-29
canonical_url: "https://tokensnotjokin.com/blog/tokenmaxxing"
description: "Nobody is tracking the tokens your documentation burns before the developer even starts."
---

*Originally published at [tokensnotjokin.com](https://tokensnotjokin.com/blog/tokenmaxxing)*

Companies are building leaderboards to track how many tokens their developers burn. Nobody is tracking how many tokens the documentation burns before the developer even starts.

## The tokenmaxxing problem

Gergely Orosz reported last week in [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-pulse-tokenmaxxing-as-a-weird-6b2) that developers at Meta, Microsoft, and Salesforce are deliberately burning tokens to inflate their AI usage metrics. Meta employees used 60.2 trillion tokens in 30 days. Salesforce set minimum spend targets of $100/month on Claude Code and $70/month on Cursor. Microsoft developers admitted to prompting throwaway projects and asking AI questions they could answer faster by reading the docs.

The industry reaction has been predictable: this is wasteful, this is gaming metrics, this is lines-of-code all over again.

And it's happening against a bigger backdrop. [Axios reported this week](https://www.axios.com/2026/04/26/ai-cost-human-workers) that AI compute costs now exceed employee costs at some companies. Nvidia's VP of applied deep learning said that for his team, compute costs are "far beyond the costs of the employees." Uber's CTO told The Information the company has already blown through its entire 2026 AI budget, largely on coding tools. Gartner projects global IT spending will hit $6.31 trillion this year, up 13.5%, driven by AI infrastructure.

Companies are spending more on AI than they planned, and they're starting to look hard at where those tokens go. Tokenmaxxing is the visible problem. But there's another version of unnecessary token spend that nobody is talking about, and it's not a choice anyone is making. It's baked into the documentation.

## The tokens nobody chose to spend

Every time a developer points Claude Code or Cursor at an API, the tool reads the documentation. The format of that documentation determines how many tokens get consumed before the developer's first prompt, before a single line of code is generated, before any work happens at all.

In my research across 21,000+ integration tests, the same API documented in OpenAPI 3.0 consumed roughly 3.8x more tokens than the same information in YAML. For a 10-endpoint API, that's 7,534 tokens versus 2,007. Same endpoints, same parameters, same information. The difference is pure format overhead.

A developer using Claude Code against an OpenAPI spec isn't tokenmaxxing. They're just using the docs their API provider published. The extra 5,500 tokens per session aren't a choice. That's not maxxing, that's taxing.

## Scale the math

Meta has 85,000 employees on AI tools. If even a fraction of them work with APIs documented in verbose formats, the documentation overhead adds up fast. Not as fast as deliberately prompting throwaway projects, but it compounds in a way that intentional waste doesn't: it happens on every single API interaction, automatically, without anyone noticing.

Salesforce is tracking individual developer spend down to 15-minute intervals. They have minimum targets and team dashboards. But the token cost of the documentation format those developers consume isn't on any dashboard. It's invisible spending that looks like normal usage.

A developer integrating five APIs in a coding session, each documented in OpenAPI, might burn 30,000+ tokens on documentation alone. Switch those specs to YAML and the same session uses about 8,000 documentation tokens. The developer didn't change their behavior. The documentation team changed the format.

## Two kinds of waste

Tokenmaxxing is visible waste. Developers choose to burn tokens on throwaway projects. It shows up on leaderboards. It gets reported in newsletters. Companies can shut it down by removing the leaderboard, which is what Meta did.

Documentation format overhead is invisible waste. Nobody chose it. Nobody tracks it. Nobody knows it's there. And removing a leaderboard doesn't fix it, because it was never on a leaderboard to begin with.

Companies worried about AI spend are looking at the wrong side of the equation. Developer behavior is one input. Documentation format is another. Our data shows format explains over 10x more variance in AI code generation outcomes than model choice. The documentation author's format decisions affect every developer who touches that API, every session, every day.

## What can be done about it

If your company tracks AI token spend, you can measure this. Take an API your developers use frequently. Tokenize the documentation in its current format. Then tokenize the same information in another format, like YAML. The difference is what your team spends on format overhead, per interaction, multiplied by every developer and every session.

You can try this right now with the [Docs Cost Calculator](https://doc-cost.vercel.app/). Paste your API spec, choose a model, and see the token cost across formats.

The tokenmaxxing conversation is about developers wasting tokens on purpose. The format conversation is about wasting tokens by default. One of those problems goes away when you remove the incentive. The other one is still there, in every API spec, in every coding session, on every team.

---

*The research behind the format numbers: [Tokens Not Jokin' on Leanpub](https://leanpub.com/tokensnotjokin)*