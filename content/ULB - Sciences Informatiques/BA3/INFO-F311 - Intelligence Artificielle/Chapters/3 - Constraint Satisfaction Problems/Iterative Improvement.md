---
title: Iterative Improvement
authors: Mihai Bors
tags:
  - AI
---


- Take an assignment with unsatisfied constraints
- Operators reassign variable values

```
while not solved
	randomly select any conflicted variable
	min-conflicts heuristic
		choose a value that violates the fewest constraints
```

## 4-Queens

> [!example] Problem Space
> **States:** 4 queens in 4 columns ($4^4 = 256$ states)
> **Operators:** move queen in column
> **Goal test:** no attacks
> **Evaluation:** $c(n) =$ number of attacks

### Performance of Min-Conflicts

Given random initial state, can solve $n$-queens in almost constant time for arbitrary $n$ with high probability.

The same appears to be true for any randomly-generated CSP except in a narrow range of the ratio

$$R = \frac{\text{number of constraints}}{\text{number of variables}}$$

![[Pasted image 20251106132558.png]]
