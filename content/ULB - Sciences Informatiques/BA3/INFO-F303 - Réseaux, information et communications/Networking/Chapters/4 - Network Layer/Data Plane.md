---
title: Data Plane
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+ Définition **Data plane:**
>
> - _local_, per-router function
> - determines how packet arriving on router input port is forwarded to router output port
>


> [!info]+ [[Forwarding table]]
> Routers maintain a forwarding table, that is used to determine which output port to use, depending on the header values of received packets

> [!example]+ Example: A typical local forwarding table contains:
>
> |header|output|
> |---|---|
> |0100|3|
> |0110|2|
> |0111|2|
> |1001|1|
>
> When a packet arrives with header value $0111$, the router forwards it to output port $2$ based on this table.
>
> ![[Pasted image 20251102110051.png]]
