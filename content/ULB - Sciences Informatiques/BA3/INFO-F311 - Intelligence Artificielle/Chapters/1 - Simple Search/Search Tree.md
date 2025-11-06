---
title: Search Tree
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> A **search tree** is a [[Arbre (théorie des graphes)#^dcd789|tree]] structure that represents the exploration of possible action sequences from an initial state to find a goal.
>
> **Components**:
> - **Root**: Start state
> - **Children**: Successors
> - **Nodes**: Show states but correspond to PLANS that achieve those states

![[Pasted image 20250925114847.png]]

> [!tip]+ Key Insight
> Each **node** in the search tree is an **entire path** in the [[State Space Graph#^e3fa58|state space graph]].

| ![[Pasted image 20250925115357.png]] | ![[Pasted image 20250925115411.png]] |
| :----------------------------------- | :----------------------------------- |
> [!note]+ Related Concepts
> - **[[State Space Graph]]**: Graph being explored
> - **[[Tree Search]]**: Algorithm using search trees
> - **[[Search Problem]]**: Problem being solved
> - **[[Systematic Search]]**: Organized exploration method
