---
title: Problème Complet
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Dans une classe de complexité donnée, certains problèmes sont **complets** pour la classe, c'est-à-dire qu'ils sont aussi difficiles que tous les autres problèmes de la classe.

## Propriété Fondamentale

> [!abstract]+ Caractérisation
> Un problème P est complet pour une classe C si :
>
> 1. **Appartenance** : P ∈ C
> 2. **Dureté** : Tout problème de C se réduit à P en temps polynomial

## Importance

> [!note]+ Utilité des Problèmes Complets
> Les problèmes complets permettent de :
>
> - Identifier les problèmes les plus difficiles d'une classe
> - Établir des bornes inférieures sur la complexité
> - Comparer la difficulté de différents problèmes

## Exemples

> [!example]+ Problèmes Complets Notables
> - **SAT** : Complet pour NP
> - **3-SAT** : Complet pour NP
> - **Coloriage de graphes** : Complet pour NP
> - **Voyageur de commerce** : Complet pour NP

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Théorie de la Complexité]]** : Cadre théorique
> - **[[Réductions entre Problèmes]]** : Méthode pour démontrer la complétude
> - **[[Classe P]]** : Classe des problèmes "faciles"
> - **[[Classe NP]]** : Classe contenant SAT
