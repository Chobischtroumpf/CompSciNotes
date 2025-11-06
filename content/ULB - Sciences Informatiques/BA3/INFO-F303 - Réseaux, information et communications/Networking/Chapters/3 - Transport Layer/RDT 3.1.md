---
title: RDT 3.1
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **RDT 3.1** simplifies [[RDT 3.0]] by eliminating NAK messages entirely. Instead of using NAK for errors, the sender's timeout mechanism handles both packet loss AND bit errors.

## Key Insight: NAK Not Needed!

> [!success]+ Timeout Handles Everything
> **Realization**:
> - We already have timeout for packet loss
> - Timeout can also handle bit errors!
> - No need for separate NAK mechanism
>
> **How it works**:
> - Bit error detected -> receiver sends nothing (or just ignores packet)
> - Sender times out
> - Sender retransmits
> - Simpler protocol with one fewer message type

> [!note]+ [[RDT 3.0]] vs RDT 3.1 Comparison
> ![[Pasted image 20251030103716.png]]
>
> **[[RDT 3.0]]**:
> - Uses ACK and NAK
> - NAK triggers immediate retransmission
> - Bit error -> NAK sent -> retransmit
>
> **RDT 3.1**:
> - Uses only ACK (no NAK)
> - Timeout triggers retransmission
> - Bit error -> no response -> timeout -> retransmit
> - More elegant, fewer message types

## The Problem: Race Conditions
**Race conditions** can occur between received ACK and retransmitted packet:
![[Pasted image 20251030104725.png]]

> [!example]+ Race Condition Scenario
> **Sequence of events**:
> 1. **Event A**:
>    - Sender sends pkt(0)
>    - Receiver gets pkt(0) successfully
>    - Receiver sends ACK back
> 2. **Timeout occurs** before ACK arrives:
>    - Sender retransmits pkt(0)
>    - ACK is received for pkt(0)
> 3. **Event B**:
>    - Sender sends pkt(1) but lost (X)
>    - ACK for retransmitted pkt(0) is received (but sender thinks that it corresponds to pkt(1))
> 4. **Event C**:
>    - Sender sends pkt(0)
>    - Receiver discards it because it expects pkt(1)
>    - Receiver sends ACK for pkt(0)

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: RDT overview
> - **[[RDT 3.0]]**: Previous version (uses NAK)
> - **[[RDT 3.2]]**: Next version (fixes race condition)
> - **[[Checksum]]**: Error detection
> - **[[Transport Layer]]**: Where RDT operates
