---
title: Per-router Control Plane
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **Per-router Control Plane** is a distributed routing architecture where individual routing algorithm components run in each router. Routers interact with each other in the [[Control Plane]] to exchange routing information and compute forwarding tables independently.

## Architecture

> [!abstract]+ Distributed Control
> ![[8623dcf78f5d5a2f88fee86ce1c3dea5.png]]
>
> **Characteristics:**
> - Each router runs its own routing protocol instance
> - Routers exchange messages with neighbors
> - Each router computes its own forwarding table
> - No central authority controls routing decisions

## Routing Protocol Goals

> [!success]+ What Routing Protocols Achieve
> **Primary goal:** Determine "good" paths from sending hosts to receiving hosts through a network of routers
>
> **Path definition:** Sequence of routers that packets traverse from source to destination
>
> **What makes a path "good":**
> - Least cost (based on [[Link Cost]])
> - Fastest transmission
> - Least congested

![[5ec3341dab6d40cfb812d489f69ffdd2.png]]

## Routing Algorithm Classification

> [!info]+ Two Main Approaches
>
> | Approach | Information | Computation | Example |
> |----------|-------------|-------------|---------|
> | **Global (Link State)** | Complete topology and all link costs | Each router computes own routing tree | OSPF |
> | **Decentralized (Distance Vector)** | Only costs to neighbors | Iterative exchange with neighbors | RIP, BGP |

### Global Algorithms

> [!note]+ Link State Approach
> **Process:**
> 1. All routers discover complete network topology
> 2. All routers learn all link cost information
> 3. Each router independently computes its routing tree
>
> **Characteristics:**
> - Routers have global view of network
> - Uses algorithms like Dijkstra's shortest path
> - Faster convergence but higher overhead

### Decentralized Algorithms

> [!note]+ Distance Vector Approach
> **Process:**
> 1. Routers initially only know link costs to attached neighbors
> 2. Iterative exchange of distance information with neighbors
> 3. Eventually, routers learn distances to all destinations
>
> **Characteristics:**
> - Routers don't know complete topology
> - Lower overhead but slower convergence
> - Based on Bellman-Ford algorithm

## Related Concepts

> [!note]+ See Also
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Data Plane]]**: Per-router forwarding function
> - **[[Link Cost]]**: Metrics used for path selection
> - **[[Optimality Principle]]**: Foundation for routing algorithms
> - **[[Router Architecture]]**: Complete router structure
> - **[[Network Layer]]**: Layer where routing occurs
