---
title: Tree Search
authors: Alessandro Dorigo
tags:
  - AI
---


> [!info]+ Definition
> **Tree search** is a fundamental algorithm for exploring a search space by systematically expanding nodes in a tree structure to find a solution.

## Algorithm

> [!abstract]+ Tree-Search Pseudocode
> ```
> function Tree-Search(problem, strategy) returns a solution, or failure
>     initialize the search tree using the initial state of problem
>     loop do
> 		if there are no candidates for expansion then return failure
>         choose a leaf node for expansion according to strategy
>         if the node contains a goal state then return the corresponding solution
>         else expand the node and add the resulting nodes to the search tree
>     end
> ```

> [!tip]+ Variations
> **Key decisions in tree search**:
> - Which leaf node to expand next
> - Whether to check for repeated states
> - Data structures for frontier, expanded nodes

## Example: Traveling in Romania

> [!example]+ Search Process
> ![[Pasted image 20250925115827.png]]
>
> | ![[Pasted image 20250925115835.png]] |
> | :--------------------------------------- |
> | ![[Pasted image 20250925115843.png]] |
> | ![[Pasted image 20250925115850.png]] |

> [!note]+ Related Concepts
> - **[[Search Tree]]**: Tree structure representing action sequences
> - **[[Search Problem]]**: Problem formulation for tree search
> - **[[Systematic Search]]**: Structured exploration approach
> - **[[Search Algorithm Properties]]**: Performance characteristics
