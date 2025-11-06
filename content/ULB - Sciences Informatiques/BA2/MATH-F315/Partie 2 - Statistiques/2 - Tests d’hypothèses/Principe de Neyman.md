---
title: Principe de Neyman
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> Le **principe de Neyman** est une méthode pour construire un test statistique en deux étapes:
>
> 1. **Contrainte de niveau**:
> 	- Se restreindre aux tests $\phi$ de **niveau $\alpha$**, c’est-à-dire aux tests satisfaisant la condition:
>   $$\mathbb{E}_\theta[\phi] \leq \alpha, \quad \forall \theta \in H_0$$
>   où $\alpha$ est une probabilité fixée à l’avance (appelée **niveau de significativité**).
>
> 2. **Optimisation de la puissance**:
> 	- Parmi les tests de niveau $\alpha$, choisir celui qui **maximise la puissance** uniformément sur $\theta \in H_1$. Cela revient à trouver le test le plus efficace pour détecter une fausse hypothèse nulle.
