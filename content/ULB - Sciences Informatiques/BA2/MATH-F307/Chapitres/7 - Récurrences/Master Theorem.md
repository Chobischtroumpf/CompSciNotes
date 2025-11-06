---
title: Master Theorem
authors: Alessandro Dorigo
tags:
  - MathDis
  - Recurrence
---


> [!info]+ Définition
> Le **Master Theorem** est une méthode simplifiée pour résoudre des récurrences de type [[Diviser pour régner (maths discrètes)#^84a5e1|diviser pour régner]] lorsqu'il n'y a qu'un seul sous-problème (c'est-à-dire $k = 1$) et lorsque le terme de coût $g(x)$ est bien défini.

> [!abstract]- Théorème 7.5.1 (Master Theorem)
> Soit donnée une équation de récurrence de type *diviser pour régner* sous la forme suivante:
> $$T(x) = a \cdot T\left(\frac{x}{b} + \varepsilon(x)\right) + g(x)$$
>
> pour $x \geq x_0$, où $k = 1$ et $a, b > 0$, et où $p = \log_b(a)$.
>
> Le Master Theorem donne trois cas selon le comportement asymptotique de $g(x)$:
>
> 1. **Cas 1**: $g(x) \in \mathcal{O}(x^{p - \delta})$ pour un certain $\delta > 0$.
>    - Dans ce cas, $T(x) \in \Theta(x^p)$.
>
> 2. **Cas 2**: $g(x) \in \Theta(x^p)$.
>    - Dans ce cas, $T(x) \in \Theta(x^p \log(x))$.
>
> 3. **Cas 3**: $g(x) \in \Omega(x^{p + \delta})$ pour un certain $\delta > 0$, et $a \cdot g \left( \frac{x}{b} \right) < c \cdot g(x)$ pour un certain $c < 1$ et pour $x$ suffisamment grand.
>    - Dans ce cas, $T(x) \in \Theta(g(x))$.

^65c937
![[Akra-Bazzi#^118e4c]]

En comparaison, le Master Theorem suppose que:
- Le nombre de sous-problèmes est constant et égal à 1.
- Les sous-problèmes sont de taille exactement $\frac{x}{b}$.
- Le terme de coût $g(x)$ suit un des trois comportements asymptotiques spécifiques, permettant une analyse simplifiée.

### Exemples
> [!example]+ $T(x) = 2 \cdot T\left(\frac{x}{2}\right) + x$ ([[Mergesort (maths discrètes)|Merge Sort]])
> - Paramètres: $a = 2$, $b = 2$, donc $p = \log_2(2) = 1$.
> - Comparaison de $g(x) = x$ avec $x^p = x$.
>   - **Cas 2** du théorème maître : $g(x) \in \Theta(x^p)$.
>   - Conclusion : $T(x) \in \Theta(x \log(x))$.

> [!example]+ $T(x) = 3 \cdot T\left(\frac{x}{4}\right) + x^2$
> - Paramètres: $a = 3$, $b = 4$, donc $p = \log_4(3) \approx 0.79$.
> - Comparaison de $g(x) = x^2$ avec $x^p$.
>   - **Cas 3** du théorème maître : $g(x) \in \Omega(x^{p + \delta})$ pour $\delta > 0$, et $a \cdot g\left(\frac{x}{b}\right) < c \cdot g(x)$.
>   - Conclusion : $T(x) \in \Theta(x^2)$.
