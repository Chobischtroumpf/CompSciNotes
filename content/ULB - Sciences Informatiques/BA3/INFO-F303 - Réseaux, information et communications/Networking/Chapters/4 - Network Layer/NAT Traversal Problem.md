---
title: NAT Traversal Problem
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+ Problem definition
>
> The NAT traversal problem occurs when a client wants to connect to a server with address 10.0.0.1, but the server address 10.0.0.1 is local to LAN (client can't use it as destination address). Only one externally visible NATed address exists: 138.76.29.7.

## Solutions

> [!abstract]+ Solution 1
>
> **Solution 1: Static Configuration**
>
> Statically configure NAT to forward incoming connection requests at given port to server.
>
> Example: (138.76.29.7, port 2500) always forwarded to 10.0.0.1 port 25000

> [!abstract]+ Solution 2
>
> **Solution 2: Universal Plug and Play (UPnP)**
> ![[5b4ef4f4464009b4ae63610520c0e9f4.png]]
> Universal Plug and Play (UPnP) Internet Gateway Device (IGD) Protocol allows NATed host to:
>
> - Learn public IP address (138.76.29.7)
> - Add/remove port mappings (with lease times)
>
> This automates static NAT port map configuration.

> [!abstract]+ Solution 3
>
> **Solution 3: Relaying (used in Skype)**
> ![[bfe4fd0b845ee26e4ba603113884b16e.png]]
> Process:
>
> 1. NATed server establishes connection to relay
> 2. External client connects to relay
> 3. Relay bridges packets between two connections
>
> Steps:
>
> - Connection to relay initiated by server (1: connection to relay initiated by NATed host)
> - Client connects to relay (2: connection to relay initiated by client)
> - Relaying established (3: relaying established)

> [!tip]+ To Note
>
> Each solution has different trade-offs:
>
> - Solution 1 requires manual configuration
> - Solution 2 requires UPnP support
> - Solution 3 adds latency and requires relay infrastructure
