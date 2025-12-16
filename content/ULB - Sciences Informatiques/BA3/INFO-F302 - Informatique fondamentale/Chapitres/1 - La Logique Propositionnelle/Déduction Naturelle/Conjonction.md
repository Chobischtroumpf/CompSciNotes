---
title: Conjonction
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Les règles pour la **conjonction** permettent d'introduire et d'éliminer le connecteur logique $\land$ dans les preuves de [[Déduction Naturelle]].

## Règles

> [!abstract]+ Règle d'Introduction
> Si j'ai une preuve de $\phi$ et une preuve de $\psi$, alors j'ai une preuve de $\phi \land \psi$ :
>
> $$\frac{\phi \quad \psi}{\phi \land \psi} \land_i$$

> [!abstract]+ Règles d'Élimination
> Si on a $\phi \land \psi$, on peut extraire chaque composante :
>
> $$\frac{\phi \land \psi}{\phi} \land_{e_1} \quad \quad \frac{\phi \land \psi}{\psi} \land_{e_2}$$

## Exemples

> [!example]+ Exemple Simple
> **Prouver** : $x \land y, z \vdash y \land z$
>
> **Preuve** :
> ```
> 1. x ∧ y        prémisse
> 2. z            prémisse
> 3. y            ∧-e₂, 1
> 4. y ∧ z        ∧-i, 3, 2
> ```

> [!example]+ Exemple avec Conjonctions Imbriquées
> **Prouver** : $(x \land y) \land z, t \land h \vdash y \land t$
>
> **Preuve** :
> ```
> 1. (x ∧ y) ∧ z  prémisse
> 2. t ∧ h        prémisse
> 3. x ∧ y        ∧-e₁, 1
> 4. y            ∧-e₂, 3
> 5. t            ∧-e₁, 2
> 6. y ∧ t        ∧-i, 4, 5
> ```

## Interprétation

> [!tip]+ Signification Intuitive
> - **Introduction** : Si on sait que $\phi$ est vrai et que $\psi$ est vrai, alors on sait que "$\phi$ et $\psi$" est vrai
> - **Élimination** : Si on sait que "$\phi$ et $\psi$" est vrai, alors on sait que $\phi$ est vrai (et que $\psi$ est vrai)

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Déduction Naturelle]]** : Système de preuve utilisant ces règles
> - **[[Double Négation]]** : Autres règles de déduction
> - **[[Les Règles de Déduction Naturelle]]** : Liste complète des règles
