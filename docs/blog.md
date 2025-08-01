---
layout: default title: Blog description: "Stay up-to-date with my latest insights on technical content, web development, and design." permalink: /blog.html
---
<div class="posts-list space-y-6">
    {% for post in site.posts reversed %}
        <div class="post-list-item">
            <h3 class="text-2xl font-bold mb-2">
                <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            <p class="post-meta">
                Published on {{ post.date | date: "%B %d, %Y" }} by {{ post.author | default: site.author }}
                {% if post.categories %}
                    in {% for category in post.categories %}<span class="text-red-700 font-semibold">{{ category }}</span>{% unless forloop.last %}, {% endunless %}{% endfor %}
                {% endif %}
            </p>
            {% if post.excerpt %}
                <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
            {% endif %}
            <a href="{{ post.url | relative_url }}" class="text-red-700 hover:underline">Read More</a>
        </div>
    {% endfor %}
</div>
