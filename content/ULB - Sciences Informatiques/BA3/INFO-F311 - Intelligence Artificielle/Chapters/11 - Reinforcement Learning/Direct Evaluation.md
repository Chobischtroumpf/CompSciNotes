---
title: Direct Evaluation
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Direct Evaluation** is a [[Passive Reinforcement Learning]] algorithm that estimates state values by averaging the total utility obtained from each state across multiple episodes.

## Algorithm

> [!abstract]+ Core Strategy
> **Process:**
> 1. Fix a policy $\pi$ to follow
> 2. Experience several episodes following $\pi$
> 3. For each state $s$:
>    - Track total utility obtained from $s$ across all episodes
>    - Count number of times $s$ was visited
> 4. Compute estimated value:
>
> $$V^\pi(s) = \frac{\text{Total utility from } s}{\text{Number of visits to } s}$$
>
> **Key idea:** Simple averaging of observed returns from each state

## Example

> [!example]+ Direct Evaluation Walkthrough
> Consider the following MDP with $\gamma = 1$:
>
> ![[649ee8e7486591fe105347793412da64.png]]
>
> **Episode analysis:**
>
> **Episode 1:** Walking through from state $D$ to termination:
> - From $D$: Total reward = 10
> - From $C$: Total reward = $(-1) + 10 = 9$
> - From $B$: Total reward = $(-1) + (-1) + 10 = 8$
>
> **After all episodes:**
>
> | $s$ | Total Reward | Times Visited | $V^\pi(s)$ |
> | :-: | :----------: | :-----------: | :--------: |
> | $A$ |     -10      |       1       |    -10     |
> | $B$ |      16      |       2       |     8      |
> | $C$ |      16      |       4       |     4      |
> | $D$ |      30      |       3       |     10     |
> | $E$ |      -4      |       2       |     -2     |

## Limitations

> [!fail]+ Major Weakness: Information Waste
> **Problem:** Direct evaluation wastes information about state transitions.
>
> ![[7d6723d462f77d96687b9094fd30229d.png]]
>
> **Example issue:**
> - States $B$ and $E$ both transition only to $C$ under $\pi$
> - Both receive reward of $-1$ when transitioning to $C$
> - By Bellman equation: $B$ and $E$ should have same value under $\pi$
>
> **What happened:**
> - Computed $V^\pi(E) = -2$ and $V^\pi(B) = 8$
> - Of 4 times in state $C$:
>   - 3 times: Transitioned to $D$ (reward +10)
>   - 1 time: Transitioned to $A$ (reward -10)
> - Pure chance: The single $-10$ reward happened after $E$, not $B$
> - This severely skewed the estimate for $E$

> [!abstract]+ Why Values Differ Despite Identical Transitions
> **Question:** If $B$ and $E$ both go to $C$ under this policy, how can their values be different?
>
> **Answer:** They shouldn't be! This is a flaw of direct evaluation:
> - Ignores information about state connections
> - Each state learned separately
> - Doesn't use knowledge that $B$ and $E$ have same successor
>
> **Resolution:** With enough episodes, values converge to truth, but this takes much longer than necessary.

> [!note]+ Related Concepts
> - **[[Passive Reinforcement Learning]]**: Framework for direct evaluation
> - **[[Temporal Difference Learning]]**: Improved alternative algorithm
> - **[[Model-Free Learning]]**: General approach category
> - **[[Reinforcement Learning]]**: Broader context
> - **[[State]]**: Values being estimated
> - **[[Policy]]**: Fixed policy being evaluated
