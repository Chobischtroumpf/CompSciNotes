---
title: exemple solutions optimales multiples
authors: Mihai Bors
tags: []
---

# solutions optimales multiples
- $\max z = 2x_1 + 4x_1$
	- $x_1 + 2x_2 \leq 5$
	- $x_1 + x_2 \leq 4$
	- $x_1, x_2 \geq 0$
- → $\max z = 2x_1 + 4x_2$
	- $x_1 + 2x_2 + s_1 = 5$
	- $x_1 + x_2 + s_2 = 4$
	- $x_1,x_2,s_1,s_2 \geq 0$
![[7833e29aa90ab6f3939b0271cacb16f0.png]]
- solution optimale : toutes les combi convexes de sommets optimaux
	- $x_1 = 0\alpha + 3(1-\alpha) = 3 - 3\alpha$
	- $x_2 = \frac{5}{2}\alpha + 1(1 - \alpha) = 1 + \frac{3}{2}\alpha$
		- $0 \leq \alpha \leq 1$
