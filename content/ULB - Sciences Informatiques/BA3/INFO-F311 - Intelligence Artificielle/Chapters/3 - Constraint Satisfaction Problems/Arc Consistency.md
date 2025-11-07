---
title: Arc Consistency
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Arc Consistency**: An arc $X \rightarrow Y$ is consistent iff for every $x$ in the tail there is some $y$ in the head which could be assigned without violating a constraint.

## Example

> [!example]+ Map Coloring
> ![[Pasted image 20251103140448.png]]

## Properties

> [!abstract]+ Theorem
> A CSP is arc consistent if all arcs are consistent.
>
> **Complexity:**
> - Arc consistency can be enforced in $\mathcal{O}(n^2d^3)$ time
> - Reducible to $\mathcal{O}(n^2d^2)$
>
> **Behavior:**
> - If $X$ loses a value, neighbors of $X$ need to be rechecked
> - Arc consistency detects failure earlier than forward checking

## Algorithm

> [!abstract]+ AC-3 Algorithm
> ```
> function AC-3(csp) returns the CSP, possibly with reduced domains
>     inputs: csp, a binary CSP with variables {X₁, X₂, ..., Xₙ}
>     local variables: queue, a queue of arcs, initially all the arcs in csp
>
>     while queue is not empty do
>         (Xᵢ, Xⱼ) ← REMOVE-FIRST(queue)
>         if REMOVE-INCONSISTENT-VALUES(Xᵢ, Xⱼ) then
>             for each Xₖ in NEIGHBORS[Xᵢ] do
>                 add (Xₖ, Xᵢ) to queue
>
> function REMOVE-INCONSISTENT-VALUES(Xᵢ, Xⱼ) returns true iff succeeds
>     removed ← false
>     for each x in DOMAIN[Xᵢ] do
>         if no value y in DOMAIN[Xⱼ] allows (x,y) to satisfy the constraint Xᵢ ↔ Xⱼ
>             then delete x from DOMAIN[Xᵢ], removed ← true
>     return removed
> ```

## Limitations

> [!tip]+ After Enforcing Arc Consistency
> After arc consistency is enforced:
> - Can have one solution left
> - Can have multiple solutions left
> - Can have no solutions left (and not know it)

> [!note]+ Related Concepts
> - **[[Constraint Graph]]**: Structure on which arc consistency operates
> - **[[Filtering]]**: Related CSP technique
> - **[[Backtracking Search]]**: Uses arc consistency
