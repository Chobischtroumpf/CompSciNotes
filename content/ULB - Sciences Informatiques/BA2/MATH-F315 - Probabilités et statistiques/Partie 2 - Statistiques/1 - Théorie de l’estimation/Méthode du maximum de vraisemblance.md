---
title: Méthode du maximum de vraisemblance
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> Un **estimateur du maximum de [[Vraisemblance#^121cc0|vraisemblance]]** de $\theta$ est une valeur $\hat{\theta}$ qui **maximise la [[Vraisemblance#^121cc0|vraisemblance]]** $L_\theta(\mathbf{X})$, donnée par:
>
> $$\text{Argmax}_\theta L_\theta(\mathbf{X})$$
>
> ou, de manière équivalente, en utilisant le **logarithme de la [[Vraisemblance#^121cc0|vraisemblance]]**:
>
> $$\hat{\theta} = \text{Argmax}_\theta \log L_\theta(\mathbf{X})$$

> [!info]+ Cas continu
> Dans le cas continu (le raisonnement pour le cas discret est similaire):
> 1. Soit $\mathbf{X} = (X_1, \dots, X_n)$, où les $X_i$ sont i.i.d. de densité $f_\theta(x)$.
> 2. La [[Vraisemblance#^121cc0|vraisemblance]] associée est donnée par:
>    $$L_\theta(\mathbf{X}) = \prod_{i=1}^n f_\theta(X_i)$$
> 3. En maximisant le logarithme de la [[Vraisemblance#^121cc0|vraisemblance]], on obtient:
>    $$\hat{\theta} = \text{Argmax}_\theta \log L_\theta(\mathbf{X}) = \text{Argmax}_\theta \sum_{i=1}^n \log f_\theta(X_i)$$

> [!abstract]- Équations de vraisemblance
> Si $\theta \mapsto f_\theta(x)$ est différentiable et si $\Theta$ est un espace paramétrique ouvert, les solutions du système:
>
> $$\sum_{i=1}^n \frac{\partial}{\partial \theta} \log f_\theta(X_i) = 0$$
> fournissent les [[Estimateur#^56cd5c|estimateurs]] $\hat{\theta}$. Ce système est appelé les **équations de [[Vraisemblance#^121cc0|vraisemblance]]**.

> [!example]+ Exemples
> ![[bc4db15c0d3b8c86b825bf26b2636427.png]]
> ![[fd6ae3d84efdfde215d821ecb61e8f7d.png]]
> ![[e04f705733692764880b0c22ded1e634.png]]
> ![[09f86c58914966872907fada591c79fe.png]]
