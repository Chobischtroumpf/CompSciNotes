---
title: Complexité algorithmique
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---

## Mesures de complexité
La complexité d'un algorithme peut être caractérisée de plusieurs manières, chacune offrant une perspective différente sur les ressources nécessaires à son exécution:

- Le nombre d'étapes
- Le temps d'exécution
- L'occupation de la mémoire
- Des mesures dépendantes de l'architecture du processeur

> [!info]+ Définition
> Si la **complexité** d'un algorithme dépend d'un paramètre $p$ (représentant la taille du problème), la complexité $C(p)$ d'un algorithme est dite d'ordre $f(p)$ s'il existe deux constantes $a$ et $b$ telles que:
> $$C(p) \leq bf(p) \text{ pour tout } p \geq a$$
>
> On note cette relation: $C(p) = O(f(p))$

![[Classes de complexité]]

> [!example]+ Exemple
> - **Méthode de Gauss** pour résoudre un système linéaire d’ordre $n$ :
> $$C(n) = \frac{2n^3}{3} + \frac{3n^2}{2} - \frac{7n}{6} \Rightarrow O(n^3)$$
> Par conséquent, cet algorithme a une complexité cubique, ou d'ordre 3.
