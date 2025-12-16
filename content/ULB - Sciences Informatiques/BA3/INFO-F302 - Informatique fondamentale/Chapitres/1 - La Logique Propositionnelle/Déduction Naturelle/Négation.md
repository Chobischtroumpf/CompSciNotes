---
title: Négation
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Les règles pour la **négation** permettent d'introduire et d'éliminer le connecteur logique $\neg$ dans les preuves de [[Déduction Naturelle]].

## Règle d'Introduction

> [!abstract]+ Preuve par l'Absurde
> Pour prouver $\neg\phi$, on suppose $\phi$ comme hypothèse et on dérive une contradiction ($\bot$) :
>
> $$\frac{\begin{array}{c} \phi \quad \text{hyp.} \\ \vdots \\ \bot \quad \text{fin hyp.}\end{array}}{\neg\phi} \neg_i$$

## Règle d'Élimination

> [!abstract]+ Détection de Contradiction
> Si on a $\phi$ et $\neg\phi$, on peut déduire une contradiction ($\bot$) :
>
> $$\frac{\phi \quad \neg\phi}{\bot} \neg_e$$

## Règle pour la Contradiction

> [!abstract]+ Principe d'Explosion
> D'une contradiction, on peut déduire n'importe quoi (ex falso quodlibet) :
>
> $$\frac{\bot}{\phi} \bot_e$$

## Exemples

> [!example]+ Introduction de la Négation
> **Prouver** : $x \rightarrow y, x, \neg y \vdash \neg x$
>
> **Preuve** :
> ```
> 1. x → y        prémisse
> 2. x            prémisse
> 3. ¬y           prémisse
> 4. | x          hyp.
> 5. | y          →-MP, 1, 4
> 6. | ⊥          ¬-e, 5, 3
> 7. ¬x           ¬-i, 4-6
> ```
>
> (Note : Ceci contredit la prémisse 2, montrant l'incohérence des prémisses)

> [!example]+ Principe d'Explosion
> **Prouver** : $x, \neg x \vdash y$
>
> **Preuve** :
> ```
> 8. x            prémisse
> 9. ¬x           prémisse
> 10. ⊥            ¬-e, 1, 2
> 11. y            ⊥-e, 3
> ```

## Interprétation

> [!tip]+ Signification Intuitive
> - **Introduction** : Pour montrer que $\phi$ est faux, on suppose $\phi$ vrai et on montre que cela mène à une contradiction
> - **Élimination** : Avoir à la fois $\phi$ et $\neg\phi$ est impossible (contradiction)
> - **Explosion** : D'une contradiction, tout peut être déduit (système incohérent)

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Déduction Naturelle]]** : Système de preuve utilisant ces règles
> - **[[Double Négation]]** : Cas particulier de la négation
> - **[[Modus Tollens (Contraposition)]]** : Utilise la négation
> - **[[Les Règles de Déduction Naturelle]]** : Liste complète des règles
