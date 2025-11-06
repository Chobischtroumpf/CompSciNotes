---
title: Loi Beta
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - Soit $\alpha > 0$ et $\beta > 0$.
> - Le paramètre $\alpha$ est le nombre de succès et $\beta$ est le nombre d’échecs.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de densité/$B$} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \begin{aligned}
> f_X(x) &= \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1} \\
> B(\alpha, \beta) &= \int_0^1 u^{\alpha - 1} (1 - u)^{\beta - 1} du \\
> &= \frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha + \beta)}
> \end{aligned}
> & [0,1] & \frac{\alpha}{\alpha + \beta} & \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**:
> - **Variable**:
> - **Probabilité**:
> - **Espérance**:
> - **Variance**:
