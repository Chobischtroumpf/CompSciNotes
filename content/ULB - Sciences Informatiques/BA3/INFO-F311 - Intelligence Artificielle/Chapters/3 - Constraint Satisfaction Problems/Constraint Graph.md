---
title: Constraint Graph
authors: Alessandro Dorigo, Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **constraint graph** is a visual representation of a [[CSP]] where nodes are variables and arcs show [[ULB - Sciences Informatiques/BA3/INFO-F311 - Intelligence Artificielle/Chapters/3 - Constraint Satisfaction Problems/Constraint|constraints]] between them.

## Binary CSP

> [!abstract]+ Structure
> **Binary CSP:** Each constraint relates (at most) two variables
>
> **Binary constraint graph:**
> - Nodes are variables
> - Arcs show constraints between variables

## Advantages

![[Pasted image 20251103134639.png]]

> [!tip]+ Usage
> General-purpose CSP algorithms use the graph structure to speed up search.
>
> **Example:** Tasmania is an independent subproblem in the map coloring example - it can be solved separately from mainland Australia.

> [!note]+ Related Concepts
> - **[[CSP]]**: Problem represented by graph
> - **[[Constraint]]**: Edges in the graph
> - **[[Arc Consistency]]**: Algorithm operating on graph structure
