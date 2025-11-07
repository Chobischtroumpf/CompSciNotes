---
title: Admissibility
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Admissibility** is a property of heuristics that ensures [[A*]] optimality.

## Two Types of Heuristics

> [!fail]+ Inadmissible (Pessimistic) Heuristics
> - Overestimate the cost to reach the goal
> - Break optimality by trapping good plans on the fringe
> - Cause [[A*]] to avoid exploring promising paths
> - The algorithm thinks certain paths are more expensive than they actually are

> [!success]+ Admissible (Optimistic) Heuristics
> - Underestimate or exactly estimate the cost to reach the goal
> - Slow down bad plans but never outweigh true costs
> - Ensure [[A*]] explores all potentially optimal paths
> - May expand more nodes, but guarantee finding the optimal solution

## Formal Definition

> [!note]+ Mathematical Formulation
> **A heuristic $h$ is admissible (optimistic) if:**
>
> $$0 \leq h(n) \leq h^*(n)$$
>
> where $h^*(n)$ is the true cost to a nearest goal
>
> **In other words:**
> - The heuristic never overestimates the actual cost
> - It can underestimate (be optimistic) or be exact
> - It must always be non-negative

## Examples

> [!example]+ Admissible Heuristics
> ![[Pasted image 20251103143057.png]]
>
> **Maze pathfinding:**
> - Manhattan distance (15 in the image)
> - The straight-line path never overestimates because you can't go through walls
> - Actual path will be ≥ the estimated distance
>
> **Pancake problem:**
> - Number of pancakes out of order (4 in the image)
> - Any solution must at least fix these out-of-order pancakes
> - Actual moves needed will be ≥ this count

## Practical Importance

> [!tip]+ Key Insight
> **Coming up with admissible heuristics is most of what's involved in using A* in practice.**
>
> The effectiveness of A* heavily depends on:
> - Finding a good admissible heuristic
> - Balancing between being too optimistic (expanding many nodes) and being informative (guiding search efficiently)
> - Domain knowledge to create heuristics that are both admissible and close to the true cost

> [!note]+ Related Concepts
> - **[[A*]]**: Uses admissible heuristics
> - **[[Search Heuristic]]**: General heuristic concept
