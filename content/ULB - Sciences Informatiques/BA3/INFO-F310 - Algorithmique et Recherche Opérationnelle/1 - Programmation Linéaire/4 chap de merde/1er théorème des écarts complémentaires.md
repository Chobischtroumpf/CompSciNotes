---
title: 1er théorème des écarts complémentaires
authors: iamscrambledeggs
tags: []
---

- soit la paire primal-duale
	- $\max c^Tx$
		- $Ax = b$
		- $x \geq 0$
	- $\min b^Ty$
		- $A^Ty \geq c$
# premier théorème des écarts complémentaires
- Si
	- $x$ une solution admissible du primal
	- $y$ une solution admissible du dual
- alors
	- une condition nécessaire suffisante (CNS) pour que x et y soient optimales simultanéments est que pour tout j = 1,...,n
		- $x_j \gt 0 \to a_j^Ty = c_j$
		- $a_j^Ty \gt c_j \to x_j = 0$
