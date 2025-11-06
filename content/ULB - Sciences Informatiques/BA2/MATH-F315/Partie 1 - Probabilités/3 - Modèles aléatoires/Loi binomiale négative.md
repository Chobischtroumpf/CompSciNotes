---
title: Loi binomiale négative
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - On compte le **nombre d'essais** lors de répétitions **indépendantes** avant d'obtenir **exactement $r$ succès**.
> - $p$ est la probabilité de succès à chaque essai.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de masse} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \mathbb{P}(X = k) = \binom{k - 1}{r - 1}(1 - p)^{k - r}p^r & \mathbb{N}\backslash \{0,1,\dots,r - 1\} & \frac{r}{p} & \frac{r(1 - p)}{p^2} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**: Reprenons l'exemple du tir à l'arc. On effectue des tirs indépendants et la probabilité de réussir un "bullseye" est de $p = 0.05$ (5%). On se demande **combien de tirs $k$** sont nécessaires pour obtenir exactement **10 "bullseyes"**.
> - **Variable**: Soit $X$ le nombre total de tirs nécessaires pour obtenir 10 "bullseyes". $X$ suit une **loi binomiale négative** avec $r = 10$ et $p = 0.05$.
> - **Probabilité**: La probabilité d'obtenir le 10ème "bullseye" exactement au $k$-ième tir est donnée par:
> $$\mathbb{P}(X = k) = \binom{k - 1}{9}(1 - 0.05)^{k - 10}(0.05)^{10}, \quad k \geq 10$$
> - **Espérance**: Le nombre moyen de tirs nécessaires pour obtenir 10 "bullseyes" est:
> $$\mathbb{E}[X] = \frac{10}{0.05} = 200$$
   Donc, en moyenne, il faut **200 tirs** pour obtenir 10 "bullseyes".
> - **Variance**: La variance, qui mesure la dispersion autour du nombre moyen de tirs nécessaires, est:
> $$\text{Var}(X) = \frac{10 \times (1 - 0.05)}{(0.05)^2} = 1900$$
   Cela signifie que la dispersion autour de cette moyenne est de **1900**.
