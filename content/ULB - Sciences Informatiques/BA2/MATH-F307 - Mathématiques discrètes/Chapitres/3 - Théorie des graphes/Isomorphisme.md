---
title: Isomorphisme
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
---


> [!abstract]- Définition
> Deux graphes $G$ et $H$ sont **isomorphes** (les distances sont préservées) s'il existe une fonction
> $$\beta:V(G)\rightarrow V(H)$$
> telle que
> 1) $\beta$ est une bijection;
> 2) $\forall u,v \in V(G), uv \in E(G) \Leftrightarrow \beta(u)\beta(v) \in E(H)$.

> [!tip]+ Stratégie
> 1. **Degrés des sommets**
> 	- On compte les degrés de chaque sommet des deux graphes.
> 	- Si les deux graphes sont isomorphes, les degrés doivent rester les mêmes.
> 2. **Coloration des sommets**
> 	- Colorier les sommets selon leur degré, en choisissant un sommet qui a le même degré sur les deux graphes.
> 3. **Matrice d'adjacence**
> 	- Représenter les graphes par leurs matrices d'adjacence $A$.
> 	- Si deux graphes sont isomorphes, leurs matrices d'adjacence sont équivalentes à une permutation des lignes et colonnes.
> 4. **Bipartition**
> 	- Pour les graphes [[Graphe planaire#^5fdfb5|planaires]], il est possible d’utiliser une [[Graphe biparti#^bff5b9|bipartition]] (en regardant si $\chi(G) \leq 2$ pour les 2 graphes) et vérifier si les distances entre les sommets sont préservées.

> [!note]
> Pour les petits graphes, on essaie de reconstruire la matrice d'adjacence:
> 1. On part d'un sommet $x$ puis on note ses sommets voisins et leurs degres aussi.
> 2. On répète cette étape sur le second graphe, en cherchant un sommet qui possède les mêmes propriétés (voisins et degrés) que celui choisi dans le premier graphe.
> 3. On continue ce processus jusqu'à avoir examiné tous les sommets de $G$ (et du coup $H$ aussi).
