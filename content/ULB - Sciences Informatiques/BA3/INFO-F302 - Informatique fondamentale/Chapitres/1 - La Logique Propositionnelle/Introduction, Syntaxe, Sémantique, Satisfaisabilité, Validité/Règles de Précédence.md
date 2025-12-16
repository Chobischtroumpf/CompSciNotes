---
title: Règles de Précédence
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Les **règles de précédence** définissent l'ordre dans lequel les opérateurs logiques sont évalués dans une formule, permettant d'omettre certaines parenthèses.

## Ordre de Précédence

> [!abstract]+ Hiérarchie des Opérateurs
> L'ordre de précédence $\prec$ sur les opérateurs est :
>
> $$\leftrightarrow \ \prec \ \rightarrow \ \prec \ \lor \ \prec \ \land \ \prec \ \neg$$
>
> **Associativité** :
> - À gauche pour $\leftrightarrow, \lor, \land$
> - À droite pour $\rightarrow$

## Exemples

> [!example]+ Applications des Règles
> **Exemples simples** :
> - $x \lor y \land z$ se lit $x \lor (y \land z)$
> - $x \rightarrow y \rightarrow x$ se lit $x \rightarrow (y \rightarrow x)$
> - $x \lor y \rightarrow z$ se lit $(x \lor y) \rightarrow z$
> - $\neg x \land y$ se lit $(\neg x) \land y$

> [!example]+ Exemple Complexe
> $x \rightarrow y \land z \rightarrow t$ se lit $x \rightarrow ((y \land z) \rightarrow t)$
>
> ![[e3efb3e1539ec235761d5385f5f44332.png]]

## Usage des Parenthèses

> [!tip]+ Remarque
> Les parenthèses permettent de :
>
> - Contrecarrer les règles de précédence si nécessaire
> - Rendre une formule plus lisible
> - Éviter d'avoir à mémoriser toutes les règles

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Bachus-Naur Form]]** : Syntaxe formelle des formules
> - **[[Formalisation Logique]]** : Application des règles de précédence
