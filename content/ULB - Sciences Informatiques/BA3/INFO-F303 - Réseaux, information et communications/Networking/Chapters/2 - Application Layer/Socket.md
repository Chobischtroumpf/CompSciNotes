---
title: Socket
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> A **socket** is the interface between the application layer and the transport layer within a host. Processes use sockets to send and receive messages to/from other processes.

^d7aa97

> [!abstract]- How Sockets Work
> **Communication Process**:
> - The sending process pushes the message out through the socket (like a door)
> - The sending process relies on the transport infrastructure on the other side to deliver the message to the receiving socket
> - Each communication requires one socket on each side (sender and receiver)
>
> **Socket Analogy**:
> - Think of a socket as a door between the application process and the transport layer
> - The application has control on the application-layer side
> - The transport layer handles delivery on the other side
>
> ![[252da51f298964b17d4639fc7db80048.png]]

> [!note]+ Socket Identification
> To receive messages, a process must have an identifier that includes:
> - **IP address** of the host
> - **Port number** associated with the process on the host
>
> Example port numbers:
> - HTTP server: port 80
> - SMTP mail server: port 25

## Related Concepts

> [!note]+ See Also
> - See [[Socket programming]] for implementation details
> - Sockets are used in both [[Client-server paradigm]] and [[Peer-to-peer paradigm]]
> - Transport layer protocols ([[TCP]], [[UDP]]) operate through sockets
