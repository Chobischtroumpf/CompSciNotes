---
title: Minimax
authors: Mihai Bors
tags:
  - AI
---



![[Pasted image 20251106184440.png]]

Minimax search: A state-space search tree, where players alternate turns and compute each node’s minimax value: the best achievable utility against a rational (optimal) adversary

## Implementation

```python
def max_value(state):
	v = -infty
	for s in state.successors:
		v = max(v, min_value(s))
	return v
```

$V(s) = \underset{s' \in \text{ successors}(s)}{\max V(s')}$

```python
def min_value(state):
	v = +infty
	for s in state.successors:
		v = min(v, max_value(s))
	return v
```

$V(s) = \underset{s' \in \text{ successors}(s)}{\min V(s')}$

### Dispatch Implementation

```python
def value(state):
	if state.terminal: return state.utility
	if agent.max: return max_value(state)
	if agent.min: return min_value(state)
```

```python
def max_value(state):
	v = -infty
	for s in state.successors:
		v = max(v, s.value)
	return v
```

```python
def min_value(state):
	v = +infty
	for s in state.successors:
		v = min(v, s.value)
	return v
```

![[Pasted image 20251106185612.png]]
![[Pasted image 20251106185931.png]]
Minimax example (to explain)

## Generalized Minimax

What if the game is not zero-sum, or has multiple players?

Generalization of minimax:
- Terminals have utility tuples
- Node values are also utility tuples
- Each player maximizes its own component
- Can give rise to cooperation and competition dynamically…

![[Pasted image 20251106185818.png]]
Generalized Pacman Minimax with 3 agents (red ghost, cyan ghost and pacman)

## Efficiency

Just like (exhaustive) DFS
- Time: $\mathcal{O}(b^m)$
- Space: $\mathcal{O}(bm)$
