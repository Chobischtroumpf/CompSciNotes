---
title: Matrice de covariance
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!abstract]- Formule générale
> $$\Sigma_X = \mathbb{E}[(X-\mu_X)(X-\mu_X)^\top]$$

> [!abstract]- Forme matricielle
> $$\Sigma_X = \begin{pmatrix}
> \text{Var}(X_1) & \text{Cov}(X_1,X_2) & \cdots & \text{Cov}(X_1,X_n) \\
> \text{Cov}(X_2,X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2,X_n) \\
> \vdots & \vdots & \ddots & \vdots \\
> \vdots & \vdots & \cdots & \vdots \\
> \text{Cov}(X_n,X_1) & \text{Cov}(X_n,X_2) & \cdots & \text{Var}(X_n)
> \end{pmatrix}$$

- Cette matrice est symétrique, ce qui signifie que $\text{Cov}(X_i,X_j) = \text{Cov}(X_j,X_i)$ pour tout $i \neq j$.
