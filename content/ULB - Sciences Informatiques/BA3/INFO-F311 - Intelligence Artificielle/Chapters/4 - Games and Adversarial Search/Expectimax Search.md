---
title: Expectimax Search
authors: Mihai Bors
tags:
  - AI
---


- Uncertain outcomes controlled by chance, not an adversary

We can't know the results of actions, due to things such as randomness, unpredictable opponents or simply due to failures (actions fail due to a certain error or model of the world)

The values should reflect average-case outcomes, not worst-case ones ([[Minimax Search|minimax]])

- Compute average score under optimal play
	- Max nodes are the same
	- Chance nodes are like min nodes but the outcome is uncertain
	- Calculate their expected utilities

![[Pasted image 20251111135158.png]]
Here for example, we have a max node followed by two chance nodes with 10 / 10 and 9 / 100. We don't know the probabilities, so we can just do 10 + 10 / 2 for the left utility and 9 + 100 / 2 for the right one. The max node will obviously pick the second one

## Implementation

```python
def value(state):
	if state.terminal: return state.utility
	if agent.max: return max_value(state)
	if agent.exp: return exp_value(state)
```

```python
def max_value(state):
	v = -infty
	for s in state.successors:
		v = max(v, min_value(s))
	return v
```

```python
def exp_value(state):
	v = 0
	for s in state.successors:
		p = probability(s)
		v += p * s.value
	return v
```

![[Pasted image 20251111135715.png]]
$$v = (1/2) (8) + (1/3) (24) + (1/6) (-12) = 10$$

- We can't do expectimax pruning. What if the next value is 5 million?

- Expectimax is usually depth-limited, we use a function to estimate the true expectimax value of utilities to avoid big computational costs

## Model

In expectimax, we have a probabilistic model of how the opponent (or environment) will behave at any state
- Could be a simple uniform distribution
- Could be sophisticated

Let’s say you know that your opponent is actually running a depth 2 minimax, using the result 80% of the time, and moving randomly otherwise

- Question: What tree search should you use?
- Expectimax! We need to figure out each chance node's probabilities, which means running a simulation of the opponent (depth-limited to avoid slowness)

## Comparison

**Minimax:** Dangerous pessimism - assuming the worst case when it's not likely
**Expectimax:** Dangerous optimism - assuming chance when the world is adversarial

![[Pasted image 20251111140622.png]]
Results from playing 5 pacman games with pacman being either minimax or expectimax and the ghost being adversarial or random
