---
title: Chemin
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
---


> [!abstract]- Définition
> Un **chemin** est une [[Promenade#^81c9d2|promenade]] dont tous les sommets sont distincts.

^377ffc

>[!note]
>Un chemin de longueur $k$ dans un graphe $G$ est un sous-graphe de la forme:
>$$P = \big(\{v_0,v_1,\dots,v_k\}, \{v_0v_1,v_1v_2,\dots,v_{k-1}v_k\}\big)$$

^dd07e6

> [!abstract]- Lemme 3.7.1
> Soit $G$ un graphe et soient $u,v \in V(G)$ des sommets différents. Si $G$ contient une [[Promenade#^81c9d2|promenade]] de $u$ à $v$, alors $G$ contient un [[Chemin#^377ffc|chemin]] entre $u$ et $v$.
>
> ![[ab3471bb6edfc07b242fb9b3884ff0be.png]]
> ![[c27720308a8fb5579dccc8ec84663cc1.png]]

> [!abstract]- Lemme 3.5.1 - Chemin Hamiltonien
> Un chemin dans un graphe $G$ est dit **hamiltonien** s’il passe par chaque sommet une et une seule fois.

^7e97b9
