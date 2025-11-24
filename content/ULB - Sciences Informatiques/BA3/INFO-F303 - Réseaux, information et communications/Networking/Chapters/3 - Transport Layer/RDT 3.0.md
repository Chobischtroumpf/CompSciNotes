---
title: RDT 3.0
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **RDT 3.0** extends [[RDT 2.1]] to handle packet loss by introducing a timeout mechanism. The sender waits a "reasonable" amount of time for an ACK; if no ACK arrives, it retransmits the packet.

## New Problem: Packet Loss

> [!warning]+ Channel Can Lose Packets
> **New assumptions**:
> - Packets can be lost (data or ACK packets)
> - Still has bit errors from [[RDT 2.1]]
>
> **How to detect loss?**
> - Checksum can't detect loss (packet never arrives!)
> - Receiver can't send NAK (doesn't know packet was sent)
> - **Solution**: Sender uses timeout

## Timeout Mechanism

> [!success]+ How Timeouts Work
> **Sender starts timer** when packet sent:
> - If ACK received before timeout -> cancel timer, proceed
> - If timeout expires -> assume packet or ACK lost, retransmit
>
> **Choosing timeout value**:
> - Must be longer than typical [[RTT]]
> - Too short -> unnecessary retransmissions
> - Too long -> slow recovery from loss
> - "Reasonable" amount of time (conservative estimate)

## Protocol Operation

![[4e7defd97757ae171edce4fe96e72696.png]]


> [!example]+ Delayed ACK Scenario (No Loss)
> 1. Sender sends packet 0, starts timer
> 2. Packet arrives at receiver
> 3. Receiver sends ACK
> 4. **ACK delayed** (but not lost)
> 5. Timer expires at sender
> 6. Sender retransmits packet 0
> 7. **Receiver gets duplicate packet 0**
> 8. Receiver discards duplicate, sends ACK
> 9. **Sender eventually receives first ACK**
> 10. Duplicate ACK ignored, sender proceeds with packet 1

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: RDT overview
> - **[[RDT 2.1]]**: Previous version (added sequence numbers)
> - **[[RDT 3.1]]**: Next step (eliminates NAK)
> - **[[Checksum]]**: Error detection
> - **[[RTT]]**: Affects timeout setting
> - **[[TCP]]**: Uses similar timeout/retransmission
