---
title: Autonomous Systems
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> An **Autonomous System (AS)**, also called a domain, is a collection of routers under the same administrative control that run the same routing protocol internally. ASes enable scalable Internet routing by aggregating routers into manageable regions with hierarchical routing.

## Why Autonomous Systems?

> [!warning]+ Scalability Problem
> **Idealized assumptions that don't hold:**
> - All routers are identical
> - Network is "flat" (no hierarchy)
>
> **Reality with billions of destinations:**
> - Can't store all destinations in routing tables
> - Routing table exchanges would overwhelm links
>
> **Solution:** Aggregate routers into regions (ASes) with hierarchical routing

## Routing Hierarchy

> [!abstract]+ Two-Level Routing
> ![[3a9f4368132824a707680d9b5555d186.png]]
>
> | Level | Name | Scope | Protocol Examples |
> |-------|------|-------|-------------------|
> | **Intra-AS** | Intradomain | Within same AS | [[OSPF]], [[RIP]], IS-IS, EIGRP |
> | **Inter-AS** | Interdomain | Among ASes | [[BGP]] |
>
> **Key principle:**
> - All routers in an AS run the same intradomain protocol
> - Different ASes can run different intradomain protocols
> - Inter-AS routing connects ASes together

## Gateway Routers

> [!note]+ AS Boundary Routers
> **Gateway routers** sit at the "edge" of their AS:
> - Have link(s) to router(s) in other ASes
> - Perform both intradomain AND interdomain routing
> - Bridge between internal and external routing
>
> **Forwarding table configuration:**
> - Intra-AS routing: determines entries for destinations within AS
> - Inter-AS + Intra-AS: determine entries for external destinations

## Intra-AS Routing Protocols

> [!info]+ Common Intradomain Protocols
>
> | Protocol | Type | Standard | Notes |
> |----------|------|----------|-------|
> | **[[OSPF]]** | Link-state | RFC 2328 | Most widely used |
> | **IS-IS** | Link-state | ISO standard | Similar to OSPF, older |
> | **[[RIP]]** | Distance vector | RFC 1723 | No longer widely used |
> | **EIGRP** | Distance vector | RFC 7868 | Formerly Cisco-proprietary |

## Inter-AS Routing

> [!abstract]+ Routing Between ASes
> ![[569d06156ebfa998d3f01170c2653715.png]]
>
> **Scenario:** Router in `AS1` receives packet destined outside `AS1`
>
> **Problem:** Which gateway router should forward the packet?
>
> **Inter-AS routing must:**
> 1. **Learn** which destinations are reachable through `AS2` vs `AS3`
> 2. **Propagate** this reachability info to all routers in `AS1`
>
> **Result:** Each router knows the best gateway for each external destination

## Example: Multi-AS Topology

> [!example]+ Interconnected ASes
> **Consider the topology above:**
> - `AS1` connects to both `AS2` and `AS3`
> - `AS1` has internal routers and gateway routers
> - Gateway routers exchange inter-AS routing information
>
> **Forwarding decision for external destination:**
> 1. Inter-AS protocol determines which AS contains destination
> 2. Inter-AS protocol identifies gateway router(s) to that AS
> 3. Intra-AS protocol determines path to chosen gateway

## Related Concepts

> [!note]+ See Also
> - **[[OSPF]]**: Link-state intra-AS protocol
> - **[[RIP]]**: Distance vector intra-AS protocol
> - **[[Link-State Routing]]**: Algorithm used by OSPF
> - **[[Distance Vector Algorithm]]**: Algorithm used by RIP
> - **[[Hierarchical Addressing]]**: Route aggregation
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Network Layer]]**: Layer where AS routing operates
