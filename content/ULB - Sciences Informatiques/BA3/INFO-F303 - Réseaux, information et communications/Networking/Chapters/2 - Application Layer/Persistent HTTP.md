---
title: Persistent HTTP
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Persistent HTTP** is an [[HTTP#^d88595|HTTP]] connection model where multiple objects can be sent over a single [[TCP]] connection, which remains open until explicitly closed. This approach significantly reduces latency and overhead compared to [[Non-persistent HTTP#^cf8bb7|non-persistent HTTP]].
## How It Works
> [!abstract]- Connection Lifecycle
> **Connection Reuse**:
> 1. TCP connection is opened once
> 2. Multiple objects are transmitted over the same connection
> 3. Connection stays open until client or server closes it
>
> **Key Mechanism**:
> - Server leaves connection open after sending response
> - Subsequent messages between same client/server use the same connection
> - Client sends requests as soon as it encounters referenced objects
## Performance Advantages
> [!success]+ Reduced Latency
> **As little as one [[RTT]] for all referenced objects when requests are pipelined**
>
> **Comparison**:
> - [[Non-persistent HTTP]]: 2 RTT per object
> - Persistent HTTP: 2 RTT for first object, then ~1 RTT per additional object
> - With pipelining: Can send multiple requests without waiting for responses
## Request Pipelining
> [!info]+ How Pipelining Works
> **Client sends requests back-to-back without waiting for responses**:
> ```
> Time 0:   Send GET request for object 1
> Time 0:   Send GET request for object 2
> Time 0:   Send GET request for object 3
> Time RTT: Receive response for object 1
> Time RTT: Receive response for object 2
> Time RTT: Receive response for object 3
> ```

> [!example]+ Performance Example
> For a page with 10 embedded objects:
>
> **[[Non-persistent HTTP]]**:
> - Total: ~22 RTT (2 RTT × 11 objects)
>
> **Persistent HTTP (no pipelining)**:
> - Total: ~12 RTT (2 RTT + 10 RTT)
>
> **Persistent HTTP (with pipelining)**:
> - Total: ~3 RTT (2 RTT for first, then overlapped requests)
## Connection Management
> [!note]+ Connection Headers
> **HTTP/1.1 Headers**:
> ```
> Connection: keep-alive
> Keep-Alive: timeout=5, max=100
> ```
>
> **Parameters**:
> - `timeout`: Seconds to keep connection open while idle
> - `max`: Maximum number of requests per connection

> [!note]+ Connection Closure
> **When Connections Close**:
> - Client sends `Connection: close` header
> - Server timeout expires
> - Maximum requests reached
> - Error conditions
> - Server explicitly closes connection

> [!caution]+ Head-of-Line Blocking
> **In HTTP/1.1 with pipelining**:
> - Responses must be sent in order
> - Large response can block smaller ones
> - Solved in [[HTTP 2]] with multiplexing
## Related Concepts
> [!note]+ See Also
> - **[[Non-persistent HTTP]]**: The older approach this improves upon
> - **[[HTTP 1.1]]**: Protocol version that made this the default
> - **[[HTTP 2]]**: Next evolution with multiplexing
> - **[[RTT]]**: Key metric showing performance improvements
> - **[[HTTP]]**: Main protocol overview
> - **[[TCP]]**: Underlying transport protocol
