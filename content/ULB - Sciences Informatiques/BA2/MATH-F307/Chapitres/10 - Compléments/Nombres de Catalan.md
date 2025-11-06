---
title: Nombres de Catalan
authors: Alessandro Dorigo
tags:
  - MathDis
  - Complements
---


> [!info]+ Définition
> Le n-ème **nombre de Catalan** est défini comme
> $$C_n = \frac{\binom{2n}{n}}{n+1} = \frac{2n!}{n!(n+1)!}$$

^469ef0

## Cas 1: Nombre de parenthésages (complets) d’un produit de $n$ facteurs

|   $C_n$   |                                              parenthésages                                               |
| :-------: | :------------------------------------------------------------------------------------------------------: |
| $C_1 = 1$ |                                               (convention)                                               |
| $C_2 = 1$ |                                                $x_1 x_2$                                                 |
| $C_3 = 2$ |                                      $x_1 (x_2 x_3), (x_1 x_2) x_3$                                      |
| $C_4 = 5$ | $((x_1 x_2) x_3) x_4, (x_1 x_2)(x_3 x_4), x_1 (x_2 (x_3 x_4)), (x_1 (x_2 x_3)) x_4, x_1 ((x_2 x_3) x_4)$ |
> [!abstract]- Lemme 10.2.1
> $$C_n = C_1 \cdot C_{n-1} + C_2 \cdot C_{n-2} + C_3 \cdot C_{n-3} + \cdots + C_{n-1} \cdot C_1 = \sum_{k=1}^{n-1} C_k \cdot C_{n-k}$$
>
> **Justification:** Pour tout $k = 1, 2, \dots, n − 1$, on peut obtenir un parenthésage d’un produit de $n$ facteurs en combinant:
> - Un parenthésage d’un produit de $k$ facteurs.
> - Un parenthésage d’un produit de $n − k$ facteurs.
>
> Tout parenthésage d’un produit de $n$ facteurs se décompose ainsi.
>
> ![[Pasted image 20241212103227.png]]

> [!abstract]- Théorème 10.2.2
> Pour tout $n \geq 1$:
>
> $$C_n = \frac{1}{n} \binom{2n-2}{n-1}$$
>
> **Démonstration:**
> - Posons la fonction génératrice ordinaire de la suite de Catalan $C_{n_{n \in \mathbb{N}_0}}$:
>   $$C(x) = \sum^\infty_{n=1} C_n \cdot x^n \quad \forall x \in \mathbb{R}$$
>
> ![[Pasted image 20241212103914.png]]
>
> En utilisant la [[Formule du binôme généralisé#^0e17b7|formule du binôme généralisé]]:
> $$\sum_{n=0}^{\infty} C_n x^n = C(x) = \frac{1}{2} - \frac{1}{2} (1 - 4x)^{1/2} = \frac{1}{2} - \frac{1}{2} \sum_{n=0}^{\infty} \binom{1/2}{n} (-4)^n x^n$$
>
> $$\implies C_n = -\frac{1}{2} \cdot \binom{1/2}{n} \cdot (-4)^n$$
>
> en identifiant les coefficients des $x^n$.
>
> ![[Pasted image 20241212104432.png]]

^1a5ab7

## Cas 2: Nombre d’arbres binaires stricts non étiquetés à $n$ feuilles

> [!abstract]- Lemme 10.2.3
> $$C_{n−1}​ = \frac{\binom{2(n−1)}{n-1}}{n} ​= \frac{(2n−2)!​}{n!(n−1)!}$$
>
> Pour tout $k = 1, 2, \dots, n - 1$, on peut obtenir un **arbre binaire strict à $n$ feuilles** en combinant:
> - Un **arbre binaire strict à $k$ feuilles**.
> - Un **arbre binaire strict à $n - k$ feuilles**.
>
> Tout arbre binaire strict à $n$ feuilles peut être construit de cette manière.
>
> ![[Pasted image 20241212105119.png]]

> [!tip]
> Le nombre d’arbres binaires stricts non étiquetés à $n$ feuilles est **égal au nombre d’arbres binaires complets non étiquetés avec $n - 1$ nœuds internes**.
## Cas 3: Nombre de triangulations d’un $(n + 1)$-gone
> [!abstract]- Lemme 10.2.4
> **Justification:** On fixe un côté du $(n + 1)$-gone.
> Dans une triangulation, ce côté fait partie d'**exactement un triangle**, et il existe exactement $n - 1$ triangles possibles auxquels il peut appartenir.
>
> Pour chaque choix de triangle, on se retrouve avec deux sous-polygones à trianguler:
> - Un polygone à **droite** du triangle (éventuellement vide).
> - Un polygone à **gauche** du triangle (éventuellement vide).
>
> Ainsi, pour tout $k = 1, 2, \dots, n - 1$, on peut obtenir une triangulation d’un $(n + 1)$-gone en combinant:
> - Une triangulation d’un $(k + 1)$-gone (polygone à gauche).
> - Une triangulation d’un $(n - k + 1)$-gone (polygone à droite).
>
> Et toute triangulation s’obtient ainsi.
>
> ![[Pasted image 20241212110451.png]]
> ![[Pasted image 20241212110507.png]]
## Autres interprétations de $C_n$

| Nombre de chemins de Dyck (rester au dessus de la diagonale) | Nombre de chemins de $(0,0)$ vers $(a,b)$ |
| :----------------------------------------------------------: | :---------------------------------------: |
|             ![[Pasted image 20241212111323.png]]             |   ![[Pasted image 20241212111416.png]]    |
> [!abstract]- Theoreme 10.2.5
> Pour tout $n \geq 1$:
>
> $$C_n = \binom{2n-2}{n-1} - \binom{2n-2}{n}$$
> ...
