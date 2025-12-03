---
title: Optimality Principle
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **Optimality Principle** states that if router $J$ is on the optimal path from router $I$ to router $K$, then the optimal path from $J$ to $K$ also falls along the same route. This principle is fundamental to all shortest-path routing algorithms.

## The Principle

> [!abstract]+ Formal Statement
> **If:**
> - The optimal path from $I$ to $K$ passes through $J$
>
> **Then:**
> - The portion of that path from $J$ to $K$ is also the optimal path from $J$ to $K$
>
> **Intuition:** Any subpath of an optimal path must itself be optimal.

> [!tip]+ Why This Works
> **Proof by contradiction:**
> - Suppose the optimal path from $I$ to $K$ goes through $J$
> - Suppose there exists a better path from $J$ to $K$
> - Then we could replace the $J \to K$ portion with this better path
> - This would create a shorter overall path from $I$ to $K$
> - Contradiction: the original path wasn't optimal
>
> Therefore, the $J \to K$ portion must be optimal.

## Consequence: Sink Trees

> [!success]+ Routing Trees
> **The set of optimal paths from all sources to a single destination forms a tree rooted at the destination.**
>
> This tree is called a **sink tree** (or **routing tree**).
>
> **Properties:**
> - Each node has exactly one path to the destination
> - No loops exist in the tree
> - Tree contains $N-1$ edges for $N$ nodes

## Example

> [!example]+ Network and Routing Tree
>
> | ![[510d4c1884d189552cc0dcc3a97fd8c7.png]] | ![[e1e394796da18e13498e8b89b24b9771.png]] |
> | :----------------------------------: | :-----------------------------------------------------: |
> | Network topology | Routing tree for router B (hop count metric) |
>
> **Observation:**
> - Left: Original network with all links
> - Right: Sink tree showing optimal paths to router B
> - Tree structure eliminates redundant paths

## Implications for Routing

> [!note]+ Algorithm Design
> **The optimality principle enables:**
> - Efficient shortest-path algorithms (Dijkstra, Bellman-Ford)
> - Incremental path computation
> - Loop-free routing when using consistent metrics
>
> **Each router only needs to know:**
> - The next hop toward each destination
> - Not the complete path

## Related Concepts

> [!note]+ See Also
> - **[[Link Cost]]**: Metrics used for path optimization
> - **[[Per-router Control Plane]]**: Implements routing algorithms
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Network Layer]]**: Layer where routing operates
