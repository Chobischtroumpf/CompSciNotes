---
title: Notation à virgule fixe
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> Un nombre réel $x$ est représenté sous la forme:
> $$ x = (-1)^s \sum_{k=-m}^{n} a_k b^k $$
> où:
> - $b$ est la **base** (ex. : 2, 10, 16),
> - $s$ est le **bit de signe** (0 pour positif, 1 pour négatif),
> - $a_k$ sont les **symboles** (entre 0 et $b-1$),
> - $n+1$ est le nombre de chiffres avant la virgule,
> - $m$ est le nombre de chiffres après la virgule.
>
> **Propriétés:**
> - La **taille de l’intervalle représentable** est limitée.
> - La **précision** est constante entre deux nombres consécutifs.
> - En **base 2**, un nombre comme $0.1$ n’a pas de représentation finie (approximation).

> [!example]+ Exemples
> - **Base 10**: [0030, 421000] $\rightarrow 30.421$
> - **Base 2**: [111, 101]
> - Si $b = 2$, alors $x = 7.625$
> - Si $b = 3$, alors $x = 13.3704$
