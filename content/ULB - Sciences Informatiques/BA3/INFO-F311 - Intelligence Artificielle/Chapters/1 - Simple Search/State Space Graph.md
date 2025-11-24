---
title: State Space Graph
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **state space [[Graphe simple|graph]]** is a mathematical representation of a [[Search Problem]] where nodes are [[Search State|search states]] and arcs are action transitions between states.

^e3fa58

![[ebb6aa971f116ac5a27e584cf2e03a43.png]]

![[bfb7403b3b9e4f56efc1327864c7873e.png]]

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
