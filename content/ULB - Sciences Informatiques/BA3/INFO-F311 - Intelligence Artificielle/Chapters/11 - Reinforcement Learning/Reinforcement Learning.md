---
title: Reinforcement Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Reinforcement Learning** is an online planning approach where an agent learns to maximize expected rewards through exploration and feedback, without prior knowledge of the transition or reward functions.

## Core Concept

> [!abstract]+ Basic Idea
> - Receive feedback in the form of rewards
> - Agent's utility is defined by the reward function
> - Must act so as to maximize expected rewards
> - All learning is based on observed samples of outcomes
>
> ![[Pasted image 20251124120112.png]]
> *Main RL loop*

## MDP Framework

> [!abstract]+ Reinforcement Learning as MDP
> Reinforcement learning still operates within the [[Markov Decision Process]] framework:
>
> **Known components:**
> - A set of states $s \in S$
> - A set of actions (per state) $A(s)$
> - Goal: Find a policy $\pi(s)$
>
> **Unknown components:**
> - Transition model $T(s, a, s')$ - not known explicitly
> - Reward function $R(s, a, s')$ - not known explicitly
>
> **Key difference:** We don't know which states are good or what actions do. We must explore to discover how the world works.

## Online vs Offline Planning

> [!abstract]+ Planning Paradigms
> **Offline planning** (solving MDPs):
> - Agents have full knowledge of $T$ and $R$
> - Can precompute optimal actions without taking any
> - Examples: [[Value Iteration]], [[Policy Iteration]]
>
> **Online planning** (reinforcement learning):
> - No prior knowledge of rewards or transitions
> - Must perform **exploration** to gather data
> - Receives **feedback** from actions taken
> - Uses feedback to estimate optimal policy
> - Eventually performs **exploitation** (reward maximization)

## Terminology

> [!abstract]+ Key Concepts
> **Sample:**
> - Tuple $(s, a, s', r)$ representing one transition
> - $s$: starting state
> - $a$: action taken
> - $s'$: successor state arrived at
> - $r$: reward received
>
> **Episode:**
> - Collection of samples from start to terminal state
> - Agent continues taking actions until termination
> - Multiple episodes used during exploration
>
> **Exploration:**
> - Process of trying actions to discover how world works
> - Collects samples and episodes
> - Gathers data for learning
>
> **Exploitation:**
> - Using learned policy to maximize rewards
> - Occurs after sufficient exploration

## Types of Reinforcement Learning

> [!abstract]+ Two Main Approaches
> **[[Model-Based Learning]]:**
> - Estimates transition function $T(s,a,s')$ and reward function $R(s,a,s')$
> - Constructs explicit model from samples
> - Solves resulting MDP with value/policy iteration
>
> **[[Model-Free Learning]]:**
> - Estimates values or Q-values directly
> - No explicit model construction
> - Never stores transition or reward estimates

> [!note]+ Related Concepts
> - **[[Markov Decision Process]]**: Framework for RL
> - **[[Model-Based Learning]]**: RL approach using explicit models
> - **[[Model-Free Learning]]**: RL approach without explicit models
> - **[[Policy]]**: What RL aims to learn
> - **[[Value Iteration]]**: Used in model-based RL
> - **[[Policy Iteration]]**: Used in model-based RL
