---
title: 8 Puzzle Problem
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> The **8-Puzzle** is a classic search problem consisting of a $3 \times 3$ grid with $8$ numbered tiles and one blank space, where the goal is to reach a target configuration by sliding tiles into the blank space.

## Problem Specification

> [!example]+ Problem Setup
> **The 8-Puzzle:**
> - **Start State:** Tiles arranged as $[7,2,4 / 5,\_,6 / 8,3,1]$
> - **Goal State:** Tiles arranged as $[\_,1,2 / 3,4,5 / 6,7,8]$
> - **Actions:** Slide tiles into the empty space (up, down, left, right)
> - **Step costs:** Uniform cost of 1 per move
>
> **Key Questions:**
> - What are the states? (Tile configurations)
> - How many states? ($9!/2 = 181,440$ reachable states)
> - What are the actions? (Slide tile into blank)
> - What are the successors from start state? (2-4 depending on blank position)

## Heuristic I: Misplaced Tiles

> [!abstract]+ Number of Tiles Misplaced
> **Heuristic:** Count the number of tiles that are not in their goal position
>
> **Why is it admissible?**
> - Each misplaced tile must be moved at least once to reach the goal
> - The heuristic counts minimum moves needed (one per misplaced tile)
> - Actual solution may require more moves (tiles blocking each other)
> - Therefore, it never overestimates
>
> **For the example start state:** $h(\text{start}) = 8$ (all tiles except blank are misplaced)

> [!success]+ Performance Comparison
> |Algorithm|4 steps|8 steps|12 steps|
> |---|---|---|---|
> |UCS|$112$|$6,300$|$3.6 \times 10^6$|
> |A* TILES|$13$|$39$|$227$|
>
> **Result:** [[A*]] with misplaced tiles heuristic dramatically reduces nodes expanded compared to [[Uniform Cost Search|UCS]]!
>
> *Statistics from Andrew Moore*

## Heuristic II: Manhattan Distance

> [!abstract]+ Total Manhattan Distance
> **Relaxed problem:** What if we had an easier 8-puzzle where any tile could slide any direction at any time, ignoring other tiles?
>
> **Heuristic:** Sum of Manhattan distances for each tile to its goal position
> - Manhattan distance = $|x_1 - x_2| + |y_1 - y_2|$
>
> **Why is it admissible?**
> - In the relaxed problem (tiles can pass through each other), Manhattan distance is the optimal solution
> - The actual problem has more constraints, so actual cost ≥ Manhattan distance
>
> **For the example start state:** $h(\text{start}) = 3 + 1 + 2 + ... = 18$

> [!success]+ Performance Comparison
> |Algorithm|4 steps|8 steps|12 steps|
> |---|---|---|---|
> |A* TILES|$13$|$39$|$227$|
> |A* MANHATTAN|$12$|$25$|$73$|
>
> **Result:** Manhattan distance is better than misplaced tiles! It's a more informed heuristic.

## Heuristic III: Actual Cost

> [!question]+ Using the Actual Cost as Heuristic?
> **How about using the actual cost as a heuristic?**
>
> **Three questions:**
> - **Would it be admissible?** Yes! (actual cost = true cost, never overestimates)
> - **Would we save on nodes expanded?** Yes, dramatically!
> - **What's wrong with it?** It's computationally infeasible to compute!
>
> **The problem:** Computing the actual cost requires solving the problem first, which defeats the purpose of using a heuristic.

## Comparing Heuristics

> [!abstract]+ Heuristic Dominance
> **For the 8-Puzzle:**
> - Manhattan distance dominates misplaced tiles
> - $h_{\text{Manhattan}}(n) ≥ h_{\text{tiles}}(n)$ for all $n$
> - Both are admissible, but Manhattan is more informed
>
> **Performance hierarchy:**
> 1. Actual cost (infeasible to compute)
> 2. Manhattan distance (best practical choice)
> 3. Misplaced tiles (simpler but less informed)
> 4. Zero heuristic (reduces to UCS)

> [!tip]+ Combining Multiple Heuristics
> If you have multiple heuristics for the 8-Puzzle:
> $$h(n) = \max(h_{\text{Manhattan}}(n), h_{\text{tiles}}(n), h_{\text{other}}(n))$$
>
> The maximum of admissible heuristics remains admissible and dominates all components.

> [!note]+ Related Concepts
> - **[[A*]]**: Optimal search algorithm using heuristics
> - **[[Search Heuristic]]**: General concept of estimation functions
> - **[[Admissibility]]**: Property ensuring optimality
> - **[[Uniform Cost Search]]**: Uninformed baseline for comparison
