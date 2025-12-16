---
title: Les Règles de Déduction Naturelle
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Les **règles de déduction naturelle** forment un système complet de règles d'inférence permettant de prouver la validité de formules en logique propositionnelle.

## Règles par Connecteur

> [!abstract]+ Organisation
> Les règles sont organisées par connecteur logique. Chaque connecteur possède généralement :
> - Une ou plusieurs règles d'**introduction** (pour créer le connecteur)
> - Une ou plusieurs règles d'**élimination** (pour utiliser le connecteur)

## Conjonction ($\land$)

![[Conjonction#Règles]]

## Disjonction ($\lor$)

![[Disjonction#Règles d'Introduction]]

![[Disjonction#Règle d'Élimination]]

## Implication ($\rightarrow$)

![[Introduction de l'Implication#Règle]]

![[Double Négation#Modus Ponens]]

![[Modus Tollens (Contraposition)#Règle]]

## Négation ($\neg$)

![[Négation#Règle d'Introduction]]

![[Négation#Règle d'Élimination]]

![[Négation#Règle pour la Contradiction]]

## Double Négation ($\neg\neg$)

![[Double Négation#Règles]]

## Récapitulatif Visuel

> [!note]+ Tableau Synthétique
>
> | Connecteur | Introduction | Élimination |
> |:----------:|:------------:|:-----------:|
> | $\land$ | De $\phi$ et $\psi$ obtenir $\phi \land \psi$ | De $\phi \land \psi$ obtenir $\phi$ (ou $\psi$) |
> | $\lor$ | De $\phi$ obtenir $\phi \lor \psi$ | Raisonnement par cas |
> | $\rightarrow$ | Supposer $\phi$, dériver $\psi$ | Modus ponens, Modus tollens |
> | $\neg$ | Supposer $\phi$, dériver $\bot$ | De $\phi$ et $\neg\phi$ obtenir $\bot$ |
> | $\neg\neg$ | De $\phi$ obtenir $\neg\neg\phi$ | De $\neg\neg\phi$ obtenir $\phi$ |

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Déduction Naturelle]]** : Système général de preuve
> - **[[Conjonction]]** : Règles pour $\land$
> - **[[Disjonction]]** : Règles pour $\lor$
> - **[[Introduction de l'Implication]]** : Règle pour $\rightarrow$
> - **[[Négation]]** : Règles pour $\neg$
> - **[[Double Négation]]** : Règles pour $\neg\neg$
> - **[[Modus Tollens (Contraposition)]]** : Règle dérivée
> - **[[Équivalence]]** : Notion liée à la validité
