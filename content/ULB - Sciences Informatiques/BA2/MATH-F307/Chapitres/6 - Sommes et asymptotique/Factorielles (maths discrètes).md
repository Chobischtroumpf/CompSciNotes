---
title: Factorielles (maths discrètes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


> [!info]+ Définition
> La **factorielle** d'un entier $n$ est définie par:
> $$n! = \prod_{k=1}^n k = 1 \cdot 2 \cdot 3 \cdot \cdots \cdot (n-1) \cdot n$$

Comme le logarithme transforme un produit en somme:
$$\log(n!) = \sum_{k=1}^n \log(k) \quad \text{avec} \quad f(x) = \log(x) \quad \text{croissante}$$
et en utilisant l'approximation intégrale:
$$\int_1^n \log(x) \, dx = \left[ x\log(x) - x \right]_1^n = n \log(n) - n + 1$$
on peut en déduire que:
$$\log(1) + n\log(n) - n + 1 \leq \log(n!) \leq \log(n) + n\log(n) - n + 1$$
ce qui conduit à l'encadrement suivant:
$$n \log(n) - n + 1 \leq \log(n!) \leq (n+1) \log(n) - n + 1$$

En passant à l'exponentielle, on obtient:
$$\frac{n^n}{e^{n-1}} \leq n! \leq \frac{n^{n+1}}{e^{n-1}}$$

> [!note]
> La différence entre les bornes supérieure et inférieure est un facteur de $n$.

> [!abstract]- Théorème 6.8.1
> Une approximation de la factorielle est donnée par:
> $$n! = \left( \frac{n}{e} \right)^n \cdot \sqrt{2 \pi n} \cdot e^{\delta(n)}$$
> où:
> $$\frac{1}{12n + 1} \leq \delta(n) \leq \frac{1}{12n}$$

> [!abstract]- Théorème 6.8.2 (Théorème de Stirling)
> L'approximation de Stirling fournit une estimation asymptotique de la factorielle:
> $$n! \sim \left( \frac{n}{e} \right)^n \cdot \sqrt{2 \pi n}$$

^35d344

> [!example]+ Exemple
> ![[Pasted image 20241023123702.png]]
