---
title: Network delay
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Network delay** is the total time required for a [[Packet#^150f99|packet]] to travel from source to destination, consisting of four main components.

^292b30

> [!abstract]- Four Sources of Delay
> $$d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$$
### 1. Processing Delay ($d_{proc}$)
> [!info]+ Processing Delay
> - **Function**: Check bit errors, determine output link
> - **Typical value**: < 1 msec
> - **Characteristics**: Usually negligible and deterministic
### 2. Queueing Delay ($d_{queue}$)
> [!info]+ Queueing Delay
> - **Function**: Time waiting at output link for transmission
> - **Characteristics**: Variable, depends on congestion level
> - **Factors**: Traffic load, buffer size, scheduling algorithm
### 3. Transmission Delay ($d_{trans}$)
> [!info]+ Transmission Delay
> - **Formula**: $d_{trans} = \frac{L}{R}$
>     - $L$ = [[Packet#^150f99|packet]] length (bits)
>     - $R$ = link transmission rate (bps)
> - **Function**: Time to push entire packet onto link
> - **Analogy**: Time to pump fluid into pipe
### 4. Propagation Delay ($d_{prop}$)
> [!info]+ Propagation Delay
> - **Formula**: $d_{prop} = \frac{d}{s}$
>     - $d$ = length of physical link (meters)
>     - $s$ = propagation speed $\approx 2 \times 10^8$ m/sec
> - **Function**: Time for signal to travel across link
> - **Analogy**: Time for fluid to flow through pipe
