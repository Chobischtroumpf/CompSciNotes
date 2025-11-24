---
title: Local Search
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Local Search** is a search strategy that improves a single solution by making local changes, contrary to tree search which keeps unexplored alternatives on the fringe.

## Core Concept

> [!abstract]+ Key Idea
> Improve a single option until we can't make it better, rather than maintaining multiple alternatives.
>
> **New successor function:** Local changes only
>
> ![[fab5f5561c66c558f84199b3fb534f7e.png]]

## Properties

> [!success]+ Advantages
> - Much faster than tree search
> - More memory efficient (only stores current state)
>
> ![[Pasted image 20251106133000.png]]

> [!fail]+ Disadvantages
> - Incomplete (may not find solution if one exists)
> - Suboptimal (may find poor quality solutions)

## Hill Climbing

> [!abstract]+ Basic Hill Climbing Algorithm
> **Strategy:**
> 1. Start wherever
> 2. Move to the best neighboring state
> 3. If no neighbors better, quit
>
> ```
> function Hill-Climbing(problem) returns a state
>     current <- make-node(problem.initial-state)
>     loop do
>         neighbor <- a highest-valued successor of current
>         if neighbor.value <= current.value then
>             return current.state
>         current <- neighbor
> ```
>
> **Analogy:** "Like climbing Everest in thick fog with amnesia"

## Visualization

> [!example]+ Hill Climbing Behavior
> ![[85243b59352616f52ab2ce7800096acb.png]]
>
> **Challenges:**
> - **Local maxima:** Peak that isn't the highest but has no better neighbors
> - **Plateaus:** Flat regions where all neighbors have the same value
> - **Ridges:** Sequences of local maxima that are difficult to navigate

> [!note]+ Related Concepts
> - **[[Simulated Annealing]]**: Escape local optima with random moves
> - **[[Local Beam Search]]**: Parallel version of local search
> - **[[Iterative Improvement]]**: Local search for CSPs
