---
title: Data Plane
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The data plane is a *local*, per-router function which determines how packets arriving at a router's input port are forwarded to the router's output port.

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
> ![[45fbf03b50166f5434f0e0d7ca40b8e4.png]]
