---
layout: default
title: Home
description: "Ed Grzetich's professional portfolio, featuring an API-driven resume, comprehensive writing samples from AWS and earlier career, and content strategy insights."    
---
<div class="project-card">
<h3 class="text-lg font-semibold text-gray-800 mb-2">Architecting a Resilient Pokémon TCG Data API for LLM Integration</h3>
<p class="text-gray-700 mb-3">This project involved the development of a Python Flask API to serve comprehensive, real-time Pokémon Trading Card Game (TCG) data. The goal was to create a robust, accessible backend capable of supporting various applications, including seamless integration with Large Language Models (LLMs).</p>
<p class="text-gray-700 mb-3">The journey from development to a fully operational backend presented several critical challenges:</p>
<ul class="list-disc pl-5 text-gray-700 space-y-1 mb-3"><li>Persistent Deployment Issues: Initial deployment attempts on a Platform-as-a-Service (PaaS) encountered elusive, low-level server termination errors (SIGTERM) that required extensive, systematic debugging beyond typical application logs.</li>
<li>Cloud Platform Migration: The necessity to pivot from one cloud provider to another, demanding adaptability in configuring environments, dependencies, and process management.</li>
<li>Complex LLM Interoperability: Designing a communication layer for LLM integration that adhered to the Model Context Protocol (MCP), involving intricate JSON-RPC messaging and standard I/O stream handling.</li></ul>
<p class="text-gray-700 mb-3">My solution involved a multi-faceted approach. I meticulously debugged the deployment issues, isolating environmental factors by simplifying the application and experimenting with various Python versions and Gunicorn configurations. This led to a strategic migration to Render.com, where the API was successfully deployed and now operates reliably, providing endpoints for card details, real-time pricing, set information, and more.</p>
<p class="text-gray-700 mb-3">Furthermore, to enable LLM interaction, I developed a dedicated Python orchestrator. This component acts as a persistent local server, meticulously handling the JSON-RPC communication protocol, including message framing (Content-Length headers), and correctly processing standard protocol messages like initialize and shutdown. This ensures a stable and compliant bridge between LLMs (e.g., Claude) and the deployed Pokémon TCG API.</p>
<p class="text-gray-700 mb-3">This project significantly deepened my expertise in backend architecture, cloud deployment, advanced troubleshooting, and the cutting-edge domain of LLM tooling and interoperability. It demonstrates my ability to build resilient systems and solve complex, multi-layered technical challenges from development through deployment and integration.</p>
<p class="text-gray-700 mb-3">Tools used:
<ul class="list-disc pl-5 text-gray-700 space-y-1 mb-3">
<li>Microsoft Visual Studio Code</li>
<li>Render.com</li>
<li>GitHub</li>
<li>Google Gemini</li>
<li>Anthropic Claude Desktop</li>
</ul>
<p class="text-gray-700 mb-3"><a href="https://github.com/grzetich/pokemon-tcg-mcp" class="text-red-700 hover:underline" target="_blank">View Project Repository on GitHub</a></p>
</div>

<div class="project-card">
<h3 class="text-lg font-semibold text-gray-800 mb-2">Spotlight: Enhancing the Snowball Edge Client Experience</h3>
    <p class="text-gray-700 mb-3">
        Consider the <a href="https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client-commands.html" class="text-red-700 hover:underline" target="_blank">Configuring and using the Snowball Edge Client</a> topic, a prime example of my impact. This topic was a consistent source of user frustration. My comprehensive audit, aligned with AWS's style and content strategy, revealed:
    </p>
    <ul class="list-disc pl-5 text-gray-700 space-y-1 mb-3">
        <li>Content bloat: It tried to be an exhaustive catalog of every available client command.</li>
        <li>Inconsistent updates: New commands were often siloed in other documents, leaving this topic incomplete and out of sync.</li>
        <li>Missing essentials: It failed to address the foundational knowledge users needed, such as how to install and configure the client.</li>
    </ul>
    <p class="text-gray-700 mb-3">
        It's helpful to understand that AWS Snowball Edge is unique: it's a physical device customers rent to move data or run compute instances without an AWS connection. This means users primarily interact with the service through the Snowball Edge Client, not the typical AWS management console.
    </p>
    <p class="text-gray-700 mb-3">
        My solution was to drastically refine the topic. I stripped away redundant command information, ensuring only core client usage and commands not better suited elsewhere remained. I personally walked through the client installation process on various operating systems, updating instructions, and had these validated by the support team.
    </p>
    <p class="text-gray-700 mb-3">
        This targeted approach—reducing noise, improving focus, and ensuring accuracy—across the Snowball Edge documentation led directly to the 30%  in upswing in customer satisfaction.
    </p>
</div>

