---
title: exemple primal dual 1
authors: iamscrambledeggs
tags: []
---

## production de peinture
- problème primal suivant
	- $\max z = 5x_1 + 4x_2$
		- $6x_1 + 4x_2 \leq 24$
			- $(C_1)$
		- $x_1 + 2x_2 \leq 6$
			- $(C_2)$
		- $x_2 \leq 2$
			- $(C_3)$
		- $-x_1 + x_2 \leq 1$
			- $(C_4)$
		- $x_1,x_2 \geq 0$

## trouver borne sup à la valeur optimale $z^*$ de $z$
- en multipliant $C_2$ par 5
	- $5x_1 + 10 x_2 \leq 30$
	- $z = (5x_1 + 4x_2) \leq z^* (= 5x_1 + 10x_2) \leq 30 (= 5 \times 6)$
- en multipliant $C_1$ par $\frac{5}{6}$ et additionnant $C_3$ avec
	- $5x_1 + \frac{13}{3}x_2 \leq 22$
	- $z (= 5x_1 + 4x_2) \leq z^* (= 5x_1 + \frac{13}{3}x_2) \leq 22 (= \frac{5}{6}\times 24 + 2)$
- en mul $C_1$ par $\frac{3}{4}$ et $C_2$ par $\frac{1}{2}$ et en additionant les deux termes
	- $\frac{3}{4}C_1 + \frac{1}{2}C_2$
		- $= \frac{3}{4}(6x_1 + 4x_2) + \frac{1}{2}(x_1 + 2x_2)$
		- $= 5x_1 + 4x_2 \leq \frac{3}{4}\times 24 + \frac{1}{2}\times 6$
	- $z = z^* = 5x_1 + 4x_2 \leq 21 (= \frac{3}{4}\times 24 + \frac{1}{2} \times 6)$

## coeff combinaison linéaire
$y_1 (6x_1 + 4x_2) + y_2 (x_1 + 2x_2) + y_3(x_2) + y_4(-x_1 + x_2) \leq 24 y_1 + 6y_2 + 2y_3 + y_4$
- $\Leftrightarrow (6y_1 + y_2 - y_4)x_1 + (4y_1 + 2y_2 + y_3 + y_4)x_2 \leq 24y_1 + 6y_2 + 2y_3 + y_4$
	- → pour que $5x_1 + 4x_2 = z \leq 24y_1 + 6y_2 + 2y_3 + y_4$
		- coeff de $x_1, x_2$ doivent être inférieurs au coeff correspondant dans $z$
→ donc trouver la plus petite borne sup pour $z$ revient à résoudre le problème dual
- $\min w = 24 y_1 + 6y_2 + 2y_3 + y_4$
	- $6y_1 + y_2 - y_4 \geq 5$
	- $4y_1 + 2y_2 + y_3 + y_4 \geq 4$
	- $y_1,y_2,y_3,y_4 \geq 0$
