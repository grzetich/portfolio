# Portfolio migration: GitHub Pages (Jekyll) -> Vercel (Eleventy)

This folder replaces docs/ in your repo wholesale. Jekyll is gone: no
Gemfile, no Ruby, no bundler. The site now builds with Eleventy (Node),
which reads the same Liquid templates and Markdown your content was
already written in. The build was run and verified: all 12 posts, all
pages, identical URLs, sitemap included.

## What changed

- _posts/ renamed to posts/ with posts/posts.json supplying layout,
  permalink (/blog/<slug>.html, same URLs as Jekyll), and the collection
  tag. Post front matter unchanged except date formats normalized to ISO
  (Eleventy rejects Jekyll's "10:00:00 -0400" style).
- eleventy.config.js and package.json replace Gemfile/bundler. _config.yml
  is no longer used (kept nothing from it that matters; site metadata now
  lives in _data/site.json so {{ site.title }} etc. keep working).
- Layouts and pages: page.title/description/etc become bare variables,
  include syntax quoted, blog loop uses collections.posts. Content prose
  untouched.
- sitemap.liquid replaces jekyll-sitemap, with real per-page lastmod dates
  from post dates.
- CLAUDE.md, GEMINI.md, feat-api.md, resume.json, resume_api.py, robots.txt,
  assets/, and yobitel/ are passthrough copies served verbatim, matching
  Jekyll's behavior for front-matter-less files. The yobitel Markdown stays
  raw Markdown.
- All the previous content edits are included: Senior Technical Writer
  objective in both resume JSON copies and the API demo, past-tense AWS
  paragraph, Vercel analytics scripts in the default layout, vercel.json
  content-negotiation rewrites.

## Local preview (optional but recommended once)

    cd docs && npm install && npm run serve

Then http://localhost:8080. `npm run build` writes _site/.

## Vercel project settings

- Root Directory: docs
- Framework Preset: Eleventy (or Other)
- Build Command: npm run build
- Output Directory: _site

Node projects are Vercel's native path; no runtime surprises like the
Ruby build. Add docs/node_modules and docs/_site to .gitignore.

## Remaining steps (unchanged from before)

1. Deploy, verify preview URL: pages, blog permalinks, /yobitel/resume.md
   returns raw Markdown.
2. Enable Web Analytics and Speed Insights in the Vercel dashboard.
3. Domains: add grzeti.ch in Vercel first, then at your DNS provider
   replace the four GitHub Pages A records (185.199.108-111.153) with
   Vercel's apex A record (dashboard shows the value, currently
   76.76.21.21); www CNAME to cname.vercel-dns.com if used. If DNS is
   behind Cloudflare, set those records to DNS-only (grey cloud).
4. After grzeti.ch serves from Vercel (response header says server:
   Vercel): repo Settings -> Pages -> Source: None, and delete the CNAME
   file. Ignore GitHub's "custom domain removed" email.
5. Verify negotiation on the live domain:
       curl -s -H "Accept: text/markdown" https://grzeti.ch/yobitel | head -3
6. Submit https://grzeti.ch/yobitel/ on the Yobitel application.
