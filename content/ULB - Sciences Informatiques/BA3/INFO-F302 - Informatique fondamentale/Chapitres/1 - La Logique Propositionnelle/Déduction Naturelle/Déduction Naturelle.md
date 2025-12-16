---
title: Déduction Naturelle
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **déduction naturelle** est un système de règles qui permettent, pas à pas, de déduire des conclusions à partir de prémisses. Elle permet de prouver qu'une formule est valide.

## Principe

> [!abstract]+ Séquent
> Supposons donnés :
> - Un ensemble de formules $\phi_1, \dots, \phi_n$ (prémisses)
> - Une formule $\psi$ (conclusion)
>
> On veut montrer que $\psi$ peut être dérivée de $\phi_1, \dots, \phi_n$, noté :
>
> $$\phi_1, \dots, \phi_n \vdash \psi$$
>
> (appelé **séquent**)

## Lien Syntaxe-Sémantique

> [!abstract]+ Théorème de Complétude et Correction
> Les règles de déduction permettent de faire le lien entre la syntaxe et la sémantique :
>
> $$\phi_1, \dots, \phi_n \vdash \psi \text{ si et seulement si } \phi_1, \dots, \phi_n \models \psi$$
>
> **Signification** :
> - Tout ce qui est démontrable est valide (**correction**)
> - Tout ce qui est valide est démontrable (**complétude**)

## Notations

> [!note]+ Symboles Utilisés
> - $\vdash \phi$ : "$\phi$ est prouvable"
> - $\models \phi$ : "$\phi$ est valide"

## Structure d'une Preuve

> [!abstract]+ Format de Dérivation
> Une preuve en déduction naturelle est une séquence d'étapes où chaque ligne contient :
>
> 1. Un numéro de ligne
> 2. Une formule
> 3. Une justification (règle appliquée et numéros de lignes utilisées)
>
> **Exemple de format** :
> ```
> 1. φ₁           prémisse
> 2. φ₂           prémisse
> 3. ψ            règle, lignes x, y
> ```

## Règles Principales

> [!note]+ Catégories de Règles
> Les règles de déduction naturelle incluent :
>
> - **[[Conjonction]]** : Introduction et élimination de $\land$
> - **[[Double Négation]]** : Introduction et élimination de $\neg\neg$
> - **Modus Ponens** : Élimination de l'implication
> - **[[Modus Tollens (Contraposition)]]** : Forme de raisonnement par contraposition
> - **Règles pour la disjonction** : Introduction et élimination de $\lor$
> - **Règles pour la négation** : Introduction et élimination de $\neg$

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Conjonction]]** : Règles pour $\land$
> - **[[Double Négation]]** : Règles pour $\neg\neg$
> - **[[Modus Tollens (Contraposition)]]** : Raisonnement par contraposition
> - **[[Les Règles de Déduction Naturelle]]** : Liste complète des règles
> - **[[Équivalence]]** : Notion liée à la validité
> - **[[Validité]]** : Propriété prouvée par la déduction naturelle
