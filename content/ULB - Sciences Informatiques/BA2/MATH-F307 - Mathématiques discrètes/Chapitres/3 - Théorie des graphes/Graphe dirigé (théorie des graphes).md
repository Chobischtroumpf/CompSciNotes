---
title: Graphe dirigé (théorie des graphes)
authors: Alessandro Dorigo
tags:
  - Graphe
---


> [!info]+ Définition
> Un **graphe dirigé** (fini et sans arcs parallèles) est une paire $D=(V,A)$ telle que:
> 1) $V$ est un ensemble fini de sommets,
> 2) $A$ est un ensemble de couples (ordonnés) de sommets, appelés **arcs** ($A \subseteq V \times V$).

^29385c

> [!abstract]- Théorème 3.8.1
> Avec $A =$ matrice d'adjacence du graphe dirigé, on a $\forall t \in \mathbb{N}_0$ et $\forall i,j = 1,\dots,n$:
> $$(A^t)_{i,j} = \#\{\text{promenades dirigées de }v_1 \text{ à } v_j \text{ de longueur }t \}$$
>
> ![[68a4b6fcbef7d69678a59691fd7dee20.png]]
> ![[d48d3c917b49ff64481cb66f684c9d42.png]]
