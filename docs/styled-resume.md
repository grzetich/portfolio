---
layout: default
title: My Styled Resume
description: "A beautifully styled and interactive view of my professional resume, dynamically rendered from JSON data."
permalink: /resume.html
---

{% assign resume = site.data.resume %}

<style>
    /* Add styles that will only apply when printing */
    @media print {
        body, .container {
            margin: 0;
            padding: 0;
            box-shadow: none;
        }
        header, footer, #download-button-container {
            display: none !important;
        }
        .section-container, .project-card {
            border: none !important;
            box-shadow: none !important;
            page-break-inside: avoid;
        }
    }
</style>

<!-- Container for the download button -->
<div id="download-button-container" style="text-align: center; margin-bottom: 1.5rem;">
    <button id="download-pdf" style="padding: 0.75rem 1.5rem; border-radius: 0.5rem; font-weight: 600; color: #ffffff; background-color: #b91c1c; border: none; cursor: pointer;">
        Download as PDF
    </button>
</div>

<!-- The main resume content that will be converted to PDF -->
<div id="resume-content">
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
                <div class="job-duties space-y-3">
                    {% assign duties_list = job.duties | split: ". " %}
                    {% for duty in duties_list %}
                        {% if duty != "" %}
                            <p class="text-gray-700">{{ duty | strip }}.</p>
                        {% endif %}
                    {% endfor %}
                </div>
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
</div>

<!-- Add the html2pdf.js library -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>

<script>
    document.getElementById('download-pdf').addEventListener('click', function () {
        const element = document.getElementById('resume-content');
        const opt = {
            margin:       0.5,
            filename:     'Grzetich-resume.pdf',
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2, useCORS: true },
            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },
            pagebreak:    { mode: 'avoid-all', before: '.project-card' }
        };

        // New Promise-based usage:
        html2pdf().set(opt).from(element).save();
    });
</script>