---
title: Search Heuristic
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> A **heuristic** is a function that estimates how close a state is to a goal, designed for a particular search problem.

> [!example]+ Examples
> **Pathfinding:**
> ![[Pasted image 20251103103810.png]]
>
> - **Manhattan distance**: Sum of horizontal and vertical distances
> - **Euclidean distance**: Straight-line distance to goal
>
> Used to estimate the distance between Pacman and food

> [!abstract] Consistency of Heuristics
>
> **Main idea: estimated heuristic costs ≤ actual costs**
>
> **Two related concepts:**
>
> **Admissibility:** heuristic cost ≤ actual cost to goal
>
> - $h(A) ≤$ actual cost from A to G
> - Ensures heuristic never overestimates total remaining cost
>
> **Consistency:** heuristic "arc" cost ≤ actual cost for each arc
>
> - $h(A) - h(C) ≤ \text{cost}(A \text{ to } C)$
> - Ensures heuristic respects the triangle inequality
>
> **Consequences of consistency:**
>
> 1. **The $f$ value along a path never decreases**
>     - $h(A) ≤ \text{cost}(A \text{ to } C) + h(C)$
>     - This means $f$ values grow monotonically
> 2. __A_ graph search is optimal_*
>     - With consistent heuristics, the first path to reach a state is guaranteed optimal
>     - No need to re-expand states

> [!note]+ Related Concepts
> - **[[Greedy Search]]**: Uses heuristic alone
> - **[[A*]]**: Combines heuristic with path cost
> - **[[Admissibility]]**: Property ensuring optimality
