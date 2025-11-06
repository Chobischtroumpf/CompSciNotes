---
title: Local Search
authors: Mihai Bors
tags:
  - AI
---


Idea is to improve a single option until we can't make it better contrary to tree search where we keep unexplored alternatives on the fringe

New successor function: local changes

![[Pasted image 20251106133000.png]]

- Much faster and more memory efficient (but incomplete and suboptimal)

## Hill Climbing

1. Start wherever
2. Move to the best neighboring state
3. If no neighbors better, quit

```
function Hill-Climbing(problem) returns a state
	current <- make-node(problem.initial-state)
	loop do
		neighbor <- a highest-valued successor of current
		if neighbor.value <= current.value then
			return current.state
		current <- neighbor
```

"Like climbing Everest in thick fog with amnesia"

![[Pasted image 20251106133306.png]]
Hill Climbing Diagram
