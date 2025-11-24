---
title: Temporal Difference Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Temporal Difference Learning (TD Learning)** is a [[Passive Reinforcement Learning]] algorithm that updates state value estimates incrementally after each transition using an exponential moving average.

## Core Idea

> [!abstract]+ Learning from Every Experience
> **Key principle:** Learn from every experience, not just at episode end
>
> ![[Pasted image 20251124142910.png]]
>
> **Contrast with [[Direct Evaluation]]:**
> - Direct evaluation: Accumulates rewards, updates at episode end
> - TD learning: Updates immediately after each transition
> - Uses iteratively improved estimates in future updates

## Motivation

> [!abstract]+ Connection to Policy Evaluation
> In standard policy evaluation with known $T$ and $R$:
>
> $$V^\pi(s) = \sum_{s'} T(s, \pi(s), s') \left[ R(s, \pi(s), s') + \gamma V^\pi(s') \right]$$
>
> Each equation equates a state's value to the weighted average of:
> - Immediate rewards received
> - Discounted values of successor states
>
> **TD learning question:** How can we compute this weighted average without knowing the weights (transition probabilities)?
>
> **TD learning answer:** Use an exponential moving average!

## Algorithm

> [!abstract]+ TD Learning Update Rule
> **Initialization:** $\forall s, V^\pi(s) = 0$
>
> **At each timestep:**
> 1. Agent in state $s$ takes action $\pi(s)$
> 2. Transitions to state $s'$
> 3. Receives reward $R(s, \pi(s), s')$
> 4. Compute **sample value:**
>
> $$\text{sample} = R(s, \pi(s), s') + \gamma V^\pi(s')$$
>
> 5. Update estimate using **exponential moving average:**
>
> $$V^\pi(s) \leftarrow (1 - \alpha) V^\pi(s) + \alpha \cdot \text{sample}$$
>
> where $\alpha$ is the **learning rate** with $0 \leq \alpha \leq 1$

## Learning Rate

> [!abstract]+ Role of $\alpha$
> **Learning rate parameter:**
> - Controls weight assigned to existing estimate: $(1 - \alpha)$
> - Controls weight assigned to new sample: $\alpha$
>
> **Typical strategy:**
> - Start with $\alpha = 1$ (first sample becomes initial estimate)
> - Gradually decrease $\alpha$ towards 0
> - Eventually: New samples contribute less (model stabilizes)

## Mathematical Analysis

> [!abstract]+ Exponential Moving Average Expansion
> Define $V^\pi_k(s)$ as the estimate after the $k$-th update and $\text{sample}_k$ as the $k$-th sample.
>
> **Recursive form:**
> $$V^\pi_k(s) \leftarrow (1 - \alpha) V^\pi_{k - 1}(s) + \alpha \cdot \text{sample}_k$$
>
> **Expanded form:**
> $$V^\pi_k(s) \leftarrow \alpha \cdot \left[ (1 - \alpha)^{k - 1} \cdot \text{sample}_1 + \cdots + (1 - \alpha) \cdot \text{sample}_{k - 1} + \text{sample}_k \right]$$
>
> **Key insight:** Since $0 \leq \alpha \leq 1$, as we raise $(1 - \alpha)$ to larger powers, it approaches 0.
>
> **Result:** Older samples receive exponentially less weight, which is desirable because older samples used worse estimates of $V^\pi(s')$.

## Example

> [!example]+ TD Learning Walkthrough
> ![[Pasted image 20251124143101.png]]
>
> **Setup:** Agent observes transitions $B \to C \to D$ with learning rate $\alpha = 0.5$, $\gamma = 1$
>
> **After transition $B \to C$ with reward $-2$:**
> - Old: $V(B) = 0$
> - Sample: $\text{sample} = -2 + 1 \times 0 = -2$
> - Update: $V(B) \leftarrow (1 - 0.5) \times 0 + 0.5 \times (-2) = -1$
>
> **After transition $C \to D$ with reward $-2$:**
> - Old: $V(C) = 0$
> - Sample: $\text{sample} = -2 + 1 \times 8 = 6$
> - Update: $V(C) \leftarrow (1 - 0.5) \times 0 + 0.5 \times 6 = 3$

## Convergence

> [!abstract]+ Convergence Guarantee
> With appropriate learning rate decay, TD learning converges to the true state values $V^\pi(s)$ for all states.
>
> **Requirements:**
> - Visit all states infinitely often
> - Decrease $\alpha$ appropriately (e.g., $\alpha_k = \frac{1}{k}$)

> [!note]+ Related Concepts
> - **[[Passive Reinforcement Learning]]**: Framework for TD learning
> - **[[Direct Evaluation]]**: Simpler but slower alternative
> - **[[Model-Free Learning]]**: General approach category
> - **[[Reinforcement Learning]]**: Broader context
> - **[[State]]**: Values being estimated
> - **[[Policy]]**: Fixed policy being evaluated
> - **[[Q-Learning]]**: Active learning extension using similar ideas
