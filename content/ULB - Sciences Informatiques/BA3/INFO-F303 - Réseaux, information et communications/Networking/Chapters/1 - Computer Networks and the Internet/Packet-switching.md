---
title: Packet-switching
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Packet-switching** is a method where hosts break application-layer messages into [[Packet|packets]], which are forwarded from one router to the next across links on the path from source to destination. Each packet is transmitted at full link capacity.

![[ce865f8c9715c2507b01be6644a36c8f.png]]

> [!abstract]- Store-and-Forward Mechanism
> - **Transmission delay**: Takes $L/R$ seconds to transmit an $L$-bit packet into link at $R$ bits/s
> - **Store-and-forward**: Entire packet must arrive at router before it can be forwarded onto the next link
> - **End-to-end delay**: $2L/R$ (assuming zero propagation delay)

> [!example]
> $L$ = 10 Kbits
> $R$ = 100 Mbps (12.5 MB/s)
> One-hop transmission delay = 0.1 msec

> [!tip]
> 1 Mbps = 0.125 MB/s

> [!abstract]- Queueing and [[Packet#^150f99|Packet]] Loss
> **[[Packet#^150f99|Packet]] queuing and loss**: If arrival rate on incoming links exceeds transmission rate of output link for a period of time:
> - **[[Packet#^150f99|Packets]] queue**: Wait to be transmitted on output link
> - **[[Packet#^150f99|Packet]] loss**: [[Packet#^150f99|Packets]] can be dropped (lost) if memory (buffer) in router fills up
>
> ![[233044cffab385ee77ecbc5f1309d8e5.png]]
> ![[9446b1b72a0e5b15425116f5c445069f.png]]
> - Check [[Network delay]]

Statistical multiplexing on link:
- No fixed pattern on link, shared on demand (?)
