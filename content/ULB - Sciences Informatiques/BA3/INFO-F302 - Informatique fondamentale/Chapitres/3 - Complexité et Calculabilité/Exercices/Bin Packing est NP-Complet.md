---
title: Bin Packing est NP-Complet
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Objectif
> Démontrer que le **problème Bin Packing** est NP-complet en le réduisant depuis le problème 2-Partition.

## Rappel du Problème

> [!abstract]+ Bin Packing
> **Entrée** :
> - $n$ objets de poids $p_1, ..., p_n$
> - $k$ sacs de capacité $C$
>
> **Question** : Peut-on ranger tous les objets dans au plus $k$ sacs sans dépasser la capacité de chaque sac ?

## Exemple

> [!example]+ Instance Concrète
> | Objets | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
> |--------|---|---|---|---|---|---|---|
> | Poids  | 3 | 4 | 4 | 3 | 3 | 2 | 1 |
>
> **Sacs de 10 kg** :
> - 3 sacs : $\{1, 2\}$, $\{3, 4, 5\}$, $\{6, 7\}$ ✓
> - 2 sacs : $\{1, 2, 4\}$, $\{3, 5, 6, 7\}$ ✓ (optimal)

## Preuve de NP-Complétude

> [!abstract]+ Étape 1 : Bin Packing ∈ NP
> **Certificat** : Une assignation de chaque objet à un numéro de sac entre 1 et $k$
>
> **Algorithme de vérification** (temps polynomial) :
> 1. Pour chaque sac $i$ de 1 à $k$ :
>    - Calculer la somme des poids des objets assignés au sac $i$
>    - Vérifier que cette somme $\leq C$
> 2. Retourner 1 si toutes les contraintes sont satisfaites, 0 sinon
>
> **Complexité** : $O(n)$ (parcours de tous les objets)

> [!abstract]+ Étape 2 : Bin Packing est NP-Dur
> **Stratégie** : Réduction en temps polynomial depuis **2-Partition** (problème NP-complet)

## Rappel : Problème 2-Partition

> [!abstract]+ Définition
> **Entrée** : $n$ entiers $c_1, ..., c_n$ tels que $S = \sum_{i=1}^n c_i$ est paire
>
> **Question** : Existe-t-il $J \subseteq \{1, ..., n\}$ tel que :
> $$\sum_{i \in J} c_i = \sum_{i \notin J} c_i = \frac{S}{2}$$

## Construction de la Réduction

> [!abstract]+ Transformation
> **Fonction de réduction** $f$ : 2-Partition $\to$ Bin Packing
>
> Entrée de 2-Partition : $(c_1, ..., c_n, S)$
>
> **Construction** :
> - Objets : $n$ objets de poids $c_1, ..., c_n$
> - Nombre de sacs : $k = 2$
> - Capacité : $C = S/2$
>
> Sortie de Bin Packing : $(p_1 = c_1, ..., p_n = c_n, k = 2, C = S/2)$

## Preuve de Correction

> [!abstract]+ Équivalence des Solutions
> **Théorème** : Il existe une solution à l'instance de 2-Partition si et seulement si il existe une solution à l'instance de Bin Packing ainsi construite.
>
> **Preuve ($\Rightarrow$)** :
> - Supposons qu'il existe une 2-partition $J$ telle que $\sum_{i \in J} c_i = S/2$
> - **Construction du rangement** :
>   - Ranger tous les objets $i \in J$ dans le sac 1
>   - Ranger tous les objets $i \notin J$ dans le sac 2
> - **Vérification** :
>   - Sac 1 : $\sum_{i \in J} p_i = \sum_{i \in J} c_i = S/2 = C$ ✓
>   - Sac 2 : $\sum_{i \notin J} p_i = \sum_{i \notin J} c_i = S/2 = C$ ✓
> - Donc on peut ranger tous les objets dans 2 sacs ✓
>
> **Preuve ($\Leftarrow$)** :
> - Supposons qu'on peut ranger tous les objets dans 2 sacs
> - Soit $A$ l'ensemble des objets dans le sac 1
> - **Contraintes** :
>   - $\sum_{i \in A} p_i \leq C = S/2$
>   - $\sum_{i \notin A} p_i \leq C = S/2$
>   - $\sum_{i \in A} p_i + \sum_{i \notin A} p_i = S$ (tous les objets)
> - **Conclusion** :
>   - Les deux inégalités + l'égalité impliquent :
>   - $\sum_{i \in A} p_i = S/2$ et $\sum_{i \notin A} p_i = S/2$
> - Donc $A$ forme une 2-partition ✓

## Complexité de la Réduction

> [!tip]+ Temps Polynomial
> **Construction de l'instance** :
> 1. Calculer $S = \sum c_i$ : $O(n)$
> 2. Créer les objets : $O(n)$
> 3. Définir $k = 2$ et $C = S/2$ : $O(1)$
>
> **Complexité totale** : $O(n)$ ✓ (polynomial)

## Conclusion

> [!success]+ Résultat
> **Bin Packing est NP-complet** car :
> 1. Bin Packing $\in$ NP (certificat vérifiable en temps polynomial)
> 2. Bin Packing est NP-dur (réduction depuis 2-Partition)
>
> **Conséquence** : Sauf si P = NP, il n'existe pas d'algorithme polynomial pour Bin Packing.

## Remarques

> [!tip]+ Observations
> **Généralisation** :
> - Cette preuve montre que Bin Packing est difficile même pour $k = 2$ sacs
> - Le problème reste NP-complet pour tout $k$ fixé $\geq 2$
>
> **Approches pratiques** :
> - Algorithmes d'approximation (First Fit, Best Fit)
> - Heuristiques
> - Programmation linéaire en nombres entiers

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème de Décision#2-Partition]]** : Problème source de la réduction
> - **[[Réduction Polynomiale]]** : Technique utilisée
> - **[[Classe NP#NP-Complet]]** : Classe de complexité
> - **[[Conséquence de la Complétude]]** : Implications pratiques
