---
title: Bus-based Switching
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> Switching via a bus is a technique where packets are transferred from input port memory to output port memory via a shared bus.
>
> **Process:**
> - Packet from input port memory to output port memory via a shared bus
> - **Bus contention:** switching speed limited by bus bandwidth
>
> $$ \text{Switching speed} \leq \text{bus bandwidth} $$

- good for local peripheral networks
- we don't pass via a memory copy
- more efficient
- the tag is the address of the bus
- we can multiplex the packet to multiple sources (?)

> [!example]+ Exemple
> 32 Gbps bus, Cisco 5600: sufficient speed for access routers

> [!tip]+
> ![[Pasted image 20251102152458.png]]
>
> The shared bus connects multiple input ports to multiple output ports. All packets must traverse the same bus, which can create a bottleneck.
