---
title: Grand Theta
authors: Alessandro Dorigo
tags:
  - MathDis
  - Algo
---


> [!info]+ Définition
> Soient $f, g : \mathbb{N} \to \mathbb{R}$ deux fonctions.
>
> On dit que $f$ est **grand-$\Theta$** de $g$, et on écrit $f \in \Theta(g)$ (ou $f = \Theta(g)$), s’il existe des constantes $C_1, C_2 > 0$ et $N \in \mathbb{N}$ telles que :
> $$\forall n \geq N : C_1 \cdot |g(n)| \leq |f(n)| \leq C_2 \cdot |g(n)|$$
>
> Cela signifie que $f$ et $g$ ont des croissances équivalentes asymptotiquement.

^076d31

> [!abstract]- Théorème 6.9.1
> Soient deux fonctions $f, g : \mathbb{N} \to \mathbb{R}^+$. Si $f \sim g$, alors  $f = \Theta(g)$.
>
> **Démonstration**:
> Par hypothèse, nous savons que
> $$\frac{f(n)}{g(n)}\ \xrightarrow{n \to +\infty}\ 1$$
> ce qui implique également que
> $$\frac{g(n)}{f(n)}\ \xrightarrow{n \to +\infty}\ 1$$
>
> Par la remarque ci-dessus, nous pouvons déduire $f = \mathcal{O}(g)$ et $g = \mathcal{O}(f)$, i.e. $f = \Theta(g). \quad \square$
