---
title: Méthodes itératives
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> Une méthode itérative de la forme:
>
> $$x^{(k+1)} = Bx^{(k)} + f$$
>
> est dite consistante avec le problème $Ax = b$ si $f$ et $B$ sont tels que $x = Bx + f$.
>
> Une méthode itérative est dite convergente si $\lim_{k\to\infty} e^{(k)} = 0$, où $e^{(k)} = x^{(k)} - x$.

> [!abstract]- Convergence
> Si la méthode itérative est consistante, alors elle est aussi convergente si et seulement si $\rho(B) < 1$, où $\rho(B)$ est le rayon spectral de $B$.

![[Méthode de Jacobi]]

![[Méthode de Gauss-Seidel]]

> [!abstract]- Convergence de Jacobi et Gauss-Seidel
> Si $A$ est une matrice à diagonale dominante stricte, les méthodes de Jacobi et Gauss-Seidel sont convergentes.
>
> Si $A$ est une matrice symétrique définie positive, la méthode de Gauss-Seidel est convergente.
