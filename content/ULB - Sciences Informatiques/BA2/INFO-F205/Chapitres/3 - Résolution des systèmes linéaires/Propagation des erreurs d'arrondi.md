---
title: Propagation des erreurs d'arrondi
authors: Alessandro Dorigo
tags:
  -
---

Deux types d'erreurs peuvent affecter la stabilité :

- **Erreurs de propagation** : erreurs initiales qui se propagent à travers les calculs
- **Erreurs de génération** : nouvelles erreurs introduites à chaque étape du calcul

Un multiplicateur obtenu avec un pivot très petit peut amplifier ces erreurs même si la valeur calculée est mathématiquement correcte.
