---
title: Adversarial Search
authors: Mihai Bors
tags:
  - AI
---


One player maximizes result, one player minimizes it (for deterministic, zero-sum games)

| ![[97e43d0d0a27ec42fc480215bf815edf.png]] | ![[fa89adef29bdfbaf2a06cd9973de4294.png]] |
| :----------------------------------: | :----------------------------------: |
|          Single-Agent Tree           |        Adversarial Game Tree         |
## Value of a State

### Single-Agent

The best achievable outcome (utility) from that state

Non-terminal state: $V(s) = \underset{s' \in \text{ successors}(s)}{\max V(s')}$
Terminal state: $V(s)$ is known

### Adversarial

Max nodes are under the [[Agent]]'s control: $V(s) = \underset{s' \in \text{ successors}(s)}{\max V(s')}$

![[00fab96c30beec80d7c51c497ee65303.png]]

Min nodes are under the Opponent's control: $V(s) = \underset{s' \in \text{ successors}(s)}{\min V(s')}$

![[0f7cb941f06d4710dee2bbc582b43bd0.png]]

![[590967387d97b84693d287d56ec71a97.png]]
Entire tree

Terminal states: $V(s)$ is known
