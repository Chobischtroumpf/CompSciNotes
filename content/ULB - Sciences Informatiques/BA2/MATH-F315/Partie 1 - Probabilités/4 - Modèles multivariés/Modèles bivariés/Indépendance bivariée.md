---
title: Indépendance bivariée
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Deux variables $X$ et $Y$ sont indépendantes
> $$\Leftrightarrow F_{X,Y}(x, y) = F_X(x) F_Y(y)$$
> $$\Leftrightarrow \mathbb{P}(X \leq x \text{ et } Y \leq y) = \mathbb{P}(X \leq x) \cdot \mathbb{P}(Y \leq y)$$

> [!info]+ Cas continu
> $$\Leftrightarrow f_{X,Y}(x, y) = f_X(x) f_Y(y)$$
> $$\Leftrightarrow f_X(x) = f_{X \vert Y}(x \vert y), \ \forall y \in \mathbb{R}$$
> $$\Leftrightarrow f_Y(y) = f_{Y \vert X}(y \vert x), \ \forall x \in \mathbb{R}$$

> [!info]+ Cas discret
> $$\Leftrightarrow p_{X,Y}(x, y) = p_X(x) p_Y(y)$$
> $$\Leftrightarrow p_X(x) = p_{X \vert Y}(x \vert y), \ \forall y \text{ admissible}$$
> $$\Leftrightarrow p_Y(y) = p_{Y \vert X}(y \vert x), \ \forall x \text{ admissible}$$
