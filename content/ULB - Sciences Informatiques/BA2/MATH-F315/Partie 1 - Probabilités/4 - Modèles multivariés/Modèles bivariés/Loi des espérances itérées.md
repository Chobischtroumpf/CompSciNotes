---
title: Loi des espérances itérées
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Définition
> Pour toute pair de [[Variable aléatoire#^dcd8d2|v.a.]] $X$ et $Y$, la **loi des espérances itérées** est donnée par:
>
> $$\mathbb{E}[\mathbb{E}[X \vert Y]] = \mathbb{E}[X]$$
> on a également
> $$\mathbb{E}[\mathbb{E}[Y \vert X]] = \mathbb{E}[Y]$$

> [!abstract]- Théorème "Loi des espérances itérées"

> Soit $X$ et $Y$ deux variables aléatoires. Alors :
> $$
> \mathbb{E}(\mathbb{E}(X|Y)) = \mathbb{E}(X)
> $$

La preuve se décompose en 5 étapes:

1) On part de l'espérance conditionnelle:
$$
\mathbb{E}(\mathbb{E}(X|Y)) = \mathbb{E}\left(\int_x xf_{X|Y}(x|Y)dx\right) \stackrel{(1)}{=} \int_y \int_x xf_{X|Y}(x|Y=y)f_Y(y)dxdy
$$

2) On utilise la définition de la densité conditionnelle:
$$
\stackrel{(2)}{=} \int_y \int_x xf_{X,Y}(x,y)dxdy
$$

3) On applique le théorème de Fubini pour réorganiser les intégrales:
$$
\stackrel{(3)}{=} \int_x x\left(\int_y f_{X,Y}(x,y)dy\right)dx
$$

4) On utilise la définition de la densité marginale:
$$
\stackrel{(4)}{=} \int_x xf_X(x)dx
$$

5) On obtient l'espérance de $X$:
$$
\stackrel{(5)}{=} \mathbb{E}(X)
$$

> [!info]+ Définition
> La densité marginale $f_X(x)$ est définie par :
> $$
> f_X(x) = \int_y f_{X,Y}(x,y)dy
> $$

> [!tip]+ Remarque
> Cette preuve utilise plusieurs fois la définition de l'espérance comme l'intégrale du produit d'une variable par sa densité de probabilité.

![[Pasted image 20241125095220.png]]
