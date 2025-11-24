---
title: IP Fragmentation and Reassembly
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+
>
> Network links have MTU (max. transfer size) - the largest possible link-level frame. Different link types have different MTUs. When a large IP packet exceeds the MTU, it is divided ("fragmented") within the network.

## Process

> [!abstract]- **Fragmentation:**
>
> - One packet becomes several packets
> - "Reassembled" only at destination (not transparent)
> - Fragments could be further fragmented
> - IP header bits used to identify and order related fragments

> [!abstract]- **Reassembly:**
>
> - Fragments are reassembled at the destination

> [!example]+ Example
> ![[aa425c15ac42736dd7c0b101cbce5027.png]]
> **Given:**
>
> - 4000 byte packet
> - MTU = 1500 bytes
>
> **Result:** One large packet becomes several smaller packets
>
> 1480 bytes in data field, offset = $\frac{1480}{8}$
>
> |length|ID|fragflag|offset|
> |---|---|--:|--:|
> |=4000|=x|=0|=0|
>
> After fragmentation:
>
> |length|ID|fragflag|offset|
> |---|---|--:|--:|
> |=1500|=x|=1|=0|
> |=1500|=x|=1|=185|
> |=1040|=x|=0|=370|
>
> - offset = 0 means it is the first fragment
> - fragflag = 0 means it is the last fragment
> - fragflag of last fragment is a copy of fragflag before fragmentation
