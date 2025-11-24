---
title: Q-State
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> The **Value of a Q-State** $Q^*(s,a)$ is the expected utility of taking action $a$ from state $s$ and acting optimally thereafter.

## Analogy to Game Trees

> [!abstract]+ Chance Nodes
> Q-states in MDPs correspond to chance nodes in game trees:
> - Represent commitment to an action before outcomes are known
> - Expected value computed over stochastic successors
> - Analogous to expectimax chance nodes

## Q-Value Function

> [!abstract]+ Optimal Q-Value Function
> ![[Pasted image 20251121144738.png]]
>
> The optimal Q-value is defined as:
>
> $$Q^*(s, a) = \sum_{s'} T(s, a, s') \left[R(s, a, s') + \gamma V^*(s')\right]$$
>
> where:
> - $s'$ ranges over all possible successor states
> - $T(s, a, s')$ is the transition probability to $s'$
> - $R(s, a, s')$ is the immediate reward
> - $\gamma$ is the discount factor
> - $V^*(s')$ is the optimal value of successor state $s'$

## Relationship to State Values

> [!abstract]+ Connection Between Q and V
> **State values are defined via Q-values:**
> $$V^*(s) = \max_a Q^*(s, a)$$
>
> **Intuition:**
> - Q-value: Value of committing to action $a$ first
> - State value: Value of being able to choose best action
> - State value is maximum over all Q-values

## Interpretation

> [!abstract]+ Understanding Q-Values
> **The Q-value $Q^*(s,a)$ represents:**
> - Expected utility of action $a$ from state $s$
> - Accounts for immediate reward plus future rewards
> - Weighted by transition probabilities
> - Assumes optimal behavior after taking action $a$
>
> **Computation:**
> - Sum over all possible next states $s'$
> - Weight by transition probability $T(s,a,s')$
> - Add immediate reward $R(s,a,s')$ plus discounted future value $\gamma V^*(s')$

> [!note]+ Related Concepts
> - **[[Markov Decision Process]]**: Framework defining Q-states
> - **[[State]]**: Related via $V^*(s) = \max_a Q^*(s,a)$
> - **[[Policy]]**: Optimal policy selects $\arg\max_a Q^*(s,a)$
> - **[[Value Iteration]]**: Computes both $V^*$ and $Q^*$
> - **[[Discount Factor]]**: $\gamma$ in the Q-value equation
> - **[[Expectimax Search]]**: Similar chance node concept
