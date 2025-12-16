---
title: Modus Tollens (Contraposition)
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Le **modus tollens** (ou contraposition) est une règle de déduction qui permet de déduire $\neg\phi$ à partir de $\phi \rightarrow \psi$ et $\neg\psi$.

## Règle

> [!abstract]+ Formulation
> Supposons que $\phi \rightarrow \psi$ et $\neg\psi$ soient vraies. Si $\phi$ était vrai, alors par le modus ponens on pourrait dériver $\psi$, ce qui serait en contradiction avec $\neg\psi$. Donc on en déduit que $\neg\phi$ est vrai.
>
> $$\frac{\phi \rightarrow \psi \quad \neg\psi}{\neg\phi} MT$$

## Exemple en Langage Naturel

> [!example]+ Application Concrète
> **Énoncés** :
> 1. S'il pleut alors la route est mouillée
> 2. La route n'est pas mouillée
>
> **Conclusion** : Il ne pleut pas
>
> **Justification** : Si il pleuvait, la route serait mouillée (par 1), mais la route n'est pas mouillée (par 2), donc il ne peut pas pleuvoir.

## Exemple Formel

> [!example]+ Preuve avec Modus Tollens
> **Prouver** : $x \rightarrow (y \rightarrow z), x, \neg z \vdash \neg y$
>
> **Preuve** :
> ```
> 1. x → (y → z)  prémisse
> 2. x            prémisse
> 3. ¬z           prémisse
> 4. y → z        →-MP, 1, 2
> 5. ¬y           MT, 4, 3
> ```

## Lien avec l'Implication Contraposée

> [!tip]+ Équivalence Logique
> Le modus tollens est basé sur l'équivalence logique :
>
> $$(A \rightarrow B) \equiv (\neg B \rightarrow \neg A)$$
>
> La contraposée d'une implication a la même valeur de vérité que l'implication originale.

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Déduction Naturelle]]** : Système de preuve utilisant cette règle
> - **[[Double Négation]]** : Règle du modus ponens
> - **[[Les Règles de Déduction Naturelle]]** : Liste complète des règles
> - **[[Équivalence]]** : Lien avec la contraposition
