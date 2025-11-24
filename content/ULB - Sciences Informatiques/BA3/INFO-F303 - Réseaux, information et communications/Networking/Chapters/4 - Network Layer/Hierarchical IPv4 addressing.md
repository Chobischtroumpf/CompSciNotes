---
title: Hierarchical IPv4 addressing
authors: Alessandro Dorigo
tags:
  - Network
---

# route aggregation

> [!info]+ Definition
> **Hierarchical addressing** allows efficient advertisement of routing information by grouping multiple network addresses into a single routing entry.

## Route Aggregation Principle

> [!tip]+
> Hierarchical addressing enables route aggregation, where multiple organization networks can be advertised as a single aggregated route, reducing the size of routing tables.

> [!example]+
>  Consider multiple organizations with contiguous address blocks:
> ![[26249f5983d52b814e3baaddc8d5bf72.png]]
> - **Organization 0:** $200.23.16.0/23$
> - **Organization 1:** $200.23.18.0/23$
> - **Organization 2:** $200.23.20.0/23$
> ...
> - **Organization 7:** $200.23.30.0/23$
>
> These organizations are all served by the same ISP (Fly-By-Night-ISP).
>
> Instead of advertising 8 separate routes to the Internet, the ISP can advertise a single aggregated route: "Send me anything with addresses beginning $200.23.16.0/20$"
>
> This single route covers all addresses from $200.23.16.0$ to $200.23.31.255$, encompassing all 8 organizations.
>
> Meanwhile, other ISPs (ISPs-R-Us) advertise their own aggregated routes, such as "Send me anything with addresses beginning $199.31.0.0/16$"

> [!abstract]+
> Route aggregation works by using a shorter prefix (e.g., $/20$ instead of $/23$) that encompasses multiple smaller subnets. The aggregated prefix includes all addresses that share the same high-order bits.

# Provider Independent (PI) Adresses - Multihoming

> [!info]+ Définition
>
> An alternative approach where Organization 8 gets a Provider Independent (PI) range of addresses. Organization 8 may have multiple providers (so-called multihoming).

> [!example]+ Exemple
>
> ![[86d303ff4400ee4b3b018df320ebdb34.png]]
> In this configuration, Organization 8 has the address range $100.56.10.0/23$ and connects to two ISPs:
>
> - **Fly-By-Night-ISP** with address range $200.23.16.0/20$
> - **ISPs-R-Us** with address range $199.31.0.0/16$
>
> Organization 8 sends the following routing information:
>
> - To Fly-By-Night-ISP: "Send me anything with addresses beginning $100.56.10.0/23$"
> - To ISPs-R-Us: "Send me anything with addresses beginning $100.56.10.0/23$"
>
> The ISPs then advertise to the Internet:
>
> - Fly-By-Night-ISP advertises: "Send me anything with addresses beginning $200.23.16.0/20$ or $100.56.10.0/23$"
> - ISPs-R-Us advertises: "Send me anything with addresses beginning $199.31.0.0/16$ or $100.56.10.0/23$"
# IP forwarding table

> [!info]+ Définition
>
> Assume forwarding is only based on the destination address. There are $2^{32}$ (i.e., 4 billion) IPv4 addresses.

> [!tip]+ Remarque
>
> Clearly all addresses in the same subnet can be aggregated into a single forwarding entry in every table (why?)
>
> - Saves space in forwarding table
> - Makes address look-up more efficient too

> [!example]+ Exemple
>
> Forwarding table in Fly-By-Night-ISP:
>
> |Destination Address Range (Subnet)|Outgoing link interface|
> |---|---|
> |$200.23.16.0/23$|0|
> |$200.23.18.0/23$|1|
> |$200.23.20.0/23$|2|
> |...|...|
# More aggregation is possible in forwarding table

> [!example]+ Exemple
> ![[ULB - Sciences Informatiques/BA3/INFO-F303 - Réseaux, information et communications/Networking/Chapters/4 - Network Layer/Images/Pasted image 20251102135526.png]]
> Multiple organizations can be aggregated:
>
> - Organization 0: $200.23.16.0/23$
> - Organization 1: $200.23.18.0/23$
> - Organization 2: $200.23.20.0/23$
> - ...
> - Organization 7: $200.23.30.0/23$
>
> All connect to Fly-By-Night-ISP ($200.23.16.0/20$), which advertises to the Internet: "Send me anything with addresses beginning $200.23.16.0/20$"

# Hierarchical addressing: more specific routes

> [!info]+ Définition
>
> Hierarchical addressing allows for route aggregation while maintaining the ability to specify more specific routes when needed.

> [!example]+ Exemple
> ![[96acd1c2e0b4d81e8a0b3bfca08f428f.png]]
> Scenario:
>
> - Assume Fly-By-Night-ISP acquires ISPs-R-Us
> - Assume organization 1 now connects through its subsidiary ISPs-R-Us
> - Good for organization 1 to keep its address range (easier management)
> - ISPs-R-Us now advertises a more specific route to Organization 1
>
> Network configuration:
>
> - Organization 0: 200.23.16.0/23200.23.16.0/23
> - Organization 1: 200.23.18.0/23200.23.18.0/23
> - Organization 2: 200.23.20.0/23200.23.20.0/23
> - ...
> - Organization 7: 200.23.30.0/23200.23.30.0/23
>
> ISP configuration:
>
> - Fly-By-Night-ISP (200.23.16.0/20200.23.16.0/20) advertises: "Send me anything with addresses beginning 200.23.16.0/20200.23.16.0/20"
> - ISPs-R-Us (199.31.0.0/16199.31.0.0/16) advertises: "Send me anything with addresses beginning 199.31.0.0/16199.31.0.0/16" or "200.23.18.0/23200.23.18.0/23"

# IP forwarding table – Overlap

> [!tip]+
> In practice, routers in the network often have overlapping entries in their table.
>
> Overlap can be avoided by splitting $200.23.16.0/20$ into smaller blocks (i.e. longer prefixes), each with outgoing link interface 1 (how?)
>
> - But it would lead to larger tables
> - Longest prefix matching is more elegant and simpler

> [!example]+ Example
>
> Internet routers advertise:
>
> - "Send me anything with addresses beginning $200.23.16.0/20$"
> - "Send me anything with addresses beginning $199.31.0.0/16$ or $200.23.18.0/23$"
>
> Forwarding table with overlapping entries:
>
> ![[751b978ee504f831e8097d1cd5f3aed1.png]]

# Longest prefix matching

> [!info]+
>
> When looking for forwarding table entry for given destination address, use longest address prefix that matches destination address.
> ![[4b0d890022cbd88e2156606b3258e53d.png]]
>
> The overlap between the first entry (prefix length unspecified but shorter) and the other more specific entries (longer prefixes) is resolved using longest prefix matching. The default route ($0/0$) matches any address when no more specific route exists.

> [!tip] How do ISPs get blocks of addresses?
> [ICANN](https://www.icann.org/) is the organization in charge of allocating IP addresses:
> - Allocates IP addresses through 5 Regional Registries (RRs)
> - Manages the DNS root zone, including managing delegation of individual TLDs (.com, .edu, .org...)

> [!tip] There aren't enough IPv4 Addresses
> the last chunk of IPv4 Addresses was allocated by ICANN in 2011
> [[NAT]] is the technology used to help with IPv4 address space exhaustion
> IPv6 IP addresses have 128 bit address space
