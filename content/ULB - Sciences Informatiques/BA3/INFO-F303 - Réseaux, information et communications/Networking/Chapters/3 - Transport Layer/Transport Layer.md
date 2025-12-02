---
title: Transport Layer
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **Transport Layer** provides logical communication between application processes running on different hosts, while the network layer provides logical communication between hosts.
>
> ![[b83979d98e90aef57209b970ffd590e0.png]]

## Transport vs Network Layer

> [!abstract]- Key Differences
> **Network Layer (IP)**:
> - Logical communication between **hosts**
> - Best-effort delivery (unreliable)
> - Handles routing between networks
>
> **Transport Layer (TCP or UDP)**:
> - Logical communication between **processes**
> - Can add reliability, ordering, congestion control
> - Extends network layer services

## Sender Responsibilities

> [!note]+ Sender Operations
> The transport layer at the sender:
> 1. Is passed an application-layer message
> 2. Determines segment header field values
> 3. Creates segment
> 4. Passes segment to IP (network layer)
>
> ![[d6b64d3d6eb2a707a68209e270598692.png]]

## Receiver Responsibilities

> [!note]+ Receiver Operations
> The transport layer at the receiver:
> 1. Receives segment from IP (network layer)
> 2. Checks header values
> 3. Extracts application-layer message
> 4. Demultiplexes message up to application via socket
>
> ![[5b24aff3cdcac1069977c986398598bb.png]]

## Related Concepts

> [!note]+ See Also
> - **[[TCP]]**: Reliable, connection-oriented transport protocol
> - **[[UDP]]**: Unreliable, connectionless transport protocol
> - **[[Multiplexing]]**: Handling data from multiple sockets
> - **[[Demultiplexing]]**: Delivering segments to correct sockets
> - **[[Checksum]]**: Error detection mechanism
> - **[[Reliable Data Transfer]]**: Principles for reliable communication
> - **[[Socket]]**: Interface between application and transport layer
> - **[[Network]]**: Protocol stack context
