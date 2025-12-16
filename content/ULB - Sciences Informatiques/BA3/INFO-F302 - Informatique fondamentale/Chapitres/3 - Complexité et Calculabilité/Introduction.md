---
title: Introduction
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **théorie de la complexité** s'intéresse à la classification des problèmes selon leur complexité algorithmique. On étudie particulièrement les problèmes les plus difficiles de chaque classe de complexité.

## Classes de Complexité

> [!abstract]+ Organisation
> De nombreuses classes de complexité ont été introduites. Dans chaque classe, on s'intéresse aux **problèmes complets** :
>
> - Un problème est **complet pour une classe** $C$ si tous les autres problèmes de $C$ peuvent s'y réduire en temps polynomial
> - Cela établit une **borne inférieure** sur leur complexité
> - Pour résoudre un problème complet de $C$, on ne peut pas faire mieux que résoudre n'importe quel problème de $C$ (modulo un polynôme pour la réduction)

## Notion de Codage

> [!example]+ Représentation de Problèmes
> **Exemple** : Coloriage de graphes avec au plus $k$ couleurs
>
> Comment représenter ce problème comme un langage ?
>
> **Objectif** : Représenter l'ensemble $\{(G_1, k_1), (G_2, k_2), ...\}$ de toutes les paires de graphes $G_i$ coloriables avec au plus $k_i$ couleurs
>
> **Codage** : Utiliser un alphabet $\Sigma = \{0, 1, \#, \$\}$
> - Chaque sommet = un entier
> - Chaque arête $(i,j)$ codée par le mot $\overline{i}\#\overline{j}$
> - $\overline{i}, \overline{j}$ : codages binaires des sommets $i, j$

> [!warning]+ Importance du Codage
> **Le codage peut influencer la complexité !**
>
> **Exemple** : Test de primalité
> ```python
> for i in range(2, floor(sqrt(n))):
>     if n % i == 0:
>         return 0
> return 1
> ```
>
> La complexité dépend du codage de $n$ (unaire vs binaire)

## Abstraction vs Pratique

> [!tip]+ Remarque
> Bien que la définition d'un problème comme langage de mots soit abstraite et utile en théorie de la calculabilité et complexité, on peut "oublier" le codage et travailler directement avec des représentations plus concrètes :
>
> - Matrice d'adjacence pour un graphe
> - Liste de voisins
> - Etc.

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème de Décision]]** : Type de problème étudié
> - **[[Classe P]]** : Problèmes résolubles en temps polynomial
> - **[[Classe NP]]** : Problèmes vérifiables en temps polynomial
> - **[[Réduction Polynomiale]]** : Méthode pour comparer les problèmes
