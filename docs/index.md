---
layout: default
title: Home
description: "Ed Grzetich's professional portfolio, featuring an API-driven resume, comprehensive writing samples from AWS and earlier career, and content strategy insights."
---

<div class="hero">
    <h1>Ed Grzetich</h1>
    <p class="subtitle">Senior Technical Writer Specializing in Developer Documentation</p>

    <div class="value-props">
        <div class="value-prop">
            <span class="icon">📚</span>
            <p>API references and SDK guides that reduce time-to-integration</p>
        </div>
        <div class="value-prop">
            <span class="icon">✅</span>
            <p>Executable code examples validated through working applications</p>
        </div>
        <div class="value-prop">
            <span class="icon">📈</span>
            <p>Documentation systems that scale across distributed teams</p>
        </div>
        <div class="value-prop">
            <span class="icon">🚀</span>
            <p>AI-assisted workflows: 70% faster production, 30% better satisfaction</p>
        </div>
    </div>

    <p class="availability">Available for full-time positions and contract engagements.</p>
</div>

<section id="approach" class="approach-section">
    <h2>My Approach to Developer Documentation</h2>

    <p class="intro">I believe great developer documentation requires building, not just writing. Over 15 years, I've developed a methodology that combines:</p>

    <div class="approach-pillars">
        <div class="pillar">
            <h3>Deep Technical Understanding</h3>
            <ul>
                <li>I build working applications to validate API accuracy</li>
                <li>I debug integration issues to understand developer friction</li>
                <li>I test across platforms to ensure documentation completeness</li>
            </ul>
        </div>

        <div class="pillar">
            <h3>AI-Augmented Workflows</h3>
            <ul>
                <li>Using tools like Claude, GitHub Copilot, and Gemini to accelerate development</li>
                <li><strong>70% reduction</strong> in documentation production time at AWS</li>
                <li><strong>30% improvement</strong> in customer satisfaction through validated examples</li>
                <li>Focus on outcomes: documentation developers can trust</li>
            </ul>
        </div>

        <div class="pillar">
            <h3>Scalable Processes</h3>
            <ul>
                <li>Documentation systems that enable teams to contribute quality content</li>
                <li>CI/CD integration for automated validation</li>
                <li>Metrics-driven improvement cycles</li>
            </ul>
        </div>
    </div>

    <p class="approach-footer">This approach has proven successful across cloud services (AWS), payment platforms (Mastercard), and defense systems (General Dynamics).</p>
</section>

<div class="project">
    <h3>AWS Amplify Help Panel Component</h3>

    <div class="project-meta">
        <span class="tag">React</span>
        <span class="tag">JavaScript</span>
        <span class="tag">AWS Amplify</span>
        <span class="tag">AI-Assisted Development</span>
        <span class="tag">Open Source</span>
    </div>

    <div class="project-section">
        <h4>The Challenge</h4>
        <p>AWS Amplify framework lacked contextual help, creating friction for app users despite developers building on a robust framework. While the framework provides excellent components for authentication, storage, and UI development, there was no built-in way for app users to get help when they needed it.</p>
    </div>

    <div class="project-section">
        <h4>My Approach</h4>
        <p>Rather than just document the gap, I built a solution using AI-assisted development (Claude Code) to create a React component providing AWS Console-style help. Drawing on my experience writing content for and debugging the AWS Management Console help panel, I designed a component that brings the same familiar, helpful experience to Amplify-built applications.</p>
    </div>

    <div class="project-section">
        <h4>Technical Execution</h4>
        <ul>
            <li>React component with context-sensitivity and accessibility (ARIA labels)</li>
            <li>JSON-based content architecture for easy localization</li>
            <li>Integration with Amplify UI framework</li>
            <li>Hideable interface optimized for mobile and desktop experiences</li>
            <li>Automated content switching based on UI state</li>
        </ul>
    </div>

    <div class="project-section">
        <h4>Key Learnings</h4>
        <p>Great documentation sometimes means extending the product itself. Understanding developer frameworks well enough to contribute improvements demonstrates deep technical empathy. This project showcases skills beyond traditional technical writing: AI prompt engineering, open-source contribution, and proactive problem-solving to address user needs.</p>
    </div>

    <div class="project-section">
        <h4>Skills Demonstrated</h4>
        <p>React/JavaScript • AI-assisted development • Open-source contribution • Developer experience design • Accessibility • Content architecture</p>
    </div>

    <div class="project-links">
        <a href="https://github.com/grzetiche/amplify-ui-help-panel" target="_blank" class="btn btn-primary">View Repository</a>
        <a href="https://github.com/aws-amplify/amplify-js/issues/14512" target="_blank" class="btn btn-secondary">GitHub Issue</a>
    </div>
</div>

<div class="project-card" markdown="1">

### How Much Do Your Docs Cost to Read?

