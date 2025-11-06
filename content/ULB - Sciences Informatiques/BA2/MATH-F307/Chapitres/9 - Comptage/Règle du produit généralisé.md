---
title: Règle du produit généralisé
authors: Alessandro Dorigo
tags:
  - MathDis
  - Comptage
---


> [!info]+ Énoncé
> Soit $S$ un ensemble de $k$-uplets (choisis dans un ensemble $E$). S’ils existent:
> - $n_1$ choix pour la 1ère composante,
> - $n_2$ choix pour la 2ème composante, en tenant compte du choix de la 1ère,
> - $n_3$ choix pour la 3ème composante, en tenant compte des choix des 1ère et 2ème,
> - $\dots$
> - $n_k$ choix pour la $k$-ème composante, en tenant compte des choix des 1ère, 2ème, ..., et $(k - 1)$-ème,
>
>   alors le nombre total de \( k \)-uplets possibles est donné par:
>   $$\vert S \vert = n_1 \cdot n_2 \cdots n_k$$

> [!example]+ Permutations de $\{1, 2, \dots, n\}$
> Pour un ensemble de $n$ éléments, le nombre de permutations est donné par:
> $$n! = n \cdot (n - 1) \cdot (n - 2) \cdots 2 \cdot 1$$

> [!example]+ Choix d'un comité (leader, secrétaire, consultant) parmi $n$ membres
> - $n$ choix pour le leader,
> - $n - 1$ choix pour le secrétaire, étant donné le choix du leader,
> - $n - 2$ choix pour le consultant, étant donné les choix du leader et du secrétaire.
>
> Donc, le nombre de comités différents possibles est:
> $$n \cdot (n - 1) \cdot (n - 2)$$
