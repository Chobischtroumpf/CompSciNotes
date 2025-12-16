---
title: Problème d'Optimisation
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Un **problème d'optimisation** est un problème où l'on cherche à maximiser ou minimiser une certaine quantité.

## Lien avec les Problèmes de Décision

> [!abstract]+ Association
> À tout problème d'optimisation peut être associé un **problème de décision** en donnant une borne :
>
> **Exemple** : Voyageur de Commerce
> - **Version optimisation** : Trouver le cycle le plus court visitant toutes les villes
> - **Version décision** : Existe-t-il un cycle de longueur $\leq k$ visitant toutes les villes ?

## Résolution

> [!tip]+ De la Décision à l'Optimisation
> Si on peut résoudre le problème de décision associé, on peut résoudre le problème d'optimisation :
>
> **Méthode par dichotomie** :
> 1. Tester différentes valeurs de la borne
> 2. Affiner par recherche binaire
> 3. Trouver la valeur optimale
>
> **Complexité** : Ajoute un facteur logarithmique

## Exemples

> [!example]+ Problèmes Classiques
> **Bin Packing** :
> - **Optimisation** : Ranger $n$ objets dans le minimum de sacs
> - **Décision** : Peut-on ranger $n$ objets dans $k$ sacs ?
>
> **Coloriage de Graphes** :
> - **Optimisation** : Trouver le nombre chromatique (minimum de couleurs)
> - **Décision** : Le graphe est-il coloriable avec $k$ couleurs ?
>
> **Plus Court Chemin** :
> - **Optimisation** : Trouver le plus court chemin entre deux sommets
> - **Décision** : Existe-t-il un chemin de longueur $\leq k$ ?

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème de Décision]]** : Version décisionnelle associée
> - **[[Classe NP]]** : Contient les versions décision de nombreux problèmes d'optimisation
> - **[[Réduction Polynomiale]]** : Transformation entre problèmes
