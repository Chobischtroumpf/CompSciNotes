---
title: Algorithme itératif
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Definition
> Un **algorithme itératif** construit progressivement une solution par **approximations successives**. Il repose sur une mise à jour récurrente de l'estimation de la solution.

> [!tip]+ Caractéristiques
> - $n$ est non borné (dépend de la [[Convergence#^6240b2|convergence]] de l'algorithme).
> - Chaque approximation utilise l’itération précédente: $$\vec{d}^{(i)} = \vec{x}^{(i-1)}$$
> - On utilise une **fonction d'itération** $\phi$, indépendante de $n$, telle que: $$\vec{x}^{(n)} = \phi(\vec{x}^{(n-1)})$$

> [!example]+ Exemple
> Méthode de Newton pour trouver une racine $x$ d’une fonction $f(\vec{x})$:
> $$x_{n + 1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
