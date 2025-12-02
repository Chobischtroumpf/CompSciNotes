---
title: Proxy server
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> A **proxy server** (or web cache) is an intermediary server that satisfies client HTTP requests without involving the origin server. It acts as both a client (to origin servers) and a server (to requesting clients).

> [!abstract]- Core Functions
> **Primary Goals**:
> - Reduce response time for client requests (cache is closer to client)
> - Reduce traffic on access links
> - Reduce load on origin servers
> - Improve overall network performance

## How Proxy Servers Work

> [!note]+ Basic Operation
> **Setup**:
> 1. User configures browser to point to the proxy server
> 2. Browser sends all HTTP requests to the proxy
>
> **Request Handling**:
> - **If object is in cache**:
>     - Proxy returns cached object directly to client
>     - Fast response, no origin server contact needed
> - **If object is not in cache**:
>     - Proxy requests object from origin server
>     - Proxy caches the received object
>     - Proxy returns object to client

![[5defd22b40547e426cb5619181616680.png]]

> [!tip]+ Dual Role
> The proxy server acts as:
> - **Server** to the original requesting client
> - **Client** to the origin server
>
> This dual nature allows it to intercept and optimize communication.

## Performance Analysis

> [!example]+ Scenario Without Proxy
> **Network Configuration**:
> - Access link rate: 1.54 Mbps
> - RTT from institutional router to server: 2 seconds
> - Web object size: 100 Kbits
> - Average request rate from browsers: 15 requests/second
> - Average data rate to browsers: 1.50 Mbps (15 req/s × 100 Kbits)
>
> **Performance Results**:
> - **LAN utilization**: 0.0015 (0.15%)
> - **Access link utilization**: 0.97 (97%) ⚠️ Very high!
> - **End-to-end delay**: Internet delay + access link delay + LAN delay
>     - = 2 sec + **minutes** (due to queueing) + microseconds
>     - **Total**: Several minutes (unacceptable!)
>
> ![[1b4aff587d75cdfcf59a09c8ed51fef1.png]]

> [!warning]+ The Bottleneck Problem
> Even if we multiply the access link speed by 100:
> - Speed improvement is minimal
> - Access link upgrade costs a lot more
> - Not a cost-effective solution

## Solution: Web Cache (Proxy)

> [!example]+ Scenario With Proxy
> **Assumptions**:
> - Cache hit rate: 0.4 (40% of requests satisfied from cache)
> - 60% of requests still go to origin server
>
> **Performance Calculations**:
> - Data rate to browsers over access link = 0.6 × 1.50 Mbps = 0.9 Mbps
> - **Access link utilization** = 0.9 / 1.54 = 0.58 (58%) ✓ Much better!
>
> **Average End-to-End Delay**:
> - = 0.6 × (delay from origin servers) + 0.4 × (delay from cache)
> - = 0.6 × (2.01 sec) + 0.4 × (milliseconds)
> - ≈ **1.2 seconds** ✓ Dramatic improvement!
>
> ![[9d6b80108a2150dda74713b935575eef.png]]

> [!success]+ Benefits
> - **Response time**: Reduced from minutes to ~1.2 seconds
> - **Link utilization**: Reduced from 97% to 58%
> - **Cost**: No expensive link upgrade needed
> - **Origin server load**: Reduced by 40%

## Proxy Types

> [!info]+ Forward Proxy
> - Client-side proxy
> - Configured by client/network
> - Used by clients to access external servers
> - Example: Corporate proxy for employee internet access

> [!info]+ Reverse Proxy
> - Server-side proxy
> - Configured by server/website
> - Clients may not know they're accessing a proxy
> - Example: CDN nodes serving website content

> [!info]+ Transparent Proxy
> - Intercepts traffic without client configuration
> - Client unaware of proxy
> - Often used by ISPs
> - Example: ISP caching proxy

## Related Concepts

> [!note]+ See Also
> - Uses [[HTTP#^d88595|HTTP]] protocol for web communication
> - Improves performance of [[Client-server paradigm]]
> - Reduces [[Network delay#^292b30|network delay]] for cached content
> - Affects [[Throughput#^325f00|throughput]] on access links
> - Works at [[Application layer protocol#^0376fb|application layer]]

> [!tip]+ Modern Evolution
> **Content Delivery Networks (CDNs)**:
> - Distributed proxy servers worldwide
> - Examples: Cloudflare, Akamai, CloudFront
> - Even better performance than single proxy
> - Serve content from geographically closest location
