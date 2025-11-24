---
title: Filtering
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Filtering** involves keeping track of domains for unassigned variables and crossing off bad options to improve backtracking search efficiency.

## Forward Checking

> [!abstract]+ Strategy
> Cross off values that violate a constraint when added to the existing assignment.
>
> ![[acdb787d97c91e232494a496a795d25f.png]]

## Constraint Propagation

> [!abstract]+ Limitation of Forward Checking
> Forward checking propagates information from assigned to unassigned variables, but doesn't provide early detection for all failures.
>
> ![[6131d5231a72f83a78241c0c990dab0d.png]]

> [!note]+ Related Concepts
> - **[[Backtracking Search]]**: Uses filtering
> - **[[Arc Consistency]]**: More powerful filtering technique
> - **[[Ordering]]**: Complementary improvement technique
