---
title: HTTP 2
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **HTTP/2** is a major revision of the [[HTTP]] protocol that introduces multiplexing, header compression, and server push capabilities to dramatically improve web performance over [[HTTP 1.1]].
## Key Features
> [!success]+ Decreased Delay
> **Reduced latency for multi-object HTTP requests**:
> - Parallel requests over single connection
> - No need for multiple TCP connections
> - Eliminates repeated handshakes

> [!success]+ Server Flexibility
> **Increased flexibility in sending objects to client**:
> - Transmission order based on client-specified priorities
> - Server can push unrequested objects to client proactively

> [!success]+ Frame-Based Architecture
> **Objects divided into frames**:
> - Schedule frames to mitigate Head-of-Line (HOL) blocking
> - Interleave multiple object transmissions
> - Better handling of varying object sizes
## Multiplexing
> [!info]+ Multiple Streams Per Connection
> **Single TCP connection carries multiple parallel streams**:
>
> ![[6341e74338991acb25c54bb96945137a.png]]
>
> **How it works**:
>
> - Each request/response is a separate stream
> - Streams are independent of each other
> - Data from different streams is interleaved
> - Stream IDs identify which frames belong together
>
> **Benefits**:
>
> - No more [[HTTP 1.1]] pipeline HOL blocking
> - Small responses don't wait behind large ones
> - Efficient use of single TCP connection
> - No need for domain sharding
## Stream Prioritization
> [!note]+ Priority Mechanism
> **Transmission order depends on client priority**:
> - Client assigns priority to each stream
> - Server uses priorities to schedule frame transmission
> - Critical resources (HTML, CSS) sent first
> - Images and other assets sent after
## Server Push
> [!info]+ Push Unrequested Objects
> **Server can send resources before client requests them**:
>
> **How it works**:
> 1. Client requests HTML page
> 2. Server analyzes page dependencies
> 3. Server pushes CSS, JS, images proactively
> 4. Resources already in client cache when needed
>
> **Example**:
> ```
> Client → Server: GET /index.html
> Server → Client: PUSH_PROMISE for /style.css
> Server → Client: PUSH_PROMISE for /script.js
> Server → Client: Response for /index.html
> Server → Client: Pushed /style.css
> Server → Client: Pushed /script.js
> ```
## Binary Framing Layer
> [!info]+ Binary vs Text
> **HTTP/2 uses binary encoding** (unlike [[HTTP 1.1]]'s text):
>
> **Structure**:
> - Messages broken into frames
> - Each frame has type, length, flags, stream ID
> - Binary format is more efficient to parse
> - Less error-prone than text parsing
>
> **Frame Types**:
> - **DATA**: Payload data
> - **HEADERS**: Header information
> - **PRIORITY**: Stream priority
> - **RST_STREAM**: Terminate stream
> - **SETTINGS**: Connection parameters
> - **PUSH_PROMISE**: Server push notification
> - **PING**: Connection health check
> - **GOAWAY**: Connection closure
> - **WINDOW_UPDATE**: Flow control
> - **CONTINUATION**: Header continuation
## Related Concepts
> [!note]+ See Also
> - **[[HTTP 1.1]]**: Previous version this improves upon
> - **[[HTTP]]**: Main protocol overview
> - **[[Persistent HTTP]]**: Connection model used
> - **[[RTT]]**: Performance metric
> - **[[TCP]]**: Underlying transport protocol (and its limitations)
> - **HTTP/3**: Next version using QUIC to solve TCP HOL
