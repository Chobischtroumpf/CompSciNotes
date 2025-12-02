---
title: Throughput
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Throughput** is the rate (bits per time unit) at which bits are being sent from sender to receiver.

^325f00

> [!abstract]- Types of Throughput
> **Instantaneous throughput**: Rate (in bits/sec) at which Host $B$ is receiving the file.
>
> **Average throughput**: Rate over a longer period of time.
> - If a file consists of $F$ bits and transferring it takes $T$ seconds for Host $B$ to receive all $F$ bits, then the **average throughput** of the file transfer is $F/T$ bits/sec.

>[!info]+ Bottleneck link
> The link on the end-to-end path that constrains end-to-end throughput.
>
> For a simple two-link path with rates $R_s$ and $R_c$:
> - If $R_s < R_c$: throughput = $R_s$ (sender link is bottleneck)
> - If $R_s > R_c$: throughput = $R_c$ (receiver link is bottleneck)
> - **General rule**: throughput = $\min(R_s, R_c)$
>
> ![[15b738a3440a5754bbb53ea7d7281f2b.png]]

> [!tip]+ Fluid Analogy
> Think of throughput like water flowing through pipes:
> - **Pipe capacity** = link bandwidth
> - **Flow rate** = throughput
> - **Narrowest pipe** determines overall flow rate
> - Multiple flows can share the same pipe capacity
>
> ![[5ef96901408e46dc7cfbf306d8c8bc4c.png]]
