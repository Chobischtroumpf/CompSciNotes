---
title: Matrice variance-covariance
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Définition
> La [[Variance#^4c0c18|variance]] du vecteur aléatoire $\underline X$ est aussi nommée la **matrice de variance-covariance** et est donnée par l’expression suivante:
> $$\text{Var}(\underline X) =
> \begin{bmatrix}
> \text{Var}(X) & \text{Cov}(X, Y) \\
> \text{Cov}(X, Y) & \text{Var}(Y)
> \end{bmatrix} =
> \begin{bmatrix} \sigma_X^2 & \sigma_{XY} \\
> \sigma_{XY} & \sigma_Y^2
> \end{bmatrix}$$

- Si $X$ et $Y$ sont indépendants, alors:
$$\text{Cov}(X, Y) = \mathbb{E}[X \cdot Y] - \mu_X \cdot \mu_Y = \mathbb{E}[X] \cdot \mathbb{E}[Y] - \mu_X \cdot \mu_Y = 0$$
