---
title: Variance
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
---


> [!info]+ Définition
> La **variance** mesure la dispersion des valeurs autour de l'[[Espérance (expected value)#^c716f7|espérance]] d'une [[Variable aléatoire#^dcd8d2|variable aléatoire]].
> $$\sigma^2 = \text{Var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2$$

^4c0c18

> [!abstract]- Cas
> $$
> \begin{array}{|c|c|}
> \hline
> \text{Cas discret} & \text{Cas continu} \\
> \hline
> \text{Var}(X) = \sum_x (x-\mathbb{E}[X])^2 p_X(x) & \text{Var}(X) = \int_{-\infty}^\infty (x-\mathbb{E}[X])^2 f_X(x) dx \\
> \hline
> \end{array}
> $$
## Propriétés

> [!info]+ La variance d'une constante est nulle
> $$\text{Var}(c) = 0$$

> [!abstract]-  Preuve
> $$\text{Var}(c) = \mathbb{E}[(c-\mathbb{E}[c])^2] = \mathbb{E}[(c-c)^2] = 0$$

> [!info]+ La variance est le carré de l'[[Écart-type|écart-type]]
> $$  \text{Var}(X) = \sigma^2
> $$
### Linéarité de la variance

> [!info]+ Formule
> $$\text{Var}(mX+b) = m^2 \cdot \text{Var}(X)$$

> [!abstract]- Preuve
> $$\begin{align*}
> \text{Var}(mX + b) &= \mathbb{E}[(mX + b - \mathbb{E}[mX + b])^2] \\
> &= \mathbb{E}[(mX + b - m\mathbb{E}[X] - b)^2] \\
> &= \mathbb{E}[(m(X - \mathbb{E}[X]))^2] \\
> &= m^2 \cdot \mathbb{E}[(X - \mathbb{E}[X])^2] \\
> &= m^2 \cdot \text{Var}(X)
> \end{align*}$$

> [!info]+ Addition des variances (indépendantes)
> $$\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) \quad \text{si $X$ et $Y$ sont indépendantes}$$
