---
title: Game
authors: Mihai Bors
tags:
  - AI
---


Task environment with > 1 agent

- Deterministic or stochastic?
- Perfect information (fully observable)?
- Two, three, or more players?
- Teams or individuals?
- Turn-taking or simultaneous?
- Zero sum?

### Standard Game

Standard games are deterministic, observable, two-player, turn-taking, zero-sum

- Initial state: $s_0$
- Players: Player($s$) indicates whose move it is
- Actions: Actions($a$) for player on move
- Transition model: Result($s, a$)
- Terminal test: Terminal-Test($s$)
- Terminal values: Utility($s, p$) for player $p$
- Or just Utility($s$) for player making the decision at root

Solution for a player is a policy $S \to A$

### Zero-Sum Game

Agents have opposite utilities
- Pure competition: one maximizes, the other minimizes

### General-Sum Games

 Agents have independent utilities
 - Cooperation, indifference, competition, shifting alliances, and more are all possible

### Team Games

Common payoff for all team members
