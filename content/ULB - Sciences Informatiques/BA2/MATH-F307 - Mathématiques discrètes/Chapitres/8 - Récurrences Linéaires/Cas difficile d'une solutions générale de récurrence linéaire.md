---
title: Cas difficile d'une solutions générale de récurrence linéaire
authors: Alessandro Dorigo
tags:
  - MathDis
---


 > [!abstract]- Théorème "Cas des racines multiples"
> Si $\alpha$ est une racine de l'équation caractéristique de multiplicité $r$, alors
> $$\alpha^n, n·\alpha^n, n^2·\alpha^n, ..., n^{r-1}·\alpha^n$$
> sont toutes solutions de l'équation de récurrence et sont linéairement indépendantes.
> Remarque : $\alpha ∈ ℂ$ est racine double de $p(X)$ si et seulement si $\alpha$ est racine de $p(X)$ et de $p'(X)$. Si $\alpha$ est racine double du polynôme caractéristique $q(X)$, alors $\alpha$ est aussi une racine double de
> $$p_n(X) = X^{n-d}q(X) = X^n - a_1·X^{n-1} - ... - a_d·X^{n-d}$$
> pour tout $n ≥ d$ et donc $\alpha$ satisfait aussi
> $$n·\alpha^n-\sum_{i=1}^{d-1} a_i·(n-i)·\alpha^{n-i} = \alpha·p_n'(\alpha) = 0$$

> [!example]+ Exemple - Reproduction d'une plante Lobelia telekii
> Soit $f(n)$ le nombre de plantes l'année $n$, avec les conditions initiales:
> $$f(0) = 0 \text{ et } f(1) = 1$$
> L'équation de récurrence est:
> $$f(n) = f(n-1) + (f(n-1)-f(n-2)) = 2f(n-1)-f(n-2)$$
> Équation caractéristique:
> $$\alpha^2-2\alpha+1=0$$
> Racines: $\alpha_1 = \alpha_2 = 1$ (multiplicité 2)
> Solution générale:
> $$f(n) = c_1\cdot1^n + c_2\cdot n\cdot1^n = c_1 + c_2n$$
> En résolvant le système:
> $$\begin{cases} f(0) = 0 & \Rightarrow c_1 + c_2\cdot0 = 0 \\ f(1) = 1 & \Rightarrow c_1 + c_2\cdot1 = 1 \end{cases}$$
> On obtient: $c_1 = 0$ et $c_2 = 1$
> Solution finale: $f(n) = n$ pour tout $n \in \mathbb{N}$
