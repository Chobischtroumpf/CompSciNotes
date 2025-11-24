---
title: Evaluation Function
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> An **Evaluation Function** scores non-terminal states in depth-limited search, providing an estimate of the true utility without exploring to terminal states.

## Purpose

> [!abstract]+ Why Evaluation Functions?
> **Problem:** Cannot always search to terminal states
> - Games too deep (e.g., chess, go)
> - Computational constraints
>
> **Solution:** Evaluate intermediate states
> - Estimate how good a position is
> - Use as substitute for true utility in depth-limited search

## Common Formulations

> [!abstract]+ Linear Evaluation Functions
> **Typical form:** Weighted linear sum of features
>
> $$\text{EVAL}(s) = w_1 f_1(s) + w_2 f_2(s) + \cdots + w_n f_n(s)$$
>
> where:
> - $f_i(s)$ are features of state $s$
> - $w_i$ are weights indicating feature importance

> [!abstract]+ Advanced Formulations
> **Non-linear functions:**
> - More complex combinations of features
> - Often trained via self-play reinforcement learning
> - Examples: Deep neural networks (AlphaGo, AlphaZero)

## Example Application

> [!example]+ Chess Evaluation
> ![[Pasted image 20251111134038.png]]
> *Chess positions evaluated in minimax tree with depth limit*
>
> **Typical chess features:**
> - Material count (piece values)
> - Piece mobility
> - King safety
> - Pawn structure
> - Control of center

## Properties

> [!abstract]+ Evaluation Function Characteristics
> **Imperfect approximations:**
> - Evaluation functions are always imperfect
> - Cannot perfectly predict game outcomes
>
> **Depth vs accuracy trade-off:**
> - **Deeper search:** Better play (compensates for less accurate evaluation)
> - **Shallower search with better evaluation:** May achieve similar play quality
> - Generally: depth matters more than evaluation accuracy
>
> **Quality indicators:**
> - Should be fast to compute
> - Should correlate with actual winning chances
> - Should handle all possible game states

> [!note]+ Related Concepts
> - **[[Expectimax Search]]**: Uses evaluation functions for depth-limited search
> - **[[Minimax Search]]**: Also uses evaluation functions when depth-limited
> - **[[Game]]**: Domain being evaluated
> - **[[Adversarial Search]]**: Framework using evaluations
