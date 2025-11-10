---
title: Convergence
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Définition
> Avec $\bar{x}^{(n)} = \vec{x}^{(n)} + \delta \vec{x}^{(n)}$ étant la suite des solutions approchées produites par un algorithme suite aux perturbations $\{\delta \vec{d}^{(i)}\}, i = 1, \dots, n$ des données:
>
> On dit qu'un algorithme est **convergent** si:
> $$\lim_{n\to\infty, \delta \vec{d}^{(n)} \to 0} \bar{x}^{(n)} = \lim_{n\to\infty, \delta \vec{d}^{(i)}\to 0} \vec{x}^{(n)} + \delta \vec{x}^{(n)} = \vec{x}$$
>
> Soit que si pour chaque $\epsilon > 0$ il existe $\nu > 0$

^6240b2

> [!tip]+ Remarque
> Les concepts de [[Stabilité#^f6ba30|stabilité]] et convergence sont fortement liés. La [[Stabilité#^f6ba30|stabilité]] assure que de petites perturbations dans les données n'entraînent pas de grandes variations dans la solution, tandis que la convergence garantit que la solution approchée tend vers la solution exacte quand le paramètre $n$ augmente.
