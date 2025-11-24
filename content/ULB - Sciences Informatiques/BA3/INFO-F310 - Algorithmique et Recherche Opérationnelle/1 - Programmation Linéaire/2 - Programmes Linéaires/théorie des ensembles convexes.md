---
title: théorie des ensembles convexes
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---
## Combinaison convexe
> [!info]+ Définition
>
> Pour un ensemble fini de points $x_1, \ldots, x_n \in \mathbb{R}^d$ et toute famille de réels positifs $\alpha_i \geq 0, i = 1, \ldots, n$ telles que :
>
> $$ \sum_{i=1}^n \alpha_i = \alpha_1 + \ldots + \alpha_n = 1 $$
>
> le point défini par :
>
> $$ \sum_{i=1}^n \alpha_i x_i = \alpha_1 x_1 + \ldots + \alpha_n x_n $$
>
> est appelé **combinaison convexe** des points $x_1, \ldots, x_n$.

## Ensemble convexe

> [!info]+ Définition
>
> Un ensemble $X \subseteq \mathbb{R}^n$ est convexe si pour toute paire de points $x, y \in X$ et tout $\alpha \in [0,1]$, la combinaison convexe $\alpha x + (1 - \alpha)y \in X$.

> [!tip]+ Remarque
>
> $X$ est convexe si et seulement si pour tout couple de points $x, y$ de $X$, le segment de droite :
>
> $$ [x,y] = {\alpha x + (1 - \alpha)y \mid \alpha \in [0,1]} $$
>
> reliant ces deux points est entièrement inclus dans $X$.
>
> Un élément $z$ de ce segment $[x,y]$ s'écrit également sous la forme :
>
> $$ z = y + \alpha(x - y) $$

> [!example]+ Exemple
>
> Exemples d'ensembles convexes :
>
> - L'ensemble vide, un singleton, l'espace $\mathbb{R}^n$
>
> - Un sous-ensemble $I$ de $\mathbb{R}$ définit un intervalle si $x, y \in I, x < z < y \Rightarrow z \in I$. Un sous-ensemble de $\mathbb{R}$ est convexe si et seulement si $I$ est un intervalle.
>
> - La boule unitaire d'un espace vectoriel :
>
>
> $$ {x \in \mathbb{R}^n \mid |x|_p \leq 1}, \quad p \in [1, \infty[ $$
>
> - Un ellipsoïde :
>
> $$ {x \in \mathbb{R}^n \mid (x - x_c)^T Q(x - x_c) \leq r} $$
>
> où $x_c \in \mathbb{R}^n$, $r \in \mathbb{R}$, et $Q$ est une matrice positive semi-définie $\in \mathbb{R}^{n \times n}$.
>
> - L'ensemble défini par des contraintes d'inégalités linéaires :
>
> $$ {x \in \mathbb{R}^n \mid Ax \leq b} = {x \in \mathbb{R}^n \mid a_i^T x \leq b_i, i = 1, \ldots, m} $$
>
> où la matrice $A \in \mathbb{R}^{m \times n}$ et le vecteur $b \in \mathbb{R}^m$.
>
> - Un hyperplan (intersection de deux demi-espaces fermés) :
>
> $$ {x \in \mathbb{R}^n \mid a^T x = b} $$

## Enveloppe convexe

> [!info]+ Définition
>
> Soit un ensemble quelconque $X \subseteq \mathbb{R}^n$. L'enveloppe convexe $\text{conv}(X)$ est l'ensemble convexe le plus petit contenant $X$.
>
> En dimension finie, $\text{conv}(X)$ est l'ensemble des combinaisons convexes finies d'éléments (points) de $X$ :
>
> $$ \text{conv}(X) = \set{x \in X \mid x = \sum_{i=1}^m \alpha_i x_i, \sum_{i=1}^m \alpha_i = 1, \alpha_i \geq 0} $$
>
> L'enveloppe convexe est définie comme intersection de demi-espaces fermés, c'est donc un ensemble lui-même fermé.

> [!tip]+ Remarque
>
> Algorithmes pour calculer l'enveloppe convexe :
>
> - Jarvis march
> - Graham scan
> - Chan's algorithm (combinaison)

## Point extrême

> [!info]+ Définition
>
> Un point $x$ d'un ensemble convexe $X \subseteq \mathbb{R}^n$ est un **point extrême** de $X$ s'il n'existe pas deux points distincts $y$ et $z \in X$ tels que :
>
> $$ x = \alpha y + (1 - \alpha)z, \quad \alpha \in ]0, 1[ $$
>
> Autrement dit, un point extrême de $X$ est un point $x$ qui ne se situe pas strictement à l'intérieur d'un segment de droite reliant deux autres points de l'ensemble :
>
> $$ x \in X, \quad x \notin \text{conv}(X \setminus {x}) $$

> [!example]+ Exemple
>
> Les points extrêmes d'un polyèdre sont ses sommets.
