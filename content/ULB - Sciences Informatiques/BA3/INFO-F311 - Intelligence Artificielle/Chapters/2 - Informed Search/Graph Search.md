---
title: Graph Search
authors: Alessandro Dorigo
tags:
  -
---


## Tree Search
> [!abstract]
>
> **Problem: Failure to detect repeated states can cause exponentially more work.**
>
> **Visualization:**
>
> **State Graph (the actual problem):**
>
> - Linear sequence: A → B → C → D
> - Each state has a self-loop (can return to itself)
> - Only 4 unique states in the problem
>
> **Search Tree (what tree search explores):**
>
> - From A, expands to B multiple times
> - From each B, expands to C multiple times
> - From each C, expands to C again, and so on
> - Creates exponential branching due to repeated states
>
> **The issue:** Tree search doesn't recognize when it revisits the same state through different paths, leading to redundant exploration and exponential growth in the search tree.
## Graph Search

> [!info] Avoiding Redundant Work In BFS
>
> We shouldn't bother expanding the circled nodes (why?)
> ![[Pasted image 20251103142840.png]]
> **Diagram explanation:** The search tree shows multiple nodes circled in red (labeled 'a', 'e', 'p', 'q') that appear multiple times at different levels of the tree.
>
> **Why shouldn't we expand them again?**
>
> - These states have already been explored
> - Any paths through these repeated states will be at least as long (or longer) than paths already found
> - Re-expanding wastes computational resources
> - In BFS specifically, the first time we reach a state is guaranteed to be via the shortest path

> [!success] Solution Idea
>
> **never expand a state twice**
>
> **How to implement:**
>
> 1. Tree search + set of expanded states ("closed set")
> 2. Expand the search tree node-by-node, but...
> 3. Before expanding a node, check to make sure its state has never been expanded before
> 4. If not new, skip it; if new, add to closed set
>
> **Important: store the closed set as a set, not a list**
>
> - Sets offer O(1) lookup time
> - Lists require O(n) lookup time
> - This makes a huge performance difference in practice

> [!question] Graph Search Considerations
>
> **Can graph search wreck completeness? Why/why not?**
>
> - Need to consider: does preventing re-expansion of states mean we might miss solutions?
> - Answer depends on the search strategy and problem properties
>
> **How about optimality?**
>
> - Does preventing re-expansion guarantee we find the optimal solution?
> - This depends on the search algorithm being used
> - For some algorithms (like BFS in unweighted graphs), yes
> - For others (like DFS), graph search alone doesn't guarantee optimality

> [!tip] Key Insights
>
> **When to use Graph Search:**
>
> - When the state space has many paths to the same state
> - When you want to avoid redundant computation
> - When memory is available to store the closed set
>
> **Trade-offs:**
>
> - **Benefit:** Dramatically reduces nodes expanded (exponential savings possible)
> - **Cost:** Memory overhead for storing the closed set
> - **Implementation:** Must use efficient data structures (hash sets, not lists)
>
> **The closed set is crucial:** It transforms tree search from potentially exploring infinite or exponential paths into a polynomial-time algorithm for many problems.

# A* Example

> [!example]+ A* Graph Search Gone Wrong?
> **Problem setup:**
>
> **State space graph:**
>
> - Start: S ($h=2$)
> - A ($h=4$), B ($h=1$), C ($h=1$), Goal: G ($h=0$)
> - Edges: S→A (1), S→B (1), A→C (1), B→C (2), C→G (3)
>
> **Search tree expansion:**
>
> - S (0+2): Start
> - SA (1+4): Path cost 1, heuristic 4, $f=5$
> - SB (1+1): Path cost 1, heuristic 1, $f=2$ ✓ (better, expand this)
>
> **Closed set:** {S, B}
>
> **Next step:**
>
> - SBC (3+1): Path cost 3, heuristic 1, $f=4$
> - SBS (2+2): Path cost 2, but S already in closed set (skip)
>
> **From SBC node:**
>
> - SBCG (6+0): Reaches goal with $f=6$
> - SBCB (5+1): Would revisit B, but B in closed set (skip)
>
> **Closed set:** {S, B, C}
>
> **Problem emerging:** The graph search has closed C, preventing exploration of potentially better paths through C.
>
> **From SA node (still in fringe):**
>
> - SAC (2+1): Path cost 2, heuristic 1, $f=3$
> - But C is already in closed set!
> - This path is blocked even though SAC→G would give total cost 2+3=5
>
> **Closed set:** {S, B, C}
>
> **The issue:** A* graph search found SBCG with cost 6, but the optimal path SACG with cost 5 was never explored because C was already closed via a worse path!
>
> **Search completes:**
>
> - SBCG (6+0): $f=6$ is selected and returned
> - SAC (2+1): Never expanded because C is in closed set
>
> **Closed set:** {S, B, C, G}
>
> **Conclusion:** A* graph search returned a suboptimal solution (cost 6 instead of cost 5) because it closed state C prematurely via a more expensive path, blocking the optimal path through C.
>
> **Why did this happen?** The heuristic was **inconsistent** (not monotonic), causing the $f$-values to not increase monotonically along paths.

> [!success] A* Graph Search with Consistent Heuristic
>
> **Same problem, but with consistent heuristic:**
>
> **Revised heuristics:**
>
> - S: $h=2$, A: $h=2$ (changed from 4), B: $h=1$, C: $h=1$, G: $h=0$
>
> **Search progression:**
>
> - S (0+2)
> - SA (1+2): $f=3$ (was $f=5$ before)
> - SB (1+1): $f=2$
> - SBC (3+1): $f=4$, SAC (2+1): $f=3$
>
> **Key difference:**
>
> - When we reach SAC with $f=3$, even though C is in closed set, we can verify this is consistent
> - Actually, with proper A* graph search with consistent heuristic, SACG (5+0) = 5 is found
>
> **Closed set:** {S, B, A, C}
>
> **Result:** SACG with $f=5$ is correctly identified as optimal! (circled in blue)

> [!example] Consistency ⇒ Non-Decreasing f-score **Side-by-side comparison:**
>
> **Left: Inconsistent heuristic**
>
> - S (0+2) → SA (1+4) → SAC (2+1)
> - $f$ values: 2 → 5 → 3 (decreases! ❌)
> - SBCA (4+4), SBCG (6+0) (circled in red)
> - Graph search fails to find optimal solution
>
> **Right: Consistent heuristic**
>
> - S (0+2) → SA (1+2) → SAC (2+1)
> - $f$ values: 2 → 3 → 3 (non-decreasing! ✓)
> - SACA (3+2), SACG (5+0) (circled in blue)
> - Graph search correctly finds optimal solution
>
> **The crucial difference:** With consistent heuristics, $f$-values never decrease along any path, which guarantees that the first time we reach a state, we've found the optimal path to that state.

> [!tip] Key Takeaways: Consistency
>
> For A\* Tree Search:
>
> - Only needs admissibility to guarantee optimality
> - Can work with inconsistent heuristics
> - May expand states multiple times
>
> For A\* Graph Search:
>
> - Needs consistency to guarantee optimality
> - Consistency implies admissibility
> - More efficient (each state expanded at most once)
> - Requires the triangle inequality to hold
>
> **Triangle inequality (consistency):** For every arc from A to C: $$h(A) - h(C) ≤ \text{cost}(A \to C)$$
>
> Or equivalently: $$h(A) ≤ \text{cost}(A \to C) + h(C)$$
>
> **Practical advice:** Most natural heuristics (Manhattan distance, straight-line distance, etc.) are consistent. When designing heuristics, aim for consistency to enable efficient graph search.
