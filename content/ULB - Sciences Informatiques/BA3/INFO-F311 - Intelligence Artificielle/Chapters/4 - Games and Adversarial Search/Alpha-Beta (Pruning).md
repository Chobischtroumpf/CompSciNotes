---
title: Alpha-Beta (Pruning)
authors: Mihai Bors
tags:
  - AI
---


$\alpha$ = best option so far from any max node on this path

![[09f77ac33d0fc3c01a73b483f5f91064.png]]
Example

The order of generation matters: more pruning is possible if good moves come first

## How it works(?)

General case (pruning children of MIN node)
- We'sre computing the min value at some node $n$
- We're looping over $n$'s children
- $n$'s estimate of the children's min is dropping
- Who cares about $n$'s value? MAX
- Let $\alpha$ be the best value that MAX can get so far at any choice point along the current path from the root
- If $n$ becomes worse than $\alpha$, MAX will avoid it, so we can prune $n$'s other children (it’s already bad enough that it won't be played)

Pruning children of MAX node is symmetric
- Let $\beta$ be the best value that MIN can get so far at any choice point along the current path from the root

![[27759291558b4df3e3cc0be5eac3f7e5.png]]

## Implementation

- $\alpha$: MAX’s best option on path to root
- $\beta$: MIN’s best option on path to root
- Initial value $\alpha = -\infty$ , $\beta = +\infty$

```python
def max_value(state, α, β):
	if state.terminal return state.utility
	v = -infty
	for s in state.successors:
		v = max(v, min_value(s, α, β))
		if v >= β
			return v
		α = max(α, v)
	return v
```

```python
def min_value(state , α, β):
	if state.terminal return state.utility
	v = +infty
	for s in state.successors:
		v = min(v, max_value(s, α, β))
		if v <= α
			return v
		β = min(β, v)
	return v
```

## Properties

> [!abstract] Theorem
> This pruning has no effect on minimax value computed for the root!

Good child ordering improves effectiveness of pruning
- Iterative deepening helps with this

With "perfect ordering":
- Time complexity drops to $\mathcal{O}(b^{m / 2})$
- Doubles solvable depth!
