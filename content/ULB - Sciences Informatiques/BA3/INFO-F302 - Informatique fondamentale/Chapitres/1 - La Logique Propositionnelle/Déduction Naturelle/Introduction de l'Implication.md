---
title: Introduction de l'Implication
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La règle d'**introduction de l'implication** permet de prouver une implication $\phi \rightarrow \psi$ en supposant $\phi$ comme hypothèse et en dérivant $\psi$.

## Règle

> [!abstract]+ Formulation
> Pour prouver $\phi \rightarrow \psi$, on suppose $\phi$ (hypothèse) et on dérive $\psi$ :
>
> $$\frac{\begin{array}{c} \phi \quad \text{hyp.} \\ \vdots \\ \psi \quad \text{fin hyp.}\end{array}}{\phi \rightarrow \psi} \rightarrow_i$$

## Exemple

> [!example]+ Application
> **Prouver** : $x, y \vdash x \rightarrow (x \land y)$
>
> **Preuve** :
> ```
> 1. x            prémisse
> 2. y            prémisse
> 3. | x          hyp.
> 4. | x ∧ y      ∧-i, 3, 2
> 5. x → (x ∧ y)  →-i, 3-4
> ```

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Déduction Naturelle]]** : Système de preuve utilisant cette règle
> - **[[Double Négation]]** : Règle du modus ponens (élimination de l'implication)
> - **[[Modus Tollens (Contraposition)]]** : Autre usage de l'implication
> - **[[Les Règles de Déduction Naturelle]]** : Liste complète des règles
