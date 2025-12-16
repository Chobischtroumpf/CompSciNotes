---
title: Autres Classes
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Au-delà de P et NP, il existe de nombreuses autres **classes de complexité** définies par différentes contraintes de ressources (temps, espace, déterminisme).

## Classes Principales

> [!abstract]+ Hiérarchie
> **PSPACE** :
> - Problèmes résolubles en espace polynomial
> - Contient NP
>
> **EXPTIME** :
> - Problèmes résolubles en temps exponentiel
> - Contient PSPACE
>
> **NPSPACE** :
> - Problèmes résolubles par algorithmes non-déterministes en espace polynomial
> - **Théorème de Savitch** : NPSPACE = PSPACE
>
> **NEXPTIME** :
> - Problèmes résolubles par algorithmes non-déterministes en temps exponentiel
>
> **kEXPTIME / kNEXPTIME** :
> - Problèmes résolubles en temps $2^{2^{...^{n}}}$ ($k$ exponentielles)
>
> **Décidable** :
> - Tous les problèmes pour lesquels il existe un algorithme de décision
> - Pas de contrainte de ressources

## Hiérarchie Complète

> [!abstract]+ Inclusions
> $$P \subseteq NP \subseteq PSPACE \subseteq EXPTIME \subseteq NEXPTIME \subseteq 2EXPTIME \subseteq ... \subseteq \text{Décidable}$$
>
> **Inclusions strictes connues** :
> - $P \subsetneq EXPTIME$ (théorème de hiérarchie temporelle)
> - $NP \subsetneq NEXPTIME$
>
> **Inclusions ouvertes** :
> - $P \stackrel{?}{=} NP$
> - $NP \stackrel{?}{=} PSPACE$

## Exemples par Classe

> [!example]+ Problèmes Représentatifs
> **PSPACE-Complet** :
> - **QSAT** : Satisfiabilité de formules quantifiées
>   - Format : $\forall x_1 \exists q_1 \forall x_2 \exists q_2 ... \forall x_n \exists q_n \ \phi$
>   - $\phi$ en FNC sur les variables $x_1, q_1, ..., x_n, q_n$
>   - Peut être résolu en espace polynomial
>   - Tous les problèmes de PSPACE se réduisent à QSAT
>
> **EXPTIME-Complet** :
> - **Jeu d'échecs généralisé** (plateau $n \times n$)
> - **Jeu de Go généralisé**
>
> **Décidable mais pas dans classes inférieures** :
> - **Problème de l'arrêt sur machines restreintes**
> - **Certains problèmes de logique du second ordre**

## Remarques Importantes

> [!tip]+ Observations
> **Séparations connues** :
> - On sait que $P \neq EXPTIME$ (théorème de hiérarchie)
> - Mais on ne sait pas si $P = NP$ !
>
> **Espace vs Temps** :
> - PSPACE capture les problèmes "raisonnables en espace"
> - Mais peut nécessiter un temps exponentiel
>
> **Classes complémentaires** :
> - co-NP : Problèmes dont le complément est dans NP
> - co-NP ≠ NP (présumé, mais non prouvé)

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Classe P]]** : Base de la hiérarchie
> - **[[Classe NP]]** : Classe centrale
> - **[[Problème de Décision]]** : Cadre formel
> - **[[Théorème de Hiérarchie]]** : Sépare certaines classes
