---
title: Uniform Cost Search
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Uniform Cost Search (UCS)** is a search algorithm that explores increasing cost contours.

> [!abstract]+ Strategy
> **Orders by path cost (backward cost) $g(n)$**
>
> ![[Pasted image 20251103105659.png]]
>
> - Explores nodes in order of total path cost from start
> - Finds cheapest path first, regardless of direction toward goal
> - Explores uniformly in all directions based purely on accumulated cost

## Properties

> [!abstract]+ Characteristics
> **The good:**
> - Complete: Guaranteed to find a solution if one exists
> - Optimal: Guaranteed to find the least cost path
>
> **The bad:**
> - Explores options in every direction
> - No information about the goal's location
> - Time and space complexity are exponential in effective depth

> [!note]+ Related Concepts
> - **[[A*]]**: Informed version of UCS
> - **[[Search Algorithm Properties]]**: Performance characteristics
> - **[[Greedy Search]]**: Alternative search strategy
