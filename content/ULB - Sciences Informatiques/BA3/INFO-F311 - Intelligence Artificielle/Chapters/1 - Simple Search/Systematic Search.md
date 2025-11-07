---
title: Systematic Search
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Systematic search** is a structured approach to exploring a search space using a frontier to separate expanded from unexplored regions.

![[Pasted image 20250925121305.png]]

## Process

> [!abstract]+ Search Steps
> 1. **Frontier** separates expanded from unexplored region of state-space graph
> 2. **Expanding a frontier node**:
>    - Moves a node from frontier into expanded
>    - Adds nodes from unexplored into frontier, maintaining property 1

> [!note]+ Related Concepts
> - **[[Tree Search]]**: Uses systematic search approach
> - **[[Search Tree]]**: Structure being systematically explored
> - **[[State Space Graph]]**: Graph being searched
> - **[[Search Algorithm Properties]]**: Characteristics of systematic approaches
