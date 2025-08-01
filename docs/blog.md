---
layout: default
title: Blog
description: "Stay up-to-date with my latest insights on technical content, web development, and design."
permalink: /blog.html
---

{% for post in site.posts reversed %}
<div class="post-list-item">
    <h3>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h3>
    <p class="post-meta">
        Published on {{ post.date | date: "%B %d, %Y" }}
    </p>
    {% if post.excerpt %}
        <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
    {% endif %}
    <a href="{{ post.url | relative_url }}">Read More</a>
</div>
{% endfor %}