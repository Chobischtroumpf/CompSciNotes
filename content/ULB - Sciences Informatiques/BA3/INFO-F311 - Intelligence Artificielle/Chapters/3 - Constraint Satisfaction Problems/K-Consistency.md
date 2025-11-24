---
title: K-Consistency
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **K-Consistency** is a hierarchy of consistency properties for [[CSP|CSPs]] that generalizes [[Arc Consistency]] to larger sets of variables.

## Levels of Consistency

> [!abstract]+ Consistency Definitions
> **1-Consistency (Node Consistency):**
> - Every single node's domain has a value which meets that node's unary constraints
>
> **2-Consistency ([[Arc Consistency]]):**
> - For each pair of nodes, any consistent assignment to one can be extended to the other
>
> **K-Consistency:**
> - For each $k$ nodes, any consistent assignment to $k - 1$ can be extended to the $k$th node

## Strong K-Consistency

> [!theorem]+ Strong N-Consistency Property
> **Claim:** Strong $n$-consistency means we can solve without backtracking!
>
> **Why?**
> - Choose any assignment to any variable
> - Choose a new variable
> - By 2-consistency, there is a choice consistent with the first
> - Choose a new variable
> - By 3-consistency, there is a choice consistent with the first 2
> - ...continuing this process guarantees a solution
>
> **Note:** Lots of middle ground between arc consistency and $n$-consistency exists (e.g., $k = 3$, called path consistency)

> [!note]+ Related Concepts
> - **[[Arc Consistency]]**: Special case where $k=2$
> - **[[CSP]]**: Problem type using consistency
> - **[[Backtracking Search]]**: Can be eliminated with strong $n$-consistency
> - **[[Filtering]]**: General technique for domain reduction
