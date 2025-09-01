---
layout: default
title: Home
description: "Ed Grzetich's professional portfolio, featuring an API-driven resume, comprehensive writing samples from AWS and earlier career, and content strategy insights."    
---

<div class="project-card" markdown="1">

### Help Panel Component for AWS Amplify Framework

AWS sponsors a neat, open-source framework that anyone can use to integrate its services into Web and mobile apps. [AWS Amplify](https://aws.amazon.com/amplify) is a thorough framework to help developers easily combine functionality like authentication, data access, and storage with a modern UI to develop apps faster. What it lacks, however, is a way to provide help for users of Amplify apps. So, Claude and I created one.

In my work at AWS, I became very familiar with the AWS Management Console help panel. I've written content for it, debugged it, and helped engineers extend it to be used outside of the console. AWS customers, too, are very familiar with the help panel. It provides them a convenient way to get guidance on their tasks and also other resources in the AWS docs that might help.

Looking at the Amplify framework, I noticed it's designed to provide what developers need to get their apps up and running quickly. It provides components for authentication, storage, and maps and location search. I opened up Claude Code and got to work on creating a help panel component so Amplify apps could provide users what they need to use the apps.

**Key functionality:**
* **Context-sensitivity**: The content in the help panel needs to automatically change to reflect the part of the UI that is in use.
* **Hideable**: The help panel needs to be hideable when the user wants it out of the way. It shouldn't always be open, taking up valuable screen area (especially important for mobile apps).
* **Accessible**: The help panel includes ARIA labels and is compatible with screen readers. Its content is contained within JSON and can easily be localized.

This project showcases a unique set of skills outside of technical writing: context engineering for AI tools, open-source contribution, and problem-solving. It shows I can go beyond writing, taking initiative to discover feature gaps that affect users, and deliver content solutions that address these gaps and user needs.

**Tools used:**
*   Claude Code
*   GitHub
*   AWS Amplify Framework

[View Project Repository](https://github.com/grzetiche/amplify-ui-help-panel) | [View GitHub Issue](https://github.com/aws-amplify/amplify-js/issues/14512)

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