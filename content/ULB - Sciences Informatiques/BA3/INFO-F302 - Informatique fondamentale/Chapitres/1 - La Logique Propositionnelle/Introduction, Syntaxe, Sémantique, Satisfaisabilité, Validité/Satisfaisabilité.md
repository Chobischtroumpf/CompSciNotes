---
title: Satisfaisabilité
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Une formule propositionnelle $\phi$ est **satisfaisable** si et seulement si il existe une fonction d'interprétation $V$ pour les propositions de $\phi$, telle que $V \models \phi$.

![[787e4f3ab2cfbe709b732419dd8f51df.png]]

## Interprétation

> [!abstract]+ Signification
> Une formule est satisfaisable s'il existe au moins une attribution de valeurs de vérité aux propositions qui rend la formule vraie.

## Satisfaisabilité d'Ensembles de Littéraux

> [!tip]+ Cas Particulier
> Un ensemble $S$ de littéraux est satisfaisable si et seulement si il ne contient pas une paire de littéraux complémentaires $\{x, \neg x\}$.
>
> **Exemples** :
> - $\{x, y, \neg z\}$ est satisfaisable
> - $\{x, \neg x, y\}$ n'est pas satisfaisable

## Relation avec la Validité

> [!abstract]+ Lien Fondamental
> Une formule $\phi$ est satisfaisable si et seulement si $\neg \phi$ n'est pas valide.
>
> Ce résultat découle directement du théorème établi dans [[Validité]].

## Exemples

> [!example]+ Formules Satisfaisables
> **Satisfaisables mais non valides** :
> - $x \land y$ (satisfaisable par $V(x) = V(y) = 1$)
> - $x \lor y$ (satisfaisable par $V(x) = 1$ ou $V(y) = 1$)
>
> **Non satisfaisables** :
> - $x \land \neg x$
> - $(x \lor y) \land \neg x \land \neg y$

## Table de Vérité

> [!example]+ Visualisation
> Pour $\phi = x \land (y \lor z)$ :
>
> | $x$ | $y$ | $z$ | $y \lor z$ | $x \land (y \lor z)$ |
> |:---:|:---:|:---:|:----------:|:--------------------:|
> | 0 | 0 | 0 | 0 | 0 |
> | 0 | 0 | 1 | 1 | 0 |
> | 0 | 1 | 0 | 1 | 0 |
> | 0 | 1 | 1 | 1 | 0 |
> | 1 | 0 | 0 | 0 | 0 |
> | 1 | 0 | 1 | 1 | 1 |
> | 1 | 1 | 0 | 1 | 1 |
> | 1 | 1 | 1 | 1 | 1 |
>
> $\phi$ est satisfaisable (3 interprétations satisfaisantes).

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Validité]]** : Concept dual de la satisfaisabilité
> - **[[Problème SAT]]** : Problème de décision de la satisfaisabilité
> - **[[Tableau Sémantique]]** : Algorithme pour tester la satisfaisabilité
> - **[[Fonction d'Interprétation]]** : Définition de $V \models \phi$
