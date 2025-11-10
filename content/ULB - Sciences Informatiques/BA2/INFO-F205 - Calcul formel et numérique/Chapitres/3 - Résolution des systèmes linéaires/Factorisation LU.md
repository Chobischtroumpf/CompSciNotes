---
title: Factorisation LU
authors: Alessandro Dorigo
tags:
  -
---


> [!info]+ Définition
> La factorisation LU consiste à décomposer une matrice $A$ en un produit d'une matrice triangulaire inférieure $L$ (avec des 1 sur la diagonale) et une matrice triangulaire supérieure $U$ :
>
> $$A = LU$$
> La résolution du système $Ax = b$ devient alors équivalente à résoudre deux systèmes triangulaires :
> 1. $Ly = b$ (substitution progressive)
> 2. $Ux = y$ (substitution rétrograde)

> [!abstract]- Determinant et factorisation LU
> Étant donnée la factorisation $A = LU$, où $L$ est triangulaire inférieure avec $l_{ii} = 1$ et $U$ est triangulaire supérieure :
>
> $$\det(A) = \det(L)\det(U) = \prod_{k=1}^{n} u_{kk}$$

![[Méthodes directes pour la factorisation LU]]

> [!abstract]- Stabilité de la factorisation LU
> Soit $\hat{L}$ et $\hat{U}$ les matrices résultant de la factorisation LU calculée en virgule flottante. Alors : $$\hat{L}\hat{U} = A + \Delta$$ où $|\Delta| \leq \gamma_n|\hat{L}||\hat{U}|$, et $\gamma_n = \frac{nu}{1-nu}$.
