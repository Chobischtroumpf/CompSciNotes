---
title: Algorithme de Vérification
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Un **algorithme de vérification** pour un problème $P$ est un algorithme de décision $A$ qui prend deux mots $(u, v)$ en entrée et retourne 1 ou 0, tel que $u \in P$ si et seulement si il existe un mot $v$ (appelé **certificat**) où $A(u, v) = 1$.

## Formalisation

> [!abstract]+ Définition Formelle
> Un algorithme de vérification pour $P \subseteq \Sigma^*$ est un algorithme de décision $A$ prenant deux mots en argument, qui termine pour toute entrée, tel que :
>
> $$P = \{u \in \Sigma^* \mid \exists v \in \Sigma^*, A(u, v) = 1\}$$
>
> Quand $A(u, v) = 1$, on dit que $v$ est un **certificat** pour $u$.

## Interprétation

> [!tip]+ Signification Intuitive
> Un algorithme de vérification permet de vérifier qu'une **solution candidate** à un problème est valide.
>
> **Différence avec algorithme de décision** :
> - **Algorithme de décision** : Trouve la solution
> - **Algorithme de vérification** : Vérifie une solution proposée

## Exemples

> [!example]+ Coloriage de Graphes
> **Problème** : Un graphe $G$ est-il coloriable avec au plus $k$ couleurs ?
>
> **Algorithme de vérification** :
> - **Entrée** : Le graphe $G$, le nombre $k$, et un coloriage $c$ (certificat)
> - **Vérification** :
>   1. Vérifier que $c$ utilise au plus $k$ couleurs
>   2. Pour chaque arête $(u, v)$, vérifier que $c(u) \neq c(v)$
> - **Retour** : 1 si valide, 0 sinon
>
> **Complexité** : Polynomial (parcours des arêtes)

> [!example]+ SAT (Satisfiabilité)
> **Problème** : Une formule propositionnelle est-elle satisfaisable ?
>
> **Algorithme de vérification** :
> - **Entrée** : La formule $\phi$ et une valuation $V$ (certificat)
> - **Vérification** : Évaluer $\phi$ sous $V$
> - **Retour** : 1 si $\phi$ est vraie sous $V$, 0 sinon
>
> **Complexité** : Polynomial (évaluation de formule)

> [!example]+ 2-Partition
> **Problème** : Peut-on partitionner un ensemble d'entiers en deux sous-ensembles de même somme ?
>
> **Algorithme de vérification** :
> - **Entrée** : Les entiers $c_1, ..., c_n$ et un sous-ensemble $J$ (certificat)
> - **Vérification** :
>   1. Calculer $S_1 = \sum_{i \in J} c_i$
>   2. Calculer $S_2 = \sum_{i \notin J} c_i$
>   3. Vérifier que $S_1 = S_2$
> - **Retour** : 1 si égalité, 0 sinon
>
> **Complexité** : Polynomial (deux sommes)

## Lien avec la Classe NP

> [!abstract]+ Définition Alternative de NP
> Un problème est dans NP si et seulement si il existe un algorithme de vérification polynomial pour ce problème.
>
> **Caractéristiques** :
> - Le certificat doit avoir une taille polynomiale
> - La vérification doit se faire en temps polynomial
> - L'existence d'un certificat équivaut à appartenir au problème

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Algorithme de Décision]]** : Variante sans certificat
> - **[[Classe NP]]** : Définie via les algorithmes de vérification
> - **[[Problème de Décision]]** : Type de problème vérifié
> - **[[Certificat]]** : Témoin de la solution
