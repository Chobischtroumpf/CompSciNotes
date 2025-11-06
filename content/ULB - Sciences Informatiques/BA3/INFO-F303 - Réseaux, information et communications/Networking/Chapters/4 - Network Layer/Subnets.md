---
title: Subnets
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+ Definition
> A **subnet** (subnetwork) consists of device interfaces that can physically reach each other _without passing through an intervening router_.

> [!tip]+ Remarque
> Devices within the same subnet can communicate directly at the link layer without requiring network-layer routing.
## Recipe for Defining Subnets

> [!abstract]+ Identifying subnets
> To identify subnets in a network:
>
> 1. Detach each interface from its host or router, creating "islands" of isolated networks
> 2. Each isolated network is called a **subnet**

> [!example]+
> Consider a network topology with the following subnets:
>  ![[Pasted image 20251102115817.png]]
>
> **Subnet $223.1.1.0/24$:**
>
> - Contains interfaces: $223.1.1.1$, $223.1.1.2$, $223.1.1.3$, $223.1.1.4$
> - All devices share the first 24 bits ($223.1.1$)
>
> **Subnet $223.1.2.0/24$:**
>
> - Contains interfaces: $223.1.2.1$, $223.1.2.9$
> - All devices share the first 24 bits ($223.1.2$)
>
> **Subnet $223.1.3.0/24$:**
>
> - Contains interfaces: $223.1.3.27$, $223.1.3.1$, $223.1.3.2$
> - All devices share the first 24 bits ($223.1.3$)
>
> In this example, the subnet mask is $/24$, meaning the high-order 24 bits represent the subnet part of the IP address.

> [!tip]+ Remarque
> The notation $/24$ (CIDR notation) indicates that the first 24 bits of the IP address are the subnet prefix, leaving 8 bits for host addresses within each subnet. This allows for $2^8 - 2 = 254$ usable host addresses per subnet.

> [!example] Another Example:
> ![[Pasted image 20251102115926.png]]
