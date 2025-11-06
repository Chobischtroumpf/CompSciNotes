---
title: HTTP
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **HTTP (HyperText Transfer Protocol)** is the Web's [[Application layer protocol|application layer protocol]]. Clients (browsers) request, receive, and display web objects. Servers respond with objects in return.

^d88595

![[Pasted image 20251020123729.png]]
> [!note]+ HTTP and TCP
> HTTP uses [[TCP]] as its transport protocol:
> **Connection Process**:
> 1. Client initiates TCP connection to server using [[Socket|sockets]] (default port 80)
> 2. Server accepts TCP connection from client
> 3. HTTP messages are exchanged between browser and web server
> 4. TCP connection is closed (or kept alive for reuse)
>
> **Benefits**:
> - Reliable data transfer
> - Ordered delivery guaranteed
> - Flow control and congestion control

> [!tip]+ Port Numbers
>
> - **HTTP**: Port 80 (standard)
> - **HTTPS**: Port 443 (secure)

> [!note]+ Stateless Protocol
> - HTTP is Stateless: **the server maintains no information about past client requests.**
>
> **Implications**
> - Each request is completely independent
> - Server doesn't remember previous interactions
> - Simplifies server design and improves scalability
>
> **Maintaining State When Needed**:
> - **Cookies**: Client-side state storage
> - **Session databases**: Server-side state storage
> - **URL parameters**: State passed in request
> - **Hidden form fields**: State embedded in pages

> [!info]+ HTTP Versions
> - HTTP has evolved through several versions, each improving performance and capabilities:
> 	- **[[Non-persistent HTTP]]**: Original approach, one object per connection
> 	- **[[Persistent HTTP]]**: Connection reuse for multiple objects
> 	- **[[HTTP 1.1]]**: Pipelined requests, persistent connections
> 	- **[[HTTP 2]]**: Multiplexing, server push, improved performance
> 	- **HTTP/3**: Built on QUIC (UDP-based) for better performance

> [!info]+ HTTP Messages
> - HTTP communication consists of two types of messages:
> 	- **[[HTTP request message]]**: Client asks for resources
> 	- **[[HTTP response message]]**: Server provides requested content
## HTTP Features
> [!note]+ Performance Concepts
>
> - **[[RTT]]**: Round-Trip Time measurement
> - **[[Conditional GET]]**: Efficient caching mechanism
> - Connection management strategies

> [!note]+ Caching
>
> - **[[Proxy server]]**: Web caches for improved performance
> - Content validation
> - Cache control headers
## Related Concepts
> [!note]+ See Also
> - Works at the [[Application layer protocol|application layer]]
> - Uses [[TCP]] for reliable transport
> - Follows [[Client-server paradigm]]
> - Communication through [[Socket|sockets]]
> - Used by [[Process|processes]] to exchange data
