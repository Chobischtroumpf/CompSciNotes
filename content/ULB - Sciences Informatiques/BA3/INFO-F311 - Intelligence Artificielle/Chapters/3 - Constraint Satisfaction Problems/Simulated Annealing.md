---
title: Simulated Annealing
authors: Mihai Bors
tags:
  - AI
---


Escape local maxima by allowing downhill moves.

```
function Simulated-Annealing(problem, schedule) returns a solution state
	inputs: problem, a problem
			schedule, a mapping from time to "temperature"
	local variables: current, a node
					 next, a node
					 T, a "temperature" controlling prob. of downward steps
	current <- Make-Node(Initial-State[problem])
	for t <- 1 to inf do
		T <- schedule[t]
		if T = 0 then return current
		next <- a randomly selected successor of current
		deltaE <- Value[next] - Value[current]
		if deltaE > 0 then current <- next
		else current <- next only with probability e^{deltaE/T}
```
