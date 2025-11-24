---
title: Alpha-Beta (Pruning)
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Alpha-Beta Pruning** is an optimization technique for [[Minimax Search]] that eliminates branches that cannot influence the final decision, significantly reducing the number of nodes evaluated.

## Key Variables

> [!abstract]+ Alpha and Beta
> **$\alpha$:** Best value that MAX can guarantee at any choice point along the current path from the root
>
> **$\beta$:** Best value that MIN can guarantee at any choice point along the current path from the root
>
> **Initial values:** $\alpha = -\infty$, $\beta = +\infty$

## How It Works

> [!abstract]+ Pruning Logic
> **General case (pruning children of MIN node):**
> - Computing the min value at node $n$
> - Looping over $n$'s children
> - $n$'s estimate is dropping
> - Let $\alpha$ be MAX's best option so far
> - If $n$ becomes worse than $\alpha$, MAX will avoid it
> - **Result:** Can prune $n$'s remaining children
>
> **Symmetric case (pruning children of MAX node):**
> - Let $\beta$ be MIN's best option so far
> - If $n$ becomes better than $\beta$, MIN will avoid it
> - **Result:** Can prune $n$'s remaining children
>
> ![[27759291558b4df3e3cc0be5eac3f7e5.png]]

## Example

> [!example]+ Pruning Visualization
> ![[09f77ac33d0fc3c01a73b483f5f91064.png]]
>
> **Note:** The order of node generation matters - good moves explored first enable more pruning

## Implementation

> [!abstract]+ Alpha-Beta Algorithm
> **Max-value function:**
> ```python
> def max_value(state, α, β):
>     if state.terminal: return state.utility
>     v = -infty
>     for s in state.successors:
>         v = max(v, min_value(s, α, β))
>         if v >= β:
>             return v  # Prune
>         α = max(α, v)
>     return v
> ```
>
> **Min-value function:**
> ```python
> def min_value(state, α, β):
>     if state.terminal: return state.utility
>     v = +infty
>     for s in state.successors:
>         v = min(v, max_value(s, α, β))
>         if v <= α:
>             return v  # Prune
>         β = min(β, v)
>     return v
> ```

## Properties

> [!abstract]+ Correctness and Efficiency
> **Theorem:** This pruning has no effect on the minimax value computed for the root!
>
> **Move ordering importance:**
> - Good child ordering improves pruning effectiveness
> - Iterative deepening helps with move ordering
>
> **With perfect ordering:**
> - **Time complexity:** $\mathcal{O}(b^{m/2})$
> - **Practical impact:** Doubles solvable depth!
> - Without pruning: $\mathcal{O}(b^m)$

> [!note]+ Related Concepts
> - **[[Minimax Search]]**: Base algorithm being optimized
> - **[[Adversarial Search]]**: General framework
> - **[[Game]]**: Environment being solved
