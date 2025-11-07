---
title: Graph Search
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Graph Search** is an optimization of tree search that avoids redundant exploration by tracking previously expanded states, preventing the algorithm from re-expanding the same state multiple times.

## The Problem with Tree Search

> [!fail]+ Repeated State Problem
> **Problem: Failure to detect repeated states can cause exponentially more work.**
>
> **Visualization:**
>
> **State Graph (the actual problem):**
> - Linear sequence: A -> B -> C -> D
> - Each state has a self-loop (can return to itself)
> - Only 4 unique states in the problem
>
> **Search Tree (what tree search explores):**
> - From A, expands to B multiple times
> - From each B, expands to C multiple times
> - From each C, expands to C again, and so on
> - Creates exponential branching due to repeated states
>
> **The issue:** Tree search doesn't recognize when it revisits the same state through different paths, leading to redundant exploration and exponential growth in the search tree.

## Avoiding Redundant Work

> [!example]+ Redundant Nodes in BFS
> We shouldn't bother expanding the circled nodes (why?)
>
> ![[Pasted image 20251103142840.png]]
>
> **Diagram explanation:** The search tree shows multiple nodes circled in red (labeled 'a', 'e', 'p', 'q') that appear multiple times at different levels of the tree.
>
> **Why shouldn't we expand them again?**
> - These states have already been explored
> - Any paths through these repeated states will be at least as long (or longer) than paths already found
> - Re-expanding wastes computational resources
> - In BFS specifically, the first time we reach a state is guaranteed to be via the shortest path

## Solution: The Closed Set

> [!success]+ Graph Search Algorithm
> **Core idea: Never expand a state twice**
>
> **Implementation:**
> 1. Tree search + set of expanded states ("closed set")
> 2. Expand the search tree node-by-node, but...
> 3. Before expanding a node, check to make sure its state has never been expanded before
> 4. If not new, skip it; if new, add to closed set
>
> **Important: Store the closed set as a set, not a list**
> - Sets offer $\mathcal{O}(1)$ lookup time
> - Lists require $\mathcal{O}(n)$ lookup time
> - This makes a huge performance difference in practice

## Correctness Considerations

> [!question]+ Impact on Completeness and Optimality
> **Can graph search wreck completeness? Why/why not?**
> - Need to consider: does preventing re-expansion of states mean we might miss solutions?
> - Answer depends on the search strategy and problem properties
> - For systematic searches (BFS, UCS), graph search maintains completeness
>
> **How about optimality?**
> - Does preventing re-expansion guarantee we find the optimal solution?
> - For some algorithms (like BFS in unweighted graphs), yes
> - For others (like DFS), graph search alone doesn't guarantee optimality
> - **Critical: A* graph search requires consistent heuristics for optimality**

## A* Graph Search Gone Wrong

> [!example]+ A* with Inconsistent Heuristic
> **Problem setup:**
>
> **State space graph:**
> - Start: S ($h=2$)
> - Intermediate: A ($h=4$), B ($h=1$), C ($h=1$)
> - Goal: G ($h=0$)
> - Edges: S -> A (1), S -> B (1), A -> C (1), B -> C (2), C -> G (3)
>
> **Search progression:**
> - S (0+2): Start with $f=2$
> - SA (1+4): Path cost 1, heuristic 4, $f=5$
> - SB (1+1): Path cost 1, heuristic 1, $f=2$ ✓ (expand this)
> - SBC (3+1): Path cost 3, heuristic 1, $f=4$
>
> **Closed set:** {S, B, C}
>
> **The problem:** C is now in closed set via the expensive path SBC (cost 3)
>
> **What happens next:**
> - SA (1+4): Still in fringe with $f=5$
> - SAC would have cost 2, but C is already closed!
> - The optimal path S -> A -> C -> G (total cost 5) is blocked
> - Instead, algorithm returns SBCG with cost 6
>
> **Why did this happen?** The heuristic was **inconsistent** (not monotonic), causing $f$-values to not increase monotonically along paths.

## A* Graph Search Done Right

> [!success]+ A* with Consistent Heuristic
> **Same problem, but with consistent heuristic:**
>
> **Revised heuristics:**
> - S: $h=2$, A: $h=2$ (changed from 4), B: $h=1$, C: $h=1$, G: $h=0$
>
> **Search progression:**
> - S (0+2): $f=2$
> - SB (1+1): $f=2$
> - SA (1+2): $f=3$
> - SAC (2+1): $f=3$
> - SACG (5+0): $f=5$ (optimal!)
>
> **Key difference:** With consistent heuristic, $f$-values never decrease:
> - S (2) -> SB (2) -> SA (3) -> SAC (3) -> SACG (5)
> - $f$ values: 2 -> 2 -> 3 -> 3 -> 5 (non-decreasing!)

## Consistency and Optimality

> [!theorem]+ Consistency -> Non-Decreasing f-score
> **Side-by-side comparison:**
>
> **Inconsistent heuristic:**
> - S (0+2) -> SA (1+4) -> SAC (2+1)
> - $f$ values: 2 -> 5 -> 3 (decreases!)
> - Graph search fails to find optimal solution
>
> **Consistent heuristic:**
> - S (0+2) -> SA (1+2) -> SAC (2+1)
> - $f$ values: 2 -> 3 -> 3 (non-decreasing!)
> - Graph search correctly finds optimal solution
>
> **The crucial difference:** With consistent heuristics, $f$-values never decrease along any path, which guarantees that the first time we reach a state, we've found the optimal path to that state.

## Key Takeaways

> [!tip]+ Summary: Tree vs Graph Search
> **For A* Tree Search:**
> - Only needs admissibility to guarantee optimality
> - Can work with inconsistent heuristics
> - May expand states multiple times
> - More nodes expanded, but simpler logic
>
> **For A* Graph Search:**
> - Needs consistency to guarantee optimality
> - Consistency implies admissibility
> - More efficient (each state expanded at most once)
> - Requires the triangle inequality to hold
>
> **Triangle inequality (consistency):** For every arc from A to C:
> $$h(A) - h(C) ≤ \text{cost}(A \to C)$$
>
> Or equivalently:
> $$h(A) ≤ \text{cost}(A \to C) + h(C)$$

> [!tip]+ Practical Advice
> **When to use Graph Search:**
> - When the state space has many paths to the same state
> - When you want to avoid redundant computation
> - When memory is available to store the closed set
>
> **Trade-offs:**
> - **Benefit:** Dramatically reduces nodes expanded (exponential savings possible)
> - **Cost:** Memory overhead for storing the closed set
> - **Requirement:** For A*, need consistent heuristics
>
> **Good news:** Most natural heuristics (Manhattan distance, straight-line distance, etc.) are consistent. When designing heuristics, aim for consistency to enable efficient graph search.

> [!note]+ Related Concepts
> - **[[A*]]**: Optimal search algorithm that benefits from graph search
> - **[[Search Heuristic]]**: Estimation function used in informed search
> - **[[Admissibility]]**: Weaker property than consistency
> - **[[Uniform Cost Search]]**: Always benefits from graph search
