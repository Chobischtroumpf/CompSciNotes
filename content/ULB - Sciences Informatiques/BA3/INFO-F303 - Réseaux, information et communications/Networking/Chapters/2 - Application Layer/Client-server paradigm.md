---
title: Client-server paradigm
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **client-server paradigm** is a distributed application architecture where clients request services from always-on servers.

![[01d218d0fe8231b6dd34d5089679e6c9.png]]

## Characteristics

> [!note]+ Server
> - **Always-on host**
> - **Permanent IP address**
> - Often located in data centers
> - Waits for client requests
> - Provides services/resources

> [!note]+ Clients
> - **Communicate with server** (not directly with each other)
> - **May be intermittently connected**
> - **May have dynamic IP addresses**
> - Initiate requests to server
> - Consume services/resources
> |**Examples**|Web, email|BitTorrent, Skype calls|

> [!example]+ Common Client-Server Applications
> - **Web**: Browser (client) ↔ Web server
> - **Email**: Mail client ↔ Mail server (SMTP, IMAP, POP3)
> - **DNS**: Resolver (client) ↔ DNS server
> - **File transfer**: FTP client ↔ FTP server

## Related Concepts

> [!note]+ See Also
> - [[Peer-to-peer paradigm]]: Alternative architecture
> - [[Process]]: Clients and servers are processes
> - [[Socket]]: Communication interface used
> - [[HTTP]]: Common client-server protocol
