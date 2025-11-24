---
title: Hierarchical IPv6 Addressing
authors: Alessandro Dorigo
tags:
  - Network
---

> [!info]+ Hierarchical Addresses to Allow for Aggregation
>
> IPv6 uses hierarchical addressing to enable efficient routing aggregation.
>
> **Prefix of 64 bits:** Identifies a site (initial part, typically 48 bits, e.g., given by ISP)
>
> **Suffix of 64 bits:** Identifies an interface in this site
>
> - May be assigned in several ways: e.g., DHCPv6, or based on interface "layer 2" address (see chapter 6), or pseudo-random
> - Pseudo-random by default in many operating systems

> [!info]+ Link-Local Addresses
>
> Link-local addresses are special IPv6 addresses used for communication within a single network link.
>
> **Properties:**
>
> - Not routable, have a scope limited to a link
> - Suffix derived from 48-bit interface "layer 2" address
> - Prefix is FE80:0:0:0
>
> $$ \text{Link-local address} = \text{FE80:0:0:0}:\text{interface-derived-suffix} $$
