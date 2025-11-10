---
title: Equations caractéristiques
authors: Alessandro Dorigo
tags:
  - MathDis
---

> [!abstract]- Formule "Équation caractéristique"
> Pour l'équation de récurrence $$f(n) = \sum_{i=1}^d a_i \cdot f(n-i) \quad \forall n \geq d$$
> avec conditions initiales $f(0)=b_0, f(1)=b_1, ..., f(d-1)=b_{d-1}$
>
> La substitution de la solution de base $f(n)=\alpha^n, \alpha \neq 0$ donne :
> $$\alpha^n = \sum_{i=1}^d a_i \cdot \alpha^{n-i} = \alpha^{n-d} \cdot \left(\sum_{i=1}^d a_i \cdot \alpha^{d-i}\right)$$
> Ce qui mène à l'équation caractéristique :
> $$\alpha^d - \sum_{i=1}^d a_i \cdot \alpha^{d-i} = 0$$
> Cette équation polynomiale de degré $d$ a $d$ solutions dans ℂ, avec multiplicité.
