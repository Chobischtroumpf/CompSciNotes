---
title: TCP Congestion Control
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **TCP Congestion Control** is a mechanism to prevent too many sources from sending too much data too fast for the network to handle. [[TCP]] uses end-to-end congestion control without explicit feedback from the network.

## Congestion Control Approaches

### End-to-End Congestion Control

> [!note]+ No Explicit Feedback
> **Approach taken by TCP**:
> - No explicit feedback from network
> - Congestion inferred from observed loss and delay
> - Sender detects congestion symptoms
> - Adjusts sending rate accordingly
>
> ![[837440469eb79d16d60c95d2a5a7e86a.png]]

### Network-Assisted Congestion Control

> [!note]+ Router Feedback
> **Alternative approach**:
> - Routers provide direct feedback to hosts
> - May indicate congestion level
> - May explicitly set sending rate
> - Examples: TCP ECN, ATM, DECbit protocols
>
> ![[655b9764e9ce7df359cfe50364e360be.png]]

## TCP Congestion Window (cwnd)

> [!success]+ Dynamic Rate Control
> **Congestion window limits transmission**:
> ```
> LastByteSent - LastByteAcked ≤ cwnd
> ```
>
> **TCP sending behavior**:
> - Send `cwnd` bytes
> - Wait RTT for ACKs
> - Send more bytes
>
> **Sending rate**:
> $$\text{TCP rate} \approx \frac{\text{cwnd}}{\text{RTT}} \text{ bytes/sec}$$
>
> **Dynamic adjustment**:
> - `cwnd` adjusted based on observed network congestion
> - Increases when network seems uncongested
> - Decreases when congestion detected
>
> ![[9f9a9d330af6e0ec92755345883adaa6.png]]

## TCP Slow Start

> [!info]+ Exponential Growth Phase
> **Initial connection behavior**:
> - Start with `cwnd = 1 MSS`
> - Double `cwnd` every [[RTT]]
> - Achieved by incrementing `cwnd` for every ACK received
> - Continue until first loss event
>
> ![[3d2f0837daaac8265a43d16bd8cbaf48.png]]

### Transition to Linear Growth

> [!note]+ Using ssthresh
> **When to switch from exponential to linear?**
> - Use threshold variable: `ssthresh`
> - Set to 1/2 of `cwnd` value just before timeout
> - When `cwnd` reaches `ssthresh`, switch to congestion avoidance
>
> **Linear growth formula**:
> ```
> cwnd = cwnd + (MSS/cwnd) × MSS for each ACK received
> ```
>
> ![[5168bdee827b9bbd503ca214b113b768.png]]

## TCP State Machine

> [!abstract]+ Three Main States
> ![[d797b7db4170c0da804df500c3145e2f.png]]

### 1. Slow Start

> [!note]+ Exponential Growth
> **Initial state**:
> - `cwnd = 1 MSS`
> - `ssthresh = 64 KB` (typical)
> - `dupACKcount = 0`
>
> **On new ACK**:
> - `cwnd = cwnd + MSS`
> - `dupACKcount = 0`
> - Transmit new segments
> - Growth: Exponential (doubles every [[RTT]])
>
> **On duplicate ACK**:
> - `dupACKcount++`
> - Stay in slow start
>
> **Transition to Congestion Avoidance**:
> - When `cwnd ≥ ssthresh`
>
> **On timeout**:
> - `ssthresh = cwnd/2`
> - `cwnd = 1 MSS`
> - `dupACKcount = 0`
> - Retransmit missing segment
> - Stay in slow start
>
> **Transition to Fast Recovery**:
> - When `dupACKcount == 3`
> - `ssthresh = cwnd/2`
> - `cwnd = ssthresh + 3`
> - Retransmit missing segment

### 2. Congestion Avoidance ([[AIMD]])

> [!note]+ Linear Growth
> **Steady state behavior**:
>
> **On new ACK**:
> - `cwnd = cwnd + MSS × (MSS/cwnd)`
> - Increases by ~1 MSS per [[RTT]]
> - `dupACKcount = 0`
> - Transmit new segments
> - Growth: Linear (additive increase)
>
> **On duplicate ACK**:
> - `dupACKcount++`
> - Stay in congestion avoidance
>
> **Transition to Fast Recovery**:
> - When `dupACKcount == 3`
> - `ssthresh = cwnd/2`
> - `cwnd = ssthresh + 3`
> - Retransmit missing segment
>
> **On timeout**:
> - `ssthresh = cwnd/2` (multiplicative decrease)
> - `cwnd = 1 MSS`
> - `dupACKcount = 0`
> - Retransmit missing segment
> - Go to slow start

