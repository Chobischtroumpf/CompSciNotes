---
title: théorème d'équivalence V2
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---
# Théorème d'équivalence entre points extrêmes et solutions de base réalisables

> [!abstract] Théorème "Équivalence entre points extrêmes et solutions de base réalisables"
>
> Soit :
>
> - $A$ une matrice réelle de dimension $m \times n$ et de rang $m$, et un vecteur réel $b$ de dimension $m$
> - $P$ un polytope convexe défini par tous les vecteurs $x$ de dimension $n$ satisfaisant les contraintes (sous forme standard) :
>
> $$ Ax = b, \quad x \geq 0 $$
>
> Un vecteur $x$ est un point extrême de $P$ si et seulement si $x$ est une solution de base réalisable pour le système défini par l'ensemble de contraintes.
>
> La condition de non-négativité permet l'équivalence avec les solutions de base réalisables.

> [!tip]+ Remarque
>
> Ce théorème officialise qu'on peut trouver la solution de base réalisable graphiquement.

## Preuve

> [!tip]+  Preuve $\Leftarrow$
>
> Supposons $x = (x_1, x_2, \ldots, x_m, 0, 0, \ldots, 0)$ est une solution de base réalisable pour l'ensemble de contraintes.
>
> Alors :
>
> $$ x_1 a_1 + \ldots + x_m a_m = b $$
>
> où les $m$ premières colonnes de $A$ sont linéairement indépendantes.
>
> Supposons que $x$ est une combinaison convexe de deux autres points $y, z \in P$ :
>
> $$ x = \alpha y + (1 - \alpha)z, \quad 0 < \alpha < 1, \quad y \neq z $$
>
> Toutes les composantes de $x, y, z \geq 0$ et $0 < \alpha < 1$, donc les $(n-m)$ dernières composantes de $y, z$ sont nulles :
>
> $$ y_1 a_1 + \ldots + y_m a_m = b $$
>
> $$ z_1 a_1 + \ldots + z_m a_m = b $$
>
> Les vecteurs colonnes de $A$ étant linéairement indépendants, il s'ensuit que $x = y = z$ et donc que $x$ est un point extrême de $P$.

> [!tip]+ Preuve $\Rightarrow$
>
> Supposons $x$ est un point extrême de $P$.
>
> Supposons que les composantes non-nulles de $x$ sont les $k$ premières composantes :
>
> $$ x_1 a_1 + \ldots + x_k a_k = b, \quad x_i > 0, \quad i = 1, \ldots, k $$
>
> Pour démontrer que $x$ est une solution de base réalisable, il faut démontrer que les vecteurs $a_1, \ldots, a_k$ sont linéairement indépendants (on procède par contradiction).
>
> Supposons que les vecteurs $a_1, \ldots, a_k$ ne sont pas linéairement indépendants. Dans ce cas, il existe une combinaison linéaire (non-triviale) telle que :
>
> $$ y_1 a_1 + \ldots + y_k a_k = 0 $$
>
> Définissons le vecteur $y = (y_1, \ldots, y_k, 0, \ldots, 0) \in \mathbb{R}^n$.
>
> Puisque $x_i > 0$ pour $1 \leq i \leq k$, il est possible de choisir $\varepsilon$ vérifiant les contraintes de non-négativité :
>
> $$ x + \varepsilon y \geq 0 $$
>
> $$ x - \varepsilon y \geq 0 $$
>
> Dans ce cas, $x = \frac{1}{2}(x + \varepsilon y) + \frac{1}{2}(x - \varepsilon y)$ serait une combinaison convexe de deux vecteurs (distincts) de $P$.
>
> Ceci est impossible puisque $x$ est un point extrême de $P$.
>
> Donc $a_1, \ldots, a_k$ sont linéairement indépendants.
