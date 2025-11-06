---
title: Cas simple d'une solutions générale de récurrence linéaire
authors: Alessandro Dorigo
tags:
  - MathDis
---


 > [!info]+ Définition
> Une équation caractéristique a $d$ racines complexes distinctes notées $\alpha_1, \alpha_2, ..., \alpha_d \in \mathbb{C}$ avec $\alpha_i \neq \alpha_j$ pour $i \neq j$.

> [!abstract]- Formule
> La solution générale est donnée par:
> $$f(n) = c_1\alpha_1^n + c_2\alpha_2^n + ... + c_d\alpha_d^n$$
> où les constantes $c_1, c_2, ..., c_d$ sont déterminées par le système d'équations:
> $$f(0) = b_0,\ f(1) = b_1,\ ...,f(d-1) = b_{d-1}$$
> Ce système forme un système linéaire de $d$ équations à $d$ inconnues: $c_1, c_2, ..., c_d$
