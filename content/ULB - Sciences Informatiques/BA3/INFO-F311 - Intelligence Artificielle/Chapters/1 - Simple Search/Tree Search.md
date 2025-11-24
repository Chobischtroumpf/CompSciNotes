---
title: Tree Search
authors: Mihai Bors
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
> ![[06fc6d68d2ce5bcd9331ec019572d20f.png]]
>
> | ![[10ee6b64272d56e3fb4b2ad795b67627.png]] |
> | :--------------------------------------- |
> | ![[ed9be9c73168b735744f63aff46f425e.png]] |
> | ![[5740fb518bb6b74e55d12693528f2657.png]] |

> [!note]+ Related Concepts
> - **[[Search Tree]]**: Tree structure representing action sequences
> - **[[Search Problem]]**: Problem formulation for tree search
> - **[[Systematic Search]]**: Structured exploration approach
> - **[[Search Algorithm Properties]]**: Performance characteristics
