---
title: Greedy Search
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Greedy search** is a search algorithm that expands the node that seems closest to the goal, using a heuristic function to estimate distance to the nearest goal for each state.

> [!abstract]+ Strategy
> **Orders by goal proximity (forward cost) $h(n)$**
>
> ![[49dba0c2d32897c8ea059e18f054415f.png]]
>
> - Expands nodes that appear closest to goal
> - Aggressively pursues the goal
> - Ignores actual path cost taken so far
> - May find solution quickly but not necessarily optimal

## Example

> [!example]+ Traveling in Romania
> ![[43c87f1b1fd2e09d3f6c8714012572ee.png]]
>
> Starting from Arad, the algorithm expands nodes based on which appears closest to Bucharest:
> - Arad (366) → Sibiu (253) → Fagaras (178) → Bucharest (0)
> - Also explores: Rimnicu, Zerind, Oradea, Neamt

## Properties

> [!warning]+ Optimality
> **Not optimal** - Greedy search does not guarantee finding the optimal solution.
>
> The resulting path may not be the shortest path to the goal.

> [!tip]+ Best Case
> Takes you straight to the goal when heuristic is accurate

> [!fail]+ Worst Case
> Like a badly-guided DFS - may explore large portions of the search space inefficiently

> [!note]+ Related Concepts
> - **[[Search Heuristic]]**: Estimation function used
> - **[[A*]]**: Combines greedy with optimal search
> - **[[Uniform Cost Search]]**: Optimal but uninformed alternative