Did you know your audience has to pay to read your docs? They do if your audience is AI. I built a token cost calculator that lets you paste any structured documentation and see how many tokens it takes to represent it across different formats—JSON, YAML, JSON Compact, Plain Text—with cost estimates at scale.

It runs entirely in the browser using cl100k_base tokenization. No AI, no API keys needed, and nothing leaves your machine.

[Try the Calculator](https://doc-cost.vercel.app){: .btn .btn-primary target="_blank"}
[Read the Blog Post]({{ site.baseurl }}/blog/docs-cost-tool.html){: .btn .btn-secondary}

</div>

<div class="project-card" markdown="1">

### Architecting a Resilient Pokémon TCG Data API for LLM Integration

This project involved the development of a Python Flask API to serve comprehensive, real-time Pokémon Trading Card Game (TCG) data. The goal was to create a robust, accessible backend capable of supporting various applications, including seamless integration with Large Language Models (LLMs).

The journey from development to a fully operational backend presented several critical challenges:

*   Persistent Deployment Issues: Initial deployment attempts on a Platform-as-a-Service (PaaS) encountered elusive, low-level server termination errors (SIGTERM) that required extensive, systematic debugging beyond typical application logs.
*   Cloud Platform Migration: The necessity to pivot from one cloud provider to another, demanding adaptability in configuring environments, dependencies, and process management.
*   Complex LLM Interoperability: Designing a communication layer for LLM integration that adhered to the Model Context Protocol (MCP), involving intricate JSON-RPC messaging and standard I/O stream handling.

My solution involved a multi-faceted approach. I meticulously debugged the deployment issues, isolating environmental factors by simplifying the application and experimenting with various Python versions and Gunicorn configurations. This led to a strategic migration to Render.com, where the API was successfully deployed and now operates reliably, providing endpoints for card details, real-time pricing, set information, and more.

Furthermore, to enable LLM interaction, I developed a dedicated Python orchestrator. This component acts as a persistent local server, meticulously handling the JSON-RPC communication protocol, including message framing (Content-Length headers), and correctly processing standard protocol messages like initialize and shutdown. This ensures a stable and compliant bridge between LLMs (e.g., Claude) and the deployed Pokémon TCG API.

This project significantly deepened my expertise in backend architecture, cloud deployment, advanced troubleshooting, and the cutting-edge domain of LLM tooling and interoperability. It demonstrates my ability to build resilient systems and solve complex, multi-layered technical challenges from development through deployment and integration.

**Tools used:**
*   Microsoft Visual Studio Code
*   Render.com
*   GitHub
*   Google Gemini
*   Anthropic Claude Desktop

[View Project Repository on GitHub](https://github.com/grzetich/pokemon-tcg-mcp)

</div>

<div class="project-card" markdown="1">

### Spotlight: Enhancing the Snowball Edge Client Experience

Consider the [Configuring and using the Snowball Edge Client](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client-commands.html) topic, a prime example of my impact. This topic was a consistent source of user frustration. My comprehensive audit, aligned with AWS's style and content strategy, revealed:

*   Content bloat: It tried to be an exhaustive catalog of every available client command.
*   Inconsistent updates: New commands were often siloed in other documents, leaving this topic incomplete and out of sync.
*   Missing essentials: It failed to address the foundational knowledge users needed, such as how to install and configure the client.

It's helpful to understand that AWS Snowball Edge is unique: it's a physical device customers rent to move data or run compute instances without an AWS connection. This means users primarily interact with the service through the Snowball Edge Client, not the typical AWS management console.

My solution was to drastically refine the topic. I stripped away redundant command information, ensuring only core client usage and commands not better suited elsewhere remained. I personally walked through the client installation process on various operating systems, updating instructions, and had these validated by the support team.

This targeted approach—reducing noise, improving focus, and ensuring accuracy—across the Snowball Edge documentation led directly to the 30%  in upswing in customer satisfaction.

</div>

<!-- <div class="project-card" markdown="1">

### S3 Documentation Updates with AI Tools

I have contributed in a number of ways to the Simple Storage Service (S3) service documentation. In the last year, the service has grown from one to three bucket types to store objects. The documentation needed some follow-on work to include descriptions of the new bucket types and to update procedures to account for changes in the console interface to accommodate the new bucket types.

I collaborated with the service team and other members of the writing team to develop the new description of [bucket types](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#BasicsBucket) to include the new bucket types (directory and table buckets) and improve the description of the original bucket type (general purpose buckets). The description of each bucket type now clearly explains why customers would want to choose it, describes how access can be granted, and includes a link for detailed information.

To update procedures to account for the changes in the console interface, I used internal AI tools and a number of prompts to automate the work.

*   I first ensured the tools understood the scope of the functionality of the new bucket types, because only procedures that included functionality of multiple bucket types would need to be changed.
*   Then, I used the tools to identify the procedures that would need to be changed.
*   Finally, I provided the tools the XML code to use to make the changes.
*   For quality control, I spot-checked the changed code and used the text output as to another AI tool to perform the procedures in the AWS console and identify any problems it found.

Using AI as a work partner was more thorough and less prone to error than other methods, such as searching the documentation for topics that needed to be updated and updating them manually or through a large-scale change like find-replace.

</div> -->

{% include api_demo.html %}

<div class="project-card" markdown="1">

**Quick Links:**

*   [For Amazon Web Services (AWS)](#for-amazon-web-services-aws)
*   [Pleasing customers by the numbers (published article)]({{ site.baseurl }}/assets/other/article.pdf)
*   [Help desk agent work instruction]({{ site.baseurl }}/assets/other/hd_wi.pdf)
*   [Laptop user's guide]({{ site.baseurl }}/assets/other/lptp_trn.pdf)

</div>

<div class="project-card" markdown="1">

### For Amazon Web Services (AWS)

While working at AWS, I have primarily supported two services: Snowball Edge and Simple Storage Service (S3). While supporting the Snowball Edge service, I was a solo writer and responsible for maintaining relationships with the product managers and software development managers of the service to be aware of feature releases and other service changes that affect the docs. I also was responsible for managing and triaging docs tickets for the service, scheduling docs work, and reporting on docs activities to the larger customer experience team as well as the service team.

For S3, I am a member of a docs team supporting one of the key AWS services. In this role, I am responsible for producing a wide range of docs, including API references, SDK code examples, and infrastructure-as-code framework. I also participate in the team's on-call rotation for ticket triage.

</div>

<div class="project-card" markdown="1">

### As a Help Desk Process Manager

When I produced these items, I worked as an internal help desk agent and process manager for an international reinsurance corporation. As process manager, I performed technical writing tasks such as contributing information to the knowledgebase used to answer customers' questions and solve their issues, producing work instructions for help desk agents, and providing information to the rest of the company from the information technology department.

I was asked by the editors of *Support World* magazine to write an [article]({{ site.baseurl }}/assets/other/article.pdf) about the help desk's experience collecting, analyzing, and acting on customer service metrics we collected as a customer satisfaction survey. I interviewed my manager, coworkers, and managers of other parts of the information technology staff for the article and worked with the publisher's editors on refining it.

The audience of the [work instruction]({{ site.baseurl }}/assets/other/hd_wi.pdf) was help desk agents. It provides instructions to complete a process as part of a larger effort to solve a networking issue. Information in the knowledgebase would guide them to this process and then direct them to the next part of the effort. I produced it in Microsoft *Word* and from a template I created to automate including information in the first-page header using VBScript.

The [selection of pages]({{ site.baseurl }}/assets/other/lptp_trn.pdf) from a laptop user's guide I produced in the same role. At the time (approximately 2000), the company was issuing laptop computers to some employees in replacement of the desktop computers. These people were expected to use the laptop computers while in the office as well as while working remotely. However, no training in doing so was provided.

We at the help desk became aware of this as calls and questions came to us about laptops and their use. Aware of this trend and with customers' questions and issues recorded by help desk agents, I went to management with the idea to provide an introductory training course and user's guide on the use of laptop computers and working remotely. My idea was approved and I produced the guide, had it printed internally by the corporate print shop, and arranged the details and resources of conducting the courses. Over approximately the next two years, I conducted the courses bi-monthly or as demand dictated, laptop users were provided copies of the guide when their desktop computers were replaced, and help desk metrics showed a decrease in questions about basic laptop use and working remotely.

This sample contains descriptive, procedural, and troubleshooting types of information and artwork describing parts of a laptop. I produced the guide in Microsoft *Word*.

</div>

<section id="work-with-me" class="work-section">
    <h2>Let's Work Together</h2>

    <p class="intro">I'm open to opportunities that leverage my expertise in API documentation and developer-focused technical writing.</p>

    <div class="engagement-types">
        <div class="engagement">
            <h3>Full-Time Roles</h3>
            <p>Senior Technical Writer positions focused on developer documentation, API references, and SDK guides</p>
        </div>

        <div class="engagement">
            <h3>Contract Engagements</h3>
            <p>Documentation audits, API documentation projects, developer portal development, documentation system architecture</p>
        </div>
    </div>

    <div class="what-i-bring">
        <h3>What I Bring</h3>
        <ul>
            <li>15+ years proven experience across major tech companies</li>
            <li>AI-assisted workflows with measurable efficiency gains</li>
            <li>Ability to ramp quickly on complex technical products</li>
            <li>Remote work track record</li>
        </ul>
    </div>

    <div class="cta-buttons">
        <a href="mailto:ed.grzetich@gmail.com" class="btn btn-primary">Contact Me</a>
        <a href="{{ site.baseurl }}/styled-resume.html" class="btn btn-secondary">View Resume</a>
        <a href="https://github.com/grzetiche" class="btn btn-secondary" target="_blank">GitHub Profile</a>
    </div>
</section>