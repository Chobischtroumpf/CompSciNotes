---
title: Search Heuristic
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **heuristic** is a function that estimates how close a state is to a goal, designed for a particular search problem.

## Examples

> [!example]+ Pathfinding Heuristics
> **Manhattan distance and Euclidean distance:**
>
> ![[6426dc636ebc45dfdc9a5cda68e30f9f.png]]
>
> - **Manhattan distance**: Sum of horizontal and vertical distances
> - **Euclidean distance**: Straight-line distance to goal
>
> Used to estimate the distance between Pacman and food in maze navigation

## Consistency of Heuristics

> [!abstract]+ Main Idea
> **Estimated heuristic costs ≤ actual costs**
>
> **Two related concepts:**
>
> **[[Admissibility]]:** Heuristic cost ≤ actual cost to goal
> - $h(A) ≤$ actual cost from A to G
> - Ensures heuristic never overestimates total remaining cost
>
> **Consistency:** Heuristic "arc" cost ≤ actual cost for each arc
> - $h(A) - h(C) ≤ \text{cost}(A \text{ to } C)$
> - Ensures heuristic respects the triangle inequality

> [!theorem]+ Consequences of Consistency
> **1. The $f$ value along a path never decreases**
> - $h(A) ≤ \text{cost}(A \text{ to } C) + h(C)$
> - This means $f$ values grow monotonically
>
> **2. A* graph search is optimal**
> - With consistent heuristics, the first path to reach a state is guaranteed optimal
> - No need to re-expand states

## Creating Admissible Heuristics

> [!abstract]+ Key Insight: Use Relaxed Problems
> Often, admissible heuristics are solutions to **relaxed problems**, where new actions are available that make the problem easier to solve.

> [!example]+ Examples of Relaxed Problems
>
> **1. Route-finding (Romania map example):**
> - **Original problem:** Must follow roads between cities
> - **Relaxed problem:** Can travel in straight lines (ignoring roads)
> - **Heuristic:** Straight-line distance = 366 km to Bucharest
> - **Why admissible:** The actual road distance must be ≥ straight-line distance
>
> **2. Pac-Man maze navigation:**
> - **Original problem:** Must navigate around walls in the maze
> - **Relaxed problem:** Can move through walls (Manhattan distance)
> - **Heuristic:** Direct Manhattan distance to goal (shown as 15)
> - **Why admissible:** The actual path length through the maze must be ≥ direct distance

## Formal Relationship Between Problems

> [!theorem]+ Relaxation Theorem
> **Definition:**
> - Let $P_1$ be the original problem
> - Let $P_2$ be a relaxed version of $P_1$
> - Relaxation means: $\mathcal{A}_1(s) \supseteq \mathcal{A}_2(s)$ for every state $s$
>   (The relaxed problem has more actions available or fewer constraints)
>
> **Theorem:**
> $$h_2^*(s) \leq h_1^*(s) \text{ for every } s$$
>
> Therefore, $h_2^*(s)$ is admissible for $P_1$
>
> **In plain English:**
> - $h_1^*(s)$ = true optimal cost in the original problem
> - $h_2^*(s)$ = true optimal cost in the relaxed problem
> - Since the relaxed problem is easier (more options), its solution cost is always ≤ the original
> - This makes the relaxed problem's solution an admissible heuristic for the original problem

## Practical Strategy

> [!tip]+ How to Create Admissible Heuristics
> **Steps:**
> 1. Identify constraints in your original problem
> 2. Remove or relax some constraints to create an easier problem
> 3. Solve (or estimate the solution to) the relaxed problem
> 4. Use that solution cost as your heuristic
>
> **Why this works:**
> - The relaxed problem is easier, so its solution cost ≤ original problem cost
> - This guarantees admissibility
> - The closer the relaxed problem is to the original, the more informative (tighter) the heuristic

## Combining Heuristics

> [!abstract]+ Dominance and Combination
> **Dominance:** $h_1 ≥ h_2$ if $∀n : h_1(n) ≥ h_2(n)$
> - Roughly speaking, larger is better as long as both are admissible
> - The zero heuristic is pretty bad (reduces A* to UCS)
> - The exact heuristic is pretty good, but usually too expensive to compute

> [!success]+ Maximum of Heuristics
> **What if we have two heuristics, neither dominates the other?**
>
> Form a new heuristic by taking the max of both:
> $$h(n) = \max(h_1(n), h_2(n))$$
>
> **Key property:** Max of admissible heuristics is admissible and dominates both!
> - This combined heuristic is always at least as good as either individual heuristic
> - It provides the best of both worlds without losing admissibility

> [!tip]+ A* Trade-off: Quality vs Computation
> **With A*: a trade-off between quality of estimate and work per node**
>
> - As heuristics get closer to the true cost, you will expand fewer nodes
> - BUT you usually do more work per node to compute the heuristic itself
>
> **The art of A*:** Finding heuristics that are:
> 1. Admissible (guarantee optimality)
> 2. Informative (close to true cost)
> 3. Cheap to compute (don't waste time calculating)

> [!note]+ Related Concepts
> - **[[Greedy Search]]**: Uses heuristic alone
> - **[[A*]]**: Combines heuristic with path cost
> - **[[Admissibility]]**: Property ensuring optimality
> - **[[Uniform Cost Search]]**: Special case with $h=0$
