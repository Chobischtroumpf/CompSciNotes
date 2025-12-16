---
title: Algorithme de Décision
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Un **algorithme de décision** pour un problème $P$ est un algorithme qui termine sur toute entrée et retourne 1 si l'entrée appartient à $P$, 0 sinon.

## Formalisation

> [!abstract]+ Définition Formelle
> Un problème $P \subseteq \Sigma^*$ est **décidé** par un algorithme $A$ si :
>
> Pour tout mot $u \in \Sigma^*$ :
> - $A$ termine et retourne 1 $\Leftrightarrow u \in P$
> - $A$ termine et retourne 0 $\Leftrightarrow u \notin P$

## Décidabilité

> [!abstract]+ Problème Décidable
> Un problème est **décidable** s'il existe un algorithme qui le décide.
>
> **Caractéristiques** :
> - L'algorithme doit toujours terminer
> - L'algorithme doit donner la bonne réponse
> - Pas de contrainte sur le temps d'exécution

## Relation avec la Complexité

> [!tip]+ Hiérarchie
> **Problèmes décidables** :
> - Incluent tous les problèmes de la classe P
> - Incluent tous les problèmes de la classe NP
> - Incluent des problèmes de complexité arbitrairement élevée
>
> **Problèmes indécidables** :
> - Aucun algorithme ne peut les résoudre
> - Exemples : Problème de l'arrêt, PCP

## Exemples

> [!example]+ Algorithmes de Décision
> **Test de Primalité** :
> ```python
> def est_premier(n):
>     if n < 2:
>         return 0
>     for i in range(2, int(sqrt(n)) + 1):
>         if n % i == 0:
>             return 0
>     return 1
> ```
> - Termine toujours
> - Décide si $n$ est premier
>
> **SAT (Satisfiabilité)** :
> - Algorithme exhaustif testant toutes les interprétations
> - Termine toujours (en temps exponentiel)
> - Décide si une formule est satisfaisable
>
> **Tri** :
> ```python
> def est_trie(L):
>     for i in range(len(L) - 1):
>         if L[i] > L[i+1]:
>             return 0
>     return 1
> ```
> - Termine toujours en temps linéaire
> - Décide si une liste est triée

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème de Décision]]** : Type de problème résolu
> - **[[Problème Indécidable]]** : Problèmes sans algorithme de décision
> - **[[Algorithme de Vérification]]** : Variante pour la classe NP
> - **[[Classe P]]** : Algorithmes de décision en temps polynomial
