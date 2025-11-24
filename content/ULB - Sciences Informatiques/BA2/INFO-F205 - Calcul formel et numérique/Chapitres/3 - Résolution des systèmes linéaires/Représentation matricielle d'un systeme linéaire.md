---
title: Représentation matricielle d'un systeme linéaire
authors: Alessandro Dorigo
tags:
  -
---

La représentation matricielle d'un système linéaire s'écrit :

$$Ax = b$$

où $A \in \mathbb{R}^{n \times m}$ est la matrice des coefficients, $x \in \mathbb{R}^{m \times 1}$ est le vecteur des inconnues et $b \in \mathbb{R}^{n \times 1}$ est le vecteur du second membre.

> [!abstract]- Théorème "Solution d'un système linéaire"
> La solution d'un système linéaire carré existe et est unique si une des conditions équivalentes suivantes est remplie :
>
> - $A$ est inversible
> - $A$ est régulière (non singulière), c.-à-d. $\det(A) \neq 0$
> - le rang $\text{rg}(A) = n$
> - le système homogène $Ax = 0$ admet seulement la solution nulle
> D'après la formule de Cramer, la solution du système est :
> $$x_j = \frac{\Delta_j}{\det(A)}, \quad j = 1, 2, \ldots, n$$
> où $\Delta_j$ est le déterminant de la matrice obtenue en remplaçant la $j$-ième colonne de la matrice $A$ par le vecteur $b$.
