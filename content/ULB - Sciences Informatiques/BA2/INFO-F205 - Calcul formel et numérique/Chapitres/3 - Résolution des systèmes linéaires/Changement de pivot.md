---
title: Changement de pivot
authors: Alessandro Dorigo
tags: []
---

> [!info]+ Définition Changement de pivot partiel et total
> 1. **Changement de pivot partiel** : Si $a_{kk}^{(k)} = 0$, on cherche le plus grand terme (en valeur absolue) non nul dans le vecteur $A(k+1:n, k)$ et on échange les lignes.
> 2. **Changement de pivot total** : Si $a_{kk}^{(k)} = 0$, on cherche le plus grand terme (en valeur absolue) non nul dans la matrice $A(k:n, k:n)$ et on échange les lignes et les colonnes.

> [!tip]+ Remarque
> Le changement de pivot est utilisé même en absence de pivots nuls afin d'améliorer la précision numérique.
