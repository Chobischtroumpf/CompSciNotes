---
title: Policy Extraction
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Policy Extraction** is the process of deriving an optimal policy $\pi^*$ from computed optimal values after solving an MDP.

## Core Idea

> [!abstract]+ Intuition
> The ultimate goal in solving an MDP is to determine an optimal policy. Once all optimal values for states are determined, we can extract the policy.
>
> **Key insight:** If you're in a state $s$, take the action $a$ which yields the maximum expected utility.

## Extraction Formula

> [!abstract]+ Policy Extraction Equation
> $$\forall s \in S, \pi^*(s) = \arg\max_a Q^*(s,a) = \arg\max_a \sum_{s'} T(s,a,s') [R(s,a,s') + \gamma V^*(s')]$$
>
> where:
> - $\pi^*(s)$ is the optimal action to take in state $s$
> - $Q^*(s,a)$ is the optimal Q-value for taking action $a$ in state $s$
> - $V^*(s')$ is the optimal value of successor state $s'$

## Performance Considerations

> [!tip]+ Q-Values vs V-Values
> **Using Q-values** (preferred for performance):
> - $\pi^*(s) = \arg\max_a Q^*(s,a)$
> - Requires only a single argmax operation
> - Fast and simple
>
> **Using V-values** (requires recomputation):
> - Must recompute all Q-values with the Bellman equation before applying argmax
> - Equivalent to performing a depth-1 expectimax
> - More computationally expensive
>
> **Recommendation:** Store optimal Q-values if policy extraction will be performed frequently

> [!note]+ Related Concepts
> - **[[Policy]]**: The output of policy extraction
> - **[[Value Iteration]]**: Computes values used for extraction
> - **[[State]]**: V-values used in extraction
> - **[[Q-State]]**: Q-values enable simpler extraction
> - **[[Markov Decision Process]]**: Framework being solved
