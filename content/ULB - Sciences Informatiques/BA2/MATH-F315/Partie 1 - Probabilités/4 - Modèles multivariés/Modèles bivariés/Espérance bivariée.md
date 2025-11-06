---
title: Espérance bivariée
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Espérance d'un vecteur bivarié
> Considérez le vecteur bivarié aléatoire $\underline X = [X,Y]^\top$. L'[[Espérance (expected value)#^c716f7|espérance]] de $\underline X$ est aussi un vecteur avec éléments qui correspondent aux [[Espérance (expected value)#^c716f7|espérances]] de $X_1$ et $X_2$:
>
> $$\mathbb{E}[\mathbf{X}] =
> \begin{bmatrix}
> \mathbb{E}[X] \\
> \mathbb{E}[Y]
> \end{bmatrix} =
> \begin{bmatrix}
> \mu_X \\
> \mu_Y
> \end{bmatrix} =
> \begin{bmatrix}
> \int_{-\infty}^\infty \int_{-\infty}^\infty z_1 f_{X,Y}(z_1, z_2) \, dz_1 dz_2 \\
> \int_{-\infty}^\infty \int_{-\infty}^\infty z_2 f_{X,Y}(z_1, z_2) \, dz_1 dz_2
> \end{bmatrix}
> $$

> [!tip]+ Alternative pour calculer les [[Espérance (expected value)#^c716f7|espérances]]
> 1. Trouver la [[Fonction de masse marginale (continue)#^b8ab39|loi marginale]]
> $$f_X(x) = \int_{-\infty}^\infty f_{X,Y}(x,z_2) \ dz_2$$
> 2. Calculer l’[[Espérance (expected value)#^c716f7|espérance]]
> $$\mathbb{E}(X) = \int_{-\infty}^\infty z_1 f_X(z_1) \ dz_1$$

> [!info]+ Espérance d’une fonction d’un vecteur bivarié
> Soit $W = w(X,Y)$, alors
> $$\mathbb{E}(W) = \mathbb{E}(w(X,Y)) = \int_{-\infty}^\infty \int_{-\infty}^\infty w(x,y) f_{X,Y}(x,y) \ dx \ dy$$

> [!abstract]- Propriétés de l’[[Espérance (expected value)#^c716f7|espérance]]
> 1. Preuve de [[Espérance (expected value)#^446fba|la somme des espérances]] (cas discret):
> $$\begin{aligned}
> \mathbb{E}[X + Y] &= \sum_{x, y} (x + y) \, p_{X, Y}(x, y) \\
> &= \sum_x \sum_y x p_{X, Y}(x, y) + y p_{X, Y}(x, y) \\
> &= \mathbb{E}[X] + \mathbb{E}[Y]
> \end{aligned}$$
>
> 2. Preuve du [[Espérance (expected value)#^c817fc|produit des espérances]] (cas discret):
> $$\begin{aligned}
> \mathbb{E}[X \cdot Y] &= \sum_{x, y} (x \cdot y) \cdot p_{X, Y}(x, y) \\
> &= \sum_x \sum_y \big( x \cdot p_X(x) \big) \cdot \big( y \cdot p_Y(y) \big) \\
> &= \mathbb{E}[X] \cdot \mathbb{E}[Y]
> \end{aligned}
> $$
