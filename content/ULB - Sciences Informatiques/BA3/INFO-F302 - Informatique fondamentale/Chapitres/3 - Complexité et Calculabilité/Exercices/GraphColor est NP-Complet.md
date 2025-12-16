---
title: GraphColor est NP-Complet
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Objectif
> Démontrer que le **problème de coloriage de graphe avec $k$ couleurs** (GRAPHCOLOR) est NP-complet en le réduisant depuis le problème 3-SAT.

## Rappel du Problème

> [!abstract]+ GRAPHCOLOR
> **Entrée** :
> - Un graphe $G = (V, E)$
> - Un entier $k$
>
> **Question** : Peut-on colorier les sommets de $G$ avec au plus $k$ couleurs telles que deux sommets adjacents n'aient jamais la même couleur ?

## Preuve de NP-Complétude

> [!abstract]+ Étape 1 : GRAPHCOLOR ∈ NP
> **Certificat** : Un coloriage $c : V \to \{1, ..., k\}$
>
> **Algorithme de vérification** (temps polynomial) :
> 1. Vérifier que $c$ utilise au plus $k$ couleurs
> 2. Pour chaque arête $(u, v) \in E$ :
>    - Vérifier que $c(u) \neq c(v)$
> 3. Retourner 1 si toutes les contraintes sont satisfaites
>
> **Complexité** : $O(|E|)$ (parcours des arêtes) ✓

> [!abstract]+ Étape 2 : GRAPHCOLOR est NP-Dur
> **Stratégie** : Réduction en temps polynomial depuis **3-SAT** (problème NP-complet)

## Rappel : Problème 3-SAT

> [!abstract]+ Définition
> **Entrée** : Une formule en FNC où chaque clause contient exactement 3 littéraux
>
> **Question** : Existe-t-il une valuation satisfaisant toutes les clauses ?
>
> **Exemple** : $(x_1 \lor x_2 \lor \neg x_3) \land (\neg x_1 \lor x_2 \lor x_n)$

## Réduction de 3-SAT vers GRAPHCOLOR

