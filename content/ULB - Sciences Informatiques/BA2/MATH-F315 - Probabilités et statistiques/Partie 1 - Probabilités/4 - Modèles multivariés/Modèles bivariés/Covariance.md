---
title: Covariance
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Définition
> Mesure de la tendance de deux variables de s’écarter de leurs [[Espérance (expected value)#^c716f7|espérances]] de manière similaire (covariance positive) ou de manière opposée (covariance négative). Deux façons de la calculer:
>
> 1. Comme un cas particulier de $w(X,Y) = (X - \mu_X) (Y - \mu_Y)$:
> $$\begin{aligned}
> \text{Cov}(X, Y) = \sigma_{X, Y} &= \mathbb{E} \big( (X - \mu_X)(Y - \mu_Y) \big) \\
> &= \int_{-\infty}^\infty \int_{-\infty}^\infty (z_1 - \mu_X)(z_2 - \mu_Y) f_{X, Y} (z_1, z_2) \ dz_1 \ dz_2
> \end{aligned}$$
>
> 2. En utilisant les propriétés de l’[[Espérance (expected value)#^c716f7|espérance]]:
> $$\begin{aligned}
> \text{Cov}(X, Y) \equiv \sigma_{XY} &= \mathbb{E}[(X - \mu_X) \cdot (Y - \mu_Y)] \\
> &= \mathbb{E}[X \cdot Y - X \cdot \mu_Y - \mu_X \cdot Y + \mu_X \cdot \mu_Y] \\
> &= \mathbb{E}[X \cdot Y] - \mathbb{E}[X] \cdot \mathbb{E}[Y]
> \end{aligned}$$

^3f0c34

- $\text{Cov}(X, X) = \sigma_{XX} = \sigma^2_X$

> [!abstract]- Propriétés
> $X,Y,Z$ sont des [[Variable aléatoire#^dcd8d2|v.a.]] et $a,b \in \mathbb{R}$. Alors:
>
> $$\begin{aligned}
> \text{Cov}(a + X, Y) &= \mathbb{E}[(a + X - (a + \mu_X)) \cdot (Y - \mu_Y)] \\
> &= \mathbb{E}[(X - \mu_X) \cdot (Y - \mu_Y)] \\
> &= \text{Cov}(X, Y) \\
> \text{Cov}(a \cdot X, b \cdot Y) &= \mathbb{E}[(a \cdot X - a \cdot \mu_X) \cdot (b \cdot Y - b \cdot \mu_Y)] \\
> &= \mathbb{E}[a \cdot (X - \mu_X) \cdot b \cdot (Y - \mu_Y)] \\
> &= a \cdot b \cdot \mathbb{E}[(X - \mu_X) \cdot (Y - \mu_Y)] \\
> &= a \cdot b \cdot \text{Cov}(X, Y) \\
> \text{Cov}(X, Y + Z) &= \mathbb{E}[(X - \mu_X) \cdot (Y + Z - \mu_Y - \mu_Z)] \\
> &= \mathbb{E}[(X - \mu_X) \cdot ((Y - \mu_Y) + (Z - \mu_Z))] \\
> &= \mathbb{E}[(X - \mu_X) \cdot (Y - \mu_Y) + (X - \mu_X) \cdot (Z - \mu_Z)] \\
> &= \text{Cov}(X, Y) + \text{Cov}(X, Z)
> \end{aligned}$$

> [!abstract]- Proposition
> De façon plus générale nous avons que si $X_i, Y_i$ sont des [[Variable aléatoire#^dcd8d2|v.a.]] et $a, b_i, c, d_j \in \mathbb{R}$ pour $i = 1, \dots, n$ et $j = 1, \dots, m$ avec des [[Variable aléatoire#^dcd8d2|v.a.]] définis de la façon suivante
> $$U = a + \sum_{i=1}^n b_i \cdot X_i \text{ et } V = c + \sum_{j=1}^m d_j \cdot Y_j$$
>
> Nous avons:
> $$\text{Cov}(U,V) = \sum_{i=1}^n \sum{j=1}^m b_i \cdot d_j \cdot \text{Cov}(X_i, Y_j)$$

> [!abstract]- Corollaires
> - $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2 \text{Cov}(X,Y)$
> - $\text{Var}(aX) = a^2 \text{Var}(X)$

> [!info]+ Preuve de la somme des [[Variance#^4c0c18|variances]]
> $$\begin{aligned}
> \text{Var}(X + Y) &= \text{Cov}(X + Y, X + Y) \\
> &= \mathbb{E}[(X + Y - \mu_{X+Y}) \cdot (X + Y - \mu_{X+Y})] \\
> &= \mathbb{E}[(X + Y - \mu_X - \mu_Y) \cdot (X + Y - \mu_X - \mu_Y)] \\
> &= \mathbb{E}[((X - \mu_X) + (Y - \mu_Y)) \cdot ((X - \mu_X) + (Y - \mu_Y))] \\
> &= \mathbb{E}[(X - \mu_X)^2 + 2(X - \mu_X)(Y - \mu_Y) + (Y - \mu_Y)^2] \\
> &= \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y) \quad \square
> \end{aligned}$$
