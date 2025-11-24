---
title: Policy Iteration
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Policy Iteration** is an alternative to [[Value Iteration]] that maintains optimality while providing significant performance gains by iterating on policies rather than values.

## Motivation

> [!abstract]+ Why Policy Iteration?
> **Limitations of value iteration:**
> - Runtime of $\mathcal{O}(|S|^2 |A|)$ per iteration
> - Values converge slowly even when policy has already converged
> - Significant overcomputation when we only need the optimal policy
>
> **Policy iteration advantages:**
> - Policy converges faster than values
> - More efficient for finding optimal policies
> - Maintains optimality guarantees

## Algorithm

> [!abstract]+ Policy Iteration Procedure
> **Steps:**
> 1. **Initialize:** Define an initial policy $\pi_0$ (can be arbitrary)
> 2. **Repeat until convergence:**
>    - **Policy Evaluation:** Compute $V^{\pi_i}(s)$ for all states $s$
>    - **Policy Improvement:** Extract better policy $\pi_{i+1}$ from values
>    - **Check convergence:** If $\pi_{i+1} = \pi_i$, then $\pi_i = \pi^*$

## Policy Evaluation

> [!abstract]+ Computing Values for Fixed Policy
> For a fixed policy $\pi$, compute the expected utility of starting in state $s$ when following $\pi$:
>
> $$V^\pi(s) = \sum_{s'} T(s, \pi(s), s') \left[ R(s, \pi(s), s') + \gamma V^\pi(s') \right]$$
>
> **Key difference from value iteration:**
> - No max operator (action is fixed by policy)
> - Creates a system of $|S|$ linear equations
>
> **Two solution methods:**
>
> **Method 1: Direct solve (faster)**
> - Treat as system of $|S|$ equations
> - Solve directly for all $V^\pi(s)$ values
>
> **Method 2: Iterative updates (slower)**
> - Use update rule until convergence:
> $$V^{\pi_i}_{k + 1}(s) \leftarrow \sum_{s'} T(s, \pi_i(s), s') \left[ R(s, \pi_i(s), s') + \gamma V^{\pi_i}_k (s') \right]$$

## Policy Improvement

> [!abstract]+ Extracting Better Policy
> Use [[Policy Extraction]] on the values from policy evaluation:
>
> $$\pi_{i + 1}(s) = \arg\max_a \sum_{s'} T(s, a, s') \left[ R(s, a, s') + \gamma V^{\pi_i}(s') \right]$$
>
> **Convergence criterion:**
> - If $\pi_{i + 1} = \pi_i$, then $\pi_i = \pi^*$
> - Policy has stabilized at optimal policy

## Example: Racecar

> [!example]+ Policy Iteration Steps
> Racecar MDP with $\gamma = 0.5$:
>
> ![[Pasted image 20251121143246.png]]
>
> **Iteration 0: Initialize policy**
>
> |         | cool | warm | overheated |
> | ------- | ---- | ---- | ---------- |
> | $\pi_0$ | slow | slow | -          |
>
> **Note:** Terminal states have no actions, so $V^{\pi_i}(\text{overheated}) = 0$ for all $i$
>
> **Policy Evaluation for $\pi_0$:**
>
> System of equations:
> $$V^{\pi_0}(\text{cool}) = 1 \cdot [1 + 0.5 \cdot V^{\pi_0}(\text{cool})]$$
> $$V^{\pi_0}(\text{warm}) = 0.5 \cdot [1 + 0.5 \cdot V^{\pi_0}(\text{cool})] + 0.5 \cdot [1 + 0.5 \cdot V^{\pi_0}(\text{warm})]$$
>
> Solving yields:
>
> |             | cool | warm | overheated |
> | :---------: | :--: | :--: | :--------: |
> | $V^{\pi_0}$ |  2   |  2   |     0      |
>
> **Policy Improvement:**
>
> $$\pi_1(\text{cool}) = \arg\max\{\text{slow} : 1 \cdot [1 + 0.5 \cdot 2], \text{fast} : 0.5 \cdot [2 + 0.5 \cdot 2] + 0.5 \cdot [2 + 0.5 \cdot 2]\}$$
> $$= \arg\max\{\text{slow} : 2, \text{fast} : 3\}$$
> $$= \boxed{\text{fast}}$$
>
> $$\pi_1(\text{warm}) = \arg\max\{\text{slow} : 0.5 \cdot [1 + 0.5 \cdot 2] + 0.5 \cdot [1 + 0.5 \cdot 2], \text{fast} : 1 \cdot [-10 + 0.5 \cdot 0]\}$$
> $$= \arg\max\{\text{slow} : 2, \text{fast} : -10\}$$
> $$= \boxed{\text{slow}}$$
>
> **Iteration 1 result:**
>
> |         | cool | warm |
> | :-----: | :--: | :--: |
> | $\pi_0$ | slow | slow |
> | $\pi_1$ | fast | slow |
>
> **Convergence check:**
> Running another iteration yields $\pi_2(\text{cool}) = \text{fast}$ and $\pi_2(\text{warm}) = \text{slow}$.
>
> Since $\pi_2 = \pi_1$, we conclude that $\pi_1 = \pi_2 = \pi^*$.
>
> |         | cool | warm |
> | :-----: | :--: | :--: |
> | $\pi_0$ | slow | slow |
> | $\pi_1$ | fast | slow |
> | $\pi_2$ | fast | slow |
>
> **Result:** Optimal policy found in just 2 iterations!

## Properties

> [!abstract]+ Policy Iteration Characteristics
> **Advantages:**
> - Often converges much faster than value iteration
> - Policy typically stabilizes before values converge
> - Guaranteed to find optimal policy
>
> **Comparison to value iteration:**
> - Policy iteration: Fewer iterations, but each iteration more expensive
> - Value iteration: More iterations, but each iteration cheaper
> - Policy iteration generally preferred when finding optimal policy

> [!note]+ Related Concepts
> - **[[Value Iteration]]**: Alternative algorithm for solving MDPs
> - **[[Policy Extraction]]**: Used in policy improvement step
> - **[[Markov Decision Process]]**: Problem being solved
> - **[[Policy]]**: What policy iteration computes
> - **[[State]]**: Values computed during policy evaluation
