---
title: RDT 3.3
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **RDT 3.3** introduces an optimization where receivers send ACK for the last properly received packet instead of sending NAK. Receiving duplicate ACKs at the sender triggers the same action as receiving NAK: retransmission.

## Key Optimization: Duplicate ACK = NAK

> [!success]+ Eliminating NAK (Again!)
> **Instead of NAK**:
> - Receiver sends ACK for last correctly received packet
> - Example: If waiting for pkt(1) but receive corrupt/duplicate pkt(0)
>   - Send ACK(1) indicating "I'm still waiting for pkt 1"
> - Sender interprets duplicate ACK as implicit NAK
>
> **Benefits**:
> - Only one message type (ACK)
> - Simpler protocol
> - Same information conveyed
> - Receiver always sends ACK (never silence)

## Sender/Receiver FSM Fragments
![[432d0894d2a58c221d79f49cbbfa7043.png]]

> [!note]+ Protocol Behavior
> **Sender**:
> - Checks if received ACK matches expected sequence number
> - **"corrupt ACK OR wrong sequence ACK"** triggers retransmission
> - Treats both as indication of problem
> - Simplifies from [[RDT 3.2]]
>
> **Receiver**:
> - Always sends ACK (even for corrupted/duplicate packets)
> - For corrupt or out-of-sequence packet:
>   - Sends ACK for last correctly received packet
>   - Example: Waiting for pkt(1), receives corrupt pkt → sends ACK(1)
>   - Signals "send me what I'm waiting for"

## The Performance Problem
**Utilization metric**: $U_{sender}$ = fraction of time sender is busy sending

### Performance Analysis

> [!example]+ Realistic Scenario
> **Network configuration**:
> - Link capacity: **1 Gbps** (1,000,000,000 bits/sec)
> - Propagation delay: **15 ms** one-way
> - RTT: **30 ms**
> - Packet size: **8,000 bits**
>
> **Transmission delay**:
> $$D_{trans} = \frac{L}{R} = \frac{8000 \text{ bits}}{10^9 \text{ bits/sec}} = 8 \text{ microseconds}$$
>
> Incredibly fast! Packet takes only 8 μs to transmit.

### Stop-and-Wait Performance
![[66e4ce344192d1f9302dfb8674d8e19f.png]]

> [!warning]+ Terrible Utilization
> **Sender must wait for ACK before sending next packet**:
>
> $$U_{sender} = \frac{L/R}{RTT + L/R} = \frac{D_{trans}}{RTT + D_{trans}}$$
>
> **For our example**:
> $$U_{sender} = \frac{0.008 \text{ ms}}{30.008 \text{ ms}} = 0.00027 = 0.027\%$$
>
> ![[9a51e190e1036e8ecb520a0317d0beb2.png]]
>
> **What this means**:
> - Sender busy only 0.027% of the time
> - Link idle 99.973% of the time
> - **1 Gbps link effectively becomes 270 Kbps!**
> - 8 μs transmitting, then 30 ms waiting
> - Massive waste of bandwidth

### Alternative Formula

> [!note]+ Bandwidth-Delay Product
> $$U_{sender} = \frac{L/R}{RTT + L/R} = \frac{1}{1 + \frac{R \cdot RTT}{L}}$$
>
> Where $\frac{R \cdot RTT}{2}$ = **bandwidth-delay product** = "in-flight" bits
>
> **Interpretation**:
> - $R \cdot RTT$ = how many bits could be sent in one RTT
> - In our example: $10^9 \times 0.03 = 30,000,000$ bits
> - But we're only sending 8,000 bits then waiting!
> - Could send 3,750 packets in the time we wait for one ACK

## The Reordering Problem
![[c23e7d5d56bea399d57ce48143b1c984.png]]

> [!example]+ Timeout Causes Reordering
> Here, the timeout causes the sender to resend pkt(0) because the ACK(0) response was delayed. The problem arises due to packet reordering:
>
> 1. **Initial transmission**: First pkt(0) is sent successfully and ACK(0) is sent back
> 2. **Timeout occurs**: Before ACK(0) arrives, sender times out and retransmits pkt(0)
> 3. **ACK(0) arrives**: The delayed ACK(0) finally arrives at sender
> 4. **Sender sends pkt(1)**: Sender moves forward and sends pkt(1)
> 5. **pkt(1) arrives**: Receiver gets pkt(1) and sends ACK(1)
> 6. **ACK(1) arrives first**: ACK(1) from pkt(1) arrives at sender
> 7. **Sender moves forward**: Sender receives ACK(1), thinks pkt(1) is acknowledged, sends new pkt(0)
> 8. **ACK(0) arrives late**: The ACK(0) from the retransmitted pkt(0) finally arrives
> 9. **Problem**: The new pkt(0) gets lost (X), but the ACK(0) that arrives makes the sender think the new pkt(0) was acknowledged, when in reality it's acknowledging the old retransmitted pkt(0)
>
> **With only 2 sequence numbers**:
> - Sender can't distinguish which transmission is being acknowledged
> - ACK(0) could be for either the retransmitted pkt(0) or the new pkt(0)
> - Creates ambiguity and causes the protocol to fail
> - More sequence numbers needed for pipelining

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: RDT overview
> - **[[RDT 3.2]]**: Previous version
> - **[[TCP]]**: Real protocol with pipelining
> - **[[RTT]]**: Key factor in performance
> - **[[Throughput]]**: What we're trying to maximize
> - **[[Transport Layer]]**: Where RDT operates
