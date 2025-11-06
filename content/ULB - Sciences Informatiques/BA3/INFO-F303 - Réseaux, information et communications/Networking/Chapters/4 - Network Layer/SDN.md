---
title: SDN
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **Software-Defined Networking (SDN)** is a network architecture approach where a remote controller computes and installs forwarding tables in routers by interacting with control agents (CAs) in routers.

## SDN Architecture

> [!tip]+ Remarque The SDN architecture separates the network into two distinct planes:
>
> **[[Control plane]]** (centralized):
>
> - A remote controller serves as the centralized "brain" of the network
> - The controller computes optimal forwarding tables for all routers
> - It communicates with control agents (CAs) in each router to install forwarding tables
> - Control logic is implemented in software on remote servers
>
> **[[Data plane]]** (distributed):
>
> - Routers contain control agents (CAs) that receive instructions from the remote controller
> - Each router maintains a local forwarding table installed by the controller
> - Packets are forwarded based on values in the arriving packet header
> - Routers focus purely on packet forwarding, not routing decisions

## Key Characteristics

> [!tip]+ Remarque In the SDN approach:
>
> - The routing intelligence is _centralized_ in the remote controller
> - Routers become simpler forwarding devices
> - The network can be programmed and reconfigured more easily through software
> - The controller has a global view of the network topology
> - Forwarding tables are computed centrally and distributed to all routers

> [!example]+ Example
> When a packet arrives with header value $0111$ at a router, the router uses the forwarding table previously installed by the remote controller to determine the appropriate output port for that packet.
![[Pasted image 20251102112026.png]]
