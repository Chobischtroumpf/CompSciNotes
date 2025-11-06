---
title: Loi log-normale
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - Soit $\mu > 0$ et $\sigma > 0$.

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de densité/répartition/$\Phi$} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \begin{aligned}
> f_X(x) &= \frac{1}{\sqrt{2 \pi} \sigma x} e^{-\frac{(\ln(x) - \mu)^2}{2\sigma^2}} \\
> F_X(x) &= \Phi_{\mu, \sigma^2}(\ln(x))
> \end{aligned}
> & \mathbb{R}^+ & e^{\mu + \frac{\sigma^2}{2}} & \left(e^{\sigma^2} - 1\right) e^{2\mu + \sigma^2} \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**:
> - **Variable**:
> - **Probabilité**:
> - **Espérance**:
> - **Variance**:

F_X
$$ F_X(x) = \mathbb{P}(X \leq x) = \mathbb{P}(\ln(X) \leq \ln(x))  = \Phi_{\mu, \sigma^2}(\ln(x))$$
