---
title: Application layer protocol
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> An **application layer protocol** defines the rules and conventions for communication between application [[Process#^6a45eb|processes]] running on different [[Host#^019621|hosts]]. It specifies the structure, meaning, and timing of messages exchanged.

^0376fb

- Application layer protocols define the following elements:
### Message Types
> [!note]+ Types of Messages Exchanged
> - **Request messages**: Client asks for service or data
> - **Response messages**: Server provides requested information
> - **Error messages**: Indicate problems or failures
> - **Status messages**: Provide information about system state
>
> Examples:
> - HTTP: `GET`, `POST`, `PUT`, `DELETE` (requests); 200 OK, 404 Not Found (responses)
> - SMTP: `MAIL FROM`, `RCPT TO`, `DATA` (commands); 250 OK, 550 Rejected (responses)
### Message Syntax
> [!note]+ Message Format and Structure
> - **Field organization**: How message fields are arranged
> - **Field delimiters**: Separators between fields (e.g., newlines, spaces)
> - **Header format**: Metadata about the message
> - **Body format**: Actual data being transmitted
>
> Example HTTP request syntax:
> ```
> GET /index.html HTTP/1.1
> Host: www.example.com
> User-Agent: Mozilla/5.0
> [blank line]
> ```
### Message Semantics
> [!note]+ Meaning of Messages and Fields
> - **Field interpretation**: What each field means
> - **Message purpose**: What each message type accomplishes
> - **Status codes**: Meaning of different response codes
> - **Error handling**: How to interpret error conditions
> Example: HTTP status code 404 means "requested resource not found"
### Message Timing
> [!note]+ Rules for When and How
> - **When to send**: Conditions triggering message transmission
> - **How to respond**: Required actions upon receiving messages
> - **Timeouts**: Maximum waiting times before retry or failure
> - **Message ordering**: Sequence requirements for messages
## Protocol Types
> [!success]+ Open Protocols
> **Definition**: Publicly available protocols with specifications defined in RFCs (Request for Comments)
>
> **Characteristics**:
> - Everyone has access to protocol definition
> - Standardized by organizations (IETF, W3C)
> - Interoperability between different implementations
> - Community-driven development
>
> **Examples**:
> - **HTTP**: Web communication
> - **SMTP**: Email transmission
> - **FTP**: File transfer
> - **DNS**: Domain name resolution
> - **SSH**: Secure shell access

> [!warning]+ Proprietary Protocols
> **Definition**: Privately owned protocols with specifications controlled by companies
>
> **Characteristics**:
> - Specification not publicly available
> - Controlled by single organization
> - May require licensing
> - Limited interoperability
>
> **Examples**:
> - **Skype**: Voice/video communication protocol
> - **Microsoft protocols**: Various Windows-specific protocols
> - **Apple protocols**: AirDrop, iMessage (partially proprietary)

> [!example]+ Common Application Layer Protocols
>
> |Protocol|Purpose|Port|Transport|
> |---|---|---|---|
> |HTTP|Web pages|80|TCP|
> |HTTPS|Secure web|443|TCP|
> |SMTP|Email sending|25|TCP|
> |POP3|Email retrieval|110|TCP|
> |IMAP|Email access|143|TCP|
> |FTP|File transfer|20, 21|TCP|
> |DNS|Name resolution|53|UDP/TCP|
> |SSH|Remote access|22|TCP|

> [!tip]+ Protocol Design Principles
> - Clear message formats and semantics
> - Efficient encoding and parsing
> - Extensibility for future features
> - Error handling and recovery
> - Security considerations
> - Backward compatibility
## Related Concepts
> [!note]+ See Also
> - Application protocols run on top of [[Transport Layer]] protocols
> - Use [[Socket#^d7aa97|sockets]] to communicate with transport layer
> - Support [[Client-server paradigm]] and [[Peer-to-peer paradigm#^08944a|Peer-to-peer paradigm]]
> - Examples: [[HTTP]], [[DNS protocol messages|DNS]]
