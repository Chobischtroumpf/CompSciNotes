---
title: Double Négation
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Les règles pour la **double négation** permettent d'introduire et d'éliminer $\neg\neg$ dans les preuves de [[Déduction Naturelle]].

## Règles

> [!abstract]+ Règle d'Introduction
> Si on a une preuve de $\phi$, on peut en déduire $\neg\neg\phi$ :
>
> $$\frac{\phi}{\neg\neg\phi} \neg\neg_i$$

> [!abstract]+ Règle d'Élimination
> Si on a une preuve de $\neg\neg\phi$, on peut en déduire $\phi$ :
>
> $$\frac{\neg\neg\phi}{\phi} \neg\neg_e$$

## Modus Ponens

> [!abstract]+ Règle d'Élimination de l'Implication
> Si on a $\phi$ et $\phi \rightarrow \psi$, on peut déduire $\psi$ :
>
> $$\frac{\phi \quad \phi \rightarrow \psi}{\psi} \rightarrow_{MP}$$

## Exemple

> [!example]+ Application du Modus Ponens
> **Énoncés** :
> 1. Il pleut
> 2. S'il pleut alors la route est mouillée
>
> **Conclusion** : La route est mouillée
>
> **Preuve formelle** :
> ```
> 1. p            prémisse (il pleut)
> 2. p → q        prémisse (s'il pleut alors la route est mouillée)
> 3. q            →-MP, 1, 2 (la route est mouillée)
> ```

## Interprétation

> [!tip]+ Signification Intuitive
> - **Double négation** : "Il n'est pas vrai que φ est faux" équivaut à "φ est vrai"
> - **Modus ponens** : Si une condition est vraie et que cette condition implique une conclusion, alors la conclusion est vraie

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Déduction Naturelle]]** : Système de preuve utilisant ces règles
> - **[[Conjonction]]** : Autres règles de déduction
> - **[[Modus Tollens (Contraposition)]]** : Règle similaire par contraposition
> - **[[Les Règles de Déduction Naturelle]]** : Liste complète des règles
