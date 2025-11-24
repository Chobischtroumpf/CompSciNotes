---
title: Méthode par perturbation
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


Lorsqu'une somme possède une structure simple, il peut être utile de la **"perturber"** pour simplifier le calcul en manipulant la somme de manière à obtenir une expression plus compacte.

> [!info]+ Définition
> La **méthode par perturbation** consiste ici à multiplier la somme par un paramètre $x$, puis à utiliser la différence entre la somme initiale et cette nouvelle expression. Cela simplifie le calcul de certaines [[Série géométrique|séries géométriques]].

> [!abstract]- Théorème 6.2.1
> Pour tout $n \geq 1$ et tout $x \neq 1$,
> $$\sum_{k=0}^{n-1} x^k = \frac{1 - x^n}{1 - x}$$
>
> **Démonstration:**
> 1. On pose $S := \sum_{k=0}^{n-1} x^k$
> 2. En multipliant $S$ par $x$ à gauche, on obtient:
> $$S = 1 + x + x^2 + \cdots + x^{n-1}$$
> $$xS = x + x^2 + x^3 + \cdots + x^n$$
> 3. En soustrayant $xS$ de $S$, on obtient:
> $$S - xS = 1 - x^n \Rightarrow S = \frac{1 - x^n}{1 - x} \quad \square$$

^ad038b

> [!example]+ Exemple
> ![[59f4d489521e0b998e1cb34ed66534d1.png]]
> ![[01a1a8524f7eeb895951a84d5828bd56.png]]
