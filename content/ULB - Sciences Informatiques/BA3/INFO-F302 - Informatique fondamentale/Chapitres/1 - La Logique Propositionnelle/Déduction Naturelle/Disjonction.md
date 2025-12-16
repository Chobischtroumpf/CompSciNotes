---
title: Disjonction
authors: Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Les règles pour la **disjonction** permettent d'introduire et d'éliminer le connecteur logique $\lor$ dans les preuves de [[Déduction Naturelle]].

## Règles d'Introduction

> [!abstract]+ Introduction à Gauche et à Droite
> Si on a $\phi$, on peut déduire $\phi \lor \psi$ (ou $\psi \lor \phi$) :
>
> $$\frac{\phi}{\phi \lor \psi} \lor_{i_1} \quad \quad \frac{\psi}{\phi \lor \psi} \lor_{i_2}$$

## Règle d'Élimination

> [!abstract]+ Raisonnement par Cas
> Pour utiliser $\phi_1 \lor \phi_2$, on considère les deux cas séparément et on montre que dans chaque cas on arrive à la même conclusion $\psi$ :
>
> $$\frac{\begin{array}{c} \quad \quad \quad \quad \phi_1 \quad \text{hyp.} \quad \quad \phi_2 \quad \text{hyp.} \\ \quad \quad \vdots \quad \quad \quad \quad \vdots \\ \phi_1 \lor \phi_2 \quad \quad \psi \quad \text{fin hyp.} \quad \psi \quad \text{fin hyp.} \end{array}}{\psi} \lor_e$$

## Exemples

> [!example]+ Introduction Simple
> **Prouver** : $x \vdash x \lor y$
>
> **Preuve** :
> ```
> 1. x        prémisse
> 2. x ∨ y    ∨-i₁, 1
> ```

> [!example]+ Élimination par Cas
> **Prouver** : $x \lor y, x \rightarrow z, y \rightarrow z \vdash z$
>
> **Preuve** :
> ```
> 1. x ∨ y        prémisse
> 2. x → z        prémisse
> 3. y → z        prémisse
> 4. | x          hyp.
> 5. | z          →-MP, 2, 4
> 6. | y          hyp.
> 7. | z          →-MP, 3, 6
> 8. z            ∨-e, 1, 4-5, 6-7
> ```

## Interprétation

> [!tip]+ Signification Intuitive
> - **Introduction** : Si $\phi$ est vrai, alors "$\phi$ ou $\psi$" est vrai (peu importe $\psi$)
> - **Élimination** : Si "$\phi$ ou $\psi$" est vrai et que les deux cas mènent à $z$, alors $z$ est vrai

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Déduction Naturelle]]** : Système de preuve utilisant ces règles
> - **[[Conjonction]]** : Règles pour $\land$
> - **[[Négation]]** : Règles pour $\neg$
> - **[[Les Règles de Déduction Naturelle]]** : Liste complète des règles
