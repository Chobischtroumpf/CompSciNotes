---
title: Passive Reinforcement Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Passive Reinforcement Learning** is a [[Model-Free Learning]] approach where an agent follows a fixed policy $\pi(s)$ and learns the state values $V^\pi(s)$ under that policy through experience.

## Task Definition

> [!abstract]+ Simplified Learning Task
> **Given:**
> - A fixed policy $\pi(s)$ to follow
> - No knowledge of transition function $T$
> - No knowledge of reward function $R$
>
> **Goal:**
> - Learn state values $V^\pi(s)$ for all states $s$
>
> **Key insight:** This is equivalent to policy evaluation for [[Markov Decision Process|MDPs]], but without access to $T$ and $R$.

> [!tip]+ Relation to Active Learning
> [[Active Reinforcement Learning]] extends passive learning by allowing the agent to update its policy while learning, eventually determining the optimal policy.

> [!note]+ Related Concepts
> - **[[Model-Free Learning]]**: General framework
> - **[[Reinforcement Learning]]**: Broader RL context
> - **[[Direct Evaluation]]**: First passive RL algorithm
> - **[[Temporal Difference Learning]]**: Improved passive RL algorithm
> - **[[Active Reinforcement Learning]]**: Extension with policy updates
> - **[[Policy]]**: What is being evaluated
> - **[[State]]**: Values being learned
