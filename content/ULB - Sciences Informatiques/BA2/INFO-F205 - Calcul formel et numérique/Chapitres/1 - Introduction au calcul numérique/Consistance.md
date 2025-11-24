---
title: Consistance
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Définition
> Un algorithme $F_n(\vec{x}^{(n)}, \vec{d}^{(n)})$ est dit **consistant** si:
> $$\lim_{n\to\infty} F_n(\vec{x}, \vec{d}^{(n)}) = F(\vec{x}, \vec{d}) = 0$$
> C'est-à-dire si la solution exacte $x$ du problème est une solution de $F_n(\vec{x}^{(n)}, \vec{d}^{(n)}) = 0$ pour $n \to \infty$

^77e44d

> [!tip]+ Remarque
> Être consistant **ne garantit pas** que $\vec{x}^{(n)}$ converge vers $x$, mais seulement que la solution du problème global est incluse dans les solutions des sous-problèmes.
