---
title: Switching Fabric
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+ Definition
>
> A switching fabric is the component of a router that transfers packets from input links to appropriate output links.

> [!abstract]+ Switching Rate
>
> **Switching rate:** Rate at which packets can be transferred from inputs to outputs
>
> - Often measured as multiple of input/output line rate
> - $N$ inputs: switching rate $N$ times line rate desirable
>
> $$ \text{Switching rate} = N \times \text{line rate (ideally)} $$
>
> Where $N$ is the number of input ports.
>
> The high-speed switching fabric connects $N$ input ports (labeled R) to $N$ output ports (labeled R).

> [!info]+ Major Types of Switching Fabrics
>
> There are three main architectures for implementing switching fabrics:
> ![[Pasted image 20251102152236.png]]
> **1. [[Memory-based switching]]:**
>
> - Uses shared memory for packet switching
> - Packets are written to and read from memory
>
> **2. [[Bus-based switching]]:**
>
> - Uses a shared bus for packet transfer
> - All ports share the same communication bus
>
> **3. [[Interconnection network]] (crossbar):**
>
> - Uses a crossbar switch or interconnection network
> - Provides direct paths between input and output ports
> - Most scalable architecture

> [!tip]+ Important note:
>
> Each switching fabric type has different performance characteristics and scalability properties. The interconnection network is typically the most efficient for high-speed routers.
