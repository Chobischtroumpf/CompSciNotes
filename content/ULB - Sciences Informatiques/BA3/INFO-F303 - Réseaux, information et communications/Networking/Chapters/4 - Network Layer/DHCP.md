---
title: DHCP
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **DHCP (Dynamic Host Configuration Protocol)** allows a host to *dynamically* obtain an IP address from a network server when it joins a network, eliminating the need for manual configuration.

## Why Use DHCP?

> [!success]+ Advantages
> **Dynamic allocation:**
> - Hosts can renew their lease on addresses in use
> - Allows reuse of addresses (only holds address while connected)
> - Supports mobile users who join/leave networks
>
> **Compared to static configuration:**
> - No need to manually configure each device
> - Reduces administrative overhead
> - Prevents address conflicts

## DHCP Message Exchange

> [!abstract]+ Four-Step Process (DORA)
> 1. **Discover:** Host broadcasts "Is there a DHCP server out there?"
> 2. **Offer:** DHCP server responds "Here's an IP address you can use"
> 3. **Request:** Host broadcasts "OK, I'll take that IP address!"
> 4. **ACK:** DHCP server confirms "OK, you've got that IP address!"
>
> ![[2014397ee8b055dd012af37e4b49b097.png]]

> [!tip]+ Optional Steps
> The first two steps (Discover and Offer) can be skipped if a client remembers and wishes to reuse a previously allocated network address (RFC 2131).

## Detailed Example

> [!example]+ DHCP in Action
> ![[89ea71d1dbf36595f4d3ebfbcf96350b.png]]
>
> **Network setup:**
> - DHCP server at `223.1.2.5` (within router)
> - New client arrives needing an IP address
> - Client has no IP and doesn't know server's address

### Message Details

> [!note]+ DHCP Discover
> ```
> src:    0.0.0.0, port 68
> dest:   255.255.255.255, port 67
> yiaddr: 0.0.0.0
> transaction ID: 654
> ```
> *Client broadcasts from `0.0.0.0` (no address yet) to `255.255.255.255` (broadcast)*

> [!note]+ DHCP Offer
> ```
> src:    223.1.2.5, port 67
> dest:   255.255.255.255, port 68
> yiaddr: 223.1.2.4
> transaction ID: 654
> lifetime: 3600 secs
> ```
> *Server offers address `223.1.2.4` with 1-hour lease*

> [!note]+ DHCP Request
> ```
> src:    0.0.0.0, port 68
> dest:   255.255.255.255, port 67
> yiaddr: 223.1.2.4
> transaction ID: 655
> lifetime: 3600 secs
> ```
> *Client requests the offered address*

> [!note]+ DHCP ACK
> ```
> src:    223.1.2.5, port 67
> dest:   255.255.255.255, port 68
> yiaddr: 223.1.2.4
> transaction ID: 655
> lifetime: 3600 secs
> ```
> *Server confirms the address assignment*

![[0aad59370cad94a8060ec4f29dcc4f80.png]]

## Why Broadcast?

> [!warning]+ Protocol Design
> **All messages are broadcast because:**
> - Client doesn't have an IP address initially
> - Client doesn't know DHCP server's address
> - Multiple DHCP servers may exist on the network
>
> **DHCP uses [[UDP]]:**
> - Must work before client has an IP address
> - Broadcasting ensures all devices on subnet receive messages

## Additional Information Provided

> [!info]+ Beyond IP Address
> DHCP can return more than just an IP address:
> - **First-hop router address:** Default gateway for the client
> - **DNS server:** Name and IP address of local DNS server
> - **Network mask:** Indicating network vs host portion of address

## Protocol Stack Example

> [!example]+ Complete DHCP Flow
> ![[92a33993ec2396ead997e12e83b7585c.png]]
>
> **Client request path:**
> 1. DHCP REQUEST message created
> 2. Encapsulated in [[UDP]]
> 3. Encapsulated in IP
> 4. Encapsulated in Ethernet frame
> 5. Broadcast on LAN
> 6. Received at router running DHCP server
> 7. Demultiplexed: Ethernet → IP → UDP → DHCP
>
> ![[e66987dfe5c234fbec98fd519f1ede77.png]]
>
> **Server response:**
> 8. DHCP ACK formulated containing:
>    - Client's IP address
>    - First-hop router IP address
>    - DNS server name and IP address
> 9. Encapsulated and forwarded to client
> 10. Client now knows: its IP, DNS server, and first-hop router

## Subnet Address Allocation

> [!abstract]+ How Networks Get Address Blocks
> **Provider Assigned (PA) addresses:**
> - Networks get allocated portion of ISP's address space
>
> **Example - ISP's block:** `200.23.16.0/20`
>
> ISP allocates to organizations:
>
> | Organization | Address Block |
> |:---:|:---:|
> | 0 | `200.23.16.0/23` |
> | 1 | `200.23.18.0/23` |
> | 2 | `200.23.20.0/23` |
> | ... | ... |
> | 7 | `200.23.30.0/23` |

^bc1a5d

## Related Concepts

> [!note]+ See Also
> - **[[IPv4]]**: IP addressing fundamentals
> - **[[Subnet]]**: Network subdivision
> - **[[CIDR]]**: Address block notation
> - **[[UDP]]**: Transport protocol used by DHCP
> - **[[NAT]]**: Often used with DHCP for private networks
> - **[[Network Layer]]**: Layer where DHCP operates
