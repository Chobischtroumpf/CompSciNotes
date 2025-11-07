---
title: Search Problem
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **search problem** consists of:
> - A [[State Space]] $\mathcal{S}$
> - An initial state $s_0$
> - Actions $\mathcal{A}(s)$ in each state
> - A transition model $\text{Result}(s,a)$
> - A goal test $G(s)$
> - Action cost $c(s,a,s')$

> [!abstract]+ Solution
> - A **solution** is an action sequence that reaches a goal state
> - An **optimal solution** has the least cost among all solutions

## Example: Traveling in Romania

> [!example]+ Problem Setup
> ![[Pasted image 20250925100954.png]]
>
> **State space**: Cities
>
> **Initial state**: Arad
>
> **Actions**: Go to adjacent city
>
> **Transition model**: Reach adjacent city
>
> **Goal test**: $s =$ Bucharest
>
> **Action cost**: Road distance from $s$ to $s'$

> [!note]+ Related Concepts
> - **[[State Space]]**: Set of all possible states
> - **[[Search State]]**: Abstracted state representation
> - **[[State Space Graph]]**: Graph representation
> - **[[Search Tree]]**: Tree exploration structure
> - **[[Tree Search]]**: Algorithm for solving search problems
