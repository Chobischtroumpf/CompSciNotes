---
title: Choix des algorithmes
authors: Alessandro Dorigo
tags:
  -
---

Différentes méthodes présentent différentes caractéristiques de stabilité :

- **Élimination de Gauss sans pivotage** : peut être instable si les pivots sont petits
- **Élimination de Gauss avec pivotage partiel** : améliore considérablement la stabilité
- **Élimination de Gauss avec pivotage total** : offre la meilleure stabilité mais est plus coûteuse
- **Factorisation de Cholesky** : stable pour les matrices symétriques définies positives