### 3. Fast Recovery

> [!note]+ Recovering from Loss
> **Purpose**: Avoid slow start when loss detected by duplicate ACKs
>
> **On new ACK**:
> - `cwnd = ssthresh`
> - `dupACKcount = 0`
> - Transmit new segments
> - Go to congestion avoidance
>
> **On duplicate ACK**:
> - `cwnd = cwnd + MSS` (inflate window)
> - Transmit new segments
> - Stay in fast recovery
>
> **On timeout**:
> - `ssthresh = cwnd/2`
> - `cwnd = 1 MSS`
> - `dupACKcount = 0`
> - Retransmit missing segment
> - Go to slow start

## TCP Goodput Analysis

> [!abstract]+ Average Throughput
> **Steady state goodput**:
> - Let $W$ = window size (in MSS) when loss occurs
> - Just before loss: throughput = $W/\text{RTT}$
> - Just after loss: throughput = $0.5W/\text{RTT}$
> - Average throughput: $0.75W/\text{RTT}$
>
> ![[ec30967af6a087492eab55f1123e2294.png]]

### Mathematical Derivation

> [!note]+ Goodput Formula
> **Average window size**: $3W/4$ (in MSS)
>
> **Number of MSS per cycle**: $\frac{3W}{4} \times \frac{W}{2} = \frac{3W^2}{8}$
>
> **Packet loss ratio**: $p = \frac{1}{3W^2/8} = \frac{8}{3W^2}$
>
> **Window size**: $W = \sqrt{\frac{8}{3p}}$
>
> **Average goodput**:
> $$\text{Goodput (bps)} = \frac{1.22 \times \text{MSS}}{\text{RTT} \times \sqrt{p}}$$

### High-Speed Example

> [!example]+ 10 Gbps Requirement
> **Parameters**:
> - Segment size: 1500 bytes
> - RTT: 100 ms
> - Target goodput: 10 Gbps
>
> **Requirements**:
> - Average window: $W = 83,333$ in-flight segments
> - Packet loss rate: $p = 2 \times 10^{-10}$
>
> **Conclusion**: New versions of TCP needed for high-speed networks!

## TCP Fairness

> [!abstract]+ Fairness Goal
> **Objective**: If $K$ TCP sessions share bottleneck link of capacity $R$, each should have average rate of $R/K$
>
> ![[f3f82f5f26ae79d1da41f41961f6694e.png]]

### Is TCP Fair?

> [!success]+ Fairness Under Ideal Conditions
> **Yes, when**:
> - Same RTT for all connections
> - Same MSS for all connections
> - Fixed number of sessions
> - All in congestion avoidance mode
>
> **Mechanism**:
> - Additive increase: slope of 1 (equal growth)
> - Multiplicative decrease: proportional reduction
> - Converges toward equal bandwidth sharing
>
> ![[e3e2e20de2d73fc7fd8b7c634d6fbcfb.png]]

### Impact of Different RTTs

> [!warning]+ RTT Unfairness
> **When RTTs differ**:
> - Connection with smaller RTT ramps up faster
> - Gets proportionally more bandwidth
>
> **Example**:
> - If $\text{RTT}_2 = 2 \times \text{RTT}_1$
> - Connection 1 ramps up twice as quickly
> - Gets approximately twice the bandwidth
>
> ![[8b0891548e982ea69c7034ac41295b27.png]]

## Related Concepts

> [!note]+ See Also
> - **[[AIMD]]**: Core congestion control algorithm
> - **[[TCP]]**: Protocol using this congestion control
> - **[[TCP Flow Control]]**: Receiver-side control mechanism
> - **[[TCP Structure]]**: Segment format and window field
> - **[[Reliable Data Transfer]]**: Error recovery with congestion control
> - **[[RTT]]**: Key metric for congestion control
> - **[[Go-Back-N]]**: Retransmission strategy
> - **[[Selective Repeat]]**: Advanced retransmission
> - **[[Transport Layer]]**: Layer where congestion control operates
