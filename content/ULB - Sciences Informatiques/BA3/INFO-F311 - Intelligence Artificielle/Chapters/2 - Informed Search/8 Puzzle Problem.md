---
title: 8 Puzzle Problem
authors: Alessandro Dorigo
tags:
  -
---

> [!example]+ Example: 8 Puzzle - Problem Setup **The 8-Puzzle:**
>
> - **Start State:** Tiles arranged as [7,2,4 / 5,_,6 / 8,3,1]
> - **Goal State:** Tiles arranged as [_,1,2 / 3,4,5 / 6,7,8]
> - **Actions:** Slide tiles into the empty space
>
> **Key Questions:**
>
> - What are the states?
> - How many states?
> - What are the actions?
> - What are the successors from the start state?
> - What are the step costs?
> - **What are possible heuristics?**

> [!note]+ 8 Puzzle I - Misplaced Tiles Heuristic
>
> **Heuristic: Number of tiles misplaced**
>
> **Why is it admissible?**
>
> - Each misplaced tile must be moved at least once to reach the goal
> - The heuristic counts minimum moves needed (one per misplaced tile)
> - Actual solution may require more moves (tiles blocking each other)
> - Therefore, it never overestimates
>
> **For the start state:** $h(\text{start}) = 8$ (all tiles except blank are misplaced)
>
> **Performance comparison:**
>
> |Algorithm|4 steps|8 steps|12 steps|
> |---|---|---|---|
> |UCS|112|6,300|3.6 × 10⁶|
> |A* TILES|13|39|227|
>
> **Result:** A* with misplaced tiles heuristic dramatically reduces nodes expanded compared to UCS!
>
> _Statistics from Andrew Moore_

> [!note] 8 Puzzle II - Manhattan Distance Heuristic
>
> **Relaxed problem:** What if we had an easier 8-puzzle where any tile could slide any direction at any time, ignoring other tiles?
>
> **Heuristic: Total Manhattan distance**
>
> - Sum of Manhattan distances for each tile to its goal position
> - Manhattan distance = |x₁ - x₂| + |y₁ - y₂|
>
> **Why is it admissible?**
>
> - In the relaxed problem (tiles can pass through each other), Manhattan distance is the optimal solution
> - The actual problem has more constraints, so actual cost ≥ Manhattan distance
>
> **For the start state:** $h(\text{start}) = 3 + 1 + 2 + ... = 18$
>
> **Performance comparison:**
>
> |Algorithm|4 steps|8 steps|12 steps|
> |---|---|---|---|
> |A* TILES|13|39|227|
> |A* MANHATTAN|12|25|73|
>
> **Result:** Manhattan distance is better than misplaced tiles! It's a more informed heuristic.

> [!question] 8 Puzzle III - Using Actual Cost as Heuristic? **How about using the actual cost as a heuristic?**
>
> **Three questions:**
>
> - **Would it be admissible?** Yes! (actual cost = true cost, never overestimates)
> - **Would we save on nodes expanded?** Yes, dramatically!
> - **What's wrong with it?** It's computationally infeasible to compute!
>
> **The problem:** Computing the actual cost requires solving the problem first, which defeats the purpose of using a heuristic.

> [!tip] A* Trade-off: Quality vs Computation __With A_: a trade-off between quality of estimate and work per node_*
>
> - As heuristics get closer to the true cost, you will expand fewer nodes
> - BUT you usually do more work per node to compute the heuristic itself
>
> __The art of A_:_* Finding heuristics that are:
>
> 1. Admissible (guarantee optimality)
> 2. Informative (close to true cost)
> 3. Cheap to compute (don't waste time calculating)

> [!abstract] Combining Heuristics **When you have multiple heuristics, you can combine them!**
>
> **Trivial heuristics:**
>
> - The zero heuristic reduces A* to UCS
> - The exact heuristic already solves the problem
>
> **Dominance:** $h_1 ≥ h_2$ if $∀n ; h_1(n) ≥ h_2(n)$
>
> - Roughly speaking, larger is better as long as both are admissible
> - The zero heuristic is pretty bad (what does A* do with h=0?)
> - The exact heuristic is pretty good, but usually too expensive!
>
> **What if we have two heuristics, neither dominates the other?**
>
> - Form a new heuristic by taking the max of both:
>
> $$h(n) = \max(h_1(n), h_2(n))$$
>
> - **Max of admissible heuristics is admissible and dominates both!**
> - This combined heuristic is always at least as good as either individual heuristic
> - It provides the best of both worlds without losing admissibility
