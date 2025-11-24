---
title: Espérance (expected value)
authors: Alessandro Dorigo
tags:
  - VarAlea
  - Proba
---


> [!info]+ Définition
> **L'espérance** d'une [[Variable aléatoire#^dcd8d2|variable aléatoire]] $X$, souvent notée $\mathbb{E}[X]$, est une mesure centrale qui prend en compte toutes les valeurs possibles de $X$, pondérées par leur probabilité, mais elle **n'est pas nécessairement égale à la [[Moyenne (sample mean)#^fa7d32|moyenne]]** observée dans un échantillon.

^c716f7

> [!abstract]- Cas
> $$
> \begin{array}{|c|c|}
> \hline
> \text{Cas discret} & \text{Cas continu} \\
> \hline
> \mathbb{E}[X] = \sum x \cdot p_X(x) & \mathbb{E}[X] = \int_{-\infty}^\infty x \cdot f_X(x) dx \\
> \hline
> \end{array}
> $$
## Propriétés

> [!info]+ Linéarité de l'espérance
> $$\mathbb{E}[mX + b] = m\mathbb{E}[X] + b$$

> [!abstract]- Preuve
> $$\begin{align*} \mathbb{E}[mX + b] &= \sum_x (mx + b)p_X(x) \\ &= m \sum_x (x \cdot p_X(x)) + b \sum_x p_X(x) \\ &= m\mathbb{E}[X] + b \cdot 1 \\ &= m\mathbb{E}[X] + b \end{align*}$$

> [!info]+ Somme de variables aléatoires
> $$ \mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$$

^446fba

> [!info]+ Produit de variables aléatoires (indépendantes)
> $$ \mathbb{E}[X \cdot Y] = \mathbb{E}[X] \cdot \mathbb{E}[Y] \quad \text{si $X$ et $Y$ sont indépendantes}$$

^c817fc
