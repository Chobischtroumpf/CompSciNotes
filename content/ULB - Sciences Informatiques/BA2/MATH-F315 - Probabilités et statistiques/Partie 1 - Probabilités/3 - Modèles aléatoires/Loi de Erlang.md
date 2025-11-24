---
title: Loi de Erlang
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - On mesure le **temps d'attente** jusqu'à la **$r$-ème arrivée** dans un **[[Loi de Poisson|processus de Poisson]]**.
> - Les événements sont **indépendants** et se produisent à un **taux constant** $\lambda$.
> - $\lambda$ représente le **taux d'occurrence moyen** des événements par unité de temps, et $r$ est le **nombre d'arrivées** que l'on attend.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de densité/répartition} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \begin{aligned}
> f_X(x) &= \frac{x^{r-1} \lambda^r e^{-\lambda x}}{(r - 1)!} \\
> F_X(x) &= 1 - e^{-\lambda t} \sum_{k=0}^{r-1} \frac{(\lambda t)^k}{k!}
> \end{aligned}
> & \mathbb{R}^+ & \frac{r}{\lambda} & \frac{r}{\lambda^2} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**:
> - **Variable**:
> - **Probabilité**:
> - **Espérance**:
> - **Variance**:

> [!abstract]- Preuve pour $F_X$
> $$\begin{aligned}
> F_X(x) = \mathbb{P}(X \leq x) &= \mathbb{P}(Po(\lambda t) \geq r) \\
> &= 1 - \sum_{k=0}^{r-1} \mathbb{P}(X_t = k) \\
> &= 1 - e^{-\lambda t} \sum_{k=0}^{r-1} \frac{(\lambda t)^k}{k!}
> \end{aligned}$$
