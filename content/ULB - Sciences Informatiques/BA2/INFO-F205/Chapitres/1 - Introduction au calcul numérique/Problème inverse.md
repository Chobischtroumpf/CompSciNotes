---
title: Problème inverse
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Définition
> Problème qui comprend l’inversion d’un opérateur, où l’application de l’opérateur est relativement simple, tandis que son inversion est compliquée.
>

Donc les observations sont en fonction de $\vec{d} = G(\vec{x})$, l’évaluation en fonction de $G(\vec{x})$, $\vec{x}$ est facile, mais on recherche $\vec{x} = G^{-1}(\vec{d})$. La complication provient (souvent) du fait que plusieurs valeurs de $\vec{x}$ produisent (presque) le même $\vec{d}$.

> [!tip]+ Remarque
> Les problèmes inverses sont souvent [[Problèmes bien ou mal posés|mal posés]]. Un problème inverse est mal posé quand deux valeurs différentes de $d$ produisent le même $x$.

> [!example]+ Exemples de problèmes inverses mal posés:
> - Trouver la position d'un obstacle à partir de l'information radar;
> - Trouver une information sur une scène 3D à partir d'une image 2D;
> - Trouver la température d'une barre métallique en connaissant la température en une autre position.
