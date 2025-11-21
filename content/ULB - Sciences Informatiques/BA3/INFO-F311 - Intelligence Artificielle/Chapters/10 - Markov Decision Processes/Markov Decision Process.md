---
title: Markov Decision Process
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **Markov Decision Process (MDP)** is a framework for modeling decision-making in situations where outcomes are partly random and partly under the control of a decision maker.
>
> "Markov" means that given the present state, the future and the past are independent. For MDPs, action outcomes depend only on the current state.

## Components

> [!abstract]+ MDP Structure
> An MDP is defined by:
> - **States** $S$: Set of all possible states
> - **Actions** $A$: Set of all possible actions
> - **Start state** $s_0$: Initial state
> - **Terminal states**: Optional end states (sink states with no outgoing edges)
> - **Discount factor** $\gamma$: Controls value of future rewards
> - **Transition function** $T(s,a,s')$: Probability of reaching state $s'$ when taking action $a$ from state $s$
> - **Reward function** $R(s,a,s')$: Reward received when transitioning from state $s$ to $s'$ via action $a$

## Example: Racing

> [!example]+ Racecar MDP
> ![[Pasted image 20251121143246.png]]
>
> **States**: $S = \{\text{cool}, \text{warm}, \text{overheated}\}$
>
> **Actions**: $A = \{\text{slow}, \text{fast}\}$
>
> **Terminal state**: Overheated (sink state with no outgoing edges)
>
> **Transition Function** $T(s,a,s')$:
> - $T(\text{cool}, \text{slow}, \text{cool}) = 1$
> - $T(\text{warm}, \text{slow}, \text{cool}) = 0.5$
> - $T(\text{warm}, \text{slow}, \text{warm}) = 0.5$
> - $T(\text{cool}, \text{fast}, \text{cool}) = 0.5$
> - $T(\text{cool}, \text{fast}, \text{warm}) = 0.5$
> - $T(\text{warm}, \text{fast}, \text{overheated}) = 1$
>
> **Reward Function** $R(s,a,s')$:
> - $R(\text{cool}, \text{slow}, \text{cool}) = 1$
> - $R(\text{warm}, \text{slow}, \text{cool}) = 1$
> - $R(\text{warm}, \text{slow}, \text{warm}) = 1$
> - $R(\text{cool}, \text{fast}, \text{cool}) = 2$
> - $R(\text{cool}, \text{fast}, \text{warm}) = 2$
> - $R(\text{warm}, \text{fast}, \text{overheated}) = -10$

## Agent Movement Through Time

> [!abstract]+ Timesteps and Trajectories
> Agent movement through an MDP is represented with discrete timesteps:
>
> $$s_0 \xrightarrow{a_0} s_1 \xrightarrow{a_1} s_2 \xrightarrow{a_2} s_3 \xrightarrow{a_3} ...$$
>
> where $s_t \in S$ is the state at timestep $t$ and $a_t \in A$ is the action taken at timestep $t$.

## Utility Functions

> [!abstract]+ Additive Utility
> Agent's goal is to maximize reward across all timesteps:
>
> $$U([s_0, a_0, s_1, a_1, s_2, ...]) = R(s_0, a_0, s_1) + R(s_1, a_1, s_2) + R(s_2, a_2, s_3) + ...$$

> [!abstract]+ Discounted Utility
> With discount factor $\gamma$, rewards decay over time:
>
> $$U([s_0, a_0, s_1, a_1, s_2, ...]) = R(s_0, a_0, s_1) + \gamma R(s_1, a_1, s_2) + \gamma^2 R(s_2, a_2, s_3) + ...$$

## Search Tree Representation

> [!abstract]+ MDP Search Trees
> MDPs can be unraveled into search trees with **Q-states** (action states):
> - Similar to expectimax chance nodes
> - Q-states model uncertainty in state transitions
> - Represented as tuple $(s, a)$ for action $a$ taken from state $s$
> - Agents spend zero timesteps in Q-states
>
> ![[Pasted image 20251121143858.png]]
> *Green nodes represent Q-states where action has been taken but not yet resolved*

## States, Q-States, and Transitions

![[Pasted image 20251121152532.png]]

> [!note]+ Related Concepts
> - **[[Policy]]**: Mapping from states to actions
> - **[[State]]**: Value of being in a state
> - **[[Q-State]]**: Value of taking an action from a state
> - **[[Discount Factor]]**: Controls time preference for rewards
> - **[[Value Iteration]]**: Algorithm for solving MDPs
> - **[[Expectimax Search]]**: Similar tree structure with chance nodes
