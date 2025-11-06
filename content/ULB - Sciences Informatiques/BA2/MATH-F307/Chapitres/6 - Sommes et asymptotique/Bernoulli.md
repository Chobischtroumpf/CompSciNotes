---
title: Bernoulli
authors: Alessandro Dorigo
tags:
  - MathDis
  - Sommes
  - Algo
---


> [!info]+ Définition
> La suite des **nombres de Bernoulli** est la seule suite
> $$(B_0, B_1, B_2, B_3, \dots) = (B_k)_{k \in \mathbb{N}}$$
>
> telle que $\forall x \in \mathbb{R}$:
> $$x = \left( B_0 + B_1 x + \frac{B_2 x^2}{2!} + \frac{B_3 x^3}{3!} + \dots \right) \cdot \left( x + \frac{x^2}{2} + \frac{x^3}{3!} + \dots \right)$$
>
> En d’autres termes:
> $$\sum_{k=0}^{\infty} B_k \cdot \frac{x^k}{k!} = \frac{x}{e^x - 1}$$

> [!abstract]- Théorème 6.4.1
> $$\sum_{k=1}^{n-1} k^p = \frac{1}{1 + p} \left( n^{p+1} + \sum_{k=1}^{p} \binom{p+1}{k} B_k n^{p+1-k} \right)$$
>
> où $B_0, B_1, B_2, \dots$ sont les nombres de Bernoulli:
> $$B_0 = 1, \quad B_1 = -\frac{1}{2}, \quad B_2 = \frac{1}{6}, \quad B_3 = 0, \quad \dots$$
>
> et
> $$\binom{n}{k} = \frac{n!}{k!(n - k)!}$$
> c’est le coefficient binomial.
>
> **Démonstration:**
> $$\begin{aligned}
> \sum_{p=0}^{\infty} \left( \sum_{k=0}^{n-1} k^p \right) \frac{x^p}{p!} &= \sum_{k=0}^{n-1} \sum_{p=0}^{\infty} \frac{(kx)^p}{p!} = \sum_{k=0}^{n-1} e^{kx} \\ &= 1 + e^x + (e^x)^2 + (e^x)^3 + \cdots + (e^x)^{n-1} \\ &= \frac{1 - e^{nx}}{1 - e^x} = \frac{x}{e^x - 1} \cdot \frac{e^{nx} - 1}{x} \\ &= \left( \sum_{k=0}^{\infty} B_k \cdot \frac{x^k}{k!} \right) \cdot \left( \sum_{i=0}^{\infty} \frac{n^{i+1}}{i+1} \cdot \frac{x^i}{i!} \right) \\ &= \sum_{p=0}^{\infty} \left( \sum_{i,k : i + k = p} B_k \cdot \frac{n^{i+1}}{i+1} \cdot \frac{p!}{i! k!} \right) \frac{x^p}{p!}
> \end{aligned}$$
>
> On a
> $$\sum_{p=0}^{\infty} \left( \sum_{k=0}^{n-1} k^p \right) \frac{x^p}{p!} = \sum_{p=0}^{\infty} \left( \sum_{i,k : i + k = p} B_k \cdot \frac{n^{i+1}}{i+1} \cdot \frac{p!}{i! k!} \right) \frac{x^p}{p!},$$
>
> mais
> $$\frac{n^{i+1}}{i+1} \cdot \frac{p!}{i! k!} = \frac{n^{i+1}}{p+1} \cdot \frac{(p+1)!}{(i+1)! k!} = \frac{n^{p-k+1}}{p+1} \cdot \binom{p+1}{k}$$
>
> et donc
> $$\sum_{p=0}^{\infty} \left( \sum_{k=0}^{n-1} k^p \right) \frac{x^p}{p!} = \sum_{p=0}^{\infty} \left( \sum_{k=0}^{p} B_k \cdot \frac{n^{p+1-k}}{p+1} \cdot \binom{p+1}{k} \right) \frac{x^p}{p!}$$
>
> d'où il résulte que
> $$\sum_{k=0}^{n-1} k^p = \sum_{k=0}^{p} B_k \cdot \binom{p+1}{k} \cdot \frac{n^{p+1-k}}{p+1}$$
