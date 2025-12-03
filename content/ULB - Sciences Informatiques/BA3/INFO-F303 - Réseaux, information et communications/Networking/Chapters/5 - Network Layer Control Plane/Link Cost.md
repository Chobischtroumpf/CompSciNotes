---
title: Link Cost
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **Link Cost** is a metric assigned to network links that routing algorithms use to determine optimal paths. The cost of a path is the sum of all link costs along that path, enabling routers to select routes that minimize total cost.

## Graph Abstraction

> [!abstract]+ Network as a Graph
> ![[393610f72a8ea9dcd5632149095b8d33.png]]
>
> **Representation:** $G = (N, E)$
> - $N$: Set of routers (nodes) = $\{u, v, w, x, y, z\}$
> - $E$: Set of links (edges) = $\{(u,v), (u,x), (u,w), (v,x), (v,w), (x,w), (x,y), (w,y), (w,z), (y,z)\}$

## Link Cost Notation

> [!note]+ Cost Representation
> **Notation:** $c_{a,b}$ = cost of direct link connecting nodes $a$ and $b$
>
> **Convention:**
> - Finite value: direct link exists with that cost
> - Infinite ($\infty$): no direct link exists between nodes

## Common Cost Metrics

> [!info]+ Types of Link Costs
>
> | Metric | Description | Optimization Goal |
> |--------|-------------|-------------------|
> | **Hop Count** | All links cost 1 | Minimize number of hops |
> | **InvCap** | Inversely proportional to link capacity | Minimize average link utilization |
> | **Delay** | Static propagation delay | Minimize latency |
> | **Administrative** | Manually configured values | Custom optimization goals |

### Hop Count

> [!note]+ Simplest Metric
> **Definition:** All link costs equal to 1
>
> **Effect:** Shortest path = fewest hops
>
> **Use case:** Simple networks where all links have similar characteristics

### Inverse Capacity (InvCap)

> [!note]+ Capacity-Based Metric
> **Definition:** Link cost inversely proportional to link capacity (in bps)
>
> $$c_{a,b} = \frac{k}{\text{capacity}_{a,b}}$$
>
> **Effect:**
> - High-capacity links have smaller costs
> - Traffic attracted to high-capacity links
> - Minimizes average link utilization

### Administrative Cost

> [!note]+ Policy-Based Metric
> **Definition:** Any link cost computed to optimize a given network objective
>
> **Examples:**
> - Load balancing given a traffic matrix
> - Preferring certain paths for policy reasons
> - Avoiding specific links or regions

## Summability Requirement

> [!warning]+ What Makes a Valid Cost Metric
> **Link costs must be summable:**
> - Path cost = sum of all link costs along the path
> - Makes sense mathematically and operationally
>
> **Valid examples:**
> - Hop count
> - Delay
> - Administrative weights
>
> **Invalid examples (not summable):**
> - Packet error rate on link
> - Link capacity (bandwidth)
>
> **Why capacity isn't summable:**
> - Path capacity ≠ sum of link capacities
> - Path capacity = minimum link capacity along path (bottleneck)

## Related Concepts

> [!note]+ See Also
> - **[[Optimality Principle]]**: Foundation for shortest-path routing
> - **[[Per-router Control Plane]]**: Uses link costs for routing decisions
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Network Layer]]**: Layer where routing operates
