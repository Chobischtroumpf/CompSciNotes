---
title: 2e théorème des écarts complémentaires
authors: iamscrambledeggs
tags: []
---

- soit la paire primal-duale
	- $\max c^Tx$
		- $Ax = b$
		- $x \geq 0$
	- $\min b^Ty$
		- $A^Ty \geq c$

# 2e th des écarts complémentaires
- Si
	- $x$ une solution admissible du primal
	- $y$ une solution admissible du dual
- alors
	- une condition nécessaire suffisante (CNS) pour que x et y soient optimales simultanéments est que
		- pour tout j = 1,...,n
			- $x_j \gt 0 \to a_j^Ty = c_j$
			- $a_j^Ty \gt c_j \to x_j = 0$
		- pour tout i=1,..m : $y_i(a_i^Tx - b_i) = 0$
			- $y_i \gt 0 \implies a_i^Tx=b_i$
			- $a_i^Tx \lt b_i \implies y_i=0$


## exemple

- (P) dont solution réalisable
	- $(x_1,x_2) = (\frac{3}{2}, \frac{3}{4})$
- $\min z = 6x_1 + 9x_2$
	- $20 x_1 + 5x_2 \geq 25$
	- $30x_1 + 20x_2 \geq 60$
	- $5x_1 + 10x_2 \geq 15$
	- $x_1,x_2 \geq 0$
→ formuler le dual (D) du PL (P)
- $\max w = 25y_1 + 60y_2 + 15y_3$
	- $20y_1 + 30y_2 + 5y_3 \leq 6$
	- $5y_1 + 20y_2 + 10 y_3 \leq 9$
	- $y_1,y_2,y_3 \leq 0$
- $\forall i = 1:m : y_i(a_i^Tx - b_i) = 0$
	- → $y_1 (20x_1+ 5x_2 - 25) = 0$
	- → $y_2 (30x_1 + 20x_2 - 60) = 0$
	- → $y_3(5x_1 + 10x_2 - 15) = 0$
- → substituer $(x_1,x_2)$
	- → $\frac{35y_1}{4} = 0 → y_1 = 0$
	- → $0 y_2 = 0 → y_2 \neq 0$
	- → $0y_3 = 0 → y_3 \neq 0$
- $\forall j= 1:n : x_j(a^T_j y- c_j) = 0$
	- → $x_1(20y_1 + 30y_2+ 5y_3 - 6) = 0$
	- → $x_2 (5y_1 + 20y_2 + 10y_3 - 9) = 0$
- → substituer $(x_1,x_2)$ et $y_1 = 0$
	- → $\frac{3}{2}(30y_2 + 5y_3 - 6) = 0$
	- → $\frac{3}{4}(20y_2 + 10y_3 - 9) = 0$
- → résolution d'un sys ) deux équations
	- → $y_2 = \frac{3}{40}$
	- → $y_3 = \frac{9}{12} = \frac{3}{4}$
- → solution du dual (D)
	- $(y_1,y_2,y_3) = (0, \frac{3}{40}, \frac{3}{4})$
