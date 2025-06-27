layout: default
title: My Styled Resume
description: "A beautifully styled and interactive view of my professional resume, dynamically rendered from JSON data."
permalink: /resume.html
---

{% assign resume = site.data.resume %}

<section id="contact-info" class="section-container">
    <h2 class="text-3xl font-bold text-gray-900 mb-4 text-center">{{ resume.contactinfo.name.first }} {{ resume.contactinfo.name.last }}</h2>
    <div class="text-center text-gray-700 leading-relaxed mb-4">
        <p class="mb-2">
            <strong>Email:</strong> <a href="mailto:{{ resume.contactinfo.email }}" class="text-red-700 hover:underline">{{ resume.contactinfo.email }}</a>
        </p>
        <p class="mb-2">
            <strong>Phone:</strong> {{ resume.contactinfo.phonenumber }}
        </p>
        <p class="mb-2">
            <strong>Location:</strong> {{ resume.contactinfo.city }}, {{ resume.contactinfo.state }}
        </p>
        <p class="mb-2">
            <strong>Website:</strong> <a href="{{ resume.contactinfo.url }}" target="_blank" class="text-red-700 hover:underline">{{ resume.contactinfo.url }}</a>
        </p>
        {% if resume.contactinfo.github %} {# Check if github field exists #}
        <p>
    <strong>GitHub:</strong> <a href="https://github.com/grzetich" target="_blank" class="text-red-700 hover:underline">github.com/grzetich</a>
</p>
        {% endif %}
    </div>
</section>

<section id="objective" class="section-container">
    <h2 class="text-3xl font-bold text-gray-900 mb-4">Summary</h2>
    <p class="text-gray-700 leading-relaxed">
        {{ resume.objective }}
    </p>
</section>

<section id="experience" class="section-container">
    <h2 class="text-3xl font-bold text-gray-900 mb-4">Experience</h2>
    <div class="space-y-8">
        {% for job in resume.experience %}
        <div class="project-card">
            <h3 class="text-xl font-semibold text-red-700 mb-1">{{ job.title }}</h3>
            <p class="text-lg text-gray-800 mb-2">{{ job.company }} &bull; {{ job.date_start }} - {% if job.date_end %}{{ job.date_end }}{% else %}Present{% endif %}</p>
            <ul class="list-disc pl-6 text-gray-700 space-y-1">
                <li>{{ job.duties }}</li>
            </ul>
        </div>
        {% endfor %}
    </div>
</section>

<section id="education" class="section-container">
    <h2 class="text-3xl font-bold text-gray-900 mb-4">Education</h2>
    <div class="project-card">
        <h3 class="text-xl font-semibold text-red-700 mb-1">{{ resume.education.degree }}</h3>
        <p class="text-lg text-gray-800">{{ resume.education.school }}</p>
    </div>
</section>
