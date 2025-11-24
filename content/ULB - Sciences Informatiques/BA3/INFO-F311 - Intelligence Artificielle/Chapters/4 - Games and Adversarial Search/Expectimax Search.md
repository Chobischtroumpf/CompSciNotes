---
title: Expectimax Search
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Expectimax Search** is an extension of [[Minimax Search]] for handling uncertain outcomes controlled by chance rather than an adversary, computing average-case outcomes instead of worst-case.

## Motivation

> [!abstract]+ When to Use Expectimax
> **Uncertainty sources:**
> - Randomness in the environment
> - Unpredictable opponents
> - Action failures (actions fail with some probability)
> - Imperfect world models
>
> **Key difference from minimax:**
> - Values reflect **average-case** outcomes, not worst-case
> - Compute average score under optimal play

## Node Types

> [!abstract]+ Expectimax Tree Structure
> **Max nodes:** Same as minimax - agent chooses action that maximizes value
>
> **Chance nodes:** Like min nodes but outcome is uncertain
> - Calculate expected utilities based on probabilities
> - Not adversarial - governed by probability distribution
>
> ![[Pasted image 20251111135158.png]]
> *Example: Max node with two chance nodes. Left node: (10 + 10)/2 = 10. Right node: (9 + 100)/2 = 54.5. Max chooses right.*

## Implementation

> [!abstract]+ Expectimax Algorithm
> **Main dispatch:**
> ```python
> def value(state):
>     if state.terminal: return state.utility
>     if agent.max: return max_value(state)
>     if agent.exp: return exp_value(state)
> ```
>
> **Max-value function:**
> ```python
> def max_value(state):
>     v = -infty
>     for s in state.successors:
>         v = max(v, exp_value(s))
>     return v
> ```
>
> **Expected-value function:**
> ```python
> def exp_value(state):
>     v = 0
>     for s in state.successors:
>         p = probability(s)
>         v += p * s.value
>     return v
> ```

## Example

> [!example]+ Expected Value Calculation
> ![[Pasted image 20251111135715.png]]
>
> **Calculation:**
> $$v = \frac{1}{2}(8) + \frac{1}{3}(24) + \frac{1}{6}(-12) = 10$$

## Limitations

> [!warning]+ Expectimax Constraints
> **Cannot prune:**
> - Unlike alpha-beta pruning, expectimax cannot prune branches
> - Must evaluate all successors (next value could be 5 million!)
>
> **Depth limiting:**
> - Usually depth-limited in practice
> - Use evaluation functions to estimate true expectimax value
> - Necessary to avoid computational explosion

## Probabilistic Modeling

> [!abstract]+ Opponent/Environment Model
> In expectimax, we have a probabilistic model of how the opponent (or environment) behaves at any state.
>
> **Models can be:**
> - Simple uniform distribution (equal probabilities)
> - Sophisticated learned models
>
> **Example scenario:**
> If you know your opponent runs depth-2 minimax 80% of the time and moves randomly 20% of the time:
> - **Solution:** Use expectimax!
> - Model each chance node with appropriate probabilities
> - Simulate opponent behavior (depth-limited to avoid slowness)

## Comparison: Minimax vs Expectimax

> [!abstract]+ Trade-offs
> **Minimax:**
> - Dangerous pessimism
> - Assumes worst case when it's not likely
>
> **Expectimax:**
> - Dangerous optimism
> - Assumes chance when the world is adversarial
>
> ![[Pasted image 20251111140622.png]]
> *Results from 5 Pacman games with different agent/ghost combinations*

> [!note]+ Related Concepts
> - **[[Minimax Search]]**: Deterministic adversarial version
> - **[[Adversarial Search]]**: General framework
> - **[[Evaluation Function]]**: Used for depth-limited expectimax
> - **[[Game]]**: Environment being modeled
