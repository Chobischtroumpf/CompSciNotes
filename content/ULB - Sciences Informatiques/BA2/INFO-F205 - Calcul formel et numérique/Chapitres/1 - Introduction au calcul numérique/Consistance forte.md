---
title: Consistance forte
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Définition
> Un **algorithme est fortement consistant** si la solution exacte $\vec{x}$ est une solution de **tous** les sous-problèmes $F_n(x, \vec{d}^{(n)}) = 0$ pour tout $n$.
> $$\lim_{n\to\infty} F_n(\vec{x}^{(n)}, \vec{d}^{(n)}) = F(x, \vec{d}^{(n)}) = 0$$
>
> C'est-à-dire si la solution exacte $x$ du problème est une solution de $F_n(\vec{x}^{(n)}, \vec{d}^{(n)}) = \vec{0}$ pour $n \to \infty$.

^77e44d

> [!tip]+ Remarque
> - La [[Consistance#^77e44d|consistance]] simple assure que $x$ est une solution **asymptotique**.
> - La **consistance forte** garantit que $x$ est **toujours** une solution intermédiaire.
