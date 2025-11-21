---
title: Game
authors: Mihai Bors
tags:
  - AI
---
> [!info]+ Definition
> A **Game** is a task environment with more than one agent, characterized by various properties that determine the appropriate solution approach.

## Game Properties

> [!abstract]+ Game Characteristics
> Games can be classified along several dimensions:
> - **Deterministic or stochastic?**
> - **Perfect information (fully observable)?**
> - **Two, three, or more players?**
> - **Teams or individuals?**
> - **Turn-taking or simultaneous?**
> - **Zero sum?**

## Standard Games

> [!abstract]+ Standard Game Definition
> **Standard games** are deterministic, observable, two-player, turn-taking, zero-sum games.
>
> **Components:**
> - **Initial state:** $s_0$
> - **Players:** Player($s$) indicates whose move it is
> - **Actions:** Actions($s$) for player on move
> - **Transition model:** Result($s, a$)
> - **Terminal test:** Terminal-Test($s$)
> - **Terminal values:** Utility($s, p$) for player $p$
>   - Or just Utility($s$) for player making the decision at root
>
> **Solution:** A policy $S \to A$ for a player

## Game Types

> [!abstract]+ Zero-Sum Games
> Agents have opposite utilities.
>
> **Pure competition:** One player maximizes while the other minimizes

> [!abstract]+ General-Sum Games
> Agents have independent utilities.
>
> **Possible dynamics:** Cooperation, indifference, competition, shifting alliances, and more

> [!abstract]+ Team Games
> Common payoff for all team members.

> [!note]+ Related Concepts
> - **[[Adversarial Search]]**: Search in competitive games
> - **[[Minimax Search]]**: Algorithm for zero-sum games
> - **[[Expectimax Search]]**: Algorithm for stochastic games
