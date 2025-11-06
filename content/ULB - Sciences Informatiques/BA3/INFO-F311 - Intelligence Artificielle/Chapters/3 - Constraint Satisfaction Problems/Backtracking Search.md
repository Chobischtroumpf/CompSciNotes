---
title: Backtracking Search
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> **Backtracking search** is an uninformed algorithm for solving [[CSP|CSPs]] that combines depth-first search with intelligent variable ordering and constraint checking.

## Strategy

> [!abstract]+ Key Features
> Combines:
> - Depth-first search
> - One variable assignment at a time
>   - Variable assignments are commutative, so fix ordering -> better branching factor
> - Incremental constraint checking
>   - Consider only values which do not conflict with previous assignments

## Performance

> [!tip]+ Efficiency Note
> Simple backtracking search is not very efficient.
>
> **Example:** With the N-Queens problem, backtracking is on average limited to $n = 25$
>
> Backtracking can be improved via:
> - Ordering
> - Filtering
> - Exploiting problem structure

## Algorithm

> [!abstract]+ Backtracking Search Pseudocode
> ```
> function Backtracking-Search(csp) returns solution/failure
>     return Recursive-Backtracking({ }, csp)
>
> function Recursive-Backtracking(assignment, csp) returns solution/failure
>     if assignment is complete then return assignment
>     var ← Select-Unassigned-Variable(Variables[csp], assignment, csp)
>     for each value in Order-Domain-Values(var, assignment, csp) do
>         if value is consistent with assignment given Constraints[csp] then
>             add {var = value} to assignment
>             result ← Recursive-Backtracking(assignment, csp)
>             if result ≠ failure then return result
>             remove {var = value} from assignment
>     return failure
> ```
>
> **Note:** Backtracking = DFS + variable-ordering + fail-on-violation

> [!note]+ Related Concepts
> - **[[CSP]]**: Problem type being solved
> - **[[Filtering]]**: Improvement technique
> - **[[Ordering]]**: Improvement technique
> - **[[Arc Consistency]]**: Constraint propagation method
