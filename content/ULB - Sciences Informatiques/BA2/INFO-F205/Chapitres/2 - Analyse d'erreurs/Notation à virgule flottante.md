---
title: Notation à virgule flottante
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> Un nombre réel $x$ est représenté sous la forme:
> $$ x = (-1)^s b^e \sum_{i=1}^t a_i b^{-i} = (-1)^s mb^{e-t}$$ > où:
> - $s$ est le **bit de signe** (0 pour positif, 1 pour négatif),
> - $t$ est le **nombre de chiffres significatifs**,
> - $m$ est la **mantisse**,
> $$m[x] = \sum_{i=1}^t a_i b^{t-i}$$
> - $b$ est la **base** (souvent 2 ou 10),
> - $e$ est l’**exposant** (définissant l’échelle du nombre).

> [!tip]+ Ensemble $\mathbb{F}$
> L’ensemble des nombres représentables en virgule flottante est noté:
> $$ \mathbb{F}(b, t, L, U) $$
> où:
> - $b$ est la **base**,
> - $t$ est le **nombre de chiffres significatifs**,
> - $L$ et $U$ sont les **bornes inférieure et supérieure de l’exposant**.
>
> **Propriétés:**
> - L’ensemble $\mathbb{F}$ **ne contient pas 0** si la représentation est normalisée.
> - $\mathbb{F}$ est un **sous-ensemble fini** de $\mathbb{R}$:
> $$ \mathbb{F}(b, t, L, U) \subset \mathbb{R} $$
> - **Bornes des valeurs représentables**:
> $$ b^{L-1} \leq |x| \leq b^U (1 - b^{-t}) $$
> - **Nombre total de valeurs représentables** (cardinal de $\mathbb{F}$):
> $$ \#(\mathbb{F}) = 2 (b - 1) b^{t-1} (U - L + 1) $$
> où $2$ vient du bit de signe.

> [!example]+ Exemples
> - $\{[3,4], e = 1, b = 10, s = 0\} \rightarrow 3.4$
> $$x = (-1)^0 10^1(3 \cdot 10^{-1} + 4 \cdot 10^{-2}) = 0.34 \cdot 10^1 = 3.4$$
> - $\{[3,4], e = -1, b = 16, s = 1\} \rightarrow -0.0127$
> $$x = (-1)^1 16^{-1}(3 \cdot 16^{-1} + 4 \cdot 16^{-2}) = -0.0127$$
