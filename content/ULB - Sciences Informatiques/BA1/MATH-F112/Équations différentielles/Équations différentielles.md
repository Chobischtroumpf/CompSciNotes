---
title: Équations différentielles
authors: Alessandro Dorigo
tags:
  - Maths
---


> [!info]+ Équation Différentielle Ordinaire (EDO)
> Une **équation différentielle ordinaire (EDO)** est une équation qui relie une fonction $y(x)$ et ses dérivées successives par rapport à une variable $x$. Elle s’écrit sous la forme générale:
> $$F(x, y, y', y'', \dots, y^{(n)}) = 0$$
>
> où:
> - $F$ est une fonction donnée,
> - $y' = dy/dx$ est la dérivée première de $y$ par rapport à $x$,
> - $y'', y^{(3)}, \dots, y^{(n)}$ sont les dérivées successives jusqu’à l’ordre $n$.
>
> L’objectif est de trouver $y(x)$, appelée la **solution générale** de l’équation différentielle.
### Problème de Cauchy

> [!abstract]- Problème de Cauchy
> Un **problème de Cauchy** consiste à résoudre une équation différentielle ordinaire (EDO) avec des **conditions initiales (C.I.)** imposées à une ou plusieurs valeurs de $x$.
>
> Formulation générale:
> - Soit une **EDO** de la forme $F(x, y, y', y'', \dots, y^{(n)}) = 0$.
> - On impose des conditions initiales telles que:
>
> $$y(x_0) = y_0, \quad y'(x_0) = y_1, \quad y''(x_0) = y_2, \quad \dots, \quad y^{(n-1)}(x_0) = y_{n-1}$$
>
> où:
>
> - $x_0$ est le point où les conditions initiales sont spécifiées,
> - $y_0, y_1, \dots, y_{n-1}$ sont des valeurs données.
>
> La solution du problème de Cauchy est une fonction $y(x)$ qui satisfait à la fois l’**EDO** et les **conditions initiales**.
