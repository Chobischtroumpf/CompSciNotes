---
title: Interconnection Network
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> Switching via an interconnection network uses advanced network topologies (Crossbar, Clos networks, etc.) initially developed to connect processors in multiprocessor systems.

> [!abstract]- Multistage Switch
> ![[Pasted image 20251106143506.png]]
>
> **Multistage switch:** $n \times n$ switch from multiple stages of smaller switches
>
> Architecture example: $3 \times 3$ crossbar or $8 \times 8$ multistage switch built from smaller-sized switches

- instead of big crossbars, we split it into multiple smaller crossbars
- the tag defines the path in the multistage switch

> [!abstract]- Exploiting Parallelism
> **Parallel switching process:**
> - Fragment IP packet into fixed length cells on entry
> - Switch cells through the fabric, reassemble IP packet at exit (don't confuse this with IP fragmentation!)
>
> $$ \text{IP packet} \xrightarrow{\text{fragment}} \text{fixed-length cells} \xrightarrow{\text{switch}} \text{reassemble} \rightarrow \text{IP packet} $$

- useful for big packets to avoid blocking
- do not confuse with [[IP Fragmentation and Reassembly]] (we don't fragment packets for the exit link, we do it internally within the network)

> [!tip]+
> This fragmentation at the switching fabric level is different from IP fragmentation and is used to improve switching efficiency.

> [!abstract]- Scaling Using Multiple Switching "Planes" in Parallel
> **Cisco CRS router:**
> - Basic unit: 8 switching planes
> - Each plane: 3-stage interconnection network
> - Up to 100's Tbps switching capacity
>
> $$ \text{Total capacity} = \text{number of planes} \times \text{capacity per plane} $$

> [!example]+
> ![[Pasted image 20251102152717.png]]
>
> The Cisco CRS router uses multiple fabric planes operating in parallel to achieve speedup and scaleup via parallelism.
>
> Multiple input ports connect to all fabric planes simultaneously, and all fabric planes connect to multiple output ports, enabling massive parallelism and high throughput.
