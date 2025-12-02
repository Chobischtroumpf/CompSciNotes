---
title: Reliable Data Transfer
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Reliable Data Transfer (RDT)** is the problem of ensuring data sent by a sender is received correctly and completely by a receiver, even when the underlying channel is unreliable. This is a fundamental challenge in network protocols, particularly for [[TCP]].

## The Challenge

> [!abstract]- Unreliable Channel Characteristics
> **Underlying channel may**:
> - Corrupt bits (bit errors)
> - Lose packets entirely
> - Reorder packets
> - Duplicate packets
> - Delay packets arbitrarily
>
> **Complexity**:
> - RDT protocol complexity depends on characteristics of unreliable channel
> - More problems to handle = more complex protocol
> - Sender and receiver don't know each other's state unless communicated

| ![[9a52e4e4d19ea679d963451ed1aecaf7.png]] | ![[8a22229cf82c4ca473aedb39491dced9.png]] |
| :----------------------------------: | :----------------------------------: |
## Key Interfaces

> [!note]+ RDT Protocol Interfaces
> **Sender side**:
> - `rdt_send()`: Called from above (application), passes data to deliver to receiver
> - `udt_send()`: Called by RDT to transfer packet over unreliable channel
>
> **Receiver side**:
> - `rdt_rcv()`: Called when packet arrives from channel
> - `deliver_data()`: Called by RDT to deliver data to upper layer (application)
>
> ![[df88e4155ac6d9119a4762ea93eb8670.png]]

> [!tip]+ Simplifications
> For learning purposes:
> - We consider only **unidirectional data transfer** (data flows one way)
> - Control information (ACKs, etc.) flows both ways
> - We use **finite state machines (FSMs)** to specify sender/receiver behavior
>
> ![[6de3b37231b63e46192be3bfc0f25ef2.png]]

## Evolution of RDT Protocols

> [!abstract]- Progressive Complexity
> The RDT protocols evolve to handle increasingly difficult channel problems:
>
> **[[RDT 1.0]]**: Perfect channel
> - No errors, no loss, no reordering
> - Simplest case (unrealistic)
>
> **[[RDT 2.0]]**: Channel with bit errors
> - Introduces error detection ([[Checksum]])
> - Uses ACK/NAK for feedback
> - Stop-and-wait protocol
>
> **[[RDT 2.1]]**: Corrupted ACK/NAK
> - Handles corrupted acknowledgments
> - Adds sequence numbers (0 and 1)
> - Receiver can detect duplicates
>
> **[[RDT 3.0]]**: Packet loss
> - Adds timeout mechanism
> - Sender retransmits on timeout
> - Handles both errors and loss
>
> **[[RDT 3.1]]**: Simplified with timer
> - Eliminates NAK (use timer for everything)
> - More elegant design
>
> **[[RDT 3.2]]**: Numbered ACKs
> - ACKs include sequence numbers
> - Alternating-Bit Protocol
> - Still has performance issues
>
> **[[RDT 3.3]]**: Duplicate ACK = NAK
> - Receiver sends ACK for last correctly received packet
> - Duplicate ACK triggers retransmission
> - More efficient signaling

## Related Concepts

> [!note]+ See Also
> - **[[RDT 1.0]]**: Reliable channel (baseline)
> - **[[RDT 2.0]]**: Bit errors
> - **[[RDT 2.1]]**: Corrupted feedback
> - **[[RDT 3.0]]**: Packet loss
> - **[[RDT 3.1]]**: Timer-based
> - **[[RDT 3.2]]**: Numbered ACKs
> - **[[RDT 3.3]]**: Duplicate ACK technique
> - **[[TCP]]**: Real implementation of RDT
> - **[[Checksum]]**: Error detection mechanism
> - **[[Transport Layer]]**: Layer where RDT operates
