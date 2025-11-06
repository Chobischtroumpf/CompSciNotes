---
title: World State
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> A **world state** is a complete description of the environment with every detail.

^407bb2

![[Pasted image 20250925102817.png]]

## Example: Pacman

> [!example]+ World State Complexity
> ![[Pasted image 20250925102837.png]]
>
> **Components**:
> - **Agent positions**: 120
> - **Food count**: 30
> - **Ghost positions**: 12
> - **Agent facing**: NSEW
>
> **State space sizes**:
> - World states: $120 \times 2^{30} \times 12^2 \times 4$
> - States for pathing: $120$
> - States for eat-all-dots: $120 \times 2^{30}$

> [!note]+ Related Concepts
> - **[[Search State]]**: Abstracted version of world state
> - **[[State Space]]**: Set of all states
> - **[[Search Problem]]**: Uses state representations
