---
title: Non-persistent HTTP
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Non-persistent HTTP** is an [[HTTP]] connection model where at most one object is sent over a single [[TCP]] connection, after which the connection is closed. Multiple objects require multiple separate connections.

^cf8bb7

## How It Works
> [!abstract]- Connection Lifecycle
> **For Each Object**:
> 1. TCP connection is opened
> 2. One object is transmitted
> 3. TCP connection is closed
>
> **Multiple Objects**:
> - Require multiple sequential or parallel connections
> - Each connection has its own setup and teardown overhead
## Performance Analysis
> [!example]+ Loading a Web Page
> User enters URL: `www.someSchool.edu/someDepartment/home.index`
>
> **Process**:
> ![[Pasted image 20251020125308.png]]
> ![[Pasted image 20251020125359.png]]
>
> **Timing Breakdown**:
> 1. **First [[RTT]]**: TCP connection setup (SYN/SYN-ACK)
> 2. **Second RTT**: HTTP request and response start
> 3. **File transmission**: Remaining data transfer
>
> **Total Response Time**:
> ```
> Response time = 2 RTT + file transmission time
> ```
>
> Where: `file transmission time = file size / average TCP throughput`
## Issues with Non-Persistent HTTP
> [!fail]+ High Latency
> - **Requires 2 [[RTT|RTTs]] per object**
> - First RTT: TCP handshake
> - Second RTT: HTTP request/response
> - Additional time for file transmission
>
> For a page with 10 objects:
> - Base HTML: 2 RTT
> - 10 embedded objects: 20 RTT
> - **Total: 22 RTT** (plus transmission times)

> [!fail]+ Resource Overhead
> - **OS overhead for each TCP connection**
> - Connection setup and teardown costs
> - Memory allocation for each connection
> - Connection state management
> - Significant server load with many clients

> [!fail]+ Inefficiency
> - **Cannot reuse connections**
> - TCP slow start for each object
> - Wasted bandwidth on repeated handshakes
> - Poor utilization of available bandwidth
## Mitigation Strategy
> [!tip]+ Parallel Connections
> **Browsers' Solution**:
> - Open multiple parallel TCP connections simultaneously
> - Fetch several objects concurrently
> - Reduces total page load time
>
> **Typical Behavior**:
> - Browsers open 6-8 parallel connections per domain
> - Still incurs overhead, but amortized across objects
> - Doesn't solve fundamental inefficiency

> [!example]+ Parallel vs Sequential
> **Sequential (one at a time)**:
> - Total time = 2RTT × N objects
>
> **Parallel (6 connections)**:
> - Total time ≈ 2RTT × ⌈N/6⌉ objects
>
> For 12 objects with RTT = 100ms:
> - Sequential: 2.4 seconds (just connection overhead!)
> - Parallel (6): 400ms (connection overhead)
