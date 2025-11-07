---
title: Local Beam Search
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Local Beam Search** maintains $K$ parallel [[Local Search]] processes that communicate and share information, combining the benefits of multiple search threads.

## Strategy

> [!abstract]+ Algorithm Overview
> **Key idea:** Run $K$ copies of a local search algorithm, initialized randomly and connected (communicating together)
>
> **For each iteration:**
> - Generate all successors from $K$ current states
> - Choose best $K$ of these to be the new current states
>
> **Difference from parallel search:**
> - Unlike $K$ independent searches, beam search shares information
> - The $K$ states "communicate" by competing for spots in the next generation
>
> ![[Pasted image 20251106164533.png]]

## Genetic Algorithms

> [!abstract]+ Evolutionary Approach
> Genetic algorithms use a natural selection metaphor:
> - Keep best $N$ hypotheses at each step (selection) based on a fitness function
> - Also have pairwise crossover operators, with optional mutation to give variety
>
> ![[Pasted image 20251106171558.png]]

> [!abstract]+ Genetic Algorithm Pseudocode
> ```
> function Genetic-Algorithm(population, fitness) returns an individual
>     repeat
>         weights <- Weighted-By(population, fitness)
>         population2 <- empty list
>         for i = 1 to Size(population) do
>             parent1, parent2 <- Weighted-Random-Choices(population, weights, 2)
>             child <- Reproduce(parent1, parent2)
>             if (small random probability) then child <- Mutate(child)
>             add child to population2
>         population <- population2
>     until some individual is fit enough, or enough time has elapsed
>     return the best individual in population, according to fitness
>
> function Reproduce(parent1, parent2) returns an individual
>     n <- Length(parent1)
>     c <- random number from 1 to n
>     return Append(Substring(parent1, 1, c), Substring(parent2, c + 1, n))
> ```

> [!note]+ Related Concepts
> - **[[Local Search]]**: Base algorithm being parallelized
> - **[[Simulated Annealing]]**: Alternative stochastic local search
> - **[[CSP]]**: Often solved with local search methods
