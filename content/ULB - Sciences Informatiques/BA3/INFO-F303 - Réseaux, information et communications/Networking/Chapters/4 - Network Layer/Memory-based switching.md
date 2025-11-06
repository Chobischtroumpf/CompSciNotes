---
title: Memory-based switching
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+
>
> Switching via memory is a technique used in first generation routers where packets are switched through the router's main memory under CPU control.

> [!abstract]+ First Generation Routers
> ![[Pasted image 20251102152414.png]]
>
> **Architecture:**
>
> - Traditional computers with switching under direct control of CPU
> - Packet copied to system's memory
> - Speed limited by memory bandwidth (2 bus crossings per packet)
>
> $$ \text{Switching speed} \leq \frac{\text{memory bandwidth}}{2} $$
>
> The factor of 2 comes from the need for 2 bus crossings per packet (input to memory, memory to output).