> [!abstract]+ Vue d'Ensemble
> On va construire, à partir d'une formule 3-SAT avec $n$ variables, un graphe $G$ et un entier $k$ tels que :
>
> $$\text{Formule satisfaisable} \Leftrightarrow G \text{ coloriable avec } k \text{ couleurs}$$
>
> **Nombre de couleurs** : $k = n + 1$
>
> **Couleurs** : $\{0, 1, \#\}$ plus une couleur par variable

## Réduction de 3-SAT vers GRAPHCOLOR

![[2d9ea3f7d8f2be84e2d497ddecc2ed3a.png]]

> [!example]+ Triangle Central
> Pour toute formule 3-SAT, créer un triangle avec 3 sommets :
> - Un sommet $T$ (True)
> - Un sommet $F$ (False)
> - Un sommet $\#$ (spécial)
> - Les trois sommets sont reliés entre eux (formant un triangle)
>
> **Propriété** : Dans tout coloriage valide avec 3 couleurs :
> - Les coloriages sont équivalents modulo permutation
> - Un littéral et sa négation ne peuvent pas être coloriés de la même couleur
> - On supposera que le nœud central est toujours colorié par $\#$
> - $T$ et $F$ utilisent les couleurs "$0$" et "$1$" (ordre quelconque)

## Encodage des Variables

**On le fait pour les $n$ propositions**

![[c6b6ae61c4bd670526fc394fcd384a61.png]]

> [!example]+ Gadget pour une Variable
> Pour chaque variable $x_i$ ($i = 1, ..., n$) :
>
> Créer un triangle :
> - Un sommet $x_i$ (la variable)
> - Un sommet $\neg x_i$ (sa négation)
> - Le sommet $\#$ (partagé)
> - Les trois sommets sont reliés entre eux
>
> **Propriétés** :
> - $x_i$ et $\neg x_i$ ont des couleurs différentes
> - Ils ne peuvent pas avoir la couleur $\#$
> - Donc l'un a la couleur $0$, l'autre la couleur $1$
> - **Interprétation** : Si $x_i$ a couleur $1 \Rightarrow x_i$ est vrai

> [!tip]+ Observation Importante
> **Relation entre littéraux** :
> - Si $x_i$ colorié en $0$ alors $\neg x_i$ colorié en $1$
> - Si $x_i$ colorié en $1$ alors $\neg x_i$ colorié en $0$
> - Un littéral et sa négation ne peuvent jamais être coloriés de la même couleur

## Répétition pour Toutes les Variables

> [!example]+ Graphe Complet pour $n$ Variables
> **Structure** :
> - Un triangle $(x_i, \neg x_i, \#)$ pour chaque variable $i = 1, ..., n$
> - Tous les triangles partagent le sommet central $\#$
> - Total : $2n + 1$ sommets pour les variables

## Encodage d'une Clause

**Encodage d'une clause**

![[05396be5f0cadc004acdc59f11cf17d3.png]]

> [!example]+ Gadget pour $(l_1 \lor l_2 \lor l_3)$
> Pour une clause $C = (l_1 \lor l_2 \lor l_3)$ où $l_i$ sont des littéraux :
>
> **Construction** :
> 1. Créer un "îlot" de 6 sommets formant une structure spéciale
> 2. L'îlot (par exemple $\neg x_1 \lor x_2 \lor x_n$) était séparé puis on l'a rattaché au graphe principal par le nœud colorié avec la couleur $1$
> 3. Connecter l'îlot aux sommets correspondant aux littéraux $l_1, l_2, l_3$
> 4. Attaches avec tous les $x_i$ de l'îlot car relation entre eux trois
>
> **Propriété clé** : L'îlot peut être colorié validement si et seulement si au moins un des littéraux $l_1, l_2, l_3$ est colorié en $1$ (c'est-à-dire au moins un est vrai).

### Détails du Gadget de Clause

> [!abstract]+ Structure de l'Îlot
> L'îlot pour $(\neg x_1 \lor x_2 \lor x_n)$ contient :
>
> **Connections** :
> - L'îlot est attaché au sommet de couleur $1$
> - L'îlot est attaché aux sommets $\neg x_1$, $x_2$, $x_n$ du graphe principal
>
> **Contrainte de coloriage** :
> - Si les trois littéraux $\neg x_1$, $x_2$, $x_n$ sont tous coloriés en $0$ (tous faux)
> - Alors l'îlot ne peut pas être colorié validement avec 3 couleurs
> - Sinon (au moins un littéral en $1$), l'îlot peut être colorié

> [!example]+ Coloriage Valide d'un Îlot
> **On attache avec les $x_i$ des propositions et de là, on propose un coloriage**
>
> ![[47564ca368fb179d332f5159eb24cf11.png]]
>
> Dans un exemple où $x_2$ est colorié en $1$ (vrai) :
> - L'îlot peut être colorié validement
> - La clause $(\neg x_1 \lor x_2 \lor x_n)$ est satisfaite

## Graphe Complet

> [!example]+ Construction Finale
> **Il faut le faire pour toutes les clauses**
>
> ![[e308425990b8a216597eb67259ca2a75.png]]
>
> **Structure totale** :
> 1. Triangle central $(T, F, \#)$
> 2. Pour chaque variable : triangle $(x_i, \neg x_i, \#)$
> 3. Pour chaque clause : un îlot connecté aux littéraux correspondants
>
> **Total de sommets** : $O(n + m)$ où $m$ est le nombre de clauses

## Preuve de Correction

> [!abstract]+ Théorème
> **Démontrer la correction de la réduction :**
>
> Il faut démontrer que :
> - Toute interprétation qui satisfait $S$ donne un coloriage du graphe avec 3 couleurs
> - Tout coloriage valide du graphe donne une interprétation qui satisfait $S$
>
> **Preuve ($\Rightarrow$)** : Valuation $\Rightarrow$ Coloriage
> - Soit $V$ une valuation satisfaisant toutes les clauses
> - **Construction du coloriage** :
>   - Colorier $\#$ avec couleur "$\#$"
>   - Pour chaque variable $x_i$ :
>     - Si $V(x_i) = 1$ : colorier $x_i$ en $1$, $\neg x_i$ en $0$
>     - Si $V(x_i) = 0$ : colorier $x_i$ en $0$, $\neg x_i$ en $1$
>   - Pour chaque clause $C = (l_1 \lor l_2 \lor l_3)$ :
>     - Au moins un littéral $l_j$ est vrai (car $V$ satisfait $C$)
>     - Donc $l_j$ est colorié en $1$
>     - L'îlot de $C$ peut être colorié validement
> - Tous les sommets sont coloriés validement ✓
>
> **Preuve ($\Leftarrow$)** : Coloriage $\Rightarrow$ Valuation
> - Soit un coloriage valide de $G$ avec $k$ couleurs
> - **Construction de la valuation** :
>   - Pour chaque variable $x_i$ :
>     - Si $x_i$ colorié en $1$ : poser $V(x_i) = 1$
>     - Si $x_i$ colorié en $0$ : poser $V(x_i) = 0$
> - **Vérification des clauses** :
>   - Soit $C = (l_1 \lor l_2 \lor l_3)$ une clause
>   - L'îlot de $C$ est colorié validement
>   - Donc au moins un littéral $l_j$ est colorié en $1$
>   - Donc au moins un littéral de $C$ est vrai sous $V$
>   - Donc $C$ est satisfaite
> - Toutes les clauses sont satisfaites ✓

## Complexité de la Réduction

> [!tip]+ Temps Polynomial
> **Construction du graphe** :
> 1. Triangle central : $O(1)$
> 2. Gadgets de variables : $O(n)$
> 3. Gadgets de clauses : $O(m)$ où $m$ = nombre de clauses
>
> **Taille du graphe** :
> - Sommets : $O(n + m)$
> - Arêtes : $O(n + m)$
>
> **Complexité totale** : $O(n + m)$ ✓ (polynomial)

## Conclusion

> [!success]+ Résultat
> **GRAPHCOLOR est NP-complet** car :
> 1. GRAPHCOLOR $\in$ NP (certificat vérifiable en temps polynomial)
> 2. GRAPHCOLOR est NP-dur (réduction depuis 3-SAT)
>
> **Conséquence** : Sauf si P = NP, il n'existe pas d'algorithme polynomial pour colorier un graphe avec un nombre minimal de couleurs.

## Remarques

> [!tip]+ Observations
> **Généralisation** :
> - Le problème est NP-complet pour $k \geq 3$
> - Pour $k = 2$ : le problème est dans P (test de bipartition)
>
> **Nombre chromatique** :
> - Trouver le nombre minimal de couleurs est aussi NP-complet
>
> **Cas particuliers polynomiaux** :
> - Graphes planaires (théorème des 4 couleurs)
> - Arbres (2 couleurs)
> - Graphes d'intervalles

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Problème de Décision#3-SAT]]** : Problème source de la réduction
> - **[[Réduction Polynomiale]]** : Technique utilisée
> - **[[Classe NP#NP-Complet]]** : Classe de complexité
> - **[[Conséquence de la Complétude]]** : Implications pratiques
