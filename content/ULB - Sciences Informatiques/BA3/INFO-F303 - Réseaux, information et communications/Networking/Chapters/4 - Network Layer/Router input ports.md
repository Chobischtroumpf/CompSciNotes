---
title: Router input ports
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+
> Input ports are responsible for receiving incoming packets, processing them at the physical and link layers, and forwarding them to the appropriate output port through the switching fabric.

> [!abstract]+ Architecture Components
>
> **Input port processing pipeline:**
>
> ![[Pasted image 20251102151712.png]]
> **Physical layer:** bit-level reception
>
> **Link layer:** e.g., Ethernet (see chapter 6)
>
> **Lookup, forwarding, queueing:** processes packets for switching

> [!info]+ Decentralized Switching
>
> Decentralized switching is a technique where forwarding decisions are made at each input port independently, rather than by a central processor.
>
> **Process:**
>
> - Using IP header field values, lookup output switch port using forwarding table in input port memory ("match plus action")
> - Goal: complete input port processing at "line speed" (also decrement TTL, update packet count stats, ...)
> - **Input port queuing:** if packets arrive faster than forwarding rate into switch fabric

> [!abstract]+ Destination-Based Forwarding
>
> **Traditional approach:**
>
> - Destination-based forwarding: forward based only on destination IP address (traditional)
>
> **Modern approach:**
>
> - Generalized forwarding: forward based on any set of header field values
> **Note that:**
> The input port must handle packets at line speed to avoid bottlenecks in the forwarding process.
