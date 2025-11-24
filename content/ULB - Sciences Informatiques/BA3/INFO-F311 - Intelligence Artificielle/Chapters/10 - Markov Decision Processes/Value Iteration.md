---
title: Value Iteration
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Value Iteration** is a dynamic programming algorithm that computes optimal values for all states by iteratively applying the Bellman update until convergence.

## Algorithm

> [!abstract]+ Value Iteration Update
> **Core update equation:**
> $$V_{k+1}(s) \leftarrow \max_a \sum_{s'} T(s, a, s') \left[ R(s, a, s') + \gamma V_k(s') \right]$$
>
> **Procedure:**
> 1. Start with $V_0(s) = 0$ for all states
> 2. Repeat update for all states until convergence
> 3. Each iteration performs one ply of expectimax from each state
>
> **Complexity:** Each iteration is $\mathcal{O}(S^2 A)$
> - $S$ = number of states
> - $A$ = number of actions

## Relationship to Bellman Equations

> [!abstract]+ Bellman Characterization
> **Bellman equations** (from [[State]] and [[Q-State]]) characterize the optimal values:
> - $V^*(s) = \max_a \sum_{s'} T(s, a, s') [R(s, a, s') + \gamma V^*(s')]$
> - $Q^*(s,a) = \sum_{s'} T(s, a, s') [R(s, a, s') + \gamma V^*(s')]$
>
> **Value iteration** computes these optimal values through iteration.

## Convergence

> [!abstract]+ Convergence Guarantee
> ![[Pasted image 20251121155049.png]]
>
> **Question:** How do we know the $V_k$ vectors converge (assuming $0 < \gamma < 1$)?
>
> **Proof sketch:**
> 1. $V_k$ and $V_{k+1}$ are depth-$(k+1)$ expectimax results in nearly identical trees
> 2. The only difference: bottom layer has actual rewards vs zeros
> 3. Bottom layer is at best all $R_{\max}$ and at worst $R_{\min}$
> 4. Everything is discounted by $\gamma^k$ at that depth
> 5. Therefore: $V_k$ and $V_{k+1}$ differ by at most $\gamma^k \max|R|$
> 6. As $k \to \infty$, $\gamma^k \to 0$, so values converge

## Q-Value Iteration

In solving for an optimal policy using value iteration, we first find all the optimal values, then extract the policy using policy extraction. However, you might have noticed that we also deal with another type of value that encodes information about the optimal policy: Q-values.

**Q-value iteration** is a dynamic programming algorithm that computes time-limited Q-values. It is described in the following equation:

$$Q_{k + 1}(s, a) \leftarrow \sum_{s'} T(s, a, s') \left[ R(s, a, s') + \gamma \max_{a'} Q_k(s', a') \right]$$
Note that this update is only a slight modification over the update rule for value iteration. Indeed, the only real difference is that the position of the max operator over actions has been changed since we select an action before transitioning when we’re in a state, but we transition before selecting a new action when we’re in a Q-state. Once we have the optimal Q-values for each state and action, we can then find the policy for a state by simply choosing the action which has the highest Q-value.

## Example: Racecar

> [!example]+ Value Iteration Steps
> Racecar MDP with $\gamma = 0.5$:
>
> **Initialization:**
>
> |     | **cool** | **warm** | **overheated** |
> | --- | -------- | -------- | -------------- |
> | $V_0$  | 0        | 0        | 0              |
>
> **First iteration:**
> $$V_1(\text{cool}) = \max\{1 \cdot [1 + 0.5 \cdot 0], 0.5 \cdot [2 + 0.5 \cdot 0] + 0.5 \cdot [2 + 0.5 \cdot 0]\}$$
> $$= \max\{1, 2\} = 2$$
>
> $$V_1(\text{warm}) = \max\{0.5 \cdot [1 + 0.5 \cdot 0] + 0.5 \cdot [1 + 0.5 \cdot 0], 1 \cdot [-10 + 0.5 \cdot 0]\}$$
> $$= \max\{1, -10\} = 1$$
>
> $$V_1(\text{overheated}) = 0$$ (terminal state)
>
> |     | **cool** | **warm** | **overheated** |
> | --- | -------- | -------- | -------------- |
> | $V_0$  | 0        | 0        | 0              |
> | $V_1$  | 2        | 1        | 0              |
>
> **Second iteration:**
> $$V_2(\text{cool}) = \max\{1 \cdot [1 + 0.5 \cdot 2], 0.5 \cdot [2 + 0.5 \cdot 2] + 0.5 \cdot [2 + 0.5 \cdot 1]\}$$
> $$= \max\{2, 2.75\} = 2.75$$
>
> $$V_2(\text{warm}) = \max\{0.5 \cdot [1 + 0.5 \cdot 2] + 0.5 \cdot [1 + 0.5 \cdot 1], 1 \cdot [-10 + 0.5 \cdot 0]\}$$
> $$= \max\{1.75, -10\} = 1.75$$
>
> |     | **cool** | **warm** | **overheated** |
> | --- | -------- | -------- | -------------- |
> | $V_0$  | 0        | 0        | 0              |
> | $V_1$  | 2        | 1        | 0              |
> | $V_2$  | 2.75     | 1.75     | 0              |
>
> **Note:** $V^*(s) = 0$ for all terminal states (no future actions possible)

## Properties

> [!abstract]+ Value Iteration Characteristics
> **Advantages:**
> - Guaranteed to converge to $V^*$
> - Works for any MDP structure
> - Simple to implement
>
> **Considerations:**
> - Requires multiple passes over all states
> - Must iterate until convergence
> - Terminal states always have $V^* = 0$

> [!note]+ Related Concepts
> - **[[Markov Decision Process]]**: Problem being solved
> - **[[State]]**: Bellman equation defines optimal values
> - **[[Q-State]]**: Can also iterate on Q-values
> - **[[Policy Extraction]]**: Extracting policy from computed values
> - **[[Time-Limited Values]]**: Interpretation of $V_k$
> - **[[Discount Factor]]**: Used in update equation
