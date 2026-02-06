# Lab 3

## Team Members
- Janessa Techathamawong

## Lab Question Answers

All answers of the lab questions are done using the website https://aws.amazon.com/what-is/restful-api/.

Why are RESTful APIs scalable?
RESTful APIs are scalable because REST optimizes client-server interactions by being 1) statelessness, as each request from a client contains everything the server needs to handle it, and doesn’t need to retain past client request information, and 2) having well-managed caching, as REST responses explicitly states whether they can be cached, partially or completely eliminates some client-server interactions. Both of these features support scalability without causing communication blockages that reduce performance.

According to the definition of “resources” provided in the AWS article above, what are the resources the mail server is providing to clients?
The mail server’s resources are users’ email messages and the structures that organize and manage them (mailboxes, metadata, and attachments).

What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
The mail server does not use the PUT method, but uses GET, POST, and DELETE. It could be extended to use PUT to update existing resources such as marking emails as read or moving them between folders.

Why are API keys used for many RESTful APIs? What purpose do they serve?
API keys allow RESTful APIs to authenticate and identify clients by requiring a unique key with each request, enabling access control and usage tracking, though they are less secure since the key is transmitted over the network, making it vulnerable to network theft.