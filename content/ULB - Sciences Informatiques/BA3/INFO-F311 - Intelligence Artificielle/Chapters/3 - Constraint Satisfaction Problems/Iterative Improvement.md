---
title: Iterative Improvement
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Iterative Improvement** is a [[Local Search]] method for [[CSP|CSPs]] that starts with an assignment with unsatisfied constraints and iteratively reassigns variable values to reduce conflicts.

## Strategy

> [!abstract]+ Min-Conflicts Heuristic
> **Algorithm:**
> ```
> while not solved
>     randomly select any conflicted variable
>     min-conflicts heuristic:
>         choose a value that violates the fewest constraints
> ```
>
> **Key idea:** At each step, choose the value that minimizes the number of constraint violations

## Example

> [!example]+ 4-Queens Problem
> **Problem space:**
> - **States:** 4 queens in 4 columns ($4^4 = 256$ states)
> - **Operators:** Move queen in column
> - **Goal test:** No attacks between queens
> - **Evaluation:** $c(n) =$ number of attacks

## Performance

> [!success]+ Efficiency of Min-Conflicts
> Given a random initial state, can solve $n$-queens in almost constant time for arbitrary $n$ with high probability.
>
> The same appears to be true for any randomly-generated [[CSP]] except in a narrow range of the ratio:
>
> $$R = \frac{\text{number of constraints}}{\text{number of variables}}$$
>
> ![[469d6a1203f30f15e894a76e09724793.png]]

> [!note]+ Related Concepts
> - **[[Local Search]]**: General framework for iterative improvement
> - **[[CSP]]**: Problem type being solved
> - **[[Simulated Annealing]]**: Alternative local search method
