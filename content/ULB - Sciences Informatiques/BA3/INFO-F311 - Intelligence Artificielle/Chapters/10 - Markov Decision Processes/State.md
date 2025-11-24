---
title: State
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> The **Value of a State** $V^*(s)$ is the expected utility of starting in state $s$ and acting optimally thereafter.

## Analogy to Game Trees

> [!abstract]+ Max Nodes
> States in MDPs correspond to max nodes in game trees:
> - Agent chooses action to maximize expected utility
> - Analogous to maximizing player in adversarial search

## Value Function

> [!abstract]+ Optimal Value Function
> ![[e4632cea8304a3e732a44b059fb41cbc.png]]
>
> The optimal value of state $s$ can be expressed in multiple equivalent ways:
>
> **Definition 1** (via [[Q-State|Q-states]]):
> $$V^*(s) = \max_a Q^*(s, a)$$
>
> **Definition 2** (Bellman equation):
> $$V^*(s) = \max_a \sum_{s'} T(s, a, s') \left[R(s, a, s') + \gamma V^*(s')\right]$$
>
> where:
> - $a$ ranges over all actions $A$
> - $s'$ ranges over all possible next states
> - $T(s, a, s')$ is the transition probability
> - $R(s, a, s')$ is the immediate reward
> - $\gamma$ is the discount factor
> - $V^*(s')$ is the value of the next state

## Interpretation

> [!abstract]+ Understanding State Values
> **The value $V^*(s)$ represents:**
> - Expected sum of discounted rewards from state $s$
> - Assumes optimal action selection at every step
> - Accounts for all possible stochastic outcomes
>
> **Computation:**
> - Consider all possible actions from $s$
> - For each action, compute expected value over successor states
> - Take maximum over all actions

> [!note]+ Related Concepts
> - **[[Markov Decision Process]]**: Framework defining states
> - **[[Q-State]]**: Value of state-action pairs
> - **[[Policy]]**: Optimal policy chooses actions that achieve $V^*(s)$
> - **[[Value Iteration]]**: Algorithm that computes $V^*$
> - **[[Discount Factor]]**: $\gamma$ in the Bellman equation
> - **[[Adversarial Search]]**: Similar max node concept
