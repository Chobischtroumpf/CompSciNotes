---
title: forme standard
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---

- prb à $n$ var ($x \in R^n$) sujet à $m$ contraintes ($b \in R^m$) et $A \in R^{m \times n}$
	- rep matricielle
		- maximize (or minimize) $c^T x$
		- subject to $x \geq 0, Ax = b$
	- rep indicielle
		- maximize (or minimize) $\sum_{j=1}^n c_jx_j$
		- subject to $\sum_{j=1}^n a_{ij}x_j = b_i, \forall i \in \set{1,...,m}$
		- $x_j \geq 0, \forall j \in \set{1,...,n}$
