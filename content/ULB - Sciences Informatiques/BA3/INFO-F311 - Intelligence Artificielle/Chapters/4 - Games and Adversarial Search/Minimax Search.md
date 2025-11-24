---
title: Minimax Search
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Minimax Search** is a state-space search tree algorithm where players alternate turns and compute each node's minimax value: the best achievable utility against a rational (optimal) adversary.

## Algorithm Overview

> [!abstract]+ Core Concept
> ![[d1a28c7ec60ad4ace0cf675bdc416a14.png]]
>
> Minimax computes the value of each state by assuming:
> - **Max nodes:** Agent chooses action that maximizes value
> - **Min nodes:** Opponent chooses action that minimizes value

## Implementation

> [!abstract]+ Basic Implementation
> **Max-value function:**
> ```python
> def max_value(state):
>     v = -infty
>     for s in state.successors:
>         v = max(v, min_value(s))
>     return v
> ```
> $$V(s) = \max_{s' \in \text{successors}(s)} V(s')$$
>
> **Min-value function:**
> ```python
> def min_value(state):
>     v = +infty
>     for s in state.successors:
>         v = min(v, max_value(s))
>     return v
> ```
> $$V(s) = \min_{s' \in \text{successors}(s)} V(s')$$

> [!abstract]+ Dispatch Implementation
> **Main dispatch:**
> ```python
> def value(state):
>     if state.terminal: return state.utility
>     if agent.max: return max_value(state)
>     if agent.min: return min_value(state)
> ```
>
> **Max-value (simplified):**
> ```python
> def max_value(state):
>     v = -infty
>     for s in state.successors:
>         v = max(v, s.value)
>     return v
> ```
>
> **Min-value (simplified):**
> ```python
> def min_value(state):
>     v = +infty
>     for s in state.successors:
>         v = min(v, s.value)
>     return v
> ```

## Example

> [!example]+ Minimax Computation
> ![[ad4ecee9d50e40892830f12ebe4216f5.png]]
> ![[3db8cb4b216892f4f476423f4e7fce1a.png]]

## Generalized Minimax

> [!abstract]+ Multi-Player Extension
> **For non-zero-sum or multi-player games:**
> - Terminals have utility tuples
> - Node values are also utility tuples
> - Each player maximizes its own component
> - Can give rise to cooperation and competition dynamically
>
> ![[f16aeb2cb269be3df52eb193924ff05c.png]]
> *Example: Generalized Pacman Minimax with 3 agents (red ghost, cyan ghost, and pacman)*

## Efficiency

> [!abstract]+ Complexity Analysis
> Similar to exhaustive DFS:
> - **Time complexity:** $\mathcal{O}(b^m)$
> - **Space complexity:** $\mathcal{O}(bm)$
>
> where $b$ is the branching factor and $m$ is the maximum depth

> [!note]+ Related Concepts
> - **[[Adversarial Search]]**: Framework for competitive games
> - **[[Alpha-Beta Pruning]]**: Optimization technique for minimax
> - **[[Game]]**: Environment being solved
> - **[[Expectimax Search]]**: Extension to stochastic environments
