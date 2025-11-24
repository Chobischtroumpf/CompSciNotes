---
title: Méthode de Jacobi
authors: Alessandro Dorigo
tags:
  -
---

La méthode de Jacobi calcule $x^{(k+1)}$ par :

$$x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j=1,j\neq i}^{n} a_{ij}x_j^{(k)}\right), \quad i = 1,\ldots,n$$

La matrice d'itération est $B_J = D^{-1}(D - A) = I - D^{-1}A$, où $D = \text{diag}(A)$.
