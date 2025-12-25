---
title: Classe NP
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La classe **NP** (Nondeterministic Polynomial time) est la classe des problèmes de décision pour lesquels une solution peut être **vérifiée** en temps polynomial.

## Définition Formelle

> [!abstract]+ Caractérisation
> Un problème $P$ est dans NP si et seulement si :
>
> Il existe :
> - Un algorithme de vérification $A$ de complexité polynomiale en temps
> - Une constante $k$
>
> Tels que pour toute entrée $u$ :
> - $u \in P$ si et seulement si
> - Il existe un certificat $v$ de longueur polynomiale ($|v| = O(|u|^k)$)
> - Tel que $A(u, v) = 1$

## Interprétations

> [!abstract]+ Définitions Équivalentes
> **Algorithme Non-Déterministe** :
> - Classe des problèmes résolubles en temps polynomial par un algorithme non-déterministe
> - L'algorithme peut faire des "choix aléatoires"
> - Si la réponse est OUI, il existe une exécution répondant OUI
> - Le certificat = suite de tirages menant à la réponse
>
> **Exemple SAT** :
> - Choisir aléatoirement une valeur pour chaque variable
> - Vérifier en temps linéaire qu'elles satisfont la formule

## Relation avec P

> [!abstract]+ Inclusion
> $$P \subseteq NP$$
>
> **Preuve** :
> - Soit un problème dans P résolu par l'algorithme $A$ en temps polynomial
> - Algorithme de vérification : Ignorer le certificat, exécuter $A$
> - Toujours polynomial, donc dans NP
>
> **Question ouverte** : $P = NP$ ?

## NP ⊆ ExpTime

> [!abstract]+ Borne Supérieure
> Tout problème de NP peut être décidé par un algorithme de complexité exponentielle en temps.
>
> **Preuve** :
> - Soit un problème dans NP avec algorithme de vérification $A$
> - Certificats de longueur au plus $a \cdot |u|^k$
> - **Algorithme exhaustif** :
>   1. Énumérer tous les certificats possibles
>   2. Pour chacun, appeler $A$
> - **Complexité** : $O(2^{a \cdot n^k} \cdot p(n))$ où $p$ est polynomial
>
> **Exemple SAT** : Énumérer toutes les interprétations possibles

## Exemples de Problèmes dans NP

> [!example]+ Problèmes Classiques
> **SAT (Satisfiabilité)** :
> - **Certificat** : Une valuation des variables
> - **Vérification** : Évaluer la formule (temps linéaire)
>
> **3-SAT** :
> - **Certificat** : Une valuation
> - **Vérification** : Polynomial
> - **Note** : NP-complet
>
> **Voyageur de Commerce** :
> - **Certificat** : Un cycle
> - **Vérification** : Calculer la longueur du cycle
>
> **Coloriage de Graphes** :
> - **Certificat** : Un coloriage
> - **Vérification** : Vérifier que deux voisins n'ont pas la même couleur
>
> **2-Partition** :
> - **Certificat** : Une partition
> - **Vérification** : Vérifier que les deux sommes sont égales
>
> **Bin Packing** :
> - **Certificat** : Un rangement des objets dans les sacs
> - **Vérification** : Vérifier que chaque sac respecte la capacité
>
> **Non-Primalité** :
> - **Certificat** : Un diviseur
> - **Vérification** : Division (polynomial)
>
> **Primalité** :
> - **Certificat** : Non trivial !
> - **Note** : Démontré dans P en 2002 (AKS)

### Exemples de Problèmes NP-Complets

> [!example]+ Problèmes Complets
> - **SAT** (Cook-Levin, 1971)
> - **3-SAT**
> - **Voyageur de Commerce**
> - **Coloriage de Graphes**
> - **Bin Packing**
> - **2-Partition**
> - **Couverture de Sommets** : Étant donné un graphe et un entier $k$, peut-on trouver un sous-ensemble $S$ de sommets tel que chaque arête a au moins une extrémité dans $S$ ?

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Classe P]]** : Sous-ensemble présumé de NP
> - **[[Algorithme de Vérification]]** : Définit l'appartenance à NP
> - **[[Conjecture P ≠ NP]]** : Question fondamentale
> - **[[Réduction Polynomiale]]** : Pour montrer la NP-dureté