<div class="project-card">
    <h3 class="text-xl font-semibold text-red-700 mb-2">S3 Documentation Updates with AI Tools</h3>
    <p class="text-gray-700 mb-3">
        I have contributed in a number of ways to the Simple Storage Service (S3) service documentation. In the last year, the service has grown from one to three bucket types to store objects. The documentation needed some follow-on work to include descriptions of the new bucket types and to update procedures to account for changes in the console interface to accommodate the new bucket types.
    </p>
    <p class="text-gray-700 mb-3">
        I collaborated with the service team and other members of the writing team to develop the new description of <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#BasicsBucket" class="text-red-700 hover:underline" target="_blank">bucket types</a> to include the new bucket types (directory and table buckets) and improve the description of the original bucket type (general purpose buckets). The description of each bucket type now clearly explains why customers would want to choose it, describes how access can be granted, and includes a link for detailed information.
    </p>
    <p class="text-gray-700 mb-3">
        To update procedures to account for the changes in the console interface, I used internal AI tools and a number of prompts to automate the work.
    </p>
    <ul class="list-disc pl-5 text-gray-700 space-y-1 mb-3">
        <li>I first ensured the tools understood the scope of the functionality of the new bucket types, because only procedures that included functionality of multiple bucket types would need to be changed.</li>
        <li>Then, I used the tools to identify the procedures that would need to be changed.</li>
        <li>Finally, I provided the tools the XML code to use to make the changes.</li>
        <li>For quality control, I spot-checked the changed code and used the text output as input to another AI tool to perform the procedures in the AWS console and identify any problems it found.</li>
    </ul>
    <p class="text-gray-700">
        Using AI as a work partner was more thorough and less prone to error than other methods, such as searching the documentation for topics that needed to be updated and updating them manually or through a large-scale change like find-replace.
    </p>
</div>

<p class="text-gray-700 font-semibold mb-4">Quick Links:</p>
<ul class="list-none flex flex-wrap gap-4 mb-8">
    <li><a href="#for-amazon-web-services-aws-section" class="text-red-700 hover:underline">For Amazon Web Services (AWS)</a></li>
    <li><a href="{{ site.baseurl }}/assets/other/article.pdf" class="text-red-700 hover:underline" target="_blank">Pleasing customers by the numbers (published article)</a></li>
    <li><a href="{{ site.baseurl }}/assets/other/hd_wi.pdf" class="text-red-700 hover:underline" target="_blank">Help desk agent work instruction</a></li>
    <li><a href="{{ site.baseurl }}/assets/other/lptp_trn.pdf" class="text-red-700 hover:underline" target="_blank">Laptop user's guide</a></li>
</ul>
<div class="project-card">
<h3 id="for-amazon-web-services-aws-section" class="text-2xl font-bold text-gray-900 mb-3">For Amazon Web Services (AWS)</h3>
<p class="text-gray-700 mb-4">
    While working at AWS, I have primarily supported two services: Snowball Edge and Simple Storage Service (S3). While supporting the Snowball Edge service, I was a solo writer and responsible for maintaining relationships with the product managers and software development managers of the service to be aware of feature releases and other service changes that affect the docs. I also was responsible for managing and triaging docs tickets for the service, scheduling docs work, and reporting on docs activities to the larger customer experience team as well as the service team.
</p>
<p class="text-gray-700 mb-4">
    For S3, I am a member of a docs team supporting one of the key AWS services. In this role, I am responsible for producing a wide range of docs, including API references, SDK code examples, and infrastructure-as-code framework. I also participate in the team's on-call rotation for ticket triage.
</p>
</div>
<div class="project-card">
<h3 id="as-a-help-desk-process-manager-section" class="text-2xl font-bold text-gray-900 mb-3 mt-6">As a Help Desk Process Manager</h3>
<p class="text-gray-700 mb-4">
    When I produced these items, I worked as an internal help desk agent and process manager for an international reinsurance corporation. As process manager, I performed technical writing tasks such as contributing information to the knowledgebase used to answer customers' questions and solve their issues, producing work instructions for help desk agents, and providing information to the rest of the company from the information technology department.
</p>
<p class="text-gray-700 mb-4">
    I was asked by the editors of *Support World* magazine to write an <a href="{{ site.baseurl }}/assets/other/article.pdf" class="text-red-700 hover:underline" target="_blank">article</a> about the help desk's experience collecting, analyzing, and acting on customer service metrics we collected as a customer satisfaction survey. I interviewed my manager, coworkers, and managers of other parts of the information technology staff for the article and worked with the publisher's editors on refining it.
</p>
<p class="text-gray-700 mb-4">
    The audience of the <a href="{{ site.baseurl }}/assets/other/hd_wi.pdf" class="text-red-700 hover:underline" target="_blank">work instruction</a> was help desk agents. It provides instructions to complete a process as part of a larger effort to solve a networking issue. Information in the knowledgebase would guide them to this process and then direct them to the next part of the effort. I produced it in Microsoft *Word* and from a template I created to automate including information in the first-page header using VBScript.
</p>
<p class="text-gray-700 mb-4">
    The <a href="{{ site.baseurl }}/assets/other/lptp_trn.pdf" class="text-red-700 hover:underline" target="_blank">selection of pages</a> from a laptop user's guide I produced in the same role. At the time (approximately 2000), the company was issuing laptop computers to some employees in replacement of the desktop computers. These people were expected to use the laptop computers while in the office as well as while working remotely. However, no training in doing so was provided.
</p>
<p class="text-gray-700 mb-4">
    We at the help desk became aware of this as calls and questions came to us about laptops and their use. Aware of this trend and with customers' questions and issues recorded by help desk agents, I went to management with the idea to provide an introductory training course and user's guide on the use of laptop computers and working remotely. My idea was approved and I produced the guide, had it printed internally by the corporate print shop, and arranged the details and resources of conducting the courses. Over approximately the next two years, I conducted the courses bi-monthly or as demand dictated, laptop users were provided copies of the guide when their desktop computers were replaced, and help desk metrics showed a decrease in questions about basic laptop use and working remotely.
</p>
<p class="text-gray-700">
    This sample contains descriptive, procedural, and troubleshooting types of information and artwork describing parts of a laptop. I produced the guide in Microsoft *Word*.
</p>
</div>
{% include api_demo.html %}