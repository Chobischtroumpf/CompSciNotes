---
title: Arithmétique modulaire
authors: Alessandro Dorigo
tags:
  - MathDis
  - TheorieDesNombres
---


> [!abstract]- Théorème 3.3.1 - Fonction $\phi$ d'Euler
> Pour $n \in \mathbb{N}$, $\phi(n)$ est le nombre d'entiers compris entre $1$ et $n$ qui sont premiers avec $n$.
>
> $$\phi(n) := \vert \{k \in [n] \mid \text{pgcd}(n,k) = 1\} \vert$$

> [!abstract]- Théorème 3.3.2
> $\forall n \in \mathbb{N}$
>
> $$\phi(n) = n \cdot \left(1 - \frac{1}{p_1} \right) \cdot \left(1 - \frac{1}{p_2} \right) \cdot \cdots \cdot \left(1 - \frac{1}{p_t} \right)$$
>
> où $\{p_1, p_2, \dots, p_t \}$ est l’ensemble des diviseurs premiers de $n$.
>
> ![[Pasted image 20241212144347.png]]
> ![[Pasted image 20241212144401.png]]

> [!abstract]- Théorème d'Euler 3.3.3
> Pour tout entier $n \in \mathbb{N}$ et tout entier $k$ premier avec $n$, on a:
> $$k^{\phi(n)} \equiv 1 \ (\text{mod}\ n)$$

^770741

> [!info]+ Espace des nombres premiers avec $n$
> Si on pose:
> $$\mathbb{Z}_n^* := \{ x \in \mathbb{Z}_n \mid x \text{ est premier avec } n \},$$
> qui sont les éléments **inversibles** dans $\mathbb{Z}_n$, alors $\phi(n) = |\mathbb{Z}_n^*|$.
>
> On peut reformuler le [[Arithmétique modulaire#^770741|théorème d'Euler]]:
>
> Pour tout $k \in \mathbb{Z}_n^*$:
> $$k^{\phi(n)} = 1 \quad (\text{dans } \mathbb{Z}_n)$$

> [!abstract]- Lemme 3.3.4
> Si $x,y \in \mathbb{Z}_n^{*}$, alors $x \cdot y \in \mathbb{Z}_n^{*}$.

> [!abstract]- Lemme 3.3.5
> Si $k \in \mathbb{Z}_n^{*}$ et $S \subseteq \mathbb{Z}_n$, alors
> $$\vert kS \vert = \vert S \vert $$
> ou $kS := \{k \cdot _nx \mid x \in S\}$.
>
> ![[Pasted image 20241014170428.png]]
> ![[Pasted image 20240930151131.png]]

> [!tip]+ Corollaire
> $\forall k \in \mathbb{Z}_n^{*} : k \mathbb{Z}_n^{*} = \mathbb{Z}_n^{*}$.

> [!abstract]- Petit théorème de Fermat 3.3.6
> Soit $p$ un nombre premier. Pour tout entier $k$ non multiple de $p$, on a:
> $$k^{p-1} \equiv 1 \ (\text{mod}\ p)$$
> Cela découle du [[Arithmétique modulaire#^770741|théorème d'Euler]], puisque $\phi(p) = p - 1$.
>
> De plus:
> $$\forall k \in \mathbb{Z}, \quad k^p \equiv k \pmod{p}$$
