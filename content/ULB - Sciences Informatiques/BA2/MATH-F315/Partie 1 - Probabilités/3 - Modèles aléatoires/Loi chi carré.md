---
title: Loi chi carré
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


> [!info]+ Caractéristiques
> - Soit $\nu > 0$ et $\nu \in \mathbb{N}_0$, appelé le **nombre de degrés de liberté**.
> - Cas particulier de la loi Gamma avec $\Gamma(1/2, \nu/2)$:
>
> $$X \sim \chi^2_\nu \iff X \sim \Gamma(1/2, \nu/2)$$

- Loi qui apparaît régulièrement dans la partie statistique (test d’hypothèses).

> [!abstract]- Proposition
> $$\Gamma(1/2) = \int_0^{\infty} \frac{e^{-u}}{\sqrt{u}} du = \sqrt{2} \cdot \int_0^{\infty} e^{-x^2/2} dx = \sqrt{2} \cdot \frac{1}{2} \cdot \sqrt{2\pi}$$

> [!abstract]- Proposition
> Cette distribution est liée à la [[Loi normale|loi normale]]:
> Si $Z \sim \mathcal{N}(0,1)$, alors $X = Z^2 \sim \chi^2_1$

> [!abstract]- Formules
> $$
> \begin{array}{|c|c|c|c|}
> \hline
> \text{Fonction de densité/répartition} & \text{Support} & \mathbb{E}[X] & \text{Var}(X) \\
> \hline
> \begin{aligned}
> f_X(x) &= \frac{e^{-\frac{x}{2}}}{\sqrt{2} \sqrt{\pi} \sqrt{x}} \\
> F_X(x) &= F_Z(\sqrt{x}) - F_Z(-\sqrt{x})
> \end{aligned}
> & \mathbb{R}^+ & \nu & 2\nu \\
> \hline
> \end{array}
> $$

> [!example]+ Exemple
> - **Contexte**:
> - **Variable**:
> - **Probabilité**:
> - **Espérance**:
> - **Variance**:

> [!abstract]- Preuve pour $f_X$
> $$\begin{align*}
> f_X(x) = F'_X(x) &= F'_Z(\sqrt{x}) \frac{1}{2\sqrt{x}} - F'_Z(-\sqrt{x}) \frac{-1}{2\sqrt{x}} \\ &= \frac{f_Z(\sqrt{x})}{\sqrt{x}} = \frac{e^{-x/2}}{\sqrt{2} \sqrt{\pi} \sqrt{x}}
> \end{align*}$$

> [!abstract]- Preuve pour $F_X$
> $$\begin{align*}
> F_X(x) &= \mathbb{P}(X \leq x) = \mathbb{P}(Z^2 \leq x) = \mathbb{P}(-\sqrt{x} \leq Z \leq \sqrt{x}) \\ &= F_Z(\sqrt{x}) - F_Z(-\sqrt{x})
> \end{align*}$$
