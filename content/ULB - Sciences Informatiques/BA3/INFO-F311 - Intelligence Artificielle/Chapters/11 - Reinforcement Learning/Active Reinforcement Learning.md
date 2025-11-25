---
title: Active Reinforcement Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Active Reinforcement Learning** is a [[Model-Free Learning]] approach where an agent simultaneously learns and improves its policy through exploration and exploitation, aiming to discover the optimal policy $\pi^*(s)$.

## Core Concept

> [!abstract]+ Learning While Acting
> **Key characteristics:**
> - Agent does not follow a fixed policy
> - Updates policy based on experience and feedback
> - Balances exploration (gathering information) and exploitation (maximizing rewards)
> - Goal: Learn optimal policy $\pi^*$ that maximizes expected cumulative reward
>
> **Contrast with [[Passive Reinforcement Learning]]:**
> - Passive: Fixed policy $\pi$, learns $V^\pi(s)$ (policy evaluation)
> - Active: Improves policy, learns $Q^*(s,a)$ or $\pi^*$ (policy optimization)

## Main Algorithm

> [!abstract]+ Q-Learning
> **[[Q-Learning]]** is the primary active reinforcement learning algorithm:
> - Learns optimal Q-values $Q^*(s,a)$ directly
> - Off-policy: Can learn optimal policy while taking suboptimal actions
> - Converges to optimal policy with sufficient exploration
> - Optimal policy extracted via: $\pi^*(s) = \arg\max_a Q^*(s,a)$

## Exploration vs Exploitation

> [!abstract]+ The Fundamental Tradeoff
> **Exploration:**
> - Try new actions to discover better strategies
> - Necessary to learn about unknown states and rewards
> - May sacrifice short-term rewards
>
> **Exploitation:**
> - Use current best policy to maximize rewards
> - Leverages already learned information
> - May miss better alternatives
>
> **Solution:** Balance both through techniques like $\epsilon$-greedy policies or optimistic initialization

> [!note]+ Related Concepts
> - **[[Q-Learning]]**: Main active RL algorithm
> - **[[Approximate Q-Learning]]**: Scalable extension of Q-learning
> - **[[Passive Reinforcement Learning]]**: Simpler fixed-policy variant
> - **[[Model-Free Learning]]**: General framework
> - **[[Reinforcement Learning]]**: Broader context
> - **[[Policy]]**: What active RL learns and optimizes
> - **[[Q-State]]**: Values learned in Q-learning
