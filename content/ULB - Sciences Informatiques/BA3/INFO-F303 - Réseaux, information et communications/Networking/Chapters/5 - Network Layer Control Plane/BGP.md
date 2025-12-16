---
title: BGP
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **BGP (Border Gateway Protocol)** is the de facto inter-domain routing protocol, often described as the "glue that holds the Internet together." BGP allows a subnet to advertise its existence and the destinations it can reach to the rest of the Internet.

## BGP Functions

> [!abstract]+ What BGP Provides
> BGP provides each [[Autonomous Systems|AS]] the means to:
>
> | Function | Protocol | Description |
> |----------|----------|-------------|
> | **Obtain reachability** | eBGP (external) | Learn subnet reachability from neighboring ASes |
> | **Propagate reachability** | iBGP (internal) | Distribute reachability info to all AS-internal routers |
> | **Determine routes** | Both | Select "good" routes based on reachability and policy |
>
> ![[Pasted image 20251203161958.png]]
>
> *Three ASes connected via eBGP, with iBGP within each AS (logical connectivity ≠ physical connectivity)*

## BGP Basics

> [!note]+ BGP Sessions
> **BGP session:** Two BGP routers ("peers") exchange BGP messages over a semi-permanent [[TCP]] connection
>
> **Key characteristics:**
> - Advertises paths to different destination IP prefixes
> - BGP is a "path vector" protocol: the full path is propagated, not just the distance (unlike [[Distance Vector Algorithm|DV]])
>
> **Example:** When `AS3` gateway `3a` advertises path `AS3,X` to `AS2` gateway `2c`:
> - `AS3` **promises** to `AS2` it will forward packets towards subnet X
>
> ![[Pasted image 20251203162203.png]]

## BGP Route Attributes

> [!info]+ Advertised Route Structure
> **BGP advertised route = prefix + attributes**
>
> | Component | Description |
> |-----------|-------------|
> | **Prefix** | Destination being advertised |
> | **AS-PATH** | List of ASes through which the advertisement has passed |
> | **NEXT-HOP** | Specific internal-AS gateway router to first AS in path |

## Policy-Based Routing

> [!note]+ Import and Export Policies
> **Import policy:**
> - Gateway receiving route advertisement decides to accept or decline path
> - Example: "Never route through AS Y"
>
> **Export policy:**
> - AS policy determines whether to advertise path to neighboring ASes
> - Controls what routes are shared with which neighbors

## Path Advertisement

> [!example]+ Path Propagation Example
> ![[Pasted image 20251203162602.png]]
>
> **Step-by-step propagation:**
> 1. `AS2` router `2c` receives path advertisement `AS3,X` (via eBGP) from AS3 router `3a`
> 2. Based on `AS2` import policy, router `2c` accepts path `AS3,X`
> 3. Router `2c` propagates (via iBGP) to all `AS2` routers
> 4. Based on `AS2` export policy, router `2a` advertises (via eBGP) path `AS2,AS3,X` to `AS1` `router` 1c

> [!example]+ Multiple Path Learning
> ![[Pasted image 20251203162638.png]]
>
> **Gateway routers may learn multiple paths to a destination:**
> - `AS1` gateway router `1c` learns path `AS2,AS3,X` from `2a`
> - `AS1` gateway router `1c` learns path `AS3,X` from `3a`
> - Based on policy, `AS1` gateway router `1c` chooses path `AS3,X`
> - Chosen path advertised within `AS1` via iBGP

## BGP Messages

> [!info]+ Message Types
> BGP messages exchanged between peers over [[TCP]] connection:
>
> | Message | Purpose |
> |---------|---------|
> | **OPEN** | Opens TCP connection to remote BGP peer and authenticates sender |
> | **UPDATE** | Advertises new path or withdraws old path |
> | **KEEPALIVE** | Keeps connection alive in absence of UPDATEs; also ACKs OPEN request |
> | **NOTIFICATION** | Reports errors in previous message; also used to close connection |

## Updating Forwarding Tables

> [!note]+ Combining BGP and OSPF
> ![[Pasted image 20251204102436.png]]
>
> **Process at router 1d:**
> - 1a, 1b, 1d learn via iBGP from 1c: "path to X goes through 1c"
> - [[OSPF]] intra-domain routing: to get to 1c, use interface 1
> - Result: to get to X, use interface 1
>
> | Destination | Interface |
> |:-----------:|:---------:|
> | ... | ... |
> | 1c | 1 |
> | X | 1 |
> | ... | ... |

> [!example]+ Another Router's Perspective
> ![[Pasted image 20251204102537.png]]
>
> **Process at router 1a:**
> - 1a, 1b, 1d learn via iBGP from 1c: "path to X goes through 1c"
> - OSPF intra-domain routing: to get to 1c, use interface 2
> - Result: to get to X, use interface 2
>
> | Destination | Interface |
> |:-----------:|:---------:|
> | ... | ... |
> | 1c | 2 |
> | X | 2 |
> | ... | ... |

