---
title: Distance Vector Algorithm
authors: Mihai Bors
tags:
  - Network
---
> [!info]+ Definition
> The **Distance Vector Algorithm** is a decentralized routing algorithm where each router maintains a vector of distances (costs) to all destinations and exchanges this information with its neighbors. Routers iteratively update their distance estimates using the Bellman-Ford equation until convergence.

## Bellman-Ford Equation

> [!abstract]+ Mathematical Foundation
> **Core equation:**
> $$d_x(y) = \min_v \{ c_{x,v} + d_v(y) \}$$
>
> Where:
> - $d_x(y)$: Cost of least-cost path from $x$ to $y$
> - $c_{x,v}$: Cost of direct link from $x$ to neighbor $v$
> - $d_v(y)$: Cost from neighbor $v$ to destination $y$
>
> **Interpretation:** The best path from $x$ to $y$ goes through whichever neighbor $v$ minimizes the total cost.

> [!example]+ Bellman-Ford Example
> ![[da36535b4c550d3aedce82cf7b40f8aa.png]]
>
> **Given:** Node $u$ wants to find least-cost path to $z$
>
> **Neighbors' known distances to $z$:**
> - $d_v(z) = 5$
> - $d_x(z) = 3$
> - $d_w(z) = 3$
>
> **Link costs from $u$:**
> - $c_{u,v} = 2$
> - $c_{u,x} = 1$
> - $c_{u,w} = 5$
>
> **Calculation:**
> $$d_u(z) = \min \{ c_{u,v} + d_v(z), \; c_{u,x} + d_x(z), \; c_{u,w} + d_w(z) \}$$
> $$d_u(z) = \min \{ 2 + 5, \; 1 + 3, \; 5 + 3 \} = \min \{ 7, 4, 8 \} = 4$$
>
> **Result:** Next hop is $x$ (achieves minimum cost of 4)

## Algorithm Structure

> [!note]+ Distance Vector Notation
> **Each node $x$ maintains:**
> - $D_x(y)$: Estimate of least cost from $x$ to $y$
> - $\vec{D}_x = [D_x(y) : y \in N]$: Distance vector (estimates to all destinations)
> - $c_{x,v}$: Link cost to each neighbor $v$
> - $\vec{D}_v$: Copy of each neighbor's distance vector

## Algorithm Operation

> [!abstract]+ Iterative Process
> **Each node repeats:**
> 1. **Wait** for change in local link cost OR message from neighbor
> 2. **Recompute** distance vector using Bellman-Ford equation:
>    $$D_x(y) \leftarrow \min_v \{ c_{x,v} + D_v(y) \} \quad \text{for each } y \in N$$
> 3. **Notify neighbors** if any distance estimate changed
>
> **Key property:** Notifications sent only when necessary (distance changed)

> [!success]+ Convergence
> Under stable conditions, $D_x(y)$ converges to the actual least cost $d_x(y)$

## Example: Computing Distance Vector

> [!example]+ Distance Vector Computation at Node B
> ![[d74fe2e4c10a6e782b8a9c1481b3ec62.png]]
>
> **Initial state at B** (after receiving DVs from neighbors a, c, e):
>
> | Destination | Initial Estimate |
> |:-----------:|:----------------:|
> | $D_b(a)$ | 8 |
> | $D_b(c)$ | 1 |
> | $D_b(d)$ | $\infty$ |
> | $D_b(e)$ | 1 |
> | $D_b(f)$ | $\infty$ |
> | $D_b(g)$ | $\infty$ |
> | $D_b(h)$ | $\infty$ |
> | $D_b(i)$ | $\infty$ |
>
> **After applying Bellman-Ford:**
>
> | Destination | Computation | Result |
> |:-----------:|:------------|:------:|
> | $D_b(a)$ | $\min\{8+0, \infty, \infty\}$ | 8 |
> | $D_b(c)$ | $\min\{\infty, 1+0, \infty\}$ | 1 |
> | $D_b(d)$ | $\min\{8+1, \infty, 1+1\}$ | 2 |
> | $D_b(e)$ | $\min\{\infty, \infty, 1+0\}$ | 1 |
> | $D_b(f)$ | $\min\{\infty, \infty, 1+1\}$ | 2 |
> | $D_b(g)$ | $\min\{\infty, \infty, \infty\}$ | $\infty$ |
> | $D_b(h)$ | $\min\{\infty, \infty, 1+1\}$ | 2 |
> | $D_b(i)$ | $\min\{\infty, \infty, \infty\}$ | $\infty$ |

## State Information Diffusion

> [!note]+ How Information Propagates
> ![[d56ed497c6ef726c7971c6f222c3fdae.png]]
>
> **Iterative propagation through network:**
>
> | Time | Information Reach |
> |:----:|:------------------|
> | $t = 0$ | Node $c$'s state known only at $c$ |
> | $t = 1$ | Propagated 1 hop (reaches $b$) |
> | $t = 2$ | Propagated 2 hops (reaches $a$, $e$) |
> | $t = 3$ | Propagated 3 hops (reaches $d$, $f$, $h$) |
> | $t = 4$ | Propagated 4 hops (reaches $g$, $i$) |
>
> **Observation:** Information spreads one hop per iteration

