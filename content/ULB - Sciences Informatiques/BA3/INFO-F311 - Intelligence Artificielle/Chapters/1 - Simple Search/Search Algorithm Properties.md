---
title: Search Algorithm Properties
authors: Mihai Bors
tags:
  - AI
---
> [!question]+ Key Questions
> - Is it complete (guaranteed to find a solution if one exists)?
> - Is it optimal (guaranteed to find the least cost path)?
> - [[Complexité algorithmique|Time complexity]]?
> - Space complexity?

## Complexity Analysis

> [!abstract]+ Notation
> Cartoon of [[Search Tree|search tree]]:
> - $b$ is the branching factor
> - $m$ is the maximum depth
> - Solutions at various depths
>
> ![[9ee25e353d9cc0b75a8bdd844cc0f72d.png]]
>
> $1 + b + b^2 + \dots + b^m = \mathcal{O}(b^m)$ nodes in the tree

## DFS Properties

> [!info]+ Depth-First Search
> **Expansion**: Some left prefix of the tree down to depth $m$
> - If $m$ is finite, takes $\mathcal{O}(b^m)$ time
>
> **Space**: Only siblings on path to root
> - Requires $\mathcal{O}(bm)$ space
>
> **Complete**: No
> - $m$ could be infinite
> - Preventing cycles may help
>
> **Optimal**: No
> - Finds the "leftmost" solution, regardless of depth or cost

![[7635db075346da2a39b5c3b8bbe15295.png]]

## BFS Properties

> [!info]+ Breadth-First Search
> **Expansion**: Processes all nodes above shallowest solution
> - With depth of shallowest solution $s$, requires $\mathcal{O}(b^s)$ time
>
> **Space**: Roughly the last tier
> - Requires $\mathcal{O}(b^s)$ space
>
> **Complete**: Yes
> - $s$ must be finite if a solution exists
>
> **Optimal**: Only if costs are equal

![[369e554d5a7fd2e1e659530c1a1664ae.png]]

## Comparison
![[5cacbdc39672fee2f9c865d004ccf958.png]]

> [!note]+ Related Concepts
> - **[[Tree Search]]**: Algorithm with these properties
> - **[[Systematic Search]]**: Structured approach
> - **[[Search Tree]]**: Structure being analyzed
