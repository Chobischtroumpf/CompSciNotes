---
title: Problème Bin Packing
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
  - Algo
---
> [!info]+ Définition
> Le **problème Bin Packing** est un problème de décision défini comme suit :
>
> **Entrée** : $n$ objets de poids $p_1, \dots, p_n$, $k$ sacs de capacité $C$
>
> **Sortie** : "oui" si et seulement si on peut ranger tous les objets dans au plus $k$ sacs sans dépasser la capacité de chaque sac

## Exemple

> [!example]+ Cas Concret
> Ranger les objets suivants dans des sacs de capacité 10 kg :
>
> | Objets | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> |--------|---|---|---|---|---|---|---|
> | Poids  | 3 | 4 | 4 | 3 | 3 | 2 | 1 |
>
> **Question** : Peut-on réussir avec 3 sacs ?
> - Oui → $\{1,2\}, \{3,4,5\}, \{6,7\}$
>
> **Question** : Et avec 2 sacs ?
> - Oui → $\{1,2,4\}, \{3,5,6,7\}$ (solution optimale)

## Propriétés

> [!note]+ Caractéristiques
> - **Classe de complexité** : NP-complet
> - **Applications pratiques** : Optimisation logistique, allocation de ressources
> - **Variantes** : First Fit, Best Fit, etc. (heuristiques d'approximation)

## Relation avec 2-Partition

> [!abstract]+ Réduction depuis 2-Partition
> Le [[Problème 2-partition]] se réduit vers Bin Packing :
>
> - Capacité : $C = S/2$ (où S est la somme des poids)
> - Nombre de sacs : $k = 2$
>
> Cette réduction montre que Bin Packing est au moins aussi difficile que 2-Partition.

## Utilisation en Théorie

> [!note]+ Applications
> Le problème Bin Packing est souvent utilisé comme cible dans les [[Réductions entre Problèmes|réductions]] pour prouver la NP-complétude d'autres problèmes.

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème 2-partition]]** : Cas particulier se réduisant à Bin Packing
> - **[[Réductions entre Problèmes]]** : Méthode pour relier les problèmes
> - **[[Classe NP]]** : Classe de complexité contenant ce problème
