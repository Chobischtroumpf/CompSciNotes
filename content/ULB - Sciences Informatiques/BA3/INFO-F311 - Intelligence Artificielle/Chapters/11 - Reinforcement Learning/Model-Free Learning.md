---
title: Model-Free Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Model-Free Learning** is a [[Reinforcement Learning]] approach that estimates values or Q-values of states directly, without constructing explicit models of the transition function $T$ or reward function $R$.

## Core Concept

> [!abstract]+ Key Idea
> **Strategy:**
> - Learn state values or Q-values through experience
> - Never store transition or reward models
> - No memory overhead for maintaining counts
> - Directly applicable to decision-making
>
> **Contrast with [[Model-Based Learning]]:**
> - Model-based: Estimates $T$ and $R$, then solves [[Markov Decision Process|MDP]]
> - Model-free: Learns values/Q-values directly from samples

## Categories of Model-Free Learning

> [!abstract]+ Two Main Classes
> **[[Passive Reinforcement Learning]]:**
> - Agent follows a fixed policy $\pi$
> - Learns state values $V^\pi(s)$ under that policy
> - Equivalent to policy evaluation without knowing $T$ and $R$
> - Algorithms: [[Direct Evaluation]], [[Temporal Difference Learning]]
>
> **[[Active Reinforcement Learning]]:**
> - Agent learns and updates policy simultaneously
> - Uses feedback to iteratively improve policy
> - Determines optimal policy through exploration
> - Algorithm: [[Q-Learning]]

## Properties

> [!success]+ Advantages
> - No memory overhead for storing transition counts
> - Values computed directly without intermediate model
> - Can be applied online during interaction
> - Scales better to large state spaces

> [!fail]+ Disadvantages
> - Cannot simulate or plan ahead without a model
> - May require more samples to converge
> - Cannot transfer learned knowledge as easily

> [!note]+ Related Concepts
> - **[[Reinforcement Learning]]**: General framework
> - **[[Model-Based Learning]]**: Alternative RL approach
> - **[[Passive Reinforcement Learning]]**: Evaluation with fixed policy
> - **[[Active Reinforcement Learning]]**: Learning optimal policy
> - **[[Direct Evaluation]]**: Passive model-free algorithm
> - **[[Temporal Difference Learning]]**: Passive model-free algorithm
> - **[[Q-Learning]]**: Active model-free algorithm
