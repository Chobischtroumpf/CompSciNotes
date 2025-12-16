---
title: Problème Indécidable
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Un problème de décision $P$ sur un alphabet $\Sigma$ est **indécidable** s'il n'existe pas d'algorithme $A$ qui :
> - Prend un mot sur $\Sigma$ en entrée
> - Termine en un nombre fini d'étapes
> - Retourne 1 si et seulement si le mot appartient à $P$

## Problème de l'Arrêt

> [!abstract]+ Définition
> **Entrée** : Le code source $c_P$ d'un programme $P$ et une entrée $x$
>
> **Question** : Le programme $P$ s'arrête-t-il sur l'entrée $x$ ?
>
> **Exemple** :
> ```
> while(true) print "bonjour";
> ```
> Ce programme ne s'arrête jamais.

### Théorème de Turing (1936)

> [!warning]+ Indécidabilité
> Le problème de l'arrêt est **indécidable**.

### Preuve par l'Absurde

> [!abstract]+ Démonstration
> **Hypothèse** : Supposons qu'il existe un programme `HALT(c_p, x)` qui décide le problème de l'arrêt.
>
> **Construction** : Définissons le programme `PARADOX` :
> ```
> PARADOX(c : string)
>     if HALT(c, c) then
>         loop forever
>     else
>         stop
> ```
>
> **Appel paradoxal** : Considérons `PARADOX(c_PARADOX)`
>
> **Cas 1** : Si le programme s'arrête
> - Alors `HALT(c_PARADOX, c_PARADOX) = 0`
> - Donc `PARADOX(c_PARADOX)` ne s'arrête pas
> - **Contradiction !**
>
> **Cas 2** : Si le programme ne s'arrête pas
> - Alors `HALT(c_PARADOX, c_PARADOX) = 1`
> - Donc `PARADOX(c_PARADOX)` s'arrête
> - **Contradiction !**
>
> **Conclusion** : Le programme `HALT` ne peut pas exister.

## Problème de la Correspondance de Post

> [!info]+ Définition (PCP)
> **Entrée** :
> - Alphabet $\Sigma = \{0, 1\}$
> - $n$ paires de mots $(u_1, v_1), ..., (u_n, v_n)$ (possiblement vides)
>
> **Question** : Existe-t-il une séquence d'indices $i_1, ..., i_k \in \{1, ..., n\}$ ($k \geq 1$) telle que :
> $$u_{i_1}u_{i_2}...u_{i_k} = v_{i_1}v_{i_2}...v_{i_k}$$

> [!example]+ Exemples
> **Instance 1** :
> - $(u_1, v_1) = (100, 00)$
> - $(u_2, v_2) = (0, 01)$
>
> **Solution** : Séquence 2, 1
> - $u_2u_1 = 0100 = v_2v_1$ ✓
>
> **Instance 2** :
> - $(u_1, v_1) = (0, 100)$
> - $(u_2, v_2) = (01, 00)$
> - $(u_3, v_3) = (110, 11)$
>
> **Solution** : Séquence 3, 2, 3, 1
> - $u_3u_2u_3u_1 = (110)(01)(110)(0)$
> - $= (11)(00)(11)(100) = v_3v_2v_3v_1$ ✓

### Théorème

> [!warning]+ Indécidabilité
> Le problème de Correspondance de Post est **indécidable**.

## Autres Problèmes Indécidables

> [!example]+ Exemples Classiques
> **10ème Problème de Hilbert** :
> - **Entrée** : Un polynôme $p(x_1, ..., x_n)$ à coefficients entiers
> - **Question** : Existe-t-il $i_1, ..., i_n \in \mathbb{Z}$ tels que $p(i_1, ..., i_n) = 0$ ?
> - **Statut** : Indécidable (Matiyasevic, 1971)
> - **Note** : Décidable dans les réels
>
> **Complexité de Kolmogorov** :
> - **Entrée** : Un mot binaire $w$ et un entier $k \in \mathbb{N}$
> - **Question** : Existe-t-il un programme Java écrivant $w$ dont le code fait au plus $k$ bits ?
> - **Note** : Le choix du formalisme influe sur la complexité
>
> **PCP avec 7 paires** :
> - **Note** : Décidable pour $n \leq 2$, ouvert pour $3 \leq n \leq 6$
>
> **Castor Affairé** :
> - **Entrée** : Un programme qui écrit des 0 et des 1 et s'arrête
> - **Question** : Est-il maximal ? (aucun programme de taille similaire n'écrit un mot plus long)

## Réduction et Indécidabilité

> [!tip]+ Méthode de Preuve
> Pour montrer qu'un problème $B$ est indécidable :
>
> 1. Prendre un problème $A$ connu comme indécidable
> 2. Montrer que si on pouvait décider $B$, on pourrait décider $A$
> 3. Conclure que $B$ est indécidable
>
> **Note** : Contrairement aux réductions pour NP-dureté, on ne demande pas que l'algorithme de réduction soit en temps polynomial.

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Algorithme de Décision]]** : Ce qu'un problème indécidable n'a pas
> - **[[Problème de Décision]]** : Cadre formel
> - **[[Classe P]]** : Problèmes décidables efficacement
> - **[[Classe NP]]** : Problèmes décidables (mais pas forcément efficacement)
