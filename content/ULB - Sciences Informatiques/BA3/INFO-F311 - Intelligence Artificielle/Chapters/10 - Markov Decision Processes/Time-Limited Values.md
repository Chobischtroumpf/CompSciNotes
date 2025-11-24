---
title: Time-Limited Values
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Time-Limited Values** $V_k(s)$ represent the optimal expected utility from state $s$ if the agent has exactly $k$ timesteps remaining before termination.

## Key Idea

> [!abstract]+ Finite Horizon Interpretation
> **$V_k(s)$ represents:**
> - Optimal value of state $s$ with $k$ timesteps left
> - Expected utility assuming game ends after $k$ more steps
> - Building block for computing infinite-horizon values

## Computation Strategy

> [!abstract]+ Bottom-Up Computation
> **Approach:** Compute values from shorter to longer time horizons
>
> **Sequence:**
> 1. $V_0(s)$: No time left (base case)
> 2. $V_1(s)$: One timestep remaining
> 3. $V_2(s)$: Two timesteps remaining
> 4. $V_3(s)$: Three timesteps remaining
> 5. Continue until convergence to $V^*(s)$
>
> ![[Pasted image 20251121153420.png]]
>
> **Example computation order:**
> - Start at root: $V_4(s)$
> - Then: $V_3(s)$, $V_2(s)$, $V_1(s)$, $V_0(s)$

## Base Case

> [!abstract]+ Zero Timesteps
> **$V_0(s) = 0$ for all states $s$**
>
> **Reasoning:**
> - No timesteps left means no actions can be taken
> - No actions means no rewards can be collected
> - Therefore, expected utility is zero

## Recursive Relationship

> [!abstract]+ Time-Limited Bellman Equation
> $$V_{k+1}(s) = \max_a \sum_{s'} T(s, a, s') [R(s, a, s') + \gamma V_k(s')]$$
>
> **Interpretation:**
> - To compute $V_{k+1}(s)$, use values $V_k(s')$ from one timestep shorter
> - Each iteration adds one more timestep of lookahead
> - Immediate reward plus discounted continuation value

## Convergence to Optimal Values

> [!abstract]+ Relationship to Value Iteration
> As $k \to \infty$, time-limited values converge to optimal values:
> $$\lim_{k \to \infty} V_k(s) = V^*(s)$$
>
> **Connection to [[Value Iteration]]:**
> - Value iteration computes $V_0, V_1, V_2, ...$ in sequence
> - Each $V_k$ is the time-limited value for $k$ timesteps
> - Iteration continues until $V_k \approx V_{k+1}$ (convergence)

## Example Interpretation

> [!example]+ Understanding $V_k$
> Consider a state $s$ in a game:
> - $V_3(s)$: "What's the best I can do from here if the game ends in exactly 3 moves?"
> - $V_5(s)$: "What's the best I can do from here if the game ends in exactly 5 moves?"
> - $V^*(s)$: "What's the best I can do from here with unlimited time?"
>
> As $k$ increases, $V_k(s)$ provides better approximations to $V^*(s)$

> [!note]+ Related Concepts
> - **[[Value Iteration]]**: Uses time-limited values in computation
> - **[[State]]**: $V^*(s)$ is the limit of $V_k(s)$
> - **[[Markov Decision Process]]**: Framework being solved
> - **[[Discount Factor]]**: Ensures convergence of time-limited values
