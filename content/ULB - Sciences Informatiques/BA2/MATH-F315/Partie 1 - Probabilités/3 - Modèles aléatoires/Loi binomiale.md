---
title: Loi binomiale
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - On répète **$n$ essais indépendants**, chaque essai ayant deux issues: succès ou échec.
> - $p$ est la probabilité de succès à chaque essai, avec $0 \leq p \leq 1$.
> - On s'intéresse au **nombre total de succès** parmi les $n$ essais.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de masse} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \mathbb{P}(X = k) = \binom{n}{k}p^k(1 - p)^{n - k} & \{0, 1, \dots, n\} & np & np(1-p) \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**: On fait du tir à l'arc, avec $9$ tirs indépendants. La probabilité de réussir un "bullseye" est de $0.05$ (5%).
> - **Variable**: Soit $X$ le nombre de "bullseyes" réalisés en 9 tirs. $X$ suit une loi binomiale avec $n = 9$ et $p = 0.05$.
> - **Probabilité**: La probabilité de réaliser exactement $k$ "bullseyes" est donnée par:
>   $$\mathbb{P}(X = k) = \binom{9}{k} (0.05)^k (0.95)^{9 - k}, \quad k \in \{0, 1, \dots, 9\}$$
> - **Espérance**: Le nombre moyen attendu de "bullseyes" est $\mathbb{E}[X] = np = 9 \times 0.05 = 0.45$. Donc, on s'attend en moyenne à environ $0.45$ "bullseyes" sur 9 tirs.
> - **Variance**: La variance, qui mesure la dispersion autour de la moyenne, est $$\text{Var}(X) = np(1 - p) = 9 \times 0.05 \times 0.95 = 0.4275$$
