---
title: Subnet
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> A **Subnet** (sub-network) consists of device interfaces that can physically reach each other *without passing through an intervening router*. Devices within the same subnet communicate directly at the link layer without requiring network-layer routing.

## Identifying Subnets

> [!abstract]+ How to Define Subnets
> **Process:**
> 1. Detach each interface from its host or router
> 2. This creates "islands" of isolated networks
> 3. Each isolated network is a **subnet**
>
> Interfaces on the same subnet share a common IP address prefix.

## Subnet Example

> [!example]+ Network Topology
> ![[08ba38cbbb3b14a0da55bd8b74a838d9.png]]
>
> **Three subnets identified:**
>
> | Subnet | Address | Hosts |
> |--------|---------|-------|
> | 1 | `223.1.1.0/24` | `223.1.1.1`, `223.1.1.2`, `223.1.1.3`, `223.1.1.4` |
> | 2 | `223.1.2.0/24` | `223.1.2.1`, `223.1.2.9` |
> | 3 | `223.1.3.0/24` | `223.1.3.27`, `223.1.3.1`, `223.1.3.2` |

## Subnet Mask

> [!note]+ Understanding the Mask
> **The `/24` notation (subnet mask):**
> - Indicates that the first 24 bits identify the subnet
> - Remaining 8 bits identify hosts within the subnet
>
> **General formula:**
> - Subnet mask of `/n` means first $n$ bits are the subnet prefix
> - Leaves $(32 - n)$ bits for host addresses
> - Usable host addresses: $2^{(32-n)} - 2$

> [!warning]+ Reserved Addresses
> **The $-2$ accounts for two reserved addresses:**
>
> | Address Type | Host Bits | Purpose |
> |-------------|-----------|---------|
> | Network address | All 0s | Identifies the subnet itself |
> | Broadcast address | All 1s | Sends to all hosts in subnet |
>
> **Example for `/24`:**
> - $2^8 - 2 = 254$ usable host addresses
> - Network address: `223.1.1.0`
> - Broadcast address: `223.1.1.255`
> - Usable range: `223.1.1.1` to `223.1.1.254`

## Another Example

> [!example]+ Complex Network
> ![[86c7cef6a07957871ea24f827afb5d3c.png]]
>
> This topology shows multiple subnets interconnected by routers, each with its own address prefix.

## Related Concepts

> [!note]+ See Also
> - **[[IPv4]]**: IP addressing fundamentals
> - **[[CIDR]]**: Flexible subnet sizing
> - **[[DHCP]]**: Automatic address assignment within subnets
> - **[[Hierarchical Addressing]]**: Route aggregation using subnets
> - **[[NAT]]**: Private subnet addressing
> - **[[Network Layer]]**: Layer where subnetting operates
