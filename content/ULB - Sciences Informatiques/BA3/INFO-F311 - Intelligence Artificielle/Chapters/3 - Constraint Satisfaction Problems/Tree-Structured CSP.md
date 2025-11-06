---
title: Tree-Structured CSP
authors: Mihai Bors
tags:
  - AI
---


> [!abstract] Theorem
> If the [[constraint graph]] has no loops, the [[CSP]] can be solved in $\mathcal{O}(n d^2)$ time.
> - General [[CSP|CSPs]] have a worst-case time of $\mathcal{O}(d^n)$

![[Pasted image 20251106130616.png]]
- Order algorithm: Choose a root variable, order variables so that parents precede children
- Remove backward: `for i = n : 2, apply RemoveInconsistent(Parent(X_i), X_i)`
- Assign forward: `for i = 1 : n, assign X_i consistently with Parent(X_i)`

> [!abstract] Claim 1
> After backward passes, all root -> arcs are consistent.
>
> **Proof:** Each $X \to Y$ was made consistent at one point and $Y$'s domain colud not have been reduced thereafter (because $Y$'s children were processed before $Y$).

> [!abstract] Claim 2
> If root -> leaf arcs are consistent, forward assignment will not backtrack.
>
> **Proof:** Whatever we assign to $A$, we know there is an assignment to $B$ and we also know that whatever we assign to $A + B$, there is an assignment to $C$.

## Nearly Tree-Structured CSPs

![[Pasted image 20251106131529.png]]

- Conditioning: instantiate a variable, prune its neighbors' domains
- Cutset conditioning: instantiate (in all ways) a set of variables such that the remaining constraint graph is a tree
- Cutset size $c$ gives runtime $\mathcal{O}((d^c) (n - c) d^2)$, very fast for small $c$

### Cutset Conditioning

1. Choose a cutset
2. Instantiate the cutset (all possible ways)
3. Compute residual CSP for each assignment
4. Solve the residual CSPs (tree structured)

![[Pasted image 20251106131638.png]]

### Tree Decomposition

Idea: create a tree-structured graph of mega-variables
Each mega-variable encodes part of the original CSP
Subproblems overlap to ensure consistent solutions

![[Pasted image 20251106131750.png]]
