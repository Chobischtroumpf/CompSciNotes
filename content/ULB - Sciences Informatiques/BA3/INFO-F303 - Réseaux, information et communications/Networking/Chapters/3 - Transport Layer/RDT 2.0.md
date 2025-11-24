---
title: RDT 2.0
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **RDT 2.0** extends [[RDT 1.0]] to handle bit errors in the channel using error detection ([[Checksum]]) and acknowledgment messages (ACK/NAK).

## Channel Assumptions

> [!abstract]- Channel Characteristics
> **Problems added**:
> - Bit errors may occur (bits flip during transmission)
>
> **Still assuming**:
> - No packet loss
> - No reordering
> - Packets arrive (eventually)

## New Mechanisms

> [!success]+ Error Detection and Recovery
> **[[Checksum]]**:
> - Detects bit errors in received packets
> - Added to each packet header
> - Receiver can detect corruption
>
> **Acknowledgments**:
> - **ACK**: Receiver explicitly tells sender packet received OK
> - **NAK**: Receiver explicitly tells sender packet had errors
> - Sender retransmits packet upon receiving NAK
>
> **Stop-and-wait**:
> - Sender sends one packet
> - Waits for receiver response (ACK or NAK)
> - Only then sends next packet

## Protocol in Action
![[b7faa65b3e993725f9728e98cf6e3216.png]]

> [!example]+ Error Scenario
> 1. Sender transmits packet
> 2. Bit error occurs during transmission
> 3. Receiver detects error via checksum
> 4. Receiver sends NAK
> 5. Sender retransmits packet
> 6. Packet arrives correctly
> 7. Receiver sends ACK
> 8. Sender proceeds to next packet

## Finite State Machines
| ![[cb03eb87cecaad6d2c6eaa2630fdd34b.png]] | ![[a4a89beafd5b8d5796cf46b5cff36434.png]] |
| :----------------------------------: | :----------------------------------: |
|              Sender FSM              |             Receiver FSM             |

> [!note]+ Sender FSM Explanation
> **Two states**:
> 1. "Wait for call from above": Ready to send new data
> 2. "Wait for ACK or NAK": Waiting for feedback
>
> **Transitions**:
> - Get data -> create packet with checksum, send, wait for response
> - Receive ACK -> return to wait for new data
> - Receive NAK -> retransmit same packet, stay in wait state

> [!note]+ Receiver FSM Explanation
> **Single state** (but with conditional actions):
> - "Wait for call from below"
>
> **Transitions**:
> - Receive packet with **no errors** -> extract data, deliver up, send ACK
> - Receive packet with **errors** -> send NAK (don't deliver data)
>
> **Key insight**:
> - Receiver state isn't known to sender unless communicated
> - ACK/NAK provides this communication

## Fatal Flaw

> [!fail]+ What If ACK/NAK Gets Corrupted?
> **The problem**:
> - ACK or NAK messages can also have bit errors
> - Checksum detects corruption
> - But what should sender do?
>
> **Possible solutions** (all problematic):
> 1. **Ask receiver to resend ACK/NAK?**
>    - Creates infinite loop of confirmations
>    - "Did you get my confirmation of your confirmation?"
>
> 2. **Add enough redundancy to recover?**
>    - Might work but complicated
>    - Just moves problem around
>
> 3. **Retransmit if ACK/NAK garbled?**
>    - Creates duplicates!
>    - Receiver can't tell if packet is new or duplicate

![[158406fe5837486c00840a23551be48c.png]]

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: Overview of RDT problem
> - **[[RDT 1.0]]**: Previous version (no errors)
> - **[[RDT 2.1]]**: Next version (fixes corrupted ACK/NAK)
> - **[[Checksum]]**: Error detection mechanism used
> - **[[Transport Layer]]**: Where these protocols operate
