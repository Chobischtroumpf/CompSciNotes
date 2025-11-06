---
title: Schéma multinomial
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Définition
> Le **schéma multinomial** modélise une expérience aléatoire $\varepsilon$ donnant lieu à $I$ résultats possibles (avec $I = 2$, on retrouve le [[Loi Bernoulli|schéma de Bernoulli]]). Chaque résultat $i(i = 1, 2, \dots, I)$ a une probabilité $p_i$, où:
>
> $$p_1 + p_2 + \cdots + p_I = 1$$
>
> On considère $n$ répétitions indépendantes de l’expérience $\varepsilon$ et on note $n_i$ le nombre de fois où le résultat $i$ apparaît.

^bc3347

> [!abstract]- Propriétés
> - Chaque $n_i$ suit une [[Loi binomiale|loi binomiale]]: $n_i \sim \text{Bin}(n, p_i)$.
> - [[Espérance (expected value)|Espérance]] de $n_i$: $\mathbb{E}[n_i] = np_i$.
> - La somme des $n_i$ est égale au nombre total de répétitions:
>   $$n_1 + n_2 + \cdots + n_I = n$$
### Vecteur multinomial
Le vecteur aléatoire $\mathbf{n} = (n_1, \dots, n_I)$ suit une **loi multinomiale** de paramètres $p_1, \dots, p_I$ et d’exposant $n$, ce qui se note:
$$\mathbf{n} \sim \text{Mult}(n; p_1, \dots, p_I)$$
