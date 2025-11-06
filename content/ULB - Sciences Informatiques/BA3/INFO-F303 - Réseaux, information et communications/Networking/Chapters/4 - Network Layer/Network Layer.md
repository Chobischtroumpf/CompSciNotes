---
title: Network Layer
authors: Alessandro Dorigo
tags:
  - Network
---

# Network-layer services and protocols

> [!info]+ Définition
> The **network layer** is responsible for moving packets from a sending host to a receiving host through the network infrastructure.

## Transport Segment Handling

> [!tip]+ Remarque The network layer handles transport segments differently on the sending and receiving sides:
>
> **Sender side:**
>
> - Encapsulates TCP/UDP segments into packets
> - Passes these packets to the link layer for transmission
>
> **Receiver side:**
>
> - Delivers TCP/UDP segments to the transport layer protocol
> - Extracts the segment from the packet for upper-layer processing

## Network Layer Protocols

> [!abstract]+ Universal Network Layer Protocol
> Network layer protocols exist in _every Internet device_, including:
>
> - Hosts (end systems)
> - Routers (intermediate systems)

## Router Functionality

> [!info]+ Définition
>  **Routers** are network devices that:
>
> - Examine header fields in all IP packets passing through them
> - Move packets from input ports to output ports to transfer packets along their end-to-end path

> [!tip]+ Remarque
> ![[Pasted image 20251102104933.png]]
> The diagram illustrates a typical network topology showing:
>
> - Mobile networks connecting to national or global ISPs
> - Enterprise networks with multiple hosts
> - Home networks with local devices
> - Routers at various layers (network, link, physical) facilitating packet forwarding across the Internet infrastructure

 Key functions:
- forwarding: move packets from a router's input link to appropriate router's output link
- routing: determine the route taken by packets from source to destination (routing algorithms)
