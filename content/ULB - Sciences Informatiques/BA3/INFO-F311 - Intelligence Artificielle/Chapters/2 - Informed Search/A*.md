---
title: A*
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> **A\* search** is an optimal search algorithm that expands nodes most likely to be on an optimal path by combining actual path cost with estimated remaining cost.

## Core Idea

> [!abstract]+ Strategy
> Expand node $n$ with lowest value of:
>
> $$f(n) = g(n) + h(n)$$
>
> ![[Pasted image 20251103105917.png]]
>
> Where:
> - $g(n)$ = cost from start to node $n$
> - $h(n)$ = estimated cost from $n$ to closest goal
> - $f(n)$ = estimated total cost of path through $n$

> [!note]
> A* combines both [[Uniform Cost Search|UCS]] and [[Greedy Search]] algorithms:
> - Backward cost $g(n)$
> - Forward cost $h(n)$

## Example

> [!example]+ Route-Finding in Romania
> ![[Pasted image 20251103105125.png]]
>
> **Goal:** Find optimal path to Bucharest
>
> **Heuristic:** Straight-line distance to Bucharest
>
> The algorithm balances:
> - Path cost already incurred ($g$)
> - Estimated remaining cost ($h$)

## Termination

> [!question]+ When Should A* Terminate?
> **Only stop when we dequeue a goal**
>
> Do not stop when we enqueue a goal - there might still be better paths in the queue.

## Optimality

> [!warning]+ Optimality Requirement
> A* is optimal only with an **admissible heuristic**
>
> - Inadmissible heuristics can cause A* to find suboptimal solutions
> - The heuristic must never overestimate the true cost

> [!theorem]+ Optimality of A* Tree Search
> **Theorem:** If $h(n)$ is admissible, A* tree search is optimal.
>
> **Proof sketch:**
> 1. Let $A$ be an optimal goal node and $B$ a suboptimal goal node
> 2. Some ancestor $n$ of $A$ is on the frontier
> 3. $f(n) \leq f(A)$ (by admissibility)
> 4. $f(A) < f(B)$ (by suboptimality of $B$)
> 5. Therefore $f(n) < f(B)$
> 6. Thus $n$ (and eventually $A$) expands before $B$

> [!note]+ Related Concepts
> - **[[Search Heuristic]]**: Estimation function
> - **[[Admissibility]]**: Property ensuring optimality
> - **[[Uniform Cost Search]]**: Special case where $h(n) = 0$
> - **[[Greedy Search]]**: Special case ignoring $g(n)$
