---
title: RDT 2.1
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **RDT 2.1** fixes the fatal flaw in [[RDT 2.0]] by adding sequence numbers to packets, allowing the receiver to detect and discard duplicate packets when ACK/NAK messages are corrupted.

## New Mechanism: Sequence Numbers

> [!success]+ How Sequence Numbers Work
> **For stop-and-wait protocol**:
> - Only 2 sequence numbers needed: **0 and 1**
> - Alternates: 0, 1, 0, 1, 0, 1, ...
> - Also called "Alternating-Bit Protocol"
>
> **Why 2 numbers suffice**:
> - Sender sends packet, waits for response
> - Only one unacknowledged packet at a time
> - Next packet can't be sent until current one acknowledged
> - Receiver only needs to distinguish "current" from "previous"

## Protocol Operation

> [!abstract]- How It Works
> **Sender**:
> - Adds sequence number to packet
> - Sends packet with sequence number
> - Waits for ACK/NAK
> - If ACK received and not corrupt -> send next packet (flip sequence number)
> - If NAK or corrupt ACK/NAK -> retransmit with same sequence number
>
> **Receiver**:
> - Checks if packet corrupt
> - Checks sequence number
> - If packet OK and expected sequence number -> deliver data, send ACK
> - If packet OK but wrong sequence number (duplicate) -> discard, send ACK anyway
> - If packet corrupt -> send NAK

## Sender FSM
![[Pasted image 20251030101026.png]]

> [!note]+ Sender States
> **Four states** (doubled from [[RDT 2.0]]):
> 1. "Wait for call 0 from above": Ready to send packet with seq=0
> 2. "Wait for ACK or NAK 0": Waiting for response to packet 0
> 3. "Wait for call 1 from above": Ready to send packet with seq=1
> 4. "Wait for ACK or NAK 1": Waiting for response to packet 1
>
> **Why two states for each sequence number?**
> - Must remember which sequence number is currently outstanding
> - State tracks whether expecting ACK for 0 or 1
>
> **Transitions**:
> - Corrupt ACK/NAK OR NAK received -> retransmit same packet
> - Valid ACK received -> move to next sequence number

## Receiver FSM
![[Pasted image 20251030101050.png]]

> [!note]+ Receiver States
> **Two states**:
> 1. "Wait for 0 from below": Expecting packet with seq=0
> 2. "Wait for 1 from below": Expecting packet with seq=1
>
> **Transitions for each state**:
> - **Receive expected sequence number + no corruption**:
>   - Extract and deliver data
>   - Send ACK
>   - Move to wait for next sequence number
>
> - **Receive wrong sequence number + no corruption (duplicate)**:
>   - Discard packet (don't deliver)
>   - Send ACK anyway (to help sender move forward: duplicate means sender never got previous ACK)
>   - Stay in same state
>
> - **Receive corrupted packet**:
>   - Send NAK
>   - Stay in same state

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: Overview of RDT problem
> - **[[RDT 2.0]]**: Previous version (no sequence numbers)
> - **[[RDT 3.0]]**: Next version (adds packet loss handling)
> - **[[Checksum]]**: Error detection used
> - **[[Transport Layer]]**: Where these protocols operate
