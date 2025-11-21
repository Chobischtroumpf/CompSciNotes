---
title: Adversarial Search
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Adversarial Search** is search in competitive environments where one player maximizes the result while another player minimizes it (for deterministic, zero-sum games).

## Comparison to Single-Agent Search

> [!abstract]+ Single-Agent vs Adversarial Trees
> | Single-Agent Tree | Adversarial Game Tree |
> |:-----------------:|:---------------------:|
> | ![[97e43d0d0a27ec42fc480215bf815edf.png]] | ![[fa89adef29bdfbaf2a06cd9973de4294.png]] |

## Value of a State

> [!abstract]+ Single-Agent Value
> **Definition:** The best achievable outcome (utility) from that state
>
> **Non-terminal state:**
> $$V(s) = \max_{s' \in \text{successors}(s)} V(s')$$
>
> **Terminal state:** $V(s)$ is known

> [!abstract]+ Adversarial Value
> **Max nodes** (under agent's control):
> $$V(s) = \max_{s' \in \text{successors}(s)} V(s')$$
>
> ![[00fab96c30beec80d7c51c497ee65303.png]]
>
> **Min nodes** (under opponent's control):
> $$V(s) = \min_{s' \in \text{successors}(s)} V(s')$$
>
> ![[0f7cb941f06d4710dee2bbc582b43bd0.png]]

## Complete Example

> [!example]+ Full Adversarial Tree
> ![[590967387d97b84693d287d56ec71a97.png]]
>
> **Terminal states:** $V(s)$ is known and propagates up the tree

> [!note]+ Related Concepts
> - **[[Game]]**: Environment being searched
> - **[[Minimax Search]]**: Complete algorithm for adversarial search
> - **[[Alpha-Beta Pruning]]**: Optimization for minimax
> - **[[Expectimax Search]]**: Extension to stochastic games
