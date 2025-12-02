---
title: Hierarchical Addressing
authors: Alessandro Dorigo, Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Hierarchical addressing** is a technique that allows efficient advertisement of routing information by grouping multiple network addresses into a single routing entry. This enables **route aggregation**, reducing the size of routing tables across the Internet.

## Route Aggregation

> [!abstract]+ Aggregation Principle
> **Instead of advertising individual routes, ISPs advertise aggregated routes:**
>
> Multiple organization networks can be combined under a single routing entry when they share a common address prefix.
>
> **Benefits:**
> - Smaller routing tables
> - Reduced routing update traffic
> - More efficient router memory usage
> - Faster route lookups

> [!example]+ ISP Aggregation Example
> ![[26249f5983d52b814e3baaddc8d5bf72.png]]
>
> **Scenario:** ISP (Fly-By-Night-ISP) has 8 customer organizations [[DHCP#^bc1a5d|from DHCP]]
>
> **Without aggregation:** Advertise 8 separate routes
>
> **With aggregation:** Single advertisement:
> "Send me anything with addresses beginning `200.23.16.0/20`"
>
> This covers all addresses from `200.23.16.0` to `200.23.31.255`.

## Provider Independent Addresses

> [!info]+ PI Addresses and Multihoming
> **Provider Independent (PI) addresses** allow organizations to maintain their address range even when connecting to multiple ISPs (multihoming).
>
> ![[86d303ff4400ee4b3b018df320ebdb34.png]]
>
> **Example configuration:**
> - Organization 8 has PI range: `100.56.10.0/23`
> - Connects to both Fly-By-Night-ISP and ISPs-R-Us
>
> **Routing advertisements:**
>
> | ISP | Advertises to Internet |
> |-----|----------------------|
> | Fly-By-Night-ISP | `200.23.16.0/20` or `100.56.10.0/23` |
> | ISPs-R-Us | `199.31.0.0/16` or `100.56.10.0/23` |

## Forwarding Tables

> [!note]+ Table Structure
> **If forwarding is based only on destination address:**
> - $2^{32}$ (4 billion) possible [[IPv4]] addresses
> - Storing every address individually is impractical
>
> **Solution:** Aggregate addresses sharing the same [[Subnet]] into single entries
>
> **Fly-By-Night-ISP forwarding table:**
>
> | Destination Address Range | Outgoing Interface |
> |---------------------------|-------------------|
> | `200.23.16.0/23` | 0 |
> | `200.23.18.0/23` | 1 |
> | `200.23.20.0/23` | 2 |
> | ... | ... |
>
> **Further aggregation:** All organizations under `200.23.16.0/20`

## Specific Routes

> [!example]+ Handling Exceptions
> ![[96acd1c2e0b4d81e8a0b3bfca08f428f.png]]
>
> **Scenario:** Fly-By-Night-ISP acquires ISPs-R-Us
> - Organization 1 now connects through ISPs-R-Us
> - Organization 1 wants to keep its address range `200.23.18.0/23`
>
> **Solution:** ISPs-R-Us advertises a more specific route:
> - `199.31.0.0/16` (its own block)
> - `200.23.18.0/23` (Organization 1's specific route)

## Overlapping Entries

> [!warning]+ Handling Overlap
> **Problem:** Routers may have overlapping entries in their forwarding tables
>
> **Two approaches:**
> 1. **Split aggregated blocks** into smaller prefixes
>    - Leads to larger tables
>    - Defeats purpose of aggregation
>
> 2. **Use [[Longest Prefix Matching]]**
>    - Keep aggregated entries
>    - Match the most specific (longest) prefix
>    - Preferred solution

## Related Concepts

> [!note]+ See Also
> - **[[Longest Prefix Matching]]**: Resolution for overlapping routes
> - **[[CIDR]]**: Flexible prefix-based addressing
> - **[[Subnet]]**: Network subdivision
> - **[[IPv4]]**: IP addressing fundamentals
> - **[[DHCP]]**: Address allocation within subnets
> - **[[Network Layer]]**: Layer where hierarchical addressing operates
