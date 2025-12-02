---
title: RTT
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **RTT (Round-Trip Time)** is the time required for a small [[Packet|packet]] to travel from client to server and back. It's a fundamental metric for measuring network latency and is critical for understanding [[HTTP]] performance.

![[d778930455842eb4007ebb01de9317e7.png]]

## RTT Measurement

> [!note]+ Components of RTT **RTT includes**:
>
> - **Propagation delay**: Time for signal to travel through medium
> - **Transmission delay**: Time to push bits onto link
> - **Processing delay**: Time for routers/switches to process packet
> - **Queueing delay**: Time waiting in buffers
>
> **Formula**:
>
> ```
> RTT ≈ 2 × (propagation + transmission + processing + queueing)
> ```
>
> (Factor of 2 because packet travels to server AND back)

## Measuring RTT

> [!info]+ Common Tools
> **ping**:
> ```bash
> ping www.example.com
> ```
>
> - Measures ICMP RTT
> - May not reflect actual HTTP RTT
>
> **traceroute/tracert**:>
> ```bash
> traceroute www.example.com
> ```
>
> - Shows RTT to each hop
> - Identifies bottlenecks
>
> **Browser Developer Tools**:
> - Network tab shows timing
> - Breaks down request phases
> - Shows actual HTTP RTT

## Related Concepts

> [!note]+ See Also
> - **[[Network delay]]**: Comprehensive view of all delay types
> - **[[HTTP]]**: Protocol that RTT directly affects
> - **[[Persistent HTTP]]**: Reduces number of RTTs needed
> - **[[HTTP 1.1]]**: Protocol version addressing RTT issues
> - **[[HTTP 2]]**: Further RTT optimizations
> - **[[Non-persistent HTTP]]**: Worst-case RTT impact
> - **[[Throughput]]**: Bandwidth metric complementing RTT
> - **[[TCP]]**: Transport protocol requiring RTT for handshake
