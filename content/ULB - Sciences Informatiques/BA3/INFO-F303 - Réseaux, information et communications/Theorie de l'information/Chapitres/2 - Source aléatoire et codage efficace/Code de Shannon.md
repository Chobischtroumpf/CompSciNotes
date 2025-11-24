---
title: Code de Shannon
authors: Alessandro Dorigo
tags:
  - ThInfo
---


Avec les probabilités décroissantes $p_1 \geq p_2 \geq \dots \geq p_q$ et soit $\ell_i = \lceil - \log_2{p_i} \rceil \geq 1$, on a:
$$\ell_1 \leq \ell_2 \leq \dots \leq \ell_q$$

> [!info] Définition
> $K(s_i)$ est formé des bits de
> $$ \left\lfloor 2^{\ell_i} \sum^{i-1}_{j=1} p_j \right\rfloor $$

> [!abstract]- Préfixe strict
> Le préfixe strict de $K(s_i)$ de longueur $\ell_j$, $j < i$, est
> $$ \left\lfloor 2^{\ell_j} \sum_{k=1}^{i-1} p_k \right\rfloor $$

> [!tip]+ Remarque
> Montrons que sa différence avec $K(s_j)$ est non nulle
> $$ 2^{\ell_j} \left( \sum_{k=1}^{i-1} p_k - \sum_{k=1}^{j-1} p_k \right) = 2^{\ell_j} \sum_{k=j}^{i-1} p_k \geq 2^{\ell_j} p_j $$
> $$ \geq 2^{-\log_2 p_j} p_j = \frac{1}{p_j} p_j = 1 $$

Le Code de Shannon est [[Code sans préfixe#^392e5f|sans préfixe]].
