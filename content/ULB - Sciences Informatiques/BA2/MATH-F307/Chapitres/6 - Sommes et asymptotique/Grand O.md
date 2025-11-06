---
title: Grand O
authors: Alessandro Dorigo
tags:
  - MathDis
  - Algo
---


> [!info]+ Définition
> Soient $f, g : \mathbb{N} \to \mathbb{R}$ deux fonctions.
>
> On dit que $f$ est **grand-$\mathcal{O}$** de $g$, et on écrit $f \in \mathcal{O}(g)$ (ou $f = \mathcal{O}(g)$), s’il existe des constantes $C > 0$ et $N \in \mathbb{N}$ telles que:
> $$\forall n \geq N : |f(n)| \leq C \cdot |g(n)|$$
>
> Cela signifie que $g$ est une borne supérieure de l’ordre de grandeur de la croissance de $f$ pour $n$ grand.

^3913d6

> [!tip]+ Remarque
> Pour deux fonctions $f, g : \mathbb{N} \to \mathbb{R}$, on a $f = \mathcal{O}(g)$ si et seulement si la fonction $n \mapsto \frac{f(n)}{g(n)}$ est bornée (à partir d’un certain $n_0$).
>
> **Attention**: il est incorrect de dire que $f = \mathcal{O}(g)$ uniquement si la limite suivante existe et est finie:
> $$\lim_{n \to +\infty} \left| \frac{f(n)}{g(n)} \right|$$
>
> En effet, cette condition est suffisante, mais pas nécessaire. Par exemple, si $f(n) = (-1)^n$ et $g(n) = 1$, alors $f = \mathcal{O}(g)$ car $|f(n)/g(n)| = |(-1)^n| = 1$, ce qui est borné. Cependant, la limite
> $$\lim_{n \to +\infty} \left| \frac{f(n)}{g(n)} \right|$$
> n'existe pas, car $f(n)$ oscille entre $1$ et $-1$.
>
> Ainsi, bien que la limite finie soit suffisante pour conclure que $f = \mathcal{O}(g)$, elle n'est pas nécessaire.
