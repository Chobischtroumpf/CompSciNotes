---
title: Loi de Gamma
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - Soit $\lambda > 0$ et $r > 0$.
> - Généralisation du [[Loi de Erlang|modèle de Erlang]] avec $r$ non entier.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de densité/Gamma} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \begin{aligned}
> f_X(x) &= \frac{x^{r-1} \lambda^r e^{-\lambda x}}{\Gamma(r)} \\
> \Gamma(r) &= \int_0^{\infty} u^{r-1} e^{-u} du
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
