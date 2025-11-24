---
title: Nombre premier
authors: Alessandro Dorigo
tags:
  - MathDis
  - Maths
  - TheorieDesNombres
  - Algo
---


> [!info]+ Définition
> Un entier naturel $p > 1$ est appelé **nombre premier** (ou un **nombre premier**) si ses seuls diviseurs positifs sont 1 et $p$ lui-même. Sinon, $p$ est appelé **composé**.

> [!abstract]- Théorème d'Euclide
> Le nombre de nombres premiers est infini.

> [!abstract]- Lemme d'Euclide
> Pour tous entiers $a$ et $b$, et un nombre premier $p$, si $p \mid ab$, alors $p \mid a$ ou $p \mid b$.
> - Soit $p$ un nombre premier, $n$ un entier naturel, et $a_1, a_2, \dots, a_n$ des entiers. Si $p \mid (a_1 a_2 \dots a_n)$, alors $p \mid a_i$ pour un certain $i = 1, 2, \dots, n$.

> [!abstract]- Théorème fondamental de l'arithmetique
> Tout entier naturel $n > 1$ peut être écrit de manière unique comme un produit de facteurs premiers, à l'ordre des facteurs près.

> [!tip]+ Corollaire
> Tout entier naturel $n > 1$ est soit un nombre premier, soit possède un facteur premier inférieur ou égal à $\sqrt{n}$.

> [!abstract]- Diviseurs à partir de la factorisation en nombres premiers
> Soient $n$ et $c$ des entiers positifs, et soit
> $$n = p_1^{\alpha_1} p_2^{\alpha_2} \dots p_k^{\alpha_k}$$
> une façon d'exprimer $n$ comme un produit de nombres premiers distincts $p_1, p_2, \dots, p_k$, où certains ou tous les exposants peuvent être égaux à zéro. L'entier $c$ divise $n$ si et seulement si
> $$c = p_1^{\beta_1} p_2^{\beta_2} \dots p_k^{\beta_k}$$
> avec $0 \leq \beta_i \leq \alpha_i$ pour $i = 1, 2, \dots, k$.

> [!abstract]- PGCD à partir de la factorisation en nombres premiers
> Soient $a$ et $b$ des entiers positifs, et soient
> $$a = p_1^{\alpha_1} p_2^{\alpha_2} \dots p_k^{\alpha_k}$$
> et
> $$b = p_1^{\beta_1} p_2^{\beta_2} \dots p_k^{\beta_k}$$
> des façons d'exprimer $a$ et $b$ comme des produits de nombres premiers distincts $p_1, p_2, \dots, p_k$, où certains ou tous les exposants peuvent être égaux à zéro. On a:
> $$\gcd(a, b) = p_1^{\lambda_1} p_2^{\lambda_2} \dots p_k^{\lambda_k}$$
> où $\lambda_i = \min(\alpha_i, \beta_i)$ pour $i = 1, 2, \dots, k$.
