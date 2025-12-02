---
title: Data Plane
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **Data Plane** is a *local*, per-router function that determines how packets arriving at a router's input port are forwarded to the router's output port. It operates in the hardware at nanosecond timescales.

## How It Works

> [!abstract]+ Forwarding Process
> **Per-packet operation:**
> 1. Packet arrives at input port
> 2. Router examines header field values
> 3. Consults [[Forwarding#^bb5745|Forwarding Table]] for output port
> 4. Forwards packet to appropriate output port
>
> **Key characteristic:**
> - Decisions made locally at each router
> - No coordination with other routers needed
> - Hardware-based for speed

## Forwarding Table

(redefined, but whatever)

> [!note]+ Table Structure
> Routers use a forwarding table to determine output ports:
>
> | Header Value | Output Port |
> |:---:|:---:|
> | 0100 | 3 |
> | 0110 | 2 |
> | 0111 | 2 |
> | 1001 | 1 |
>
> When a packet arrives with header value `0111`, the router forwards it to output port `2` based on this table.

> [!example]+ Forwarding Example
> ![[45fbf03b50166f5434f0e0d7ca40b8e4.png]]
>
> **Process:**
> 1. Packet with header `0111` arrives at input
> 2. Router performs table lookup
> 3. Match found: output port = 2
> 4. Packet forwarded to output port 2

## Related Concepts

> [!note]+ See Also
> - **[[Control Plane]]**: Network-wide routing decisions
> - **[[Network Layer]]**: Layer containing data plane
> - **[[Router Architecture]]**: Complete router structure
> - **[[Switching Fabric]]**: Connects input to output ports
