---
title: Distance relative
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> La **distance relative** $\eta(x_i)$ entre deux nombres consécutifs $x_i$ et $x_{i+1}$ en représentation à virgule flottante est définie par:
> $$ \eta(x_i) = \frac{|x_{i+1} - x_i|}{x_i} $$
> Elle mesure l'écart relatif entre deux nombres adjacents en machine.

## Formule générale
Si $x_i$ et $x_{i+1}$ ont le **même exposant**, alors:
$$ \eta(x_i) = \frac{|x_{i+1} - x_i|}{x_i} = \frac{m[x_{i+1}]b^{e-t} - m[x_i]b^{e-t}}{m[x_i]b^{e-t}} = \frac{b^{-t}}{m[x_i]} = \frac{1}{m[x_i]} $$
où $m[x_i]$ est la **mantisse** du nombre réel $x_i$.

Si $x_{i+1}$ a un **exposant plus grand** que $x_i$, alors:
$$
\begin{cases}
x_{i+1} = b^{t-1}b^{e+1-t} = b^e \\
x_i = (b^t - 1)b^{e-t} = b^e - b^{e-t}
\end{cases}
$$
et donc:
$$ x_{i+1} - x_i = b^{e-t} $$
> [!tip]+ Remarque
> On retrouve donc la même expression pour la distance relative:
> $$ \eta(x_i) = \frac{1}{m[x_i]} $$

Puisque $b^t > m \geq b^{t-1}$, alors:
$$ b^{-t} < \frac{1}{m} \leq b^{1-t} $$
On en déduit:
$$ \frac{\epsilon}{b} < \eta(x_i) \leq \epsilon $$

Avec $\epsilon$ étant [[Epsilon machine#^ddcbf6|l'epsilon machine]].
