---
title: Epsilon machine
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> L’**epsilon machine** $\epsilon$ est la **distance relative maximale** entre deux nombres consécutifs en machine.
> - Dépend de la **base $b$** et du **nombre de chiffres significatifs $t$**:
> $$ \epsilon = b^{1-t} $$
> - **La distance relative minimale** est $\frac{\epsilon}{b}$.
> - En notation IEEE 754, $\epsilon$ correspond à `eps` en MATLAB.

^ddcbf6

> [!example]+ Exemple
> Considérons le nombre $x_i = 1 = 0.1 \cdot b^1$, donc $e = 1$.
> - Sa mantisse est:
> $$ m[x_i] = (-1)^s x_i b^{t-e} = 1 \cdot 1 \cdot b^{t-1} = 1000\dots00 $$
> - La valeur minimale de $m[x_i]$ est donc atteinte.
> - La distance entre $x_i$ et son successeur est:
> $$ x_{i+1} - x_i = \eta(x_i) = \frac{1}{m[x_i]} = b^{1-t} = \epsilon $$

> [!abstract]- Conclusion
> - Pour $x_i = 1$, on a :
>   $$ x_{i+1} = 1 + \epsilon $$
> - Donc $\epsilon$ est la **plus petite valeur ajoutable à 1** pour obtenir un nombre distinct en virgule flottante.
