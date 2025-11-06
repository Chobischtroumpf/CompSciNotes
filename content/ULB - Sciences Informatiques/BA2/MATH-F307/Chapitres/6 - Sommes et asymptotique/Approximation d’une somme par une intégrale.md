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
> ![[Pasted image 20241104151433.png]]
> ![[Pasted image 20241104151441.png]]

> [!abstract]- Théorème 6.6.2
> Si $f : \mathbb{R}_+ \to \mathbb{R}$ continue et décroissante, alors
> $$\int_{1}^{n} f(x) \, dx + f(n) \leq \sum_{k=1}^{n} f(k) \leq f(1) + \int_{1}^{n} f(x) \, dx$$
