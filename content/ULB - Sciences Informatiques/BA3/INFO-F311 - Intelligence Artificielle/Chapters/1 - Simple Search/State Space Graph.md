---
title: State Space Graph
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **state space [[Graphe simple|graph]]** is a mathematical representation of a [[Search Problem]] where nodes are [[Search State|search states]] and arcs are action transitions between states.

^e3fa58

![[Pasted image 20250925112520.png]]

![[Pasted image 20250925112536.png]]

> [!abstract]+ Properties
> - The goal test is a set of goal nodes
> - Each state occurs only once

> [!example]+ Example
> In a pathfinding problem, each $(x,y)$ coordinate is a node, and NSEW movements are arcs connecting adjacent coordinates.

> [!note]+ Related Concepts
> - **[[Graphe simple|Graph]]**: Recap about graphs
> - **[[Search Problem]]**: Problem represented by graph
> - **[[Search State]]**: Nodes in the graph
> - **[[Search Tree]]**: Tree structure for exploring graph
> - **[[Tree Search]]**: Algorithm traversing the graph
