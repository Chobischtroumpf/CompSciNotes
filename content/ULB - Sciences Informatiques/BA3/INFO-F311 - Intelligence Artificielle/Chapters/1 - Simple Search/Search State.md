---
title: Search State
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> A **search state** is an abstracted representation keeping only the details relevant for planning.

^f0ce36

## Examples

> [!example]+ Problem: Pathing
> **States**: $(x,y)$ location
>
> **Actions**: NSEW
>
> **Successor**: Update location only
>
> **Goal test**: Is $(x,y) =$ END

> [!example]+ Problem: Eat-All-Dots
> **States**: {$(x,y)$, dot booleans}
>
> **Actions**: NSEW
>
> **Successor**: Update location and possibly a dot boolean
>
> **Goal test**: Dots all false

> [!note]+ Related Concepts
> - **[[State Space]]**: Set containing all search states
> - **[[World State]]**: Complete state description
> - **[[Search Problem]]**: Uses search states
> - **[[State Space Graph]]**: Graph of search states
