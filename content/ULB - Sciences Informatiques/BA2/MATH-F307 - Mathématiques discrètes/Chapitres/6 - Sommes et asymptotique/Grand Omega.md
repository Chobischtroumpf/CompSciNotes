---
title: Grand Omega
authors: Alessandro Dorigo
tags:
  - MathDis
  - Algo
---


> [!info]+ Définition
> Soient $f, g : \mathbb{N} \to \mathbb{R}$ deux fonctions.
>
> On dit que $f$ est **grand-$\Omega$** de $g$, et on écrit $f \in \Omega(g)$ (ou $f = \Omega(g)$) ssi $g \in \mathcal{O}(f)$. Autrement dit, il existe des constantes $C > 0$ et $N \in \mathbb{N}$ telles que:
> $$\forall n \geq N : |f(n)| \geq C \cdot |g(n)|$$
>
> Cela signifie que $f$ est au moins aussi rapide en croissance que $g$ pour $n$ grand.

^52d6fc
