---
title: Creating admissible Heuristics
authors: Alessandro Dorigo
tags:
  -
---


> [!note]+ Creating Admissible Heuristics
> **Key insight: Use relaxed problems**
>
> Often, admissible heuristics are solutions to **relaxed problems**, where new actions are available that make the problem easier to solve.

> [!example]- Examples of Relaxed Problems
>
> **1. Route-finding (Romania map example):**
>
> - Original problem: Must follow roads between cities
> - Relaxed problem: Can travel in straight lines (ignoring roads)
> - Heuristic: Straight-line distance = 366 km to Bucharest
> - This is admissible because the actual road distance must be ≥ straight-line distance
>
> **2. Pac-Man maze navigation:**
>
> - Original problem: Must navigate around walls in the maze
> - Relaxed problem: Can move through walls (Manhattan distance)
> - Heuristic: Direct Manhattan distance to goal (shown as 15)
> - This is admissible because the actual path length through the maze must be ≥ direct distance

> [!abstract]+ Formal Relationship Between Problems
>
> **Definition:**
>
> - Let $P_1$ be the original problem
> - Let $P_2$ be a relaxed version of $P_1$
> - Relaxation means: if $\mathcal{A}_1(s) \supseteq \mathcal{A}_2(s)$ for every state $s$
>     - (The relaxed problem has more actions available or fewer constraints)
>
> **Theorem:** $$h_2^_(s) \leq h_1^_(s) \text{ for every } s$$
>
> Therefore, $h_2^*(s)$ is admissible for $P_1$
>
> **In plain English:**
>
> - $h_1^*(s)$ = true optimal cost in the original problem
> - $h_2^*(s)$ = true optimal cost in the relaxed problem
> - Since the relaxed problem is easier (more options), its solution cost is always ≤ the original
> - This makes the relaxed problem's solution an admissible heuristic for the original problem

> [!tip]- Practical Strategy
>
> **How to create admissible heuristics:**
>
> 1. Identify constraints in your original problem
> 2. Remove or relax some constraints to create an easier problem
> 3. Solve (or estimate the solution to) the relaxed problem
> 4. Use that solution cost as your heuristic
>
> **Why this works:**
>
> - The relaxed problem is easier, so its solution cost ≤ original problem cost
> - This guarantees admissibility
> - The closer the relaxed problem is to the original, the more informative (tighter) the heuristic
