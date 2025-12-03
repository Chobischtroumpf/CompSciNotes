---
title: OSPF
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **OSPF (Open Shortest Path First)** is a publicly available link-state routing protocol where each router floods Link-State Advertisements (LSAs) to all other routers in the entire AS (Autonomous System). OSPF is layered directly over IP (not using [[TCP]] or [[UDP]]) and uses Dijkstra's algorithm to compute forwarding tables.

## Core Characteristics

> [!abstract]+ How OSPF Works
> **Classic link-state approach:**
> 1. Each router floods OSPF Link-State Advertisements (LSAs) to all other routers
> 2. Each router builds complete topology from received LSAs
> 3. Each router runs Dijkstra's algorithm to compute forwarding table
>
> **Protocol details:**
> - Layered directly over IP (protocol number 89)
> - No transport layer (UDP/TCP) overhead
> - Uses FIB (Forwarding Information Base) as forwarding table

## Forwarding Information Base (FIB)

> [!note]+ FIB Structure
> **The FIB binds:**
> - Destination IP prefixes (some encoding router IDs)
> - Local outgoing interfaces
> - Next hop routers
>
> **Result:** Complete forwarding table derived from shortest-path tree

## Advanced Features

> [!success]+ OSPF Capabilities
>
> | Feature | Description |
> |---------|-------------|
> | **Security** | LSAs can be authenticated to prevent malicious intrusion |
> | **ECMP** | Multiple same-cost paths stored in forwarding table for load balancing |
> | **Designated Router** | Reduces LSA traffic when multiple routers share a subnet |
> | **Hierarchical OSPF** | Two-level hierarchy for large topologies |

### Equal Cost MultiPath (ECMP)

> [!note]+ Load Balancing
> **When multiple paths have the same least cost:**
> - All paths are stored in the forwarding table
> - Traffic is distributed across all equal-cost paths
> - Improves bandwidth utilization and provides redundancy

### Designated Router

> [!note]+ Reducing LSA Traffic
> **Problem:** When several routers connect to the same subnet (through a switch), full mesh LSA exchange is inefficient
>
> **Solution:** One router is designated to exchange LSAs with all other routers in that subnet
> - Other routers in the subnet do not exchange LSAs directly with each other
> - Reduces $\mathcal{O}(n^2)$ exchanges to $\mathcal{O}(n)$

## Hierarchical OSPF

> [!abstract]+ Two-Level Hierarchy
> **Structure:**
> - **Local areas:** Groups of routers with detailed internal topology
> - **Backbone (Area 0):** Connects all local areas together
>
> **Key principle:**
> - Link-state advertisements flooded only within area or backbone
> - Each node has detailed topology only for its own area/backbone
> - Nodes only know direction to reach destinations in other areas

> [!example]+ Hierarchical OSPF Topology
> ![[4ccbb3164aa4f030934107fc68cab45b.png]]
>
> **Router types in hierarchical OSPF:**
>
> | Router Type | Function |
> |-------------|----------|
> | **Area Border Router** | Summarizes distances to destinations in own area, advertises in backbone |
> | **Boundary Router** | Connects to other autonomous systems (external networks) |
> | **Backbone Router** | Runs OSPF limited to backbone area |
> | **Local Router** | Operates within a single area |

### Router Responsibilities

> [!note]+ Local Routers
> **Operations:**
> - Flood LSAs only within their area
> - Compute routing within area using Dijkstra's algorithm
> - Forward packets destined outside area via area border router

> [!note]+ Area Border Routers
> **Operations:**
> - Participate in both local area and backbone
> - Summarize distances to all destinations in their area
> - Advertise summarized routes into the backbone
> - Enable inter-area routing without full topology knowledge

## Related Concepts

> [!note]+ See Also
> - **[[Link-State Routing]]**: Algorithm OSPF implements
> - **[[Link Cost]]**: Metrics used for path computation
> - **[[Per-router Control Plane]]**: Distributed routing architecture
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Hierarchical Addressing]]**: Route summarization concepts
> - **[[Network Layer]]**: Layer where OSPF operates
