---
title: Cycle (théorie des graphes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
---


Formellement appris en `MATH-F307`. Pour les cycles vus de manière algorithmique, voir *link*.

> [!info]+ Définition
> Un **cycle** dans un graphe $G$ est un circuit
$$ W = v_0 \ e_1 \ v_1 \ e_2 \ \cdots \ e_{k-1} \ v_{k-1} \ e_k \ v_0$$
dont les sommets $v_0,v_1,\dots,v_{k-1}$ sont différents.

^4c6fe0

> [!note]
> Un cycle de longueur $k$ dans un graphe $G$ est un sous-graphe de la forme:
$$C = \big(\{v_0,v_1,\dots,v_{k-1}\}, \{v_0v_1,v_1v_2,\dots,v_{k-1}v_0\}\big)$$

> [!abstract]- Lemme 3.5.1 - Cycle Hamiltonien
> Un [[Cycle (théorie des graphes)#^4c6fe0|cycle]] dans un graphe $G$ est dit **hamiltonien** si c'est un [[Chemin#^7e97b9|chemin hamiltonien]] qui commence et termine sur le même sommet
> - Un graphe est dit **hamiltonien** s’il admet un cycle hamiltonien.
