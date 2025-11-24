---
title: Approximation d’une somme par une intégrale
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
---


> [!abstract]- Théorème 6.6.1
> Si $f : \mathbb{R}_+ \to \mathbb{R}$ continue et croissante, alors
> $$f(1) + \int_{1}^{n} f(x) \, dx \leq \sum_{k=1}^{n} f(k) \leq \int_{1}^{n} f(x) \, dx + f(n)$$
> ![[d50018ffe0afbf01a88747bf73f923c6.png]]
> ![[7dfb7543b794a733bfdbfd768eb90199.png]]

> [!abstract]- Théorème 6.6.2
> Si $f : \mathbb{R}_+ \to \mathbb{R}$ continue et décroissante, alors
> $$\int_{1}^{n} f(x) \, dx + f(n) \leq \sum_{k=1}^{n} f(k) \leq f(1) + \int_{1}^{n} f(x) \, dx$$
