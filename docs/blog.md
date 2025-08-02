---
layout: default
title: Blog
description: "Stay up-to-date with my latest insights on technical content, web development, and design."
permalink: /blog.html
---
<div class="posts-list">
    {% for post in site.posts reversed %}
        <div class="post-list-item">
            <h3>
                <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
            </h3>
            <p class="post-meta">
                Published on {{ page.date | date: "%B %d, %Y" }}
            </p>
            {% if post.excerpt %}
                <p class="post-excerpt">{{ page.description | strip_html | truncatewords: 30 }}</p>
            {% endif %}
            <a href="{{ page.url | relative_url }}">Read More</a>
        </div>
    {% endfor %}
</div>