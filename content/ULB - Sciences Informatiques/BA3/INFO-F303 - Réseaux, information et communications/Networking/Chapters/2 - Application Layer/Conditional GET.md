---
title: Conditional GET
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Conditional GET** is an [[HTTP]] mechanism that allows a client to request a resource only if it has been modified since a specific date or version, preventing unnecessary data transfer when the client's cached copy is still valid.

> [!tip]+ Why Conditional `GET`?
> **Don't send object if cache has up-to-date version**:
> - Saves bandwidth
> - Reduces server load
> - Faster response for user
> - Lower latency
> - Reduced network congestion
## How Conditional GET Works
> [!note]+ Client Side (Cache)
> **Cache specifies date of cached copy in [[HTTP request message|HTTP request]]**:
>
> **Request Headers**:
> ```
> GET /document.html HTTP/1.1
> Host: www.example.com
> If-Modified-Since: Wed, 21 Oct 2025 07:28:00 GMT
> ```
>
> **Alternative (using ETag)**:
> ```
> GET /document.html HTTP/1.1
> Host: www.example.com
> If-None-Match: "686897696a7c876b7e"
> ```

> [!note]+ Server Side
> **Server response depends on modification status**:
>
> **If object has NOT been modified**:
> ```
> HTTP/1.0 304 Not Modified
> Date: Thu, 22 Oct 2025 08:15:00 GMT
> ETag: "686897696a7c876b7e"
> Cache-Control: max-age=3600
> ```
> - **No object body sent** (saves bandwidth!)
> - Status code 304
> - Client uses cached version
>
> **If object HAS been modified**:
> ```
> HTTP/1.1 200 OK
> Date: Thu, 22 Oct 2025 08:15:00 GMT
> Last-Modified: Wed, 21 Oct 2025 12:00:00 GMT
> ETag: "new-etag-value-123"
> Content-Length: 1234
>
> [new object data]
> ```
> - Status code 200
> - Full object in response body
> - Client updates cache

![[Pasted image 20251027155202.png]]
## Related Concepts
> [!note]+ See Also
> - **[[HTTP]]**: Main protocol framework
> - **[[HTTP response message]]**: 304 status code details
> - **[[HTTP request message]]**: Validation headers
> - **[[Proxy server]]**: Web caches that use conditional GET
> - **[[HTTP 1.1]]**: Protocol version that refined conditional GET
> - **[[RTT]]**: Performance metric - conditional GET saves RTT + transmission time
