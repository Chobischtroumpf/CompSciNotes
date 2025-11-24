---
title: Divisibilité
authors: Alessandro Dorigo
tags:
  - MathDis
  - TheorieDesNombres
---


> [!info]+ Définition
> Soient $a$ et $b$ deux entiers. On dit que **$a$ divise $b$**, noté $a \mid b$, s'il existe un entier $k$ tel que $b = a \cdot k$.

^7f33d2

> [!tip]+ Corollaires
> - Si $a \mid b \land b \mid c$, alors $a \mid c$.
> - Si $a \mid b \land a \mid c$, alors $a \mid sb + tc$ pour tout $s,t$.
> - Pour tout $c \neq 0, a \mid b$ ssi $ca \mid cb$.
> 	- Si $a$ divise $b$ et $c$, alors $a$ divise toute combinaison linéaire de $b$ et $c$.

> [!info]+ Définition (algorithme de division)
> **Énoncé**: Soient $n \in \mathbb{Z}$ et $d \in \mathbb{Z}_{0}$. Il existe un unique couple d'entiers $(q, r)$ tel que:
> $$n = q \cdot d + r \quad \text{avec} \quad 0 \leq r < |d|$$
> où $q$ est le quotient et $r$ est le reste de la division euclidienne de $n$ par $d$.
