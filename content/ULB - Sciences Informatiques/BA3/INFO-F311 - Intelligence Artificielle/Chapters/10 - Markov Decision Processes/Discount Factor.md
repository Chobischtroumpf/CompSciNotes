---
title: Discount Factor
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **Discount Factor** $\gamma$ models the exponential decay in the value of rewards over time, where $0 < \gamma < 1$.

## Purpose

> [!abstract]+ Why Discount?
> **Reasons for discounting:**
> - Rewards now are better than rewards later
> - Models uncertainty about the future
> - Can be interpreted as $(1-\gamma)$ probability of episode ending at each step
> - Helps algorithms converge mathematically

## Mechanics

> [!abstract]+ How Discounting Works
> **With discount factor $\gamma$:**
> - Reward at timestep $t$ is multiplied by $\gamma^t$
> - Each time we descend a level in the tree, multiply by $\gamma$ once
>
> **Effect:**
> - Immediate rewards: Full value
> - One step away: Worth $\gamma$ times as much
> - Two steps away: Worth $\gamma^2$ times as much
> - $k$ steps away: Worth $\gamma^k$ times as much

## Utility Functions

> [!abstract]+ Additive vs Discounted Utility
> **Additive utility** (no discounting):
> $$U([s_0, a_0, s_1, a_1, s_2, ...]) = R(s_0, a_0, s_1) + R(s_1, a_1, s_2) + R(s_2, a_2, s_3) + ...$$
>
> **Discounted utility** (with factor $\gamma$):
> $$U([s_0, a_0, s_1, a_1, s_2, ...]) = R(s_0, a_0, s_1) + \gamma R(s_1, a_1, s_2) + \gamma^2 R(s_2, a_2, s_3) + ...$$

## Convergence Guarantee

> [!abstract]+ Proof of Finite Value
> For $0 < \gamma < 1$, discounted utility is guaranteed to be finite:
>
> $$U([s_0, s_1, s_2, ...]) = \sum_{t=0}^{\infty} \gamma^t R(s_t, a_t, s_{t+1})$$
>
> $$\leq \sum_{t=0}^{\infty} \gamma^t R_{\max} = \frac{R_{\max}}{1 - \gamma}$$
>
> where $R_{\max}$ is the maximum reward attainable at any timestep.
>
> **Key insight:** Geometric series converges when $|\gamma| < 1$

## Stationary Preferences

> [!abstract]+ Preference Theorem
> If we assume stationary preferences:
>
> $$[a_1, a_2, ...] \succ [b_1, b_2, ...]$$
> $$\Updownarrow$$
> $$[r, a_1, a_2, ...] \succ [r, b_1, b_2, ...]$$
>
> Then we can define utilities using only two formulations:
> - Additive utility
> - Discounted utility

## Choosing $\gamma$

> [!abstract]+ Discount Factor Selection
> **Typical range:** $0 < \gamma < 1$
>
> **Effects of different values:**
> - $\gamma \to 0$: Only immediate rewards matter (myopic)
> - $\gamma \to 1$: Future rewards nearly as important as immediate (far-sighted)
> - $\gamma = 1$: No discounting (requires finite horizon or terminal states)
>
> **Why not $\gamma \leq 0$?**
> - Negative $\gamma$ causes reward signs to flip-flop at alternating timesteps
> - Not meaningful in most real-world situations

> [!note]+ Related Concepts
> - **[[Markov Decision Process]]**: Uses discount factors in utility computation
> - **[[State]]**: Value includes discounted future rewards
> - **[[Q-State]]**: Q-values include discount factor
> - **[[Value Iteration]]**: Algorithm that applies discounting
