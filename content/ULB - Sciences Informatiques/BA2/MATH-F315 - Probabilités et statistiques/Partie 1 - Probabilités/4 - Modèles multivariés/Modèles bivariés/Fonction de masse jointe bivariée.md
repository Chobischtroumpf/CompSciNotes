---
title: Fonction de masse jointe bivariée
authors: Alessandro Dorigo
tags:
  - Proba
---


Soient $X$ et $Y$ deux [[Variable aléatoire#^dcd8d2|variables aléatoires]] discrètes prenant respectivement les valeurs possibles:
$$x_1, x_2, \dots \quad \text{et} \quad y_1, y_2, \dots$$

> [!info]+ Définition
> La **[[Fonctions de probabilités#Fonction de masse (Mass Function)|fonction de masse]] jointe** est donc définie comme:
> $$p_{X,Y}(x_i, y_j) = \mathbb{P}(X = x_i, Y = y_j), \quad \text{pour } i, j = 1, 2, \dots$$
>
> Cette fonction donne la probabilité conjointe que $X$ prenne la valeur $x_i$ et $Y$ prenne la valeur $y_j$.

^11d377

> [!note]
> La [[Fonction de répartition jointe bivariée#^398bb0|fonction de répartition jointe]] de deux [[Variable aléatoire#^dcd8d2|variables aléatoires]] discrètes peut être exprimée comme une somme des probabilités conjointes pour toutes les valeurs $x_k \leq x_i$ et $y_l \leq y_j$:
>
> $$F_{X,Y}(x_i, y_j) = \sum_{k=1}^{i} \sum_{l=1}^{j} p_{X,Y}(x_k, y_l)$$

> [!tip]+ Important
> La somme de toutes les probabilités dans l'espace discret (valeurs possibles de $X$ et $Y$) doit être égale à 1:
>
> $$\sum_{i=1}^\infty \sum_{j=1}^\infty p_{X,Y}(x_i, y_j) = 1$$
