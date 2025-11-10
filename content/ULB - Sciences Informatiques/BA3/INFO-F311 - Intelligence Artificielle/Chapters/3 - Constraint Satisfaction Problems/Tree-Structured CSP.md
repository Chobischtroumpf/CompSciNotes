---
title: Tree-Structured CSP
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Tree-Structured CSPs** are [[CSP|CSPs]] where the [[Constraint Graph]] has no loops, allowing for efficient polynomial-time solutions.

## Main Result

> [!abstract]+ Efficiency of Tree-Structured CSPs
> If the constraint graph has no loops, the [[CSP]] can be solved in $\mathcal{O}(n d^2)$ time.
>
> **Comparison:**
> - General [[CSP|CSPs]] have a worst-case time of $\mathcal{O}(d^n)$
> - Tree-structured CSPs are exponentially faster!

## Algorithm

> [!abstract]+ Tree CSP Solution Algorithm
> ![[d389835e34ad4d4940f6c960c4ba8576.png]]
>
> **Three phases:**
> 1. **Order:** Choose a root variable, order variables so that parents precede children
> 2. **Remove backward:** `for i = n : 2, apply RemoveInconsistent(Parent(X_i), X_i)`
> 3. **Assign forward:** `for i = 1 : n, assign X_i consistently with Parent(X_i)`

## Correctness

> [!abstract]+ Claim 1: Backward Pass Correctness
> After backward passes, all root → leaf arcs are consistent.
>
> **Proof:** Each $X \to Y$ was made consistent at one point and $Y$'s domain could not have been reduced thereafter (because $Y$'s children were processed before $Y$).

> [!abstract]+ Claim 2: Forward Assignment Correctness
> If root → leaf arcs are consistent, forward assignment will not backtrack.
>
> **Proof:** Whatever we assign to $A$, we know there is an assignment to $B$, and we also know that whatever we assign to $A + B$, there is an assignment to $C$.

## Nearly Tree-Structured CSPs

> [!abstract]+ Handling Near-Tree Structures
> ![[e62dad15b29b123ce01d07e006cf5356.png]]
>
> **Two approaches:**
> - **Conditioning:** Instantiate a variable, prune its neighbors' domains
> - **Cutset conditioning:** Instantiate (in all ways) a set of variables such that the remaining constraint graph is a tree

### Cutset Conditioning

> [!abstract]+ Cutset Conditioning Algorithm
> **Steps:**
> 1. Choose a cutset
> 2. Instantiate the cutset (all possible ways)
> 3. Compute residual CSP for each assignment
> 4. Solve the residual CSPs (tree structured)
>
> ![[8532ed2a406715c4633238f64dd9696b.png]]
>
> **Complexity:**
> - Cutset size $c$ gives runtime $\mathcal{O}(d^c \cdot (n - c) \cdot d^2)$
> - Very fast for small $c$

### Tree Decomposition

> [!abstract]+ Tree Decomposition Strategy
> **Idea:** Create a tree-structured graph of mega-variables
> - Each mega-variable encodes part of the original CSP
> - Subproblems overlap to ensure consistent solutions
>
> ![[ca36de0d0c07c92c114c06929de19941.png]]

> [!note]+ Related Concepts
> - **[[CSP]]**: Problem type being solved
> - **[[Constraint Graph]]**: Structure being analyzed
> - **[[Arc Consistency]]**: Used in backward pass
> - **[[Backtracking Search]]**: Avoided with tree structure
> - **[[Filtering]]**: Related preprocessing technique
