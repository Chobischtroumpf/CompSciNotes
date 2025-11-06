---
title: Diviser pour régner (maths discrètes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Recurrence
  - Algo
---


> [!info]+ Définition
> Une récurrence de type **diviser pour régner** est une récurrence de la forme
> $$\begin{aligned}
> T(x) = a_1 \cdot T(b_1x + \varepsilon_1(x)) + a_2 \cdot T(b_2x + \varepsilon_2(x)) + \cdots + a_k \cdot T(b_k + \varepsilon_k(x)) + g(x)
> \end{aligned}$$
>
> pour $x \geq x_0$ et avec $k$ fixé, où:
> - $T : \mathbb{R} \rightarrow \mathbb{R}$ est une fonction non-négative et bornée pour $0 \leq x \leq x_0$,
> - $a_i > 0$ (coefficients positifs),
> - $0 < b_i < 1$ (les sous-problèmes sont des fractions de la taille originale),
> - $x_0$ est une constante,
> - $\vert \varepsilon_i(x) \vert \in \mathcal{O} \left( \frac{x}{\log^2(x)} \right)$ (petite erreur par rapport à la taille du sous-problème),
> - $g$ est une fonction non-négative telle que $\vert g'(x) \vert \leq x^c$ pour une constante $c \in \mathbb{R}$.

^84a5e1
### Autre récurrence de type diviser pour régner
> [!info]+ Définition
> La récurrence suivante modélise un processus où un problème de taille $n$ est divisé en deux sous-problèmes de tailles proches, avec une opération supplémentaire de coût constant:
>
> $$\begin{cases}
> T(1) = 0 \\
> T(n) = T \left( \left\lceil \frac{n}{2} \right\rceil \right) + T \left( \left\lfloor \frac{n}{2} \right\rfloor \right) + 1 \quad \text{pour } n \in \mathbb{Z}_{\geq 2}
> \end{cases}$$

> [!example]+ Exemples
> - $T(2) = T(1) + T(1) + 1 = 0 + 0 + 1 = 1$
> - $T(3) = T(2) + T(1) + 1 = 1 + 0 + 1 = 2$
> - $T(4) = T(2) + T(2) + 1 = 1 + 1 + 1 = 3$
> - $T(5) = T(3) + T(2) + 1 = 2 + 1 + 1 = 4$
> Après quelques calculs, on peut conjecturer que:
> $$T(n) = n − 1, \quad \forall n \in \mathbb{Z}_{\geq 2}$$

> [!abstract]- Théorème 7.2.1
> Pour tout $n \in \mathbb{Z}_{\geq 1}$, on a:
> $$T(n) = n - 1$$
>
> ![[Pasted image 20241111113906.png]]

![[Pasted image 20241105094448.png]]
