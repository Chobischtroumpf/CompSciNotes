---
title: Série géométrique
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


> [!info]+ Définition
> Une **série géométrique** est la somme des termes d'une **progression géométrique**, c'est-à-dire d'une suite où chaque terme est obtenu en multipliant le terme précédent par une constante appelée **raison**.

^6b35ec

> [!note]+ Note
> Si les termes d’une somme géométrique deviennent de plus en plus petits, la somme est dite **géométriquement décroissante**. Si, au contraire, les termes deviennent de plus en plus grands, la somme est dite **géométriquement croissante**.
>
> Dans les deux cas, la somme est souvent approximativement égale au terme ayant la plus grande valeur absolue.

> [!example]+ Exemple
> ![[Pasted image 20241104100329.png]]

> [!abstract]- Formules
> Pour une progression géométrique de raison $r$, la somme des $n$ premiers termes de la suite, notée $S_n$, peut s'écrire comme:
> $$S_n = a + ar + ar^2 + ar^3 + \cdots + ar^{n-1}$$
> où $a$ est le premier terme de la suite.

> [!abstract]- Corollaire 6.0.1
> La formule pour la somme des $n$ premiers termes est donnée par:
> $$S_n = a \frac{1 - r^n}{1 - r} \quad \text{si } r \neq 1$$
>
> *Cette formule est utile pour simplifier le calcul de sommes où les termes croissent ou décroissent de manière exponentielle.*

> [!abstract]- Corollaire 6.0.2
> Pour une somme infinie d'une série géométrique (si $|r| < 1$), la formule devient:
> $$S = \frac{a}{1 - r}$$
>
> **Démonstration:**
> $$\sum_{k=0}^{\infty} r^k = \lim_{n \to \infty} \sum_{k=0}^{n-1} r^k = \lim_{n \to \infty} \frac{1 - r^n}{1 - r} = \frac{1}{1 - r}$$
> car $-1 < r < 1$
