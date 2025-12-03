---
title: Router Architecture
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Router architecture** describes the internal structure of a router, consisting of two main functional planes: the [[Control Plane]] (routing processor) operating in software, and the [[Data Plane]] (high-speed switching fabric) operating in hardware.

## High-Level Architecture

> [!abstract]+ Router Components
> ![[001c5c38d94e16fee83abac4a864291b.png]]
>
> | Component | Plane | Implementation | Time Frame |
> |-----------|-------|----------------|------------|
> | Routing processor | [[Control Plane]] | Software | Milliseconds |
> | [[Switching Fabric]] | [[Data Plane]] | Hardware | Nanoseconds |
> | Input/Output ports | [[Data Plane]] | Hardware | Nanoseconds |

## Input Port Processing

> [!note]+ Input Port Pipeline
> ![[ec8c2d996dc5b0f4a8cb47316c0701f3.png]]
>
> **Three-stage processing:**
>
> | Stage | Function |
> |-------|----------|
> | Physical layer | Bit-level reception (line termination) |
> | Link layer | Protocol processing (e.g., Ethernet) |
> | Lookup/Forwarding | Destination lookup and queueing |

> [!success]+ Decentralized Switching
> **Goal:** Complete input port processing at "line speed"
>
> **Operations performed:**
> - Use IP header fields to lookup output port via forwarding table
> - Decrement TTL
> - Update packet count statistics
> - Queue packets if they arrive faster than fabric can switch
>
> **Forwarding approaches:**
> - **Destination-based:** Forward based only on destination IP (traditional)
> - **Generalized:** Forward based on any set of header field values

## Output Port Processing

> [!note]+ Output Port Functions
> **Transmit-side operations:**
> - Receive packets from [[Switching Fabric|switching fabric]]
> - Buffer packets in output queue
> - Schedule packets for transmission
> - Perform link-layer encapsulation
> - Transmit on outgoing link

## Related Concepts

> [!note]+ See Also
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Data Plane]]**: Per-router forwarding function
> - **[[Switching Fabric]]**: Transfers packets between ports
> - **[[Port Queueing]]**: Input and output buffering
> - **[[Longest Prefix Matching]]**: Lookup algorithm used in input ports
> - **[[Network Layer]]**: Layer where routers operate
