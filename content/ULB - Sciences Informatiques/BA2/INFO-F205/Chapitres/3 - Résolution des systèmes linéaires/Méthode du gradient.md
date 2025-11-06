---
title: Méthode du gradient
authors: Alessandro Dorigo
tags:
  -
---

### Méthode du gradient à pas fixe

La méthode du gradient peut être vue comme une méthode de minimisation de la forme quadratique :

$$\Phi(y) = \frac{1}{2}y^T Ay - y^T b$$

dont le gradient est $\nabla\Phi(y) = Ay - b$.

### Méthode de la plus profonde descente

Utilise la direction du résidu $r^{(k)} = b - Ax^{(k)}$ et calcule un pas optimal :

$$\alpha_k = \frac{(r^{(k)})^T r^{(k)}}{(r^{(k)})^T Ar^{(k)}}$$

$$x^{(k+1)} = x^{(k)} + \alpha_k r^{(k)}$$

### Méthode du gradient conjugué

Utilise des directions de descente $p^{(k)}$ qui sont $A$-conjuguées :

$$p^{(k+1)} = r^{(k+1)} - \beta_k p^{(k)}$$

avec

$$\beta_k = \frac{(Ap^{(k)})^T r^{(k+1)}}{(Ap^{(k)})^T p^{(k)}}$$

et

$$\alpha_k = \frac{(p^{(k)})^T r^{(k)}}{(p^{(k)})^T Ap^{(k)}}$$

> [!abstract]- Théorème "Convergence du gradient conjugué" Soit $A$ une matrice symétrique définie positive d'ordre $n$. La méthode du gradient conjugué conduit à la solution exacte en au plus $n$ itérations.
