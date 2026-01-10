---
layout: "posts"
title: "Making data conversational: Building MCP Servers as API bridges"
description: "How I built an MCP server as a thin bridge on top of our REST API to serve both developers and end users from a single backend."
date: 2026-01-09
categories: [Web Development, AI]
hero_image: "/assets/images/layers.jpg"
---

At the [Fort Wayne AI](https://www.fortwayne-ai.com/) meetup on 09 January, I presented about a pattern I've discovered while building [Vibe Data](https://vibe-data.com): Making data conversational by using a model context protocol (MCP) server on top of existing REST APIs. Your API provide your data, an MCP server provides access to the API for a desktop LLM client like Claude or ChatGPT, and the LLM client provides conversational access to your data.

This post captures what I learned building this architecture and what I shared with the developer community.

<div style="margin: 2rem 0;">
  <script async class="speakerdeck-embed" data-id="170f452c020f4f26a8112329fdd86a03" data-ratio="1.7777777777777777" src="//speakerdeck.com/assets/embed.js"></script>
</div>

## The situation: Two audiences, one backend

When you're building a data platform, you inevitably face a challenge: different users need different interfaces.

**Developers want:**
- Programmatic API access
- JSON they can transform
- Full control for automation
- Integration with their tools

**End users want:**
- Quick answers to questions
- No coding required
- Natural language queries
- Simple, intuitive interfaces

The traditional approach is to build two separate systems: a REST API for developers and dashboards or reports for end users. But this creates maintenance overhead, duplicate business logic, and architectural complexity.

## The Solution: MCP as an API bridge

I've found a better pattern: **build your REST API first, then add an MCP server as a thin conversational wrapper.**

Here's the architecture:
```
          Data platform
                 │
            REST API
    (Business Logic | Auth | Rate Limiting)
                 │
        ┌────────┴────────┐
        │                 │
   Direct API        MCP Server
    Access            (~200 lines)
        │                 │
   Developers      Users + Claude
   (JSON/Code)     (Conversation)
```

The REST API remains your single source of truth. All business logic, authentication, rate limiting, and caching live here. The MCP server is just a formatting layer that:

1. Receives structured tool calls from Claude.
2. Translates them to API requests.
3. Formats JSON responses as natural language.
4. Returns conversational text.

## Why this pattern works

### 1. Separation of concerns

Your API handles the hard stuff:
- Database queries
- Authentication and authorization
- Rate limiting and caching
- Business logic and validation

Your MCP server handles presentation:
- Formatting JSON as readable text
- Adding context and insights
- Transforming data into conversation

When your API changes, both interfaces get the update automatically. No duplicate logic to maintain.

### 2. Opportunity for two products from one source

You can serve both audiences without building twice:
- **API tier**: Developers get JSON, higher rate limits, programmatic access
- **Conversational tier**: End users get Claude access, simpler pricing

Same backend. Different value propositions.

### 3. Progressive enhancement

You're not choosing between API or MCP. You're adding conversational access to an existing system:
- Start with API (proven, understood, lots of tooling)
- Add MCP layer when ready (thin wrapper, low risk)
- Keep both interfaces running (serve more users)

## What I learned building this

### MCP works best as a bridge

Don't try to rebuild your entire backend in MCP. Don't put business logic in your MCP tools. Build a solid REST API first. That's your product. The MCP server should be ~200 lines of code that calls your API and formats responses.

**In demo:**
```javascript
// Mock data for education
const data = mockData.getCurrentMetrics(toolId);
return this._successResponse({ data });
```

**In production:**
```javascript
// Real HTTP request
const response = await fetch(
  `${this.baseURL}/tools/${toolId}/metrics`,
  {
    headers: { 'Authorization': `Bearer ${this.apiKey}` }
  }
);
return await response.json();
```

Same structure. Only the data source changes. Everything else - tools, formatters, MCP server - stays identical.

### Different interfaces for different users

Developers want JSON they can transform however they need. They'll build custom dashboards, automate reports, integrate with other systems. Give them an API.

End users just want answers. They don't want to learn `curl` commands or read API documentation. They want to ask "What's Cursor's growth trend?" and get an answer. Give them Claude with MCP.

You can serve both without building duplicate systems.

### The formatting layer is where MCP adds value

Your API returns data:
```json
{"downloads": 8100000, "growth_pct": 55.8}
```

Your MCP server transforms it:
```
Cursor grew 55% over the quarter, reaching 8.1M monthly 
downloads, indicating strong developer adoption.
```

Same data. One is optimized for machines. One is optimized for humans.

This formatting layer, turning structured data into meaningful insights, is where conversational interfaces shine. It's not just passing through JSON; it's contextualizing and explaining it.

## The Demo: Making data conversational

During the presentation, I demonstrated this with Vibe Data's adoption intelligence and Claude desktop:

**Query 1:** "What's Cursor's adoption trend over the last quarter?"
- Claude calls `get_tool_history` tool
- MCP server calls REST API
- Returns formatted trend analysis with growth calculations

**Query 2:** "How does Cursor compare to GitHub Copilot?"
- Claude calls `compare_tools`
- Gets metrics for both
- Synthesizes side-by-side comparison with key insights

**Query 3:** "Which AI coding tools are growing fastest right now?"
- Claude calls `get_trending_tools`
- Ranks by growth percentage
- Presents as ordered list with context

The pattern works because Claude can compose these tools in ways I didn't pre-build. Ask "compare the top 3 trending tools" and Claude chains multiple calls automatically. A report would need that query to be pre-built and a dashboard might require the user to pick the appropriate options from menus.

## Being honest about limitations

MCP isn't magic, and I told the audience that. Current challenges:

**Discovery:** Users don't automatically know what tools are available. They have to ask or explore. The ecosystem needs better tool discovery UIs.

**Distribution:** When you add new tools, users need to update locally. Cloud-hosted MCP servers would solve this with instant updates.

**Anticipation:** You still need to build specific tools for specific questions. MCP doesn't eliminate the need to think about what users need.

**But even with these limitations, it's better:**
- Natural language beats clicking through filters.
- Claude can compose tools dynamically.
- Graceful degradation ("I don't have Reddit data") beats silent missing features or cryptic error codes.
- Standardized protocol beats reinventing the wheel.

Understanding both strengths and friction points, not just evangelizing uncritically, helps drive real adoption.

## Real-world use cases

This pattern works for any product with data exposed by APIs:

**B2B SaaS:**
- API → Analytics platforms, customer dashboards
- MCP → "How's our MRR trending?" "Which customers churned?"

**E-commerce:**
- API → Inventory systems, order management
- MCP → "What products are low stock?" "Show me returns this week"

**Internal Tools:**
- API → Automated reports, integrations
- MCP → "Find pending invoices" "Compare Q3 vs Q4 sales"

The pattern is universal: build API first, wrap with MCP, serve both technical and non-technical users.

## The code: Open source educational implementation

I've open-sourced an educational MCP server that demonstrates this pattern: [github.com/grzetich/ai-developer-tools-mcp](https://github.com/grzetich/ai-developer-tools-mcp)

It uses sample data to show the architecture without requiring database access. The structure is identical to production:
```
src/
├── tools/          # MCP tool definitions
├── api/            # API client (THE BRIDGE)
├── data/           # Mock data (simulates database)
└── utils/          # Response formatters
```

In production, only `api/client.js` changes - from mock data to real `fetch()` calls. Everything else stays the same.

## What's next

I'm continuing to refine this pattern at Vibe Data, where the MCP server serves production traffic alongside our REST API. The dual-interface approach lets us serve both developers building integrations and investors asking questions.

I'm also exploring how to solve the distribution and discovery challenges, potentially through cloud-hosted MCP servers that auto-update when new tools are deployed like my [Pokémon MCP server](https://github.com/grzetich/pokemon-mcp).

If you're building with MCP or thinking about conversational interfaces for your data, I'd love to hear what patterns you're discovering. Reach out on [GitHub](https://github.com/grzetich) or [email](mailto:ed.grzetich@gmail.com).

## Resources

- **Educational MCP Server:** [github.com/grzetich/ai-developer-tools-mcp](https://github.com/grzetich/ai-developer-tools-mcp)
- **Presentation Slides:** [View on SpeakerDeck](https://speakerdeck.com/egrzetich/making-data-conversational-building-mcp-servers-as-api-bridges)
- **MCP Documentation:** [modelcontextprotocol.io](https://modelcontextprotocol.io)