---
title: Vraisemblance
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition (discret)
> La **vraisemblance** _(likelihood)_ est définie comme la [[Fonction de masse jointe multivariée (discrète)#^9fa2f4|probabilité jointe]] $L_\theta(\mathbf{X})$ du vecteur aléatoire $\mathbf{X} = (X_1, \dots, X_n)$, évaluée pour les observations données $(X_1, \dots, X_n)$.
>
> Si chaque $X_i$ suit une loi discrète de probabilité $p_\theta$, la vraisemblance s’écrit:
>
> $$L_\theta(\mathbf{X}) = L_\theta(X_1, \dots, X_n) = \prod_{i=1}^n p_\theta(X_i)$$

^121cc0

> [!info]+ Définition (continu)
> La **vraisemblance** _(likelihood)_ est définie comme la [[Fonction de densité jointe multivariée (continue)#^3366ee|densité jointe]] $L_\theta(\mathbf{X})$ du vecteur aléatoire $\mathbf{X} = (X_1, \dots, X_n)$, évaluée pour les observations données $(X_1, \dots, X_n)$.
>
> Si chaque $X_i$ suit une [[Fonctions de probabilités#Fonction de densité (Probability Density Function - PDF)|densité]] de probabilité $f_\theta$, alors la vraisemblance s’écrit:
>
> $$L_\theta(\mathbf{X}) = L_\theta(X_1, \dots, X_n) = \prod_{i=1}^n f_\theta(X_i)$$

> [!tip]+ Conditions de régularité
> 1. La vraisemblance $L_\theta(x)$ est **positive** et **dérivable** par rapport à $\theta$
> 2. La vraisemblance est **normalisée**: $\int L_\theta(x) \ dx = 1$
> 3. La **variance** de la dérivée du logarithme de la vraisemblance est **finie**: $\text{Var}_\theta\left(\frac{\partial}{\partial \theta} \log L_\theta(x)\right) < \infty$

^2d4e46
