---
title: Factorisation de Cholesky
authors: Alessandro Dorigo
tags:
  -
---


> [!abstract]- Factorisation de Cholesky
> Soit $A \in \mathbb{R}^{n \times n}$ une matrice symétrique définie positive. Alors il existe une unique matrice triangulaire supérieure $H$ dont les termes diagonaux sont positifs telle que
>
> $$A = H^T H$$

> [!tip]+ Remarque
> Une matrice symétrique $A$ est dite définie positive si $x^T Ax > 0$ pour tout vecteur $x$.

> [!abstract]- Formules de Cholesky :
> $$\begin{aligned}
> &\text{Pour } i = 1 \text{ à } n : \\
> &\quad\quad h_{ii} = \sqrt{a_{ii} - \sum_{k=1}^{i-1} h_{ki}^2} \\
> &\quad\quad \text{Pour } j = i+1 \text{ à } n : \\
> &\quad\quad\quad\quad h_{ij} = \frac{a_{ij} - \sum_{k=1}^{i-1} h_{ki}h_{kj}}{h_{ii}}
> \end{aligned} $$

> [!tip]+ Remarque
> La factorisation de Cholesky a une complexité de $\mathcal{O}(n^3/3)$, comparée à $\mathcal{O}(2n^3/3)$ pour la factorisation LU standard.
