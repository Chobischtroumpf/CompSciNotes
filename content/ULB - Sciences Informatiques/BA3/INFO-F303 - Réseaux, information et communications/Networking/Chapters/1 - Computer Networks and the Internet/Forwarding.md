---
title: Forwarding
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Forwarding** is the local action of moving arriving [[Packet#^150f99|packets]] from a router's input link to the appropriate router output link.

^bbdee6

> [!note]+ Forwarding Table
> The forwarding table contains:
> - **Header value patterns**: Address prefixes to match
> - **Output link**: Which interface to forward matching packets
> - **Next hop information**: Where to send the packet next
>
> ![[Pasted image 20250918151042.png]]

> [!abstract]- Forwarding vs [[Routing#^02e221|Routing]]
>
> |Forwarding|Routing|
> |---|---|
> |**Local action**|**Global action**|
> |Move packet from input to output|Determine end-to-end paths|
> |Uses forwarding table|Uses routing algorithms|
> |Nanosecond timescales|Second/minute timescales|
> |Data plane function|Control plane function|
