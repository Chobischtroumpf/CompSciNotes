---
title: Problème 2-partition
authors: Alessandro Dorigo
tags:
  - InfoFond
  - Algo
---


> [!info]+ Définition
> Le **problème 2-partition** est un problème de décision défini comme suit:
>
> **INPUT**: $m$ entiers naturels $c_1, \dots, c_m$ tels que $S := \sum_{i=1}^m c_i$ est paire
> **OUTPUT**: "oui" si et seulement si il existe $J \subseteq \{ 1, \dots, m \}$ tel que $\sum_{i \in J} c_i = \sum_{i \notin J} c_i$

^264e40

- Cela revient à déterminer s'il est possible de partitionner un ensemble d'entiers en deux sous-ensembles ayant la même somme (égale à $S/2$).

> [!example]+ Exemple
> Soit l'ensemble $\{ 1, 4, 2, 3, 2 \}$:
> - Somme totale $S = 12$
> - Partition possible: $\{ 1, 2, 3 \}$ et $\{ 4, 2 \}$
> - Vérification: $1 + 2 + 3 = 6$ et $4 + 2 = 6$

> [!abstract]- Propriétés du problème
>
> - **Classe de complexité** : NP-complet
> - **Problème de décision** : Réponse oui/non uniquement
> - **Applications** : Équilibrage de charges, partitionnement équitable

> [!abstract]- Réduction vers [[Problème Bin Packing#^a7a3c5|Bin Packing]]
> Le problème 2-partition se réduit vers [[Problème Bin Packing#^a7a3c5|Bin Packing]]:
>
> **Transformation**:
> - Capacité des sacs: $C = S/2$
> - Nombre de sacs: $k = 2$
> - Objets: $1, \dots, m$ de poids $c_1, \dots, c_m$
>
> **Équivalence**: Il existe une 2-partition $\Leftrightarrow$ on peut ranger tous les objets dans 2 sacs de capacité $S/2$

- Ce problème est souvent utilisé comme point de départ pour prouver la NP-complétude d'autres problèmes par [[Réductions entre problèmes#^0954bf|réduction]].
