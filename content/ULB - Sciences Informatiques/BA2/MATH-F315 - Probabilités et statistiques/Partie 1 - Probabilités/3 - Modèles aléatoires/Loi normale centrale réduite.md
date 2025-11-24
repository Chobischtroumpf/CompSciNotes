---
title: Loi normale centrale réduite
authors: Alessandro Dorigo
tags:
  - Proba
  - VarAlea
  - ModAlea
---


- On ne peut pas calculer les probabilités associées à une [[Loi normale|loi normale]] “à la main”.

Même si on prend $\mu = 0$ et $\sigma = 1$:
$$F_X(x) = \mathbb{P}(X \leq x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2 \pi}} e^{-x^2 / 2} dx$$

> [!info]+ Caractéristiques
> - Soit $X \sim \mathcal{N}(\mu, \sigma^2)$.
> - Alors $Z = \frac{X - \mu}{\sigma} \equiv X = \mu + \sigma Z$.
> - Donc $Z \sim \mathcal{N}(0,1)$.
> $$F_X(x) = \mathbb{P}(X \leq x) = \mathbb{P}(\mu + \sigma Z \leq x) = \mathbb{P}\left(Z \leq \frac{x - \mu}{\sigma}\right) = F_Z\left(\frac{x - \mu}{\sigma}\right)$$

^dd4c44

> [!tip]+ Quantiles
> | ![[0621f588c6db0e7faa6ca5a7c5df57da.png]] | ![[0b47f8b9ed6a7c33acc48e21adc8a302.png]] |
> | :----------------------------------: | :----------------------------------: |
>
> Nous utilisons souvent $z_\alpha$, la valeur avec probabilité $\alpha$ de dépassement. Ceci correspond à un quantile de $Z$:
> $$1 - F_Z(z_\alpha) = \alpha \iff F_Z(z_\alpha) = 1 - \alpha \iff z_\alpha = Q_Z(1 - \alpha)$$
> $$
> \begin{array}{|c|c|}
> \hline
> \alpha & z_\alpha \\
> \hline
> 10\% & 1{,}28 \\
> \hline
> 5\% & 1{,}645 \\
> \hline
> 2{,}5\% & 1{,}96 \\
> \hline
> 1\% & 2{,}33 \\
> \hline
> 0{,}5\% & 2{,}575 \\
> \hline
> \end{array}
> $$

> [!tip]+ Tableau de la loi normale centrée réduite
> ![[1db5e2f1048f61dd0343f834cc7a05a3.png]]


> [!tip]
> Soient $a,b$ deux valeurs consecutives de $X$ présentes dans le tableau de la loi normale centrée réduite, et $c$ une valeur entre celles-ci.
> $$\begin{array}{c}
> \mathbb{P}(X\leq a)=p_1\\
> \mathbb{P}(X\leq b)=p_2
> \end{array}
> $$
> Soient alors $\Delta p = p_2\ -\ p_1$  et $\alpha = \frac{c-a}{b-a}$.
> Nous avons :
> $$\mathbb{P}(X\leq c) \approx p_1+\alpha\cdot\Delta p$$
