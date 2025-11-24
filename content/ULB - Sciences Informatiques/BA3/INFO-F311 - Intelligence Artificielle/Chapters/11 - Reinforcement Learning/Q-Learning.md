---
title: Q-Learning
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Q-Learning** is a revolutionary [[Model-Free Learning]] algorithm that learns optimal Q-values directly without requiring transition or reward models, enabling **off-policy learning** of the optimal policy.

## Motivation

> [!abstract]+ Why Q-Learning?
> **Problem with previous methods:**
> - [[Direct Evaluation]] and [[Temporal Difference Learning]] learn $V^\pi(s)$
> - To find optimal policy, we need Q-values: $Q^*(s,a)$
> - Computing Q-values from V-values requires $T$ and $R$:
>
> $$Q^*(s, a) = \sum_{s'} T(s, a, s') \left[ R(s, a, s') + \gamma V^*(s') \right]$$
>
> **Solution:** Learn Q-values directly, bypassing need for models!

## Q-Value Iteration

> [!abstract]+ Foundation: Value Iteration for Q-Values
> Standard [[Value Iteration]] for states:
> $$V_{k+1}(s) \leftarrow \max_a \sum_{s'} T(s, a, s') \left[ R(s, a, s') + \gamma V_k(s') \right]$$
>
> **Q-value iteration** (with model):
> $$Q_{k + 1}(s, a) \leftarrow \sum_{s'} T(s, a, s') \left[ R(s, a, s') + \gamma \max_{a'} Q_k(s', a') \right]$$
>
> **Key difference:** Max operator moved after transition
> - States: Select action before transitioning
> - Q-states: Transition before selecting new action

## Sample-Based Q-Value Updates

> [!abstract]+ Q-Learning Update Rule
> **Without model, use samples:**
>
> 1. Agent in state $s$ takes action $a$
> 2. Transitions to state $s'$
> 3. Receives reward $R(s, a, s')$
> 4. Compute **Q-value sample:**
>
> $$\text{sample} = R(s, a, s') + \gamma \max_{a'} Q(s', a')$$
>
> 5. Update Q-value using exponential moving average:
>
> $$Q(s, a) \leftarrow (1 - \alpha) Q(s, a) + \alpha \cdot \text{sample}$$
>
> where $\alpha$ is the learning rate

## Derivation Parallel to TD Learning

> [!abstract]+ Similar to Temporal Difference Learning
> **[[Temporal Difference Learning]] for V-values:**
> - Sample: $\text{sample} = R(s, \pi(s), s') + \gamma V^\pi(s')$
> - Update: $V^\pi(s) \leftarrow (1 - \alpha) V^\pi(s) + \alpha \cdot \text{sample}$
>
> **Q-Learning for Q-values:**
> - Sample: $\text{sample} = R(s, a, s') + \gamma \max_{a'} Q(s', a')$
> - Update: $Q(s, a) \leftarrow (1 - \alpha) Q(s, a) + \alpha \cdot \text{sample}$
>
> **Key difference:** Max over next actions instead of following fixed policy

## Off-Policy Learning

> [!abstract]+ Revolutionary Property
> **Off-policy learning:** Q-learning learns the optimal policy even while taking suboptimal or random actions.
>
> **Comparison:**
> - **On-policy learning** ([[Direct Evaluation]], [[Temporal Difference Learning]]):
>   - Learn values of the policy being followed
>   - Evaluation of specific policy
>
> - **Off-policy learning** (Q-Learning):
>   - Learn optimal Q-values regardless of actions taken
>   - Can explore randomly and still converge to $Q^*$
>   - Separates behavior from learning
>
> **Why it works:**
> - Update uses $\max_{a'} Q(s', a')$ (optimal choice)
> - Not constrained by action actually taken
> - Learns what would be best, not what was done

## Convergence Guarantee

> [!abstract]+ Theoretical Result
> **Theorem:** As long as we:
> - Spend enough time exploring (visit all state-action pairs infinitely)
> - Decrease learning rate $\alpha$ appropriately
>
> Then Q-learning converges to optimal Q-values $Q^*(s,a)$ for every state-action pair.
>
> **Result:** Optimal policy directly available via:
> $$\pi^*(s) = \arg\max_a Q^*(s,a)$$

## Example

> [!example]+ Q-Learning Update
> **Scenario:**
> - Current state: $s$
> - Take action: $a$
> - Arrive in state: $s'$
> - Receive reward: $r = +5$
> - Current estimates: $Q(s,a) = 10$, $\max_{a'} Q(s', a') = 8$
> - Discount: $\gamma = 0.9$
> - Learning rate: $\alpha = 0.5$
>
> **Update calculation:**
> 1. Sample: $\text{sample} = 5 + 0.9 \times 8 = 12.2$
> 2. Update: $Q(s,a) \leftarrow (1 - 0.5) \times 10 + 0.5 \times 12.2 = 11.1$
>
> **Result:** $Q(s,a)$ increased from 10 to 11.1

## Properties

> [!success]+ Revolutionary Advantages
> - **Model-free:** No need for $T$ or $R$
> - **Off-policy:** Learns optimal policy from any behavior
> - **Direct:** Learns Q-values directly, not via V-values
> - **Practical:** Widely applicable to real-world problems
> - **Optimal:** Converges to optimal policy with sufficient exploration

> [!note]+ Related Concepts
> - **[[Active Reinforcement Learning]]**: Framework for Q-learning
> - **[[Model-Free Learning]]**: General approach category
> - **[[Reinforcement Learning]]**: Broader context
> - **[[Q-State]]**: What Q-learning learns values for
> - **[[Policy]]**: Optimal policy derived from Q-values
> - **[[Temporal Difference Learning]]**: Similar update mechanism
> - **[[Value Iteration]]**: Q-value iteration is sample-based version
> - **[[Markov Decision Process]]**: Problem being solved
