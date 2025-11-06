---
title: Ordering
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> **Ordering** refers to heuristics for choosing which variable to assign next and which value to try first in backtracking search.

## Variable Ordering

> [!abstract]+ Minimum Remaining Values (MRV)
> **Strategy:** Choose the variable with the fewest legal values left in its domain
>
> **Also called:**
> - "Most constrained variable"
> - "Fail-fast" ordering
>
> **Rationale:** Detect failures as early as possible

## Value Ordering

> [!abstract]+ Least Constraining Value (LCV)
> **Strategy:** Choose the value that rules out the fewest values in the remaining variables
>
> **Rationale:** Leave maximum flexibility for future assignments

> [!note]+ Related Concepts
> - **[[Backtracking Search]]**: Uses ordering heuristics
> - **[[Filtering]]**: Complementary improvement technique
> - **[[CSP]]**: Problem type using these heuristics
