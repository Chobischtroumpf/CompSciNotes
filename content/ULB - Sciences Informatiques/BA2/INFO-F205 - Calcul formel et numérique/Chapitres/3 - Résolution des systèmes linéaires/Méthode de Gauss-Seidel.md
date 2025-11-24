---
title: Méthode de Gauss-Seidel
authors: Alessandro Dorigo
tags:
  -
---


La méthode de Gauss-Seidel utilise les valeurs $x_i^{(k+1)}$ déjà calculées :

$$x_i^{(k+1)} = \frac{1}{a_{ii}}\left(b_i - \sum_{j=1}^{i-1} a_{ij}x_j^{(k+1)} - \sum_{j=i+1}^{n} a_{ij}x_j^{(k)}\right), \quad i = 1,\ldots,n$$

La matrice d'itération est $B_{GS} = (D - E)^{-1}F$, où $D - A = E + F$, avec $E$ triangulaire inférieure stricte et $F$ triangulaire supérieure stricte.
