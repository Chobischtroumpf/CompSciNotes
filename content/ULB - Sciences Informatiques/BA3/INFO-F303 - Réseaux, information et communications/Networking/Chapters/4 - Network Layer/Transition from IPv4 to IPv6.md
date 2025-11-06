---
title: Transition from IPv4 to IPv6
authors: Alessandro Dorigo
tags:
  - Network
---

# Tunneling and Encapsulation

> [!tip]+ The Problem
>
> Not all routers can be upgraded simultaneously:
>
> - No "flag days"
> - How will network operate with mixed IPv4 and IPv6 routers?


> [!info]+ Tunneling
>
> **Tunneling:** IPv6 packet carried as _payload_ in IPv4 packet among IPv4 routers ("packet within a packet")
>
> Tunneling is used extensively in other contexts as well.
> ![[Pasted image 20251102150530.png]]
> IPv4 packet structure with tunneling:
>
> $$ \text{IPv4 packet} = \text{IPv4 header fields} + \text{IPv6 packet (as payload)} $$
>
> Where:
>
> - IPv4 header fields include: IPv4 source, dest addr
> - IPv6 packet includes: IPv6 header fields (IPv6 source dest addr) + UDP/TCP payload

## Tunneling Scenarios

> [!example]+ **Scenario 1: Ethernet connecting two IPv6 routers**
> ![[Pasted image 20251102150545.png]]
> Network: A (IPv6) — B (IPv6) — _Ethernet connects two IPv6 routers_ — E (IPv6) — F (IPv6)
>
> Link-layer frame contains: The usual packet as payload in link-layer frame

> [!example]+ **Scenario 2: IPv4 network connecting two IPv6 routers**
> ![[Pasted image 20251102150604.png]]
> Network: A (IPv6) — B (IPv6/v4) — _IPv4 network_ — E (IPv6/v4) — F (IPv6)
>
> IPv6 packets are tunneled through the IPv4 network.

> [!example]+ **Scenario 3: IPv4 tunnel connecting two IPv6 routers**
> ![[Pasted image 20251102150616.png]]
> Network: A (IPv6) — B (IPv6/v4) — _IPv4 tunnel connecting IPv6 routers_ — E (IPv6/v4) — F (IPv6)
>
> IPv4 packet structure: IPv4 packet contains tunneling (IPv6 packet as payload in a IPv4 packet)

> [!example]+ Logical vs Physical View
>
> **Logical view:**
> ![[Pasted image 20251102150634.png]]
> A (IPv6) — B (IPv6/v4) — _IPv4 tunnel connecting IPv6 routers_ — E (IPv6/v4) — F (IPv6)
>
> **Physical view:**
> ![[Pasted image 20251102150656.png]]
> A (IPv6) — B (IPv6/v4) — C (IPv4) — D (IPv4) — E (IPv6/v4) — F (IPv6)
>
> Flow details:
>
> - A-to-B: IPv6 (flow: X, src: A, dest: F, data)
> - B-to-C: IPv6 inside IPv4 (src:B, dest: E, Flow: X, Src: A, Dest: F, data)
> - B-to-C: IPv6 inside IPv4 (src:B, dest: E, Flow: X, Src: A, Dest: F, data)
> - B-to-C: IPv6 inside IPv4 (src:B, dest: E, Flow: X, Src: A, Dest: F, data)
> - E-to-F: IPv6 (flow: X, src: A, dest: F, data)

> [!info]+ IPv6 adoption
> in 2025, Google statistics states that roughly 45% of connections are through IPv6
