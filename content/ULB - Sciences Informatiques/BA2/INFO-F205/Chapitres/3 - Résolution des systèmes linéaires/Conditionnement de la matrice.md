---
title: Conditionnement de la matrice
authors: Alessandro Dorigo
tags: []
---

Le conditionnement $\kappa(A)$ joue un rôle crucial :

- Un $\kappa(A)$ proche de 1 indique un problème bien conditionné
- Un $\kappa(A)$ grand indique un problème mal conditionné, sensible aux erreurs

Pour des matrices spéciales :

- Matrices orthogonales : $\kappa_2(A) = 1$ (conditionnement optimal)
- Matrices de Hilbert : $\kappa_2(H_n)$ croît très rapidement avec $n$ (très mal conditionnées)
- Matrices de Vandermonde : le conditionnement dépend des points $x_i$ et peut être très élevé si deux points sont proches
