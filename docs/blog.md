---
layout: default
title: Blog
description: "Insights on technical writing, AI-assisted workflows, developer documentation, and building better developer experiences."
permalink: /blog.html
---

<div class="page-header">
    <h1>All Posts</h1>
    <p class="page-description">
        Insights on technical writing, AI-assisted workflows, developer documentation,
        and building better developer experiences.
    </p>
</div>

<div class="blog-grid">
    {% assign sorted_posts = site.posts | sort: "date" | reverse %}
    {% for post in sorted_posts %}
    <article class="blog-card">
        <a href="{{ post.url | relative_url }}" class="card-link">
            {% if post.hero_image %}
            <div class="card-image">
                <img src="{{ post.hero_image }}" alt="{{ post.title }}" loading="lazy" />
                <div class="date-badge">{{ post.date | date: "%b %d, %Y" }}</div>
            </div>
            {% else %}
            <div class="card-image card-image-placeholder">
                <div class="date-badge">{{ post.date | date: "%b %d, %Y" }}</div>
            </div>
            {% endif %}
            <div class="card-content">
                <h3 class="card-title">{{ post.title }}</h3>
                {% if post.description %}
                <p class="card-excerpt">{{ post.description | strip_html | truncatewords: 30 }}</p>
                {% endif %}
                {% if post.categories %}
                <div class="card-tags">
                    {% for category in post.categories limit:3 %}
                    <span class="tag">{{ category }}</span>
                    {% endfor %}
                </div>
                {% endif %}
            </div>
        </a>
    </article>
    {% endfor %}
</div>
