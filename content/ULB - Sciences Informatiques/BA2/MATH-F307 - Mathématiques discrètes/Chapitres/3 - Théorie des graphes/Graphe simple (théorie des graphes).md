---
title: Graphe simple (théorie des graphes)
authors: Alessandro Dorigo
tags:
  - Graphe
---


> [!info]+ Définition
> Un graphe **simple** est un graphe non dirigé quelconque $G$ sans arêtes parallèles ni boucles.

> [!abstract]- Lemme 3.2.1
> Dans un graphe simple, le [[Degré#^3c01ed|degré]] maximal d'un sommet est limité par $\vert V \vert - 1$.

> [!abstract]- Théorème 3.2.2
> Si un graphe est [[Graphe complet|complet]], on sait que: $$\vert E \vert = \binom{\vert V \vert}{2}$$
>
> **Partie 1:** $G$ est complet $\implies \vert E \vert = \binom{\vert V \vert}{2}$
>
> Si $G$ est complet, on sait que $d(v_i) = \vert V \vert - 1$.
> - Donc on peut dire que: $$\sum_{v\in V} d(v) = \vert V \vert \cdot (\vert V \vert -1) = 2 \vert E \vert$$
> - D’après le [[Degré#^a3f053|handshaking lemma]]
>
> Mais on cherche $\vert E \vert$: $$\vert E \vert = \frac{\vert V \vert \cdot (\vert V \vert - 1)}{2} = \binom{\vert V \vert}{2}$$
> - Donc si $G$ est complet, alors cela implique $\vert E \vert = \binom{\vert V \vert}{2}$.
>
> **Partie 2:** $\vert E \vert = \binom{\vert V \vert}{2} \implies G$ est complet
>
> On suppose par l'absurde que $G$ n'est pas complet. Cela implique que $\exists v_1 \in V$ dans $G$ qui n'est pas connecté à tous les autres sommets, donc $d(v_1) < \vert V \vert - 1$ ou plus précisément $d(v_1) = \vert V \vert - 2$.
>
> Calculons la somme des degrés de $G$: $$\sum_{v\in V} d(v) = (\vert V\vert - 1) \cdot (\vert V \vert -1) + \vert V \vert - 2 < 2 \vert E \vert$$
> - Si la somme des degrés de $G < 2 \vert E \vert$, on a donc aussi $\vert E \vert < \binom{\vert V \vert}{2}$, donc une contradiction. $\square$
