---
layout: posts
title: Help panel component for AWS Amplify framework
date: 2025-08-12 10:00:00 -0400
categories: [Technical Writing, Web Development, AI]
hero_image: /assets/images/amplify-help-panel.png
description: "Extending an open-source framework for user assistance."
---
AWS sponsors a neat, open-source framework that anyone can use to integrate its services into Web and mobile apps. [AWS Amplify](https://aws.amazon.com/amplify) is a thorough framework to help developers easily combine functionality like authentication, data access, and storage with a modern UI to develop apps faster. What it lacks, however, is a way to provide help for users of Amplify apps. So, Claude and I created one.

In my work at AWS, I became very familiar with the AWS Management Console help panel. I've written content for it, debugged it, and helped engineers extend it to be used outside of the console. AWS customers, too, are very familiar with the help panel. It provides them a convenient way to get guidance on their tasks and also other resources in the AWS docs that might help.

Looking at the Amplify framework, I noticed it's designed to provide what developers need to get their apps up and running quickly. It provides components for authentication, storage, and maps and location search. I opened up Claude Code and got to work on creating a help panel component so Amplify apps could provide users what they need to use the apps.

## Key functionality
I wanted the help panel to share some key functionality with the management console help panel:   
* **Context-sensitivity**: The content in the help panel needs to automatically change to reflect the part of the UI that is in use. 
* **Hideable**: The help panel needs to be hideable when the user wants it out of the way. It shouldn't always be open, taking up valuable screen area (especially important for mobile apps).
* **Accessible**: The help panel includes ARIA labels and is compatible with screen readers. Its content is contained within JSON and can easily be localized.

## Working with Claude Code
I knew this would make a great project for Claude Code. The Amplify framework is well documented, giving Claude excellent context for its work, and the key functionality I wanted to implement was clear and brief.

I gave Claude Code my requirements and pointed it to the Amplify documentation. I also provided a resource about contributing to the project, so it could make informed decisions like which language to use to implement the component and how to structure the project. Here was the initial context:
>* We're going to create a new component for the Amplify framework. Here are the framework docs (https://docs.amplify.aws/) and the library of UI components (https://docs.amplify.aws/). When we're done, we're going to contribute it to the Amplify repository, so it's important that we follow the contribution guidelines (https://docs.amplify.aws/contribute/getting-started/) throughout the project.
>* The new component is a help panel that can be used for any Amplify app. It needs to have the following functionality:
    * The content in the help panel needs to automatically change to reflect the part of the UI that is in use. 
    * The help panel needs to be hideable when the user wants it out of the way. It shouldn't always be open, taking up valuable screen area (especially important for mobile apps).
    * The help panel includes ARIA labels and is compatible with screen readers. Its content should be contained outside of the code used to display it so that it can be easily edited and localized.
>* You'll need to create a demo that I can use.
>* You'll need to create tests, run them, and show me the results.

With that, Claude Code went to work. It showed me the code it was writing and explained its steps and how they related to the functional requirements for the component and the contribution guidelines. In a few minutes, it launched a local build of the demo. I reviewed it and made some suggestions, it incorporated them, and I asked it to restart the local build so I could see them. After a few rounds of testing like this and some successful tests, we had a good contribution to the project. I also asked it to create a `CLAUDE.md` file for the project, add to it the information it found useful, and to include the file in `.gitignore`.

To complete the project, Claude and I worked together on a readme for the component's repository and the issue description for the Amplify repository. The [issue](https://github.com/aws-amplify/amplify-js/issues/14512) is in consideration and the [help panel repository](https://github.com/grzetiche/amplify-ui-help-panel) is available, including the demo that Claude created.

## Technical skills demonstrated
This project showcases unique set of skills outside of technical writing:
* Context engineering: The context I provided to it was an important part of a successful project. There were no hallucinations during Claude's work and the code it produced worked the first time and passed testing.
* Open-source contribution: With Claude Code's help, I was able to produce a high-quality contribution to an open-source project, including a robust feature request and a fully-functional demo.
* Problem-solving: I saw an opportunity to help make a user interface better for users and took concrete, measurable steps to implement it.

## Why this matters for my portfolio

It shows I can go beyond writing, taking initiative to discover feature gaps that affect users, and deliver content solutions that address these gaps and user needs. In doing so, I'm contributing to an open-source project which demonstrates cross-functional collaboration, remote teamwork, and clear communication. Finally, the help panel component demonstrates my ability to effectively use AI-assisted coding and context engineering to quickly produce a real product that addresses a need. 