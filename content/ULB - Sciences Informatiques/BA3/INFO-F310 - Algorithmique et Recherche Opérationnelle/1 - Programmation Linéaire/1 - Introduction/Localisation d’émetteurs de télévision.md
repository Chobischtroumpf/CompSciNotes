---
title: Localisation d’émetteurs de télévision
authors: Alessandro Dorigo
tags:
  - Algo
  - Maths
---


> [!info]+ Énoncé
> Cinq sites on étés retenus pour construire des émetteurs de télévision destines a desservir 10 localités. Le tableau ci-dessous donne, pour chaque site, le coût de construction d'un émetteur sur ce site et les localités desservies par cet émetteur:
>
> ![[d186d4685bb87525c0d3c5ff3416cef0.png]]
>
> Comment couvrir toutes les localités avec le nombre minimum d’émetteurs?

## Solutions
Modélisation au moyen du problème de couverture par sous-ensembles
- L'installation d'un émetteur sur le site $i$ permet de couvrir un sous-ensemble $L_i$ de l'ensemble des localités $\{ 1, 2, \dots, 10 \}$
- Par exemple, l'installation de l’émetteur sur le site 2 (5) permet de couvrir les localités $\{ 2, 4 \}$ ($\{ 3, 5, 6, 7, 9 \}$)

L'objectif est de couvrir toutes les localités avec le nombre minimum d’émetteurs
- Chaque site $i$ a un coût de construction pour l’émetteur $\alpha_i$
- On doit minimiser la somme du coût de construction (et donc de localisation) des émetteurs afin d'assurer la couverture de toutes les localités par ces émetteurs

> [!tip] Modèle
> - [[Paramètre#^dda459|Paramètres]] (fixes): $\alpha_i$ $(i = 1, \dots, 5)$ coût de construction de l'émetteur pour chaque site $i = 1, \dots, 5$
> - [[Variable#^ca18e2|Variables]] booléennes: $x_i$ $(i = 1, \dots, 5) = 1$ si le site $i$ est choisi pour la construction d'un émetteur et $x_i = 0$ autrement
> - [[Fonction objectif]] (à minimiser):
> $$\sum_{i=1}^{5} \alpha_i x_i \equiv \alpha_1 x_1 + \alpha_2 x_2 + \alpha_3 x_3 + \alpha_4 x_4 + \alpha_5 x_5$$
> - [[Contrainte#^77d260|Contraintes]] de couverture: toute localité $j$ doit être couverte au moins une fois par un site émetteur
> $$\sum_{i \in \{1,\ldots,5\}: j \in L_i} x_i \geq 1, \quad \forall j \in \{1, \ldots, 10\}$$
