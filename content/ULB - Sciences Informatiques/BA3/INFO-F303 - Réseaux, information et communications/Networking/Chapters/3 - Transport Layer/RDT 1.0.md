---
title: RDT 1.0
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **RDT 1.0** is the simplest [[Reliable Data Transfer]] protocol, designed for a perfectly reliable underlying channel with no bit errors, no packet loss, and no reordering.

## Channel Assumptions

> [!success]+ Perfect Channel
> The underlying channel is perfect:
> - No bit errors
> - No packet loss
> - No packet reordering
> - Infinite buffer capacity

## Protocol Operation

> [!abstract]- How It Works
> **Sender**:
> - Waits for data from upper layer
> - Packages data into packet
> - Sends packet into channel
> - No acknowledgment needed
>
> **Receiver**:
> - Waits for packet from channel
> - Extracts data from packet
> - Delivers data to upper layer
> - No acknowledgment sent

## Finite State Machines
| ![[Pasted image 20251030095525.png]] | ![[Pasted image 20251030095531.png]] |
| :----------------------------------: | :----------------------------------: |
|             Sender FSM              |            Receiver FSM             |

> [!note]+ FSM Explanation
> **Sender state**:
> - Single state: "Wait for call from above"
> - Transition: `rdt_send(data)` -> create packet, send via `udt_send()`
> - Returns to same state
>
> **Receiver state**:
> - Single state: "Wait for call from below"
> - Transition: `rdt_rcv(packet)` -> extract data, deliver via `deliver_data()`
> - Returns to same state

## Related Concepts

> [!note]+ See Also
> - **[[Reliable Data Transfer]]**: Overview of RDT problem
> - **[[RDT 2.0]]**: Next step - handles bit errors
> - **[[Transport Layer]]**: Where RDT protocols operate
> - **[[UDP]]**: Actually provides this level of (un)reliability
> - **[[TCP]]**: Provides full reliability unlike RDT 1.0
