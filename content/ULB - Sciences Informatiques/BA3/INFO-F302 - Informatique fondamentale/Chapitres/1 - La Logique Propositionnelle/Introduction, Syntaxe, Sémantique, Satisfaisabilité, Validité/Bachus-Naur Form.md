---
title: Bachus-Naur Form
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **forme de Backus-Naur (BNF)** est une notation formelle pour décrire la syntaxe des formules de la logique propositionnelle.

## Vocabulaire

> [!abstract]+ Composants du Langage
> Le vocabulaire du langage de la logique propositionnelle est composé de :
>
> - **Propositions** : $x, y, z, \dots$ notées $X, Y, \dots$
> - **Constantes** : vrai ($\top$) et faux ($\bot$)
> - **Connecteurs logiques** : $\land, \lor, \rightarrow, \leftrightarrow, \neg$
> - **Parenthèses** : $(, )$

## Règle de Formation

> [!note]+ Syntaxe BNF
> Soit $X$ un ensemble de propositions. Les formules de la logique propositionnelle respectent la règle de formation BNF :
>
> $$\phi ::= \top \mid \bot \mid x \mid \phi_1 \land \phi_2 \mid \phi_1 \lor \phi_2 \mid \phi_1 \rightarrow \phi_2 \mid \phi_1 \leftrightarrow \phi_2 \mid \neg \phi_1 \mid (\phi_1)$$
>
> où $\phi_1$, $\phi_2$ sont des formules propositionnelles bien formées (respectent les règles syntaxiques de la logique propositionnelle).

## Interprétation

> [!abstract]+ Formules Bien Formées
> Une formule est **bien formée** si elle respecte la syntaxe BNF, c'est-à-dire si elle peut être construite en appliquant récursivement les règles de formation à partir des propositions atomiques et des constantes.

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[ULB - Sciences Informatiques/BA3/INFO-F302 - Informatique fondamentale/Chapitres/1 - La Logique Propositionnelle/Introduction, Syntaxe, Sémantique, Satisfaisabilité, Validité/Règles de Précédence]]** : Ordre d'évaluation des opérateurs
> - **[[Formalisation Logique]]** : Utilisation de la syntaxe BNF
> - **[[Fonction d'Interprétation]]** : Attribution de valeurs de vérité aux formules
