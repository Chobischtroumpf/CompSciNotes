---
title: K-Consistency
authors: Mihai Bors
tags:
  - AI
---


- 1-Consistency (Node Consistency): Every single node's domain has a value which meets that node's unary constraints
- 2-Consistency ([[Arc Consistency]]): For each pair of nodes, any consistent assignment to one can be extended to the other
- $K$-Consistency:  For each $k$ nodes, any consistent assignment to $k - 1$ can be extended to the $k$th node

## Strong $K$-Consistency

Claim: strong $n$-consistency means we can solve without backtracking!

Why?
- Choose any assignment to any variable
- Choose a new variable
- By 2-consistency, there is a choice consistent with the first
- Choose a new variable
- By 3-consistency, there is a choice consistent with the first 2
- …
- Lots of middle ground between arc consistency and $n$-consistency! (e.g. $k = 3$, called path consistency)
