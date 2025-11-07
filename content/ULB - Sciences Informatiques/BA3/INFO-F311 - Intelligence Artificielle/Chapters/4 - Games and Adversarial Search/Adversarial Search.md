---
title: Adversarial Search
authors: Mihai Bors
tags:
  - AI
---


One player maximizes result, one player minimizes it (for deterministic, zero-sum games)

| ![[Pasted image 20251106183453.png]] | ![[Pasted image 20251106183500.png]] |
| :----------------------------------: | :----------------------------------: |
|          Single-Agent Tree           |        Adversarial Game Tree         |
## Value of a State

### Single-Agent

The best achievable outcome (utility) from that state

Non-terminal state: $V(s) = \underset{s' \in \text{ successors}(s)}{\max V(s')}$
Terminal state: $V(s)$ is known

### Adversarial

Max nodes are under the [[Agent]]'s control: $V(s) = \underset{s' \in \text{ successors}(s)}{\max V(s')}$

![[Pasted image 20251106184126.png]]

Min nodes are under the Opponent's control: $V(s) = \underset{s' \in \text{ successors}(s)}{\min V(s')}$

![[Pasted image 20251106184131.png]]

![[Pasted image 20251106184145.png]]
Entire tree

Terminal states: $V(s)$ is known
