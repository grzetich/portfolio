---
layout: print
title: Ed Grzetich - Resume
description: "Professional resume for Ed Grzetich, Senior Technical Writer specializing in developer documentation."
permalink: /resume.html
---

{% assign resume = site.data.resume %}

<div class="button-container">
    <button id="download-pdf" class="download-btn">Download as PDF</button>
</div>

<h1>{{ resume.contactinfo.name.first }} {{ resume.contactinfo.name.last }}</h1>

<div class="contact-info">
    <p>
        <strong>Email:</strong> <a href="mailto:{{ resume.contactinfo.email }}">{{ resume.contactinfo.email }}</a> |
        <strong>Phone:</strong> {{ resume.contactinfo.phonenumber }}
    </p>
    <p>
        <strong>Location:</strong> {{ resume.contactinfo.city }}, {{ resume.contactinfo.state }} |
        <strong>Website:</strong> <a href="{{ resume.contactinfo.url }}">{{ resume.contactinfo.url }}</a> |
        <strong>GitHub:</strong> <a href="https://github.com/grzetich">github.com/grzetich</a>
    </p>
</div>

<section class="summary">
    <h2>Summary</h2>
    <p>{{ resume.objective }}</p>
</section>

<section>
    <h2>Experience</h2>
    {% for job in resume.experience %}
    <div class="job">
        <div class="job-header">
            <div class="job-title">{{ job.title }}</div>
            <div class="job-company">{{ job.company }} • {{ job.date_start }} - {% if job.date_end %}{{ job.date_end }}{% else %}Present{% endif %}</div>
        </div>
        <div class="job-duties">
            {% assign duties_list = job.duties | split: ". " %}
            {% for duty in duties_list %}
                {% if duty != "" %}
                    <p>{{ duty | strip }}.</p>
                {% endif %}
            {% endfor %}
        </div>
    </div>
    {% endfor %}
</section>

<section class="education">
    <h2>Education</h2>
    <div class="degree">{{ resume.education.degree }}</div>
    <div class="school">{{ resume.education.school }}</div>
</section>