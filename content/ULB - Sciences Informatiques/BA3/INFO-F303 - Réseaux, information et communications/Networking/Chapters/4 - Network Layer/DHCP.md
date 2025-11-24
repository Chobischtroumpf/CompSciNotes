---
title: DHCP
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **DHCP (Dynamic Host Configuration Protocol)** allows a host to _dynamically_ obtain an IP address from a network server when it "joins" a network.

> [!tip]+ Advantages:
>
> - Hosts can renew their lease on an address currently in use
> - Allows reuse of addresses (only holds address while connected/"on")
> - Provides support for mobile users who join/leave networks

## DHCP Protocol Overview

> [!abstract]+ Message exchange steps:
>
> 1. **DHCP discover**: Host broadcasts a DHCP discover message [optional]
> 2. **DHCP offer**: DHCP server responds with a DHCP offer message [optional]
> 3. **DHCP request**: Host requests an IP address with a DHCP request message
> 4. **DHCP ack**: DHCP server sends the address with a DHCP ack message

> [!example]+ DHCP Client-Server Scenario
> Consider a network topology with DHCP server at address $223.1.2.5$:
> ![[89ea71d1dbf36595f4d3ebfbcf96350b.png]]
> ![[0aad59370cad94a8060ec4f29dcc4f80.png]]
>
> - The server is located within the router at $223.1.2.5$
> - When a DHCP client arrives in the network (e.g., at $223.1.2.2$), it needs to obtain an IP address
> - The client has no IP address and doesn't know the IP address of the DHCP server(s)
>
>**The complete DHCP exchange proceeds as follows:**
>![[2014397ee8b055dd012af37e4b49b097.png]]
> **DHCP discover** (broadcast):
>
> - Client broadcasts: "Is there a DHCP server out there?"
> - Source: $0.0.0.0$ (client has no IP yet)
> - Destination: $255.255.255.255$ (broadcast)
> - Message includes transaction ID
>
> **DHCP offer** (broadcast):
>
> - Server broadcasts: "I'm a DHCP server! Here's an IP address you can use"
> - Source: $223.1.2.5$ (DHCP server)
> - Destination: $255.255.255.255$ (broadcast on subnet)
> - Offered address: $223.1.2.4$
> - Lifetime: $3600$ seconds
>
> **DHCP request** (broadcast):
>
> - Client broadcasts: "OK, I'll take that IP address!"
> - Requested address: $223.1.2.4$
> - Transaction ID matches the offer
>
> **DHCP ACK** (broadcast):
>
> - Server broadcasts: "OK, You've got that IP address!"
> - Confirms address: $223.1.2.4$
> - Provides additional configuration information

> [!tip]+
> The first two steps (discover and offer) can be skipped if a client remembers and wishes to reuse a previously allocated network address (RFC 2131).
>
> DHCP uses UDP because it needs to work before the client has an IP address, and broadcasting ensures all devices on the subnet receive the messages.

## DHCP: More Than IP Addresses

> [!note]+
> DHCP can return more than just an allocated IP address on a subnet:
>
> - Address of first-hop router for client
> - Name and IP address of local DNS server
> - Network mask (indicating network versus host portion of address)
> - Additional configuration parameters

## DHCP Protocol Stack Example

> [!example]+ Exemple **Client side (connecting laptop):**
>
> - Connecting laptop will use DHCP to get IP address, address of first-hop router, and address of DNS server
> - DHCP REQUEST message is encapsulated in UDP, encapsulated in IP, encapsulated in Ethernet
> - Ethernet frame is broadcast on LAN, received at router running DHCP server
> - Ethernet frame is demux'ed to IP, then demux'ed to UDP, then to DHCP
>
> **Server side (router with DHCP server):**
>
> - DCP server formulates DHCP ACK containing client's IP address, IP address of first-hop router for client, and name & IP address of DNS server
> - Encapsulated DHCP server reply is forwarded to client, demuxing up to DHCP at client
> - Client now knows its IP address, name and IP address of DNS server, and IP address of its first-hop router

> [!tip]+ Remarque The protocol stack for DHCP messages follows the standard layered architecture:
>
> - Application layer: DHCP
> - Transport layer: UDP
> - Network layer: IP
> - Link layer: Ethernet (Eth)
> - Physical layer: Physical medium (Phy)
