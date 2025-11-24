---
title: HTTP 1.1
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **HTTP/1.1** is a major revision of the [[HTTP]] protocol that introduced [[Persistent HTTP|persistent connections]] as the default behavior and added request pipelining to improve performance over HTTP/1.0.
## Key Features
> [!success]+ Persistent Connections by Default
> - Multiple objects sent over single [[TCP]] connection
> - Connection remains open between requests
> - Must explicitly use `Connection: close` to disable
> - Dramatically reduces latency compared to [[Non-persistent HTTP]]

> [!success]+ Request Pipelining
> - **Multiple, pipelined GET requests over single TCP connection**
> - Client can send multiple requests without waiting for responses
> - Reduces idle time and improves throughput
>
> **How it works**:
>
> ```
> Client → Server: GET /page1.html
> Client → Server: GET /image1.jpg
> Client → Server: GET /style.css
> Server → Client: Response for /page1.html
> Server → Client: Response for /image1.jpg
> Server → Client: Response for /style.css
> ```

> [!success]+ Host Header
> - Required `Host:` header in all requests
> - Enables virtual hosting (multiple domains per IP)
> - Example: `Host: www.example.com`
## The HOL Blocking Problem
> [!example]+ HOL Blocking Scenario
> **Client requests**:
> - 1 large object (5 MB)
> - 3 smaller objects (50 KB each)
>
> ![[5b2e2233ce1ceaa32c5f4af5cd7c8b10.png]]
>
> **What happens**:
> 1. Client sends all 4 GET requests immediately (pipelined)
> 2. Server must send large object first (if requested first)
> 3. Small objects wait behind large object transmission
> 4. Total time dominated by large object
>
> **Impact**:
> - Small objects experience unnecessary delay
> - Cannot prioritize urgent resources
> - User perceives slow page load

> [!fail]+ TCP Loss Recovery Amplifies HOL
> **When packet loss occurs**:
> - TCP must retransmit lost segments
> - All subsequent data is held up
> - Entire pipeline stalls waiting for retransmission
> - Even objects not affected by loss are delayed
## Related Concepts
> [!note]+ See Also
> - **[[HTTP]]**: Main protocol overview
> - **[[Persistent HTTP]]**: Connection model introduced as default
> - **[[HTTP 2]]**: Next version that solves HOL blocking
> - **[[RTT]]**: Performance metric for measuring improvements
> - **[[Conditional GET]]**: Cache validation mechanism
> - **[[Non-persistent HTTP]]**: Previous connection model
