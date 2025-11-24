---
title: Fonction de densité jointe bivariée
authors: Alessandro Dorigo
tags:
  - Proba
---


Soient $X$ et $Y$ deux [[Variable aléatoire#^dcd8d2|variables aléatoires]] continues.

> [!info]+ Définition
> La **fonction de densité jointe** de $X$ et $Y$ est définie comme la dérivée partielle seconde de la [[Fonction de répartition jointe bivariée#^398bb0|fonction de répartition jointe]] $F_{X,Y}(x, y)$:
> $$f_{X,Y}(x, y) = \frac{\partial}{\partial x} \frac{\partial}{\partial y} F_{X,Y}(x, y)$$
>
> Elle représente la densité de probabilité conjointe de $X$ et $Y$ en un point $(x, y)$.

^a838ff

> [!note]
> La [[Fonction de répartition jointe bivariée#^398bb0|fonction de répartition jointe]] peut être exprimée comme une intégrale double de la fonction de densité jointe $f_{X,Y}(z_1, z_2)$:
> $$F_{X,Y}(x, y) = \int_{-\infty}^y \int_{-\infty}^x f_{X,Y}(z_1, z_2) \ dz_1 \ dz_2$$

> [!tip]+ Important
> La densité jointe doit s’intégrer à 1 sur tout l’espace:
> $$\int_{-\infty}^\infty \int_{-\infty}^\infty f_{X,Y}(x, y) \ dx \ dy = 1$$
