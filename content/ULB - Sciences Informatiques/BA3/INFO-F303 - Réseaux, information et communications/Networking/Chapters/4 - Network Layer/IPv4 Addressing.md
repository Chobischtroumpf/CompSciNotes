---
title: IPv4 Addressing
authors: Alessandro Dorigo
tags:
  - Network
---

> [!note] IPv4 Address
> 32-bit identifier associated with each host or router interface

> [!note] Interface
> connection between host/router and physical link
> - routers typically have multiple interfaces
> - host typically only has one or a few interfaces (e.g.: wired Ethernet, wireless WIFI)

## IP Address Structure

> [!info]+ Définition IP addresses have a hierarchical structure composed of two parts:
>
> **Subnet part** (also called **address prefix**):
>
> - Represents the high-order bits of the IP address
> - Devices in the same subnet share common high-order bits
> - Identifies the network portion of the address
>
> **Host part**:
>
> - Represents the remaining low-order bits of the IP address
> - Uniquely identifies individual devices within the subnet
> - Distinguishes different hosts on the same network

> [!example]+ Example
> In the subnet notation 223.1.1.x, the first three octets (223.1.1) represent the subnet prefix, while the remaining bits identify individual hosts within that subnet.
> ![[9a6fa82268cb12ca1fe30bc060c4c9a3.png]]
