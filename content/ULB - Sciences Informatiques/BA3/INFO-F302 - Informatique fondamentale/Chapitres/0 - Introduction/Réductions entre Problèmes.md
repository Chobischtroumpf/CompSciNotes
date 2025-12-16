---
title: Réductions entre Problèmes
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Une **réduction** d'un problème A vers un problème B est une méthode permettant d'encoder toute entrée du problème A comme une entrée du problème B, de sorte qu'une solution existe pour l'entrée de A si et seulement si une solution existe pour l'entrée correspondante de B.

## Principe

> [!abstract]+ Fonctionnement
> Réduire un problème A vers un problème B, c'est trouver une fonction f telle que :
>
> - f transforme toute entrée $I_A$ du problème A en une entrée $I_B = f(I_A)$ du problème B
> - $I_A$ a une solution $\Leftrightarrow I_B$ a une solution
>
> **Notation** : $A \leq B$ ("A se réduit à B")

## Types de Réductions

> [!note]+ Pour Problèmes de Décision
> Réduire un problème A vers un problème B signifie encoder toute entrée $I_A$ comme une entrée $I_B$ telle que la réponse est "oui" pour $I_A$ si et seulement si la réponse est "oui" pour $I_B$.

> [!note]+ Pour Problèmes Généraux
> Pour les problèmes qui ne sont pas de décision :
>
> - Toute solution de $I_A$ s'encode en une solution de $I_B$
> - Réciproquement, toute solution de $I_B$ se décode en une solution de $I_A$

## Propriétés

> [!abstract]+ Implications
> Si $A \leq B$, alors :
>
> 1. **Résolution** : Un algorithme pour B donne un algorithme pour A
> 2. **Complexité** : Si B est "facile", alors A est "facile"
> 3. **Indécidabilité** : Si A est indécidable, alors B est indécidable
> 4. **Transitivité** : Si $A \leq B$ et $B \leq C$, alors $A \leq C$

## Exemple

> [!example]+ 2-Partition vers Bin Packing
> **[[Problème 2-partition]]** $\leq$ **[[Problème Bin Packing]]**
>
> **Réduction** :
> - Prendre $C = S/2$ (où S est la somme totale)
> - Prendre $k = 2$ sacs
>
> **Équivalence** :
> - Il existe une 2-partition $\Leftrightarrow$ on peut ranger tous les objets dans 2 sacs

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème Complet]]** : Utilise les réductions pour sa définition
> - **[[Théorie de la Complexité]]** : Cadre d'utilisation des réductions
> - **[[Problème 2-partition]]** : Exemple de source de réduction
> - **[[Problème Bin Packing]]** : Exemple de cible de réduction
