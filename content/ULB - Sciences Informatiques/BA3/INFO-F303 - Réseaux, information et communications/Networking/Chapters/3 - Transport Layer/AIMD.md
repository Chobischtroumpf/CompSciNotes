---
title: AIMD
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **AIMD (Additive Increase Multiplicative Decrease)** is a congestion control algorithm used by [[TCP]] where senders gradually increase their sending rate until packet loss occurs, then sharply decrease it. This approach efficiently finds and utilizes available network capacity.

## Core Concept

> [!abstract]+ Probing for Bandwidth
> **Basic strategy**:
> - Senders increase sending rate until packet loss (congestion) occurs
> - Upon loss, decrease sending rate
> - Repeat cycle to continuously adapt to network conditions

## Additive Increase

> [!success]+ Gradual Growth
> **Increase sending rate by 1 MSS every [[RTT]] until loss detected**
>
> **How it works**:
> - Add one Maximum Segment Size (MSS) per round-trip time
> - Linear growth in congestion window
> - Gentle probing for available bandwidth
> - Prevents sudden network overload

## Multiplicative Decrease

> [!warning]+ Sharp Reduction
> **Cut sending rate in half at each loss event**
>
> **How it works**:
> - Immediate response to congestion signal
> - Fast backoff to relieve congestion
> - Preserves network stability

![[42cb92b99c00f243659d4de064606035.png]]

## TCP Implementation Details

> [!note]+ Two Types of Loss Detection
> **In TCP Reno**:
>
> **Triple Duplicate ACK (3 DUPACK)**:
> - Mild congestion (isolated packet loss)
> - Cut rate in half
> - Next packets still being received
> - Requires sending window >= 4 MSS
>
> **Timeout**:
> - More severe congestion
> - Cut to 1 MSS per RTT
> - Used when 3 DUPACK not received
> - Network appears heavily congested

## Fairness Properties

> [!tip]+ Converging to Fair Share
> **Why AIMD achieves fairness**:
> - Additive increase: all flows grow at same rate (slope of 1)
> - Multiplicative decrease: decreases proportionally
> - System converges toward equal bandwidth sharing
> - Oscillates around fair allocation

## Related Concepts

> [!note]+ See Also
> - **[[TCP Congestion Control]]**: Uses AIMD algorithm
> - **[[TCP]]**: Protocol implementing AIMD
> - **[[Go-Back-N]]**: Reliability mechanism used with AIMD
> - **[[RTT]]**: Time unit for additive increase
> - **[[TCP Structure]]**: MSS definition
> - **[[Transport Layer]]**: Layer where AIMD operates
