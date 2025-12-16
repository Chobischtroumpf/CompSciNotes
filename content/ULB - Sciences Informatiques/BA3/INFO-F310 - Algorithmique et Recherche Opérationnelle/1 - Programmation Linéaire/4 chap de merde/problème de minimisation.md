---
title: problème de minimisation
authors: iamscrambledeggs
tags: []
---

# problème de minimisation
## sous forme canonique
- problème primal
	- $n$ var primales et $m$ contraintes ($m \lt n$)
		- $c,x \in \mathbb{R}^{n}$
		- $b \in \mathbb{R}^{m}$
		- $A \in \mathbb{R}^{m \times n}$
	- $\min c^T x$
		- $Ax \leq b$
		- $x \geq 0$
- problème dual
	- $m$ variable duales et $n$ contraintes ($m \lt n$)
		- $c \in \mathbb{R}^{n}$
		- $b,y \in \mathbb{R}^{m}$
		- $A \in \mathbb{R}^{m \times n}$
	- $\max b^T y$
		- $A^T y \leq c$
			- $y \geq 0$
##  sous forme standard
- problème primal
	- $n$ var primales et $m$ contraintes ($m \lt n$)
		- $c,x \in \mathbb{R}^{n}$
		- $b \in \mathbb{R}^{m}$
		- $A \in \mathbb{R}^{m \times n}$
	- $\min c^T x$
		- $Ax = b$
		- $x \geq 0$
- problème dual
	- $m$ variable duales et $n$ contraintes ($m \lt n$)
		- $c \in \mathbb{R}^{n}$
		- $b,y \in \mathbb{R}^{m}$
		- $A \in \mathbb{R}^{m \times n}$
	- $\max b^T y$
		- $A^T y \leq c$
		- $y$ non-restreinte
