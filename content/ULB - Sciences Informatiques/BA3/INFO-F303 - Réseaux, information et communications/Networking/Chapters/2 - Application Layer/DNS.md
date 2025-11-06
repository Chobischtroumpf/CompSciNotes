---
title: DNS
authors: Alessandro Dorigo
tags:
  - Network
---


> [!info]+ Definition
> **DNS (Domain Name System)** is a distributed database implemented in a hierarchy of name servers that translates domain names to IP addresses.
## Core Functions
> [!abstract]- What DNS Does
> - **Name resolution**: Translates hostnames to IP addresses (www.example.com → 93.184.216.34)
> - **Host aliasing**: Multiple names for same host
> - **Mail server aliasing**: MX records for email routing
> - **Load distribution**: One name maps to multiple IP addresses
## DNS Hierarchy
![[Pasted image 20251027163338.png]]

> [!note]+ Name Resolution Process
> Client wants IP for www.amazon.com:
> 1. Query **root server** to find .com DNS server
> 2. Query **.com DNS server** to get amazon.com DNS server
> 3. Query **amazon.com DNS server** to get IP address
>
> **Caching**: Once learned, mappings are cached (with TTL)
## Query Types
> [!info]+ Iterative Query
> - Contacted server replies with **name of next server to contact**
> - Client does the work of contacting each server
> - Caching happens in local DNS server
>
> ![[Pasted image 20251027163921.png]]

> [!info]+ Recursive Query
> - Puts burden on contacted server to resolve the name
> - Heavy load at upper hierarchy levels
> - Less commonly used
>
> ![[Pasted image 20251027164013.png]]
## Related Concepts
> [!note]+ See Also
> - [[DNS records]]: Detailed record types
> - [[DNS protocol messages]]: Message format details
> - [[Application layer protocol]]: DNS operates at this layer
> - Uses [[UDP]] (port 53) for queries, [[TCP]] for zone transfers
