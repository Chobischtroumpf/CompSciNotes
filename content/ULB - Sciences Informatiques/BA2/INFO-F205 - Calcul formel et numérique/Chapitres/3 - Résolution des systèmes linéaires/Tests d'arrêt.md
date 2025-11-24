---
title: Tests d'arrêt
authors: Alessandro Dorigo
tags:
  -
---


> [!info]+ Définition
> 1. **Test sur l'incrément** : $|x^{(k+1)} - x^{(k)}| < \varepsilon$
> 2. **Test sur le résidu** : $|r^{(k)}| = |Ax^{(k)} - b| < \varepsilon$
>
> Pour le test sur l'incrément, on peut montrer que l'erreur est dans ce cas bornée par :
> $$|e^{(k+1)}| \leq \frac{\gamma}{1-\gamma}\varepsilon$$
> où $\gamma = |B|$.
>
> Et pour le test sur le résidu :
> $$|e^{(k)}| \leq \kappa(A)\frac{|\varepsilon|}{|A|}$$
> où $\kappa(A)$ est le conditionnement de $A$.
