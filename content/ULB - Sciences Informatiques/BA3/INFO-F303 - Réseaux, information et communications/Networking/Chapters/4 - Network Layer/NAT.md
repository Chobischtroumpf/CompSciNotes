---
title: NAT
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **NAT (Network Address Translation)** is a technique that allows all devices in a local network to share a single public IP address. All devices in the local network have 32-bit addresses in a "private" IP address space ($10/8$, $172.16/12$, $192.168/16$ prefixes) that can only be used in the local network.

> [!tip]+
>
> Advantages of NAT:
>
> - Just one IP address needed from provider ISP for all devices
> - Can change addresses of host in local network without notifying outside world
> - Can change ISP without changing addresses of devices in local network
> - Security: devices inside local net not directly addressable, visible by outside world

## Implementation

> [!abstract]+
>
> NAT router must (transparently):
>
> **Outgoing packets:** replace (source IP address, port #) of every outgoing packet to (NAT IP address, new port #)
>
> - Remote clients/servers will respond using (NAT IP address, new port #) as destination address
>
> **Remember** (in NAT translation table) every (source IP address, port #) to (NAT IP address, new port #) translation pair
>
> **Incoming packets:** replace (NAT IP address, new port #) in destination fields of every incoming packet with corresponding (source IP address, port #) stored in NAT table

> [!example]+ Example
> ![[Pasted image 20251102142303.png]]
> 1. Host $10.0.0.1$ sends packet to $128.119.40.186$, port $80$
> 2. NAT router changes packet source address from $10.0.0.1$, $3345$ to $138.76.29.7$, $5001$, updates table
> 3. Reply arrives, destination address: $138.76.29.7$, $5001$
> 4. NAT router changes packet dest addr from $138.76.29.7$, $5001$ to $10.0.0.1$, $3345$

## Additional Properties

> [!tip]+
>
> - Possible to restrict incoming traffic even more (e.g., only from contacted outside host, by adding fields in WAN side of table)
> - 16-bit port-number field: $60,000$ simultaneous connections with a single LAN-side address!

> [!tip]+
>
> NAT has been controversial:
>
> - Routers "should" only process up to layer 3
> - Address "shortage" should be solved by IPv6
> - Violates end-to-end argument (port # manipulation by network-layer device)
> - NAT traversal: what if client wants to connect to server behind NAT?
>
> But NAT is here to stay:
>
> - Extensively used in home and institutional nets, 4G/5G cellular nets
