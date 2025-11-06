---
title: CSP
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> **Constraint Satisfaction Problem (CSP)** is a special subset of search problems with a structured representation.

## Components

> [!abstract]+ CSP Structure
> - **State** is defined by variables $X_i$ with values from a domain $D$ (sometimes $D$ depends on $i$)
> - **Goal test** is a set of [[ULB - Sciences Informatiques/BA3/INFO-F311 - Intelligence Artificielle/Chapters/3 - Constraint Satisfaction Problems/Constraint|constraints]] specifying allowable combinations of values for subsets of variables
> - Allows useful general-purpose algorithms with more power than standard search algorithms

## Examples

> [!example]+ Map Coloring
> ![[Pasted image 20250923165107.png]]
>
> **Variables**: $\{WA, NT, Q, NSW, V, SA, T\}$ (Australia's states)
>
> **Domains**: $D = \{red, green, blue\}$
>
> **Constraints**: Adjacent regions must have different colors
> - Implicit: $WA \neq NT$
> - Explicit: $(WA, NT) \in \{(red, green), (red, blue), \ldots\}$
>
> **Solutions**: Assignments satisfying all constraints
> - Example: $\{WA=red, NT=green, Q=red, NSW=green, V=red, SA=blue, T=green\}$

> [!example]+ N-Queens Problem
> **Variables**: $Q_k$ (position of queen in column $k$)
>
> **Domain**: $\{1, 2, 3, \ldots, N\}$ (row positions)
>
> **Constraints**: $\forall i,j$ non-threatening$(Q_i, Q_j)$
>
> **Performance**: Can be solved for $n \approx 25$ with basic backtracking, $n \approx 1000$ with ordering heuristics

> [!example]+ Cryptarithmetic
> $$TWO + TWO = FOUR$$
>
> **Variables**: $F, T, U, W, R, O, X_1, X_2, X_3$ (letters and carry digits)
>
> **Domain**: $\{0, 1, 2, \ldots, 9\}$
>
> **Constraints**:
> - alldiff$(F, T, U, W, R, O)$
> - Arithmetic equations like $O + O = R + 10 \cdot X_1$

## Types of Variables

> [!info]+ Discrete Variables
> **Finite domains:**
> - Size $d$ means $\mathcal{O}(d^n)$ complete assignments
> - Examples: Boolean CSPs, SAT problem
>
> **Infinite domains:**
> - Examples: Integers, strings (e.g., job scheduling with start/end times)
> - Linear constraints solvable, nonlinear undecidable

> [!info]+ Continuous Variables
> **Real-valued:**
> - Examples: Telescope observation times
> - Linear constraints solvable in polynomial time by LP methods

> [!note]+ Related Concepts
> - **[[Search Problem]]**: More general problem formulation
> - **[[Constraint]]**: Restrictions on variable assignments
> - **[[Constraint Graph]]**: Graph representation of CSP
> - **[[Backtracking Search]]**: Algorithm for solving CSPs
