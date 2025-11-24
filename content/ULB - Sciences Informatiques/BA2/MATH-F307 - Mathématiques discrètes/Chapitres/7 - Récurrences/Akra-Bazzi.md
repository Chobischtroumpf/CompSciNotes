---
title: Akra-Bazzi
authors: Alessandro Dorigo
tags:
  - MathDis
  - Recurrence
---


> [!tip]+ Remarque
> Le [[Akra-Bazzi#^e2e8a1|théorème d'Akra-Bazzi]] est une généralisation du [[Master Theorem#^65c937| Master Theorem]] qui permet de traiter des récurrences plus complexes, en particulier lorsque:
> - Il y a plusieurs sous-problèmes (c'est-à-dire $k \geq 1$).
> - Les tailles des sous-problèmes ne sont pas simplement des fractions fixes de la taille initiale.
> - Le terme de coût $g(x)$ peut avoir des comportements asymptotiques plus généraux.

^118e4c

### Théorèmes
> [!abstract]- Théorème 7.4.1 (Akra-Bazzi)
> Soit $T$ une récurrence de type [[Diviser pour régner (maths discrètes)#^84a5e1|diviser pour régner]] et soit $p \in \mathbb{R}$ tel que $\sum_{i=1}^{k} a_i b_i^p = 1$. Alors
>
> $$T(x) \in \Theta \left( x^p + x^p \int_{1}^{x} \frac{g(u)}{u^{p+1}} \, du \right)$$

^e2e8a1

> [!abstract]- Théorème 7.4.2
> Si $g(x) = \Theta(x^t)$ pour $t \geq 0$ et $\sum_{i=1}^k a_i b_i^t < 1$, alors
> $$T(x) \in \Theta(g(x)) = \Theta(x^t)$$
### Exemples
> [!example]+ $T(x) = 2 \cdot T(\frac{x}{2}) + (x-1)$ (Mergesort)
> - Paramètres: $g(x) = x - 1$, $k = 1$, $p = 1$ car $2 \cdot \left(\frac{1}{2}\right)^p = 1 \Rightarrow p = 1$.
>
> - Application du théorème **Akra-Bazzi**:
> $$\begin{aligned}
> T(x) &\in \Theta \left( x + x \int_{1}^{x} \frac{u - 1}{u^2} \, du \right) \\
> &= \Theta \left( x + x \left[ \log(u) + \frac{1}{u} \right]_{1}^{x} \right) \\
> &= \Theta \left( x + x \left( \log(x) + \frac{1}{x} - 1 \right) \right) \\
> &= \Theta(x \log(x))
> \end{aligned}$$

> [!example]+ $T(x) = T \left( \frac{x}{2} + \epsilon_1(x) \right) + T \left( \frac{x}{2} + \epsilon_2(x) \right) + 1$
> - Paramètres: $g(x) = 1$, $k = 2$, $p = 1$ car $1 \cdot \left(\frac{1}{2}\right)^p + 1 \cdot \left(\frac{1}{2}\right)^p = 1 \Rightarrow p = 1$.
>
> - Application du théorème **Akra-Bazzi**:
> $$\begin{aligned}
> T(x) &\in \Theta \left( x + x \int_{1}^{x} \frac{1}{u^2} \, du \right) \\
> &= \Theta \left( x + x \left[ \frac{1}{u} \right]_{1}^{x} \right) \\
> &= \Theta \left( x + x \left( -\frac{1}{x} + 1 \right) \right) \\
> &= \Theta(x)
> \end{aligned}$$

> [!example]+ $T(x) = 2 \cdot T \left( \frac{x}{2} \right) + \frac{8}{9} \cdot T \left( \frac{3x}{4} \right) + x^2$
> - Paramètres: $g(x) = x^2$, $k = 2$, $p = 2$ car $2 \cdot \left(\frac{1}{2}\right)^p + \frac{8}{9} \cdot \left(\frac{3}{4}\right)^p = 1 \Rightarrow p = 2$.
>
> - Application du théorème **Akra-Bazzi**:
> $$\begin{aligned}
> T(x) &\in \Theta \left( x^2 + x^2 \int_{1}^{x} \frac{u^2}{u^3} \, du \right) \\
> &= \Theta \left( x^2 + x^2 \left[ \log(u) \right]_{1}^{x} \right) \\
> &= \Theta \left( x^2 + x^2 \log(x) \right) \\
> &= \Theta \left( x^2 \log(x) \right)
> \end{aligned}$$

> [!example]+ $T(x) = 3 \cdot T \left( \frac{x}{3} \right) + 4 \cdot T \left( \frac{x}{4} \right) + x^2$
> - Paramètres:
> 	- Condition pour $p$: $3 \cdot \left(\frac{1}{3}\right)^p + 4 \cdot \left(\frac{1}{4}\right)^p = 1$
> 	- Si $p = 1$, alors $3 \cdot \frac{1}{3} + 4 \cdot \frac{1}{4} > 1$;
> 	- Si $p = 2$, alors $3 \cdot \frac{1}{9} + 4 \cdot \frac{1}{16} < 1$;
> 	- Donc, il existe $1 < p < 2$.
>
> - Application du théorème **Akra-Bazzi**:
> $$\begin{aligned}
> T(x) &\in \Theta \left( x^p + x^p \int_{1}^{x} \frac{u^2}{u^{p+1}} \, du \right) \\
> &= \Theta \left( x^p + x^p \left[ \frac{u^{2 - p}}{2 - p} \right]_{1}^{x} \right) \\
> &= \Theta \left( x^p + x^p \left( \frac{x^{2 - p}}{2 - p} - \frac{1}{2 - p} \right) \right) \\
> &= \Theta \left( x^2 \right)
> \end{aligned}$$
