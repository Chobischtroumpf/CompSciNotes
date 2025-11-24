---
title: Search Tree
authors: Mihai Bors
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

![[f811811627d50150dd5d5e6d53289bce.png]]

> [!tip]+ Key Insight
> Each **node** in the search tree is an **entire path** in the [[State Space Graph#^e3fa58|state space graph]].

| ![[2dc39ebefd6e35f40c51e799e5740bce.png]] | ![[36f8997b70dbabd7cee9deb24e8cef66.png]] |
| :----------------------------------- | :----------------------------------- |
> [!note]+ Related Concepts
> - **[[State Space Graph]]**: Graph being explored
> - **[[Tree Search]]**: Algorithm using search trees
> - **[[Search Problem]]**: Problem being solved
> - **[[Systematic Search]]**: Organized exploration method
