---
title: Routing Information Protocol
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> **RIP (Routing Information Protocol)** is an intra-domain routing protocol based on the [[Distance Vector Algorithm]]. First included in BSD-UNIX in 1982, RIP uses hop count as its distance metric and exchanges distance vectors with neighbors periodically.

## Protocol Characteristics

> [!abstract]+ Core Features
> **RIP specifications:**
>
> | Feature | Description |
> |---------|-------------|
> | **Algorithm** | [[Distance Vector Algorithm]] |
> | **Transport** | [[UDP]] port 520 |
> | **Distance metric** | Hop count |
> | **Maximum distance** | 15 hops (16 = $\infty$) |
> | **Update interval** | Every 30 seconds |
> | **Max destinations per advertisement** | 25 subnets |
>
> **Loop prevention:**
> - Uses [[Distance Vector Algorithm#^479ecd|Poison Reverse]]
> - Variant: Split Horizon (subnets with $\infty$ distance omitted from DV)

## Distance Metric

> [!note]+ Hop Count
> **Each link has cost 1** (regardless of bandwidth or delay)
>
> **Implications:**
> - Simple to understand and implement
> - Maximum network diameter: 15 hops
> - Not suitable for large networks
> - Does not consider link quality or capacity

## Example

> [!example]+ RIP Distance Vector
> ![[40d8ded88f992ce5a8fe54414b393213.png]]
>
> **From router A to destination subnets:**
>
> | Subnet | Hops |
> |:------:|:----:|
> | u | 1 |
> | v | 2 |
> | w | 2 |
> | x | 3 |
> | y | 3 |
> | z | 2 |
>
> Router A maintains this distance vector and shares it with neighbors every 30 seconds.

## Limitations

> [!warning]+ Why RIP Is No Longer Widely Used
> **Scalability issues:**
> - 15-hop limit restricts network size
> - Slow convergence due to count-to-infinity problem
> - Periodic updates consume bandwidth even when topology is stable
>
> **Modern alternatives:**
> - [[OSPF]]: Link-state, faster convergence, no hop limit
> - EIGRP: Enhanced distance vector with faster convergence

## Related Concepts

> [!note]+ See Also
> - **[[Distance Vector Algorithm]]**: Algorithm RIP implements
> - **[[OSPF]]**: Modern link-state alternative
> - **[[Autonomous Systems]]**: Intra-AS routing context
> - **[[UDP]]**: Transport protocol used by RIP
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Network Layer]]**: Layer where RIP operates
