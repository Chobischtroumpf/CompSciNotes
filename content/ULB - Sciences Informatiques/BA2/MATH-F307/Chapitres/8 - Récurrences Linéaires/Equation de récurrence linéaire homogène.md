---
title: Equation de récurrence linéaire homogène
authors: Alessandro Dorigo
tags:
  - MathDis
---


 > [!info]+ Définition
> Une équation de récurrence est dite linéaire homogène si elle est du type:
>
> $$ f(n) = a_1 \cdot f(n-1) + a_2 \cdot f(n-2) + ... + a_d \cdot f(n-d)$$
> $$ = \sum_{i=1}^d a_i \cdot f(n-i) \quad \forall n \geq d$$
> où les $a_i \in \mathbb{R}$ sont fixés et $d$ est l'ordre de la récurrence.

> [!abstract]- Formule
> Solution de base d'une récurrence linéaire homogène :
> $$f(n) = \alpha^n$$ pour une constante $\alpha \in \mathbb{C}, \alpha \neq 0$.
>
> $$\text{Si } f(n) = \alpha_1^n \text{ et } f(n) = \alpha_2^n$$  sont solutions à une équation de récurrence linéaire (sans conditions initiales), alors
> $$f(n) = c_1 \cdot \alpha_1^n + c_2 \cdot \alpha_2^n$$
> est également solution de la même équation pour toutes constantes $c_1$ et $c_2$.

> [!example]+ Exemple (Fibonacci)
> $$f(n) = f(n-1) + f(n-2) \quad \forall n \geq 2$$
> $$\Leftrightarrow \alpha^n = \alpha^{n-1} + \alpha^{n-2} \quad \forall n \geq 2$$
> $$\Leftrightarrow \alpha^2 - \alpha - 1 = 0 \quad \text{[division par } \alpha^{n-2}\text{]}$$
> $$\Leftrightarrow \alpha = \frac{1 \pm \sqrt{5}}{2}$$
>
> Deux solutions particulières :
> $$f(n) = \varphi^n \quad \text{où } \varphi = \frac{1 + \sqrt{5}}{3} \text{ (nombre d'or)}$$
> $$f(n) = \bar{\varphi}^n \quad \text{où } \bar{\varphi} = \frac{1 - \sqrt{5}}{3}$$
