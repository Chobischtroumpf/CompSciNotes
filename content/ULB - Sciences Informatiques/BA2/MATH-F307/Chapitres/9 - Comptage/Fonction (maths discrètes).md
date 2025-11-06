---
title: Fonction (maths discrètes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Comptage
  - Maths
---


> [!info]+ Définition
> Une **fonction** est une relation $f \subseteq X \times Y$ de $X$ à $Y$ telle que tout élément de $X$ est en relation avec exactement un élément de $Y$. On écrit $f : X \to Y$.
>
> - **Domaine**: $X$ est appelé le domaine de la fonction.
> - **Co-domaine**: $Y$ est appelé le co-domaine de la fonction.

> [!note]+ Remarque
> Si $f \subseteq X \times Y$ est une fonction, on écrit $y = f(x)$ si et seulement si $(x, y) \in f$, et on dit que $y$ est **l’image** de $x$ via $f$.
###  Règle fonctionelle - “mapping rule”
1. Si $f : X \to Y$ est surjective, alors $|X| \geq |Y|$.
2. Si $f : X \to Y$ est **injective**, alors $|X| \leq |Y|$.
3. Si $f : X \to Y$ est **bijective**, alors $|X| = |Y|$ (c'est la **règle de bijection**).

![[Pasted image 20241112150919.png]]
### Principe des Tiroirs (ou "Pigeonhole Principle")
Soient $X$ et $Y$ deux ensembles finis. Si $\vert X \vert > k \cdot \vert Y \vert$, alors pour toute fonction $f : X \to Y$ il existe un élément $y \in Y$ qui est l'image de **au moins** $k + 1$ éléments de $X$ via $f$.

- Le cas particulier où $k = 1$ correspond au **principe des tiroirs**: si plus de $n$ objets sont placés dans $n$ tiroirs, alors au moins un tiroir contient deux objets ou plus.

> [!example]+ Exemple
> Si plus de $n$ chaussettes sont placées dans $n$ tiroirs, alors il existe au moins un tiroir contenant deux chaussettes ou plus.
