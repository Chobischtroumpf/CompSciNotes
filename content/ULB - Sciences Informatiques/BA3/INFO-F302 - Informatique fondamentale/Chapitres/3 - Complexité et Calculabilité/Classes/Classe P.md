---
title: Classe P
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La classe **P** est la classe des problèmes de décision qui peuvent être résolus par un algorithme en temps polynomial.

## Définition Formelle

> [!abstract]+ Caractérisation
> Un problème $P \subseteq \Sigma^*$ est dans la classe P si et seulement si :
>
> Il existe un algorithme $A$ et une constante $k$ tels que :
> - Pour tout mot $u$ de longueur $n$
> - $A$ retourne 1 en temps $O(n^k)$ si et seulement si $u \in P$
> - $A$ retourne 0 en temps $O(n^k)$ si et seulement si $u \notin P$

## Interprétation

> [!tip]+ Problèmes "Faciles"
> La classe P représente les problèmes considérés comme **résolubles efficacement** en pratique :
>
> - Temps polynomial = "raisonnable"
> - Contraste avec temps exponentiel = "impraticable"
>
> **Note** : Cette distinction est une simplification (un $O(n^{1000})$ n'est pas vraiment "efficace")

## Exemples de Problèmes dans P

> [!example]+ Problèmes Classiques
> **Tri** :
> - **Problème** : Un tableau est-il trié ?
> - **Complexité** : $O(n)$
> - **Algorithme** : Parcours simple
>
> **Plus Court Chemin** :
> - **Problème** : Trouver le plus court chemin dans un graphe
> - **Complexité** : $O(|E| + |V| \log |V|)$ (Dijkstra)
> - **Dans P** : Polynomial en la taille de l'entrée
>
> **Primalité (codage binaire)** :
> - **Problème** : Un entier $n$ (codé en binaire) est-il premier ?
> - **Complexité** : Polynomial (AKS, 2002)
> - **Note** : Ce résultat a résolu une question ouverte de longue date
>
> **Primalité (codage unaire)** :
> - **Problème** : Un entier $n$ (codé en unaire) est-il premier ?
> - **Complexité** : $O(\sqrt{n})$ (test naïf)
> - **Dans P** : Polynomial en la taille de l'entrée ($n$ symboles)
>
> **Matching Maximum** :
> - **Problème** : Trouver un couplage maximum dans un graphe
> - **Complexité** : $O(|V|^3)$ (Edmonds)

## Stabilité par Composition

> [!abstract]+ Propriétés de Clôture
> La classe P est stable par :
>
> **Composition** :
> - Si $f$ et $g$ sont calculables en temps polynomial
> - Alors $f \circ g$ est calculable en temps polynomial
> - Car $O(n^a) \circ O(n^b) = O(n^{ab})$
>
> **Union et Intersection** :
> - Si $P_1, P_2 \in$ P
> - Alors $P_1 \cup P_2 \in$ P et $P_1 \cap P_2 \in$ P
>
> **Complément** :
> - Si $P \in$ P alors $\overline{P} \in$ P

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Classe NP]]** : Surensemble présumé de P
> - **[[Algorithme de Décision]]** : Définit l'appartenance à P
> - **[[Conjecture P ≠ NP]]** : Question fondamentale
> - **[[Réduction Polynomiale]]** : Préserve l'appartenance à P
