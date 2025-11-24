---
title: Model-Based Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Model-Based Learning** is a [[Reinforcement Learning]] approach that estimates the transition and reward functions from exploration samples, then uses these estimates to solve the MDP with standard planning algorithms.

## Strategy

> [!abstract]+ Core Approach
> **Transition function approximation:**
> - Generate approximation $\hat{T}(s, a, s')$ by keeping counts
> - Count arrivals in each state $s'$ after entering Q-state $(s, a)$
> - **Normalize** counts to generate probabilities:
>   $$\hat{T}(s, a, s') = \frac{\#(s, a, s')}{\#(s, a)}$$
>
> **Reward function approximation:**
> - Directly record rewards observed for each $(s, a, s')$ tuple
> - $\hat{R}(s, a, s')$ = observed reward value
>
> **Key insight:** Normalization scales counts to sum to one, allowing interpretation as probabilities

## Example

> [!example]+ Model-Based Learning Walkthrough
> Consider the following [[Markov Decision Process|MDP]] with states $S = \{ A, B, C, D, E, x \}$, where $x$ is the terminal state, and discount factor $\gamma = 1$:
>
> ![[Pasted image 20251124121932.png]]
>
> Agent explores for four episodes under policy $\pi_{\text{explore}}$ (directional triangle = motion direction, blue square = `exit` action):
>
> ![[Pasted image 20251124122024.png]]
>
> **Collected samples:** 12 total (3 per episode)
>
> **Count table:**
>
> | $s$ |      $a$       | $s'$ | $\text{count}$ |
> | :-: | :------------: | :--: | :------------: |
> | $A$ | $\text{exit}$  | $x$  |       1        |
> | $B$ | $\text{east}$  | $C$  |       2        |
> | $C$ | $\text{east}$  | $A$  |       1        |
> | $C$ | $\text{east}$  | $D$  |       3        |
> | $D$ | $\text{exit}$  | $x$  |       3        |
> | $E$ | $\text{south}$ | $C$  |       2        |
>
> **Estimated transition function:** $\hat{T}(s, a, s')$
>
> Recall $T(s, a, s') = P(s' \vert a, s)$. Estimate by dividing counts:
>
> $$\hat{T}(A, \text{exit}, x) = \frac{\#(A, \text{exit}, x)}{\#(A, \text{exit})} = \frac{1}{1} = 1$$
> $$\hat{T}(B, \text{east}, C) = \frac{\#(B, \text{east}, C)}{\#(B, \text{east})} = \frac{2}{2} = 1$$
> $$\hat{T}(C, \text{east}, A) = \frac{\#(C, \text{east}, A)}{\#(C, \text{east})} = \frac{1}{4} = 0.25$$
> $$\hat{T}(C, \text{east}, D) = \frac{\#(C, \text{east}, D)}{\#(C, \text{east})} = \frac{3}{4} = 0.75$$
> $$\hat{T}(D, \text{exit}, x) = \frac{\#(D, \text{exit}, x)}{\#(D, \text{exit})} = \frac{3}{3} = 1$$
> $$\hat{T}(E, \text{north}, C) = \frac{\#(E, \text{north}, C)}{\#(E, \text{north})} = \frac{2}{2} = 1$$
>
> **Estimated reward function:** $\hat{R}(s, a, s')$
>
> $$\hat{R}(A, \text{exit}, x) = -10$$
> $$\hat{R}(B, \text{east}, C) = -1$$
> $$\hat{R}(C, \text{east}, A) = -1$$
> $$\hat{R}(C, \text{east}, D) = -1$$
> $$\hat{R}(D, \text{exit}, x) = +10$$
> $$\hat{R}(E, \text{north}, C) = -1$$

## Convergence

> [!abstract]+ Law of Large Numbers
> As we collect more samples through additional episodes:
> - Models $\hat{T}$ and $\hat{R}$ improve
> - $\hat{T}$ converges towards true $T$
> - $\hat{R}$ acquires knowledge of previously undiscovered rewards
> - New $(s, a, s')$ tuples discovered
>
> **Exploitation:**
> - End training when sufficient samples collected
> - Generate policy $\pi_{\text{exploit}}$ using [[Value Iteration]] or [[Policy Iteration]]
> - Use estimated models $\hat{T}$ and $\hat{R}$ for planning
> - Deploy $\pi_{\text{exploit}}$ for reward maximization

## Properties

> [!success]+ Advantages
> - Simple and intuitive approach
> - Remarkably effective in practice
> - Uses only counting and normalization
> - Generates complete model of environment

> [!fail]+ Disadvantages
> - Expensive to maintain counts for every $(s, a, s')$ tuple
> - Memory overhead can be significant
> - Requires storing all transition counts

> [!note]+ Next Steps
> [[Model-Free Learning]] develops methods to bypass maintaining counts altogether and avoid the memory overhead required by model-based learning.

> [!note]+ Related Concepts
> - **[[Reinforcement Learning]]**: General framework
> - **[[Model-Free Learning]]**: Alternative RL approach
> - **[[Markov Decision Process]]**: Problem being solved
> - **[[Value Iteration]]**: Used to solve estimated MDP
> - **[[Policy Iteration]]**: Alternative solver for estimated MDP
> - **[[Q-State]]**: Q-states $(s,a)$ for which counts are maintained
