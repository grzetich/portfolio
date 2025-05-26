 I am a highly experienced technical writer and content strategist with a proven track record of delivering high-quality technical information and content solutions on diverse topics for diverse audiences in coordination with teams around the corner and around the world. Skilled in leveraging AI for content enhancement and driving measurable improvements in customer satisfaction.

  I get up to speed on new subject matter quickly, and I will make an immediate positive impact on your team's performance.

  View my [writing samples](#writing-samples) and [resumé](assets/other/Grzetich.pdf) or contact me via [email](mailto:ed.grzetich@gmail.com).

# Writing samples
These writing samples focus on work I did very early in my career and this year. The [most recent samples](#for-amazon-web-services-aws) highlight content strategy and metrics analysis I did resulting in higher customer satisfaction for documentation, a collaborative writing effort I lead to revise a highly-visible topic, and a task I substituted artificial intelligence (AI) tools for manual work to decrease error and risk.

The [earlier samples](#as-a-help-desk-process-manager) include work instructions for troubleshooting computer network issues, an article I wrote for an industry publication, and samples from a training course I created, wrote the material for, and conducted in person.

[For Amazon Web Services (AWS)](#for-amazon-web-services-aws) | [Pleasing customers by the numbers published article](/assets/other/article.pdf) | [Help desk agent work instruction](/assets/other/hd_wi.pdf)  |  [Laptop user's guide](/assets/other/lptp_trn.pdf) 

## For Amazon Web Services (AWS)
While working at AWS, I have primarily supported two services: Snowball Edge and Simple Storage Service (S3). While supporting the Snowball Edge service, I was a solo writer and responsible for maintaining relationships with the product managers and software development managers of the service to be aware of feature releases and other service changes that affect the docs. I also was responsible for managing and triaging docs tickets for the service, scheduling docs work, and reporting on docs activities to the larger customer experience team as well as the service team.

For S3, I am a member of a docs team supporting one of the key AWS services. In this role, I am responsible for producing a wide range of docs, including API references, SDK code examples, and infrastructure-as-code framework. I also participate in the team's on-call rotation for ticket triage.

### Snowball Edge service documentation
For the [Snowball Edge service documentation](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html), I improved customer satisfaction over 30%. I used data about the documentation content to identify topics in need of improvement in three areas:
* Poor customer sentiment.
* Low pageview.
* Subject of a high number of tickets.

I worked with members of the service and support teams to ensure content on the identified pages was correct and current and looked for opportunities to rewrite or combine topics that had little information or were separate from related topics and resulted in difficulty to find complete information on a subject or task. 

As a specific example, let's look at the [Configuring and using the Snowball Edge Client topic](https://docs.aws.amazon.com/snowball/latest/developer-guide/using-client-commands.html) in the AWS docs. This topic consistently received poor customer sentiment. When I reviewed it and compared it to the AWS styleguide and content strategy, I identified a number of issues:
* **The topic contained too much information.** It attempted to include all of the commands available in the Snowball Edge Client tool. 
* **The information it did contain was incomplete.** Often when a new feature was developed that had a new command for the client, it was include in another topic in the docs and wasn't added to the list in this topic. When an existing feature was upgraded or expanded, the information about the client commands weren't updated in this topic.
* **The topic contained the wrong type of information.** In reviewing the topic with members of the service and support teams, I learned that the topic didn't provide information about the basics of using the client, such as how to install it on supported operating systems and how to configure it for use. 
  
Before I introduce the ways I improved the topic, some background information about the AWS Snowball Edge service is as helpful. AWS Snowball Edge is unique in AWS because it is a physical device that customers rent and is shipped to them to move data to or from AWS S3 or to run AWS compute instances without a connection to AWS. This makes the Snowball Edge service and device unique among AWS services because it can't be used through the main AWS customer interface, the management console. Instead, while customers have the devices, they interact with they through the Snowball Edge Client. 

To improve this topic, I decided to reduce the content to cover the basic information about using the client and other commands that didn't have a better place in the docs. I carefully compared the information about commands in this topic to other locations in the docs to ensure coverage and removed that information from this topic. I downloaded and installed the client on the supported operating systems, updated the instructions for doing so, and had them reviewed by the support team. 

By decreasing the length of the topic, focusing the information it provides, and removing incorrect or incomplete information in this topic and others in the docs, I was able to improve the customer satisfaction of the docs for this service by 30%.

### S3
I have contributed in a number of ways to the Simple Storage Service (S3) service documentation. In the last year, the service has grown from one to three bucket types to store objects. The documentation needed some follow-on work to include descriptions of the new bucket types and to update procedures to account for changes in the console interface to accommodate the new bucket types. 

I collaborated with the service team and other members of the writing team to develop the new description of [bucket types](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#BasicsBucket) to include the new bucket types (directory and table buckets) and improve the description of the original bucket type (general purpose buckets). The description of each bucket type now clearly explains why customers would want to choose it, describes how access can be granted, and includes a link for detailed information.

To update procedures to account for the changes in the console interface, I used internal AI tools and a number of prompts to automate the work.
  * I first ensured the tools understood the scope of the functionality of the new bucket types, because only procedures that included functionality of multiple bucket types would need to be changed.
  * Then, I used the tools to identify the procedures that would need to be changed. 
  * Finally, I provided the tools the XML code to use to make the changes.
  * For quality control, I spot-checked the changed code and used the text output as input to another AI tool to perform the procedures in the AWS console and identify any problems it found.

Using AI as a work partner was more thorough and less prone to error than other methods, such as searching the documentation for topics that needed to be updated and updating them manually or through a large-scale change like find-replace. 

## As a help desk process manager
When I produced these items, I worked as an internal help desk agent and process manager for an international reinsurance corporation. As process manager, I performed technical writing tasks such as contributing information to the knowledgebase used to answer customers' questions and solve their issues, producing work instructions for help desk agents, and providing information to the rest of the company from the information technology department. 

I was asked by the editors of *Support World* magazine to write an [article](/assets/other/article.pdf) about the help desk's experience collecting, analyzing, and acting on customer service metrics we collected as a customer satisfaction survey. I interviewed my manager, coworkers, and managers of other parts of the information technology staff for the article and worked with the publisher's editors on refining it.

The audience of the [work instruction](/assets/other/hd_wi.pdf) was help desk agents. It provides instructions to complete a process as part of a larger effort to solve a networking issue. Information in the knowledgebase would guide them to this process and then direct them to the next part of the effort. I produced it in Microsoft *Word* and from a template I created to automate including information in the first-page header using VBScript. 

The [selection of pages](/assets/other/lptp_trn.pdf) from a laptop user's guide I produced in the same role. At the time (approximately 2000), the company was issuing laptop computers to some employees in replacement of the desktop computers. These people were expected to use the laptop computers while in the office as well as while working remotely. However, no training in doing so was provided. 

We at the help desk became aware of this as calls and questions came to us about laptops and their use. Aware of this trend and with customers' questions and issues recorded by help desk agents, I went to management with the idea to provide an introductory training course and user's guide on the use of laptop computers and working remotely. My idea was approved and I produced the guide, had it printed internally by the corporate print shop, and arranged the details and resources of conducting the courses. Over approximately the next two years, I conducted the courses bi-monthly or as demand dictated, laptop users were provided copies of the guide when their desktop computers were replaced, and help desk metrics showed a decrease in questions about basic laptop use and working remotely.

This sample contains descriptive, procedural, and troubleshooting types of information and artwork describing parts of a laptop. I produced the guide in Microsoft *Word*.