## Path Vector Protocol

> [!success]+ Loop Prevention via AS-PATH
> **If an [[Autonomous Systems|AS]] sees itself in the AS-PATH advertised by a neighbor AS, it discards the route.**
>
> This prevents routing loops and is part of the import policy.
>
> **Advantages over [[Distance Vector Algorithm#^479ecd|Poison Reverse]]:**
> - More powerful loop detection
> - Can detect loops involving any number of ASes
> - Made possible by the presence of AS-PATH in advertisements

> [!example]+ AS-PATH Loop Detection
> ![[Pasted image 20251204103347.png]]
>
> **Information AS6 receives from neighbors to reach prefixes in AS4:**
>
> | From AS | AS-PATH | Action |
> |:-------:|:--------|:------:|
> | AS2 | AS2-AS3-AS4 | Accept |
> | AS7 | AS7-AS3-AS4 | Accept |
> | AS5 | AS5-**AS6**-AS7-AS3-AS4 | **Discard** |
> | AS9 | AS9-AS5-**AS6**-AS7-AS3-AS4 | **Discard** |
>
> Routes from AS5 and AS9 are discarded because their AS-PATHs contain AS6 as an intermediate AS.

## BGP Route Selection

> [!abstract]+ Selection Criteria
> When a router learns multiple routes to a destination AS, it selects based on (in order):
>
> | Priority | Criterion | Description |
> |:--------:|-----------|-------------|
> | 1 | **Local preference** | Policy decision: prefer most rewarding next AS |
> | 2 | **Shortest AS-PATH** | Fewest ASes to traverse |
> | 3 | **Closest gateway** | Hot potato routing (lowest intra-domain cost) |
> | 4 | **Tie-breakers** | Additional criteria if still tied |

> [!note]+ Local Preference (Business Relationships)
> **Preference order:**
> 1. Routes through **Customer AS** (most preferred - they pay you)
> 2. Routes through **Peer AS** (settlement-free)
> 3. Routes through **Provider AS** (least preferred - you pay them)

### Hot Potato Routing

> [!example]+ Hot Potato Criterion
> ![[Pasted image 20251204105512.png]]
>
> **Scenario:**
> - Router 2d learns (via iBGP) it can route to X via 2a or 2c
> - Intra-domain cost to 2a: 201
> - Intra-domain cost to 2c: 263
>
> **Decision:** 2d chooses 2a because 201 < 263
>
> **Key principle:** Choose the local gateway with least intra-domain cost. Don't worry about inter-domain cost!

## BGP Export Policy

> [!warning]+ Avoiding Transit Traffic
> **ISPs typically only want to route traffic to/from their customer networks.**
>
> They do not want to carry transit traffic between other ISPs (costly with no revenue).

> [!example]+ Export Policy in Action
> ![[Pasted image 20251204111132.png]]
>
> **Scenario:**
> - A advertises path `Aw` to B and to C
> - B chooses **not** to advertise `BAw` to C
>   - Reason: B gets no revenue for routing `CBAw` (none of C, A, w are B's customers)
> - C does not learn about `CBAw` path
> - C will route `CAw` (not using B) to get to w

### Advertisement Rules by Relationship

> [!note]+ From Provider/Customer
> ![[Pasted image 20251204111239.png]]
>
> Advertisements flow in both directions between providers and customers.

> [!note]+ From Peer
> ![[Pasted image 20251204111249.png]]
>
> Peer advertisements have restricted propagation.

### Valley-Free Routing

> [!success]+ Valley-Free Property
> Following these export rules, data traffic (flowing backward relative to advertisements) will be **valley-free**:
>
> 1. After going down once, packets can only continue downhill
> 2. After a plateau, packets can only continue downhill
> 3. After going up once, can go uphill, downhill, or cross a plateau

## BGP Pipeline Summary

> [!abstract]+ Route Processing Pipeline
> ![[Pasted image 20251204111312.png]]
>
> ```
> Incoming BGP announcements
>         ↓
>    Input Filters
>         ↓
>   All Accepted Routes
>         ↓
>    Route Selection
>         ↓
>   Best Routes (FIB)
>         ↓
>    Export Filters
>         ↓
> Outgoing BGP announcements
> ```
>
> | Stage | Examples |
> |-------|----------|
> | **Input filters** | Avoid cycles in AS-PATH, avoid certain ASes |
> | **Route selection** | Local preference → shortest AS-PATH → hot potato |
> | **Export filters** | Don't carry transit between providers/peers |

## Related Concepts

> [!note]+ See Also
> - **[[Autonomous Systems]]**: ASes that BGP connects
> - **[[TCP]]**: Transport protocol for BGP sessions
> - **[[Distance Vector Algorithm]]**: BGP is a path vector variant
> - **[[OSPF]]**: Intra-domain protocol used with BGP
> - **[[Hierarchical Addressing]]**: Route aggregation concepts
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Network Layer]]**: Layer where BGP operates
