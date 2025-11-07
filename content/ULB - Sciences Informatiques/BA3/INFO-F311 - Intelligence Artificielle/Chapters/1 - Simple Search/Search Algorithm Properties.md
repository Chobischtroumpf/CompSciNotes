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
> ![[Pasted image 20250925122839.png]]
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

![[Pasted image 20250925123620.png]]

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

![[Pasted image 20250925124422.png]]

## Comparison
![[Pasted image 20251022154436.png]]

> [!note]+ Related Concepts
> - **[[Tree Search]]**: Algorithm with these properties
> - **[[Systematic Search]]**: Structured approach
> - **[[Search Tree]]**: Structure being analyzed
