---
title: Memory-based Switching
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> Switching via memory is a technique used in first generation [[Switch#^97dbe2|routers]] where [[Packet#^150f99|packets]] are switched through the router's main memory under CPU control.

> [!abstract]+ First Generation Routers
> ![[47ea001e77a7769c7f347213e949ff16.png]]
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
