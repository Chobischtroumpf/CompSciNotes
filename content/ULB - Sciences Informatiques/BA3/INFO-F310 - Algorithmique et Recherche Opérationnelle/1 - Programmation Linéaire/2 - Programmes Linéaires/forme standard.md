---
title: forme standard
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---
## Forme Standard

> [!info]+ Définition
>
> Un problème d'optimisation linéaire à $n$ variables ($x \in \mathbb{R}^n$) sujet à $m$ contraintes ($b \in \mathbb{R}^m$) et $A \in \mathbb{R}^{m \times n}$ peut être exprimé sous **forme standard**.
>
> **Représentation matricielle :**
>
> $$
> \begin{align} &\text{maximize (or minimize)} \quad c^T x \\ &\text{subject to} \quad x \geq 0, \quad Ax = b \end{align}
> $$
>
> **Représentation indicielle :**
>
> $$ \begin{align} &\text{maximize (or minimize)} \quad \sum_{j=1}^n c_j x_j \\ &\text{subject to} \quad \sum_{j=1}^n a_{ij} x_j = b_i, \quad \forall i \in {1, \ldots, m} \ &x_j \geq 0, \quad \forall j \in {1, \ldots, n} \end{align} $$