## Link Cost Changes

### Good News Travel Fast

> [!success]+ Decreased Link Cost
> ![[8229bd91e5bbdc270a8c9337a1fc8e99.png]]
>
> **Scenario:** Link cost $c_{x,y}$ decreases from 4 to 1
>
> | Time | Event |
> |:----:|:------|
> | $t_0$ | $y$ detects change, computes $D_y(x) = 1$, notifies neighbors |
> | $t_1$ | $z$ receives update, computes $D_z(x) = 2$, notifies neighbors |
> | $t_2$ | $y$ receives update, no change needed, algorithm converges |
>
> **Result:** Fast convergence (2 iterations)

### Bad News Travel Slow

> [!warning]+ Increased Link Cost (Count-to-Infinity Problem)
> ![[46cf71ee086a7d8aa35799813e000ac9.png]]
>
> **Scenario:** Link cost $c_{x,y}$ increases from 4 to 60
>
> | Iteration | $y$'s View | $z$'s View |
> |:---------:|:-----------|:-----------|
> | 0 | $D_y(x) = 60$ (direct), but $z$ claims path of cost 5 | $D_z(x) = 5$ (via $y$) |
> | 1 | $D_y(x) = 6$ (via $z$) | $D_z(x) = 6$ (old info) |
> | 2 | $D_y(x) = 7$ | $D_z(x) = 7$ |
> | 3 | $D_y(x) = 8$ | $D_z(x) = 8$ |
> | ... | ... | ... |
> | 47 | Finally converges | Finally converges |
>
> **Problem:**
> - $y$ and $z$ keep incrementing costs
> - Each thinks they can reach $x$ via the other
> - Takes 47 iterations to stabilize!

> [!abstract]+ Count-to-Infinity Explanation
> **Why this happens:**
> - $y$ doesn't know $z$'s path to $x$ goes through $y$
> - $z$ advertises cost 5, but that path uses the now-expensive link
> - Routers "count up" until cost exceeds direct path
>
> **Solutions:**
> - Split horizon: Don't advertise routes back to where you learned them
> - Poison reverse: Advertise infinity for routes learned from a neighbor back to that neighbor
> - Define infinity as a small number (e.g., 16 in [[RIP]])

## Poisoned Reverse

> [!success]+ How Poisoned Reverse Works
> **Idea:** If node $C$ uses node $B$ as next hop to reach destination $A$, then $C$ "lies" to $B$ about its distance to $A$.
>
> **Rules:**
> - When $C$ sends its DV **to $B$**: replace $D_C(A)$ with $\infty$
> - When $C$ sends its DV **to any other neighbor**: keep the real $D_C(A)$
>
> **Effect:** $B$ cannot choose $C$ as next hop to reach $A$, thus avoiding a routing loop.

^479ecd

> [!example]+ Poisoned Reverse in Action
> **Topology:** Linear network A — B — C — D — E
>
> **Scenario:** Link A-B goes down
>
> | A | B | C | D | E | State |
> |:-:|:-:|:-:|:-:|:-:|:------|
> | - | 1 | 2 | 3 | 4 | Initially |
> | - | $\infty$ | 2 | 3 | 4 | After 1 exchange |
> | - | $\infty$ | $\infty$ | 3 | 4 | After 2 exchanges |
> | - | $\infty$ | $\infty$ | $\infty$ | 4 | After 3 exchanges |
> | - | $\infty$ | $\infty$ | $\infty$ | $\infty$ | After 4 exchanges |
>
> **Result:** Fast convergence! No count-to-infinity problem.

> [!warning]+ Poisoned Reverse Is Not a Panacea
> **Poisoned reverse fails with loops involving 3 or more nodes.**
> - Poisoned reverse only prevents 2-node loops

## Comparison: Link-State vs Distance Vector

> [!info]+ Algorithm Comparison
>
> | Aspect | Link-State | Distance Vector |
> |--------|------------|-----------------|
> | **Information** | Complete topology | Only neighbor distances |
> | **Message complexity** | $O(nE)$ messages | Exchange between neighbors only |
> | **Convergence speed** | Fast ($O(n^2)$ algorithm) | Varies; can be slow |
> | **Robustness** | Node computes own table | Node can advertise incorrect paths |

## Related Concepts

> [!note]+ See Also
> - **[[Link-State Routing]]**: Alternative routing algorithm
> - **[[Link Cost]]**: Metrics used in path computation
> - **[[Optimality Principle]]**: Foundation for Bellman-Ford
> - **[[Per-router Control Plane]]**: Distributed routing architecture
> - **[[Control Plane]]**: Network-wide routing logic
> - **[[Network Layer]]**: Layer where distance vector operates
