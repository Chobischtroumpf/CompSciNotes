---
title: Sémantique
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **sémantique** définit la valeur de vérité d'une formule propositionnelle $\phi$ formée à partir des propositions d'un ensemble $X$, évaluée avec la fonction d'interprétation $V$, notée $\llbracket \phi \rrbracket_V$.
>
> En particulier, on a $\llbracket \phi \rrbracket_V \in \{0, 1\}$.

## Définition Inductive

> [!abstract]+ Cas de Base
> La fonction $\llbracket \phi \rrbracket_V$ est définie par induction sur la syntaxe de $\phi$ :
>
> **Constantes et propositions** :
> - $\llbracket \top \rrbracket_V = 1$
> - $\llbracket \bot \rrbracket_V = 0$
> - $\llbracket x \rrbracket_V = V(x)$

> [!abstract]+ Cas Inductifs
> **Connecteurs logiques** :
> - $\llbracket \neg \phi \rrbracket_V = 1 - \llbracket \phi \rrbracket_V$
> - $\llbracket \phi_1 \lor \phi_2 \rrbracket_V = \max(\llbracket \phi_1 \rrbracket_V, \llbracket \phi_2 \rrbracket_V)$
> - $\llbracket \phi_1 \land \phi_2 \rrbracket_V = \min(\llbracket \phi_1 \rrbracket_V, \llbracket \phi_2 \rrbracket_V)$
> - $\llbracket \phi_1 \rightarrow \phi_2 \rrbracket_V = \max(1 - \llbracket \phi_1 \rrbracket_V, \llbracket \phi_2 \rrbracket_V)$
> - $\llbracket \phi_1 \leftrightarrow \phi_2 \rrbracket_V = \min(\llbracket \phi_1 \rightarrow \phi_2 \rrbracket_V, \llbracket \phi_2 \rightarrow \phi_1 \rrbracket_V)$

## Syntaxe Minimale

> [!tip]+ Connecteurs Essentiels
> On peut se passer des opérateurs $\land, \rightarrow, \leftrightarrow$ car pour toute formule $A, B$ :
>
> - $A \land B \equiv \neg(\neg A \lor \neg B)$
> - $A \rightarrow B \equiv \neg A \lor B \equiv \neg(A \land \neg B)$
> - $A \leftrightarrow B \equiv \neg(A \land \neg B) \land \neg(B \land \neg A)$
>
> Ainsi, $\{\neg, \lor\}$ forme un ensemble complet de connecteurs.

## Exemple

> [!example]+ Calcul de Valeur de Vérité
> Soit $\phi = (x \rightarrow y) \land \neg z$ et $V(x) = 1, V(y) = 0, V(z) = 1$.
>
> **Calcul** :
> - $\llbracket x \rrbracket_V = 1$
> - $\llbracket y \rrbracket_V = 0$
> - $\llbracket z \rrbracket_V = 1$
> - $\llbracket x \rightarrow y \rrbracket_V = \max(1-1, 0) = 0$
> - $\llbracket \neg z \rrbracket_V = 1 - 1 = 0$
> - $\llbracket \phi \rrbracket_V = \min(0, 0) = 0$

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Fonction d'Interprétation]]** : Base de l'évaluation sémantique
> - **[[Satisfaisabilité]]** : Existence d'une interprétation satisfaisante
> - **[[Validité]]** : Vérité sous toutes les interprétations
> - **[[Bachus-Naur Form]]** : Syntaxe des formules
