---
title: Monte Carlo Tree Search
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Monte Carlo Tree Search (MCTS)** is an algorithm for large branching factor games that uses random simulations (rollouts) and selective search to make decisions without explicit evaluation functions.

## Motivation

> [!abstract]+ When to Use MCTS
> **Problem:** Games with extremely large branching factors
> - Example: Go has branching factor > 300
> - Traditional minimax becomes impractical
>
> **Solution:** MCTS combines two key ideas:
> 1. **Evaluation by rollouts:** Play many times using a policy (e.g., random) and count wins/losses
> 2. **Selective search:** Explore promising parts of the tree without fixed horizon constraints

## Basic MCTS (Version 1.0)

> [!example]+ Simple Rollout Approach
> ![[74cd4785c8b993ffe58a6505ed9978c5.png]]
>
> **Strategy:**
> - Consider three actions (left, middle, right)
> - Simulate each action 100 times
> - Record win percentage for each
> - Choose action with highest win rate
>
> **Example results:**
> - Left: 57/100 wins (57%)
> - Middle: 39/100 wins (39%)
> - Right: 65/100 wins (65%)
> - **Decision:** Choose right action

## Adaptive Allocation (Version 0.9)

> [!abstract]+ Smart Simulation Distribution
> **Insight:** Don't waste simulations on clearly bad actions
>
> ![[8c874bd89ac9d9e2f6f48b15bce21825.png]]
>
> **Strategy:**
> - Start with few simulations per action
> - Identify poor-performing actions early
> - Reallocate remaining computational budget to promising actions
> - Example: After 10 simulations each, allocate remaining 90 to left and right only

## Handling Uncertainty

> [!abstract]+ Variance Consideration
> **Problem:** Similar win percentages with different simulation counts
>
> ![[34d4b9cc271fcf7577a5cb89fbcf7764.png]]
>
> **Key insight:**
> - Action with fewer simulations has higher variance
> - Less confident about true win percentage
> - May need more simulations to be certain
>
> **Trade-off:**
> - **Exploitation:** Choose currently best action
> - **Exploration:** Test uncertain actions more

## UCB Algorithm

> [!abstract]+ Upper Confidence Bound
> **UCB1 criterion** balances "promising" vs "uncertain" actions:
>
> $$\text{UCB1}(n) = \frac{U(n)}{N(n)} + C \times \sqrt{\frac{\log N(\text{Parent}(n))}{N(n)}}$$
>
> where:
> - $N(n)$ = total number of rollouts from node $n$
> - $U(n)$ = total number of wins for Player(Parent($n$))
> - $C$ = exploration parameter (user-specified)
>
> **Components:**
> - **First term:** $\frac{U(n)}{N(n)}$ captures how promising the node is (exploitation)
> - **Second term:** $C \times \sqrt{\frac{\log N(\text{Parent}(n))}{N(n)}}$ captures uncertainty (exploration)
>
> **Parameter $C$:**
> - Balances exploration vs exploitation
> - Depends on application and search stage
> - Later stages: typically explore less, exploit more

## MCTS V2.0: UCT Algorithm

> [!abstract]+ Upper Confidence bounds applied to Trees
> **UCT** uses the UCB criterion in tree search problems.
>
> **Three-step iteration:**
> 1. **Selection:** Use UCB criterion to move down tree layers from root until reaching an unexpanded leaf node
> 2. **Expansion & Simulation:** Add a new child to that leaf, run a rollout from the child to determine wins
> 3. **Backpropagation:** Update win counts from child back up to root node
>
> **Final decision:**
> - After sufficient iterations, choose action leading to child with highest $N$
> - High $N$ indicates both promising and well-explored action

## Properties

> [!abstract]+ UCT Characteristics
> **Convergence:**
> - As $N \to \infty$, UCT approaches minimax behavior
> - Inherently explores more promising children more often
>
> **Advantages:**
> - No evaluation function needed
> - Handles large branching factors well
> - Anytime algorithm (improves with more computation)
> - Asymmetric tree growth (focuses on promising variations)
>
> **Applications:**
> - Go (achieved superhuman performance)
> - General game playing
> - Real-time strategy games
> - Planning under uncertainty

> [!note]+ Related Concepts
> - **[[Game]]**: Environment being searched
> - **[[Adversarial Search]]**: General framework
> - **[[Minimax Search]]**: Traditional approach MCTS can approximate
> - **[[Expectimax Search]]**: Handles uncertainty differently
