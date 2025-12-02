---
title: Longest Prefix Matching
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Longest Prefix Matching** is a forwarding table lookup algorithm where, given a destination address, the router uses the entry with the longest address prefix that matches the destination.

## Why Longest Prefix Matching?

> [!abstract]+ The Problem
> **Overlapping prefixes create ambiguity:**
>
> When multiple forwarding table entries match a destination address, the router must decide which entry to use.
>
> **Solution:** Always use the most specific match (longest prefix)
>
> **Benefits:**
> - Enables aggressive route aggregation
> - Allows specific routes to override general routes
> - Keeps forwarding tables small

## How It Works

> [!example]+ Matching Example
> ![[4b0d890022cbd88e2156606b3258e53d.png]]
>
> **Forwarding table:**
>
> | Prefix | Link Interface |
> |--------|---------------|
> | `11001000 00010111 0001**** ********` (/20) | 1 |
> | `11001000 00010111 0001001* ********` (/23) | 2 |
>
> **Two destination addresses:**
>
> | Address | Matches /20? | Matches /23? | Selected Interface |
> |---------|-------------|-------------|-------------------|
> | `11001000 00010111 00011000 10100001` | Yes | No | **1** |
> | `11001000 00010111 00010010 10101010` | Yes | Yes | **2** (longer prefix) |
>
> **Analysis:**
> - First address: Bits 21-23 are `100`, but prefix 2 requires `001` → only matches /20
> - Second address: Bits 21-23 are `001` → matches both prefixes, use longest (/23)

## Aggregation Trade-offs

> [!tip]+ Why This Approach?
> **Prefix matching enables efficient aggregation:**
> - Entries with the same prefix are typically in the same geographic area
> - One entry per [[Subnet]], or one per aggregation of subnets
> - Address block size is always a power of 2
>
> **Longest prefix matching adds flexibility:**
> - Allows even more aggregation
> - Specific routes can override aggregated routes
> - Trade-off: more complex lookup procedure

## Implementation

> [!note]+ Performance Considerations
> **Challenge:** Matching must be extremely fast for line-speed forwarding
>
> **Hardware solutions:**
>
> | Technology | Description |
> |------------|-------------|
> | **TCAM** | Ternary Content Addressable Memory |
> | **Tries** | Tree-based data structures |
>
> **TCAM characteristics:**
> - Content addressable: present address, retrieve action
> - One clock cycle lookup regardless of table size
> - Supports "don't care" bits for prefix matching
>
> **Software implementations:**
> - Use **trie** data structures
> - Efficient for variable-length prefix matching
> - Common in software routers and SDN controllers

> [!abstract]+ TCAM Operation
> **How TCAMs work:**
> 1. Destination address presented to TCAM
> 2. All entries compared in parallel
> 3. Matching entries identified simultaneously
> 4. Longest match selected by priority encoding
> 5. Output action retrieved in single clock cycle

## Related Concepts

> [!note]+ See Also
> - **[[Hierarchical Addressing]]**: Route aggregation using prefixes
> - **[[CIDR]]**: Classless addressing with variable-length prefixes
> - **[[Router Input Ports]]**: Where lookup occurs
> - **[[Data Plane]]**: Per-router forwarding function
> - **[[Forwarding]]**: Packet forwarding process
> - **[[Network Layer]]**: Layer where prefix matching operates
