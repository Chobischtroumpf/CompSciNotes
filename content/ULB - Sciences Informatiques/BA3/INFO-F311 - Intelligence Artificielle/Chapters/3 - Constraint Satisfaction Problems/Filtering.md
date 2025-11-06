---
title: Filtering
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> **Filtering** involves keeping track of domains for unassigned variables and crossing off bad options to improve backtracking search efficiency.

## Forward Checking

> [!abstract]+ Strategy
> Cross off values that violate a constraint when added to the existing assignment.
>
> ![[Pasted image 20251103140258.png]]

## Constraint Propagation

> [!abstract]+ Limitation of Forward Checking
> Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures.
>
> ![[Pasted image 20251103140344.png]]

> [!note]+ Related Concepts
> - **[[Backtracking Search]]**: Uses filtering
> - **[[Arc Consistency]]**: More powerful filtering technique
> - **[[Ordering]]**: Complementary improvement technique
