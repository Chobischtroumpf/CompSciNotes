---
title: Fonction de répartition marginale (discrète)
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Définition
> Pour des [[Variable aléatoire#^dcd8d2|variables aléatoires]] discrètes $X$ et $Y$, les **fonctions de répartition marginales** permettent de déterminer la probabilité cumulative associée à $X$ ou $Y$, indépendamment de l'autre variable.

^eaea22

> [!abstract]- Fonction de répartition marginale de $X$
> La fonction de répartition marginale de $X$, notée $F_X(x_i)$, est définie comme la probabilité cumulative que $X$ prenne une valeur inférieure ou égale à $x_i$, indépendamment de $Y$:
> $$F_X(x_i) = \mathbb{P}(X \leq x_i) = \sum_{k=1}^i \sum_{l=1}^\infty p_{X,Y}(x_k, y_l)$$
>
> En simplifiant, cette somme devient:
> $$F_X(x_i) = \sum_{k=1}^i p_X(x_k)$$
>
> où $p_X(x_k)$ est la [[Fonction de masse marginale (continue)#^d2486d|fonction de masse marginale]] de $X$.

^cb4dc6

> [!abstract]- Fonction de répartition marginale de $Y$
> $$F_Y(y_j) = \mathbb{P}(Y \leq y_j) = \sum_{l=1}^j \sum_{k=1}^\infty p_{X,Y}(x_k, y_l)$$
>
> En simplifiant, cette somme devient:
> $$F_Y(y_j) = \sum_{l=1}^j p_Y(y_l)$$
>
> où $p_Y(y_l)$ est la [[Fonction de masse marginale (discrète)#^82e8ae|fonction de masse marginale]] de $Y$.
