---
title: Bus-based switching
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+
>
> Switching via a bus is a technique where packets are transferred from input port memory to output port memory via a shared bus.
>
> **Process:**
>
> - Packet from input port memory to output port memory via a shared bus
> - **Bus contention:** switching speed limited by bus bandwidth
>
> $$ \text{Switching speed} \leq \text{bus bandwidth} $$

> [!example]+ Exemple
>
> 32 Gbps bus, Cisco 5600: sufficient speed for access routers

> [!tip]+ Remarque
> ![[Pasted image 20251102152458.png]]
> The shared bus connects multiple input ports to multiple output ports. All packets must traverse the same bus, which can create a bottleneck.
