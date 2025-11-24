---
title: Conditionnement d'une matrice
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> Le conditionnement d'une matrice est défini par
> $$\kappa_p(A) = |A|_p |A^{-1}|_p$$
> où $|\cdot|_p$ est une norme matricielle.
> ### Propriétés du conditionnement :
> - $\kappa_p(A) \geq 1$, puisque $1 = |I| = |A \cdot A^{-1}| \leq |A| \cdot |A^{-1}| = \kappa(A)$
> - $\kappa_p(\alpha A) = \kappa_p(A), \forall \alpha \in \mathbb{R}$
> - $\kappa_p(A) = \kappa_p(A^{-1})$
> - Si $A$ est une matrice orthogonale, alors $\kappa_2(A) = 1$
> - Pour $p = 2$, $\kappa_2(A) = \frac{\sigma_1(A)}{\sigma_n(A)}$ où $\sigma_1(A)$ est la plus grande valeur singulière et $\sigma_n(A)$ est la plus petite

> [!tip]+ Remarque Le conditionnement exprime la sensibilité de la solution du système $Ax = b$ aux perturbations des données. Plus $\kappa_p(A)$ est grand, plus la solution est sensible.
