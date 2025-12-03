---
title: Port Queueing
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Port queueing** occurs when packets arrive at router ports faster than they can be processed or transmitted. Queueing can happen at both input ports (before the [[Switching Fabric|switching fabric]]) and output ports (before transmission), leading to delays and potential packet loss.

## Input Port Queueing

> [!warning]+ When Fabric Is the Bottleneck
> **Condition for input queueing:**
> $$\text{Switch fabric rate} < \sum_{i=1}^{N} \text{Input port rate}_i$$
>
> **Consequences:**
> - Queueing delay at input buffers
> - Packet loss due to input buffer overflow
> - Head-of-line (HOL) blocking

### Head-of-Line Blocking

> [!abstract]+ HOL Blocking Problem
> ![[db110b18d02a2eba279f877fbfaf9fad.png]]
>
> **Scenario:**
> - Multiple input queues with packets destined for different outputs
> - Output port contention: only one packet can be transferred per output port
>
> **HOL blocking occurs when:**
> - A packet at the head of an input queue is blocked (output busy)
> - Packets behind it cannot proceed, even if their outputs are free

> [!example]+ HOL Blocking Example
> **Initial situation:**
> - Red packets in two queues destined for same output
> - Only one red packet can transfer; other is blocked
>
> **One packet time later:**
> - Green packet blocked behind red packet
> - Green packet's output port is free, but it cannot proceed
> - Results in unnecessary delay

## Output Port Queueing

> [!warning]+ When Link Is the Bottleneck
> ![[d5351ee753d1c526422877d821439f6e.png]]
>
> **Condition for output queueing:**
> $$\text{Arrival rate from fabric} > \text{Output link speed}$$
>
> **Consequences:**
> - Packets queue at output port waiting for transmission
> - Delay increases with queue length
> - Packet loss when buffer overflows

## Buffer Management

> [!note]+ Buffering Requirements
> ![[fc4f3c8ca86f7f63391d14a32a218cef.png]]
>
> **Buffering is required when:**
> - Packets arrive from fabric faster than link transmission rate
>
> **Key decisions:**
> - **Drop policy:** Which packet to drop when buffer is full?
> - **Scheduling:** Which packet to transmit next?

## Scheduling Disciplines

> [!info]+ Packet Scheduling
> **Scheduling discipline** determines which queued packet is transmitted next.
>
> | Discipline | Description |
> |------------|-------------|
> | FIFO | First-In-First-Out (simple, no prioritization) |
> | Priority | Higher priority packets transmitted first |
> | WFQ | Weighted Fair Queueing (proportional bandwidth sharing) |
> | Round Robin | Cycles through queues in order |
>
> **Trade-offs:**
> - FIFO: Simple but no QoS differentiation
> - Priority: May starve low-priority traffic
> - WFQ: Fair but more complex

## Related Concepts

> [!note]+ See Also
> - **[[Router Architecture]]**: Complete router structure
> - **[[Switching Fabric]]**: Connects input to output ports
> - **[[Data Plane]]**: Per-router forwarding function
> - **[[Network Layer]]**: Layer where queueing occurs
