---
title: Loi de Poisson
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - On compte le **nombre de succès** (événements) qui se produisent dans un **intervalle de temps**.
> - Les événements sont **indépendants** et ont lieu avec un taux constant $\lambda > 0$ (le nombre moyen d'événements par unité de temps).
> - Le nombre de répétitions est infini, mais la **probabilité individuelle de chaque événement** est infinitésimale.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de masse} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \mathbb{P}(X = x) = \frac{e^{-\lambda}\lambda^x}{x!} & \mathbb{N} & \lambda & \lambda \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**: On observe le nombre d'avions qui atterrissent à l'aéroport de Zaventem entre 12h30 et 14h00. Le nombre moyen d'atterrissages par intervalle de 1h30 est de 7 (c'est notre $\lambda$).
> - **Variable**: Soit $X$ le nombre d'avions qui atterrissent durant cette période. $X$ suit une **loi de Poisson** avec paramètre $\lambda = 7$.
> - **Probabilité**: La probabilité d'observer exactement $x$ avions qui atterrissent est donnée par:
> $$\mathbb{P}(X = x) = \frac{e^{-7}7^x}{x!}, \quad x \in \mathbb{N}$$
> - Par exemple, la probabilité qu'exactement **5 avions** atterrissent durant cette période est:
> $$\mathbb{P}(X = 5) = \frac{e^{-7}7^5}{5!} = 0.1277$$
> - **Espérance**: Le nombre moyen attendu d'avions qui atterrissent est:
> $$\mathbb{E}[X] = \lambda = 7$$
> - **Variance**: La variance du nombre d'atterrissages est:
> $$\text{Var}(X) = \lambda = 7$$
