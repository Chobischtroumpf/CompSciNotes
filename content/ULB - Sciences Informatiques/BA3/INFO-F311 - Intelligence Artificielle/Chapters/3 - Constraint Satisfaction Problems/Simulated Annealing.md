---
title: Simulated Annealing
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> **Simulated Annealing** is a [[Local Search]] algorithm that escapes local maxima by allowing downhill moves with probability that decreases over time, inspired by the physical process of annealing in metallurgy.

## Algorithm

> [!abstract]+ Pseudocode
> ```
> function Simulated-Annealing(problem, schedule) returns a solution state
>     inputs: problem, a problem
>             schedule, a mapping from time to "temperature"
>     local variables: current, a node
>                      next, a node
>                      T, a "temperature" controlling prob. of downward steps
>
>     current <- Make-Node(Initial-State[problem])
>     for t <- 1 to inf do
>         T <- schedule[t]
>         if T = 0 then return current
>         next <- a randomly selected successor of current
>         deltaE <- Value[next] - Value[current]
>         if deltaE > 0 then current <- next
>         else current <- next only with probability e^{deltaE/T}
> ```

## Key Mechanism

> [!abstract]+ Temperature Schedule
> **How it works:**
> - **High temperature (early):** Accept bad moves frequently → exploration
> - **Low temperature (late):** Accept bad moves rarely → exploitation
> - **Temperature = 0:** Equivalent to Hill Climbing
>
> **Acceptance probability for downhill moves:**
>
> $$P(\text{accept}) = e^{\frac{\Delta E}{T}}$$
>
> where $\Delta E < 0$ for downhill moves

## Properties

> [!abstract]+ Theoretical Guarantee
> **Stationary distribution:**
> $$p(x) \propto e^{\frac{E(x)}{kT}}$$
>
> If $T$ decreases slowly enough, it will converge to an optimal state.

> [!warning]+ Practical Limitation
> The more downhill steps you need to escape a local optimum, the less likely you are to ever make them all in a row.
>
> **Trade-off:**
> - Slow cooling schedule -> better chance of finding global optimum, but slower
> - Fast cooling schedule -> faster convergence, but may get stuck in local optima

> [!note]+ Related Concepts
> - **[[Local Search]]**: General framework
> - **[[Local Beam Search]]**: Alternative approach using multiple states
