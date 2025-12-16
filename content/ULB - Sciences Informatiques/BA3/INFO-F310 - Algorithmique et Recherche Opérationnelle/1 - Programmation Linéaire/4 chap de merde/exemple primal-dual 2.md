---
title: exemple primal-dual 2
authors: iamscrambledeggs
tags: []
---

# exemple

- problème primal
	- $\max z = 5x_1 + 12x_2 + 4x_3$
		- $x_1 + 2x_2 + x_3 \leq 10$
			- $(y_1)$
		- $2x_1 - x_2 + 3x_3 = 8$
			- $(y_2)$
		- $x_1,x_2,x_3 \geq 0$
- problème dual
	- $\min w = 10y_1 + 8y_2$
		- $y_1 + 2y_2 \geq 5$
			- $(x_1)$
		- $2y_1 - y_2 \geq 12$
			- $(x_2)$
		- $y_1 + 3y_2 \geq 4$
			- $(x_3)$
		- $y_1 \geq 0$
