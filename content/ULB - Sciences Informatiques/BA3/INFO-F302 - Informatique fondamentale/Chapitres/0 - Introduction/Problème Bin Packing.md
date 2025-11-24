---
title: Problème Bin Packing
authors: Alessandro Dorigo
tags:
  - InfoFond
  - Algo
---


> [!info]+ Définition
> Le **problème Bin Packing** est un problème de décision défini comme suit:
>
> **INPUT**: $n$ objets de poids $p_1, \dots, p_n$, $k$ sacs de capacité $C$
> **OUTPUT**: "oui" si et seulement si on peut ranger tous les objets dans au plus $k$ sacs sans dépasser la capacité de chaque sac

^a7a3c5

> [!example]+ Exemple
> Ranger les objets suivants dans des sacs de capacité 10kg:
>
> |Objets|1|2|3|4|5|6|7|
> |---|---|---|---|---|---|---|---|
> |Poids|3|4|4|3|3|2|1|
>
> **Question**: Peut-on réussir avec 3 sacs?
> Oui $\rightarrow \{ 1,2 \}, \{ 3,4,5 \}, \{ 6,7 \}$
>
> **Question**: Et avec 2 sacs?
> Oui $\rightarrow \{ 1,2,4 \}, \{ 3,5,6,7 \}$ (solution optimale)

> [!abstract]- Propriétés du problème
> - **Classe de complexité**: NP-complet
> - **Applications pratiques**: Optimisation logistique, allocation de ressources
> - **Variantes**: First Fit, Best Fit, etc. (heuristiques d'approximation)

- Le problème Bin Packing est souvent utilisé comme cible dans les [[Réductions entre problèmes#^0954bf|réductions]] pour prouver la NP-complétude d'autres problèmes.
