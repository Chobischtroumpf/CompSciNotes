---
title: Équivalence
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Deux formules $\phi$ et $\psi$ sont dites **équivalentes** si la formule $\phi \leftrightarrow \psi$ est valide. On note $\phi \equiv \psi$ pour signifier que $\phi$ et $\psi$ sont équivalentes.

## Interprétation

> [!abstract]+ Signification
> $\phi \equiv \psi$ signifie que pour toute fonction d'interprétation $V$ :
>
> $$\llbracket \phi \rrbracket_V = \llbracket \psi \rrbracket_V$$
>
> Autrement dit, $\phi$ et $\psi$ ont toujours la même valeur de vérité.

## Propriété de Substitution

> [!tip]+ Remplacement dans les Formules
> Si $\phi \equiv \psi$, alors dans toute formule $\gamma$ contenant $\phi$, on peut remplacer $\phi$ par $\psi$ pour obtenir une formule $\gamma'$ équivalente à $\gamma$.
>
> **Exemple** :
>
> Dans la formule
> $$\gamma = (x \lor y) \land \neg(x \land z)$$
>
> on peut remplacer $\neg(x \land z)$ par $(\neg x \lor \neg z)$ pour obtenir
> $$\gamma' = (x \lor y) \land (\neg x \lor \neg z)$$
>
> et on a $\gamma \equiv \gamma'$.

## Équivalences Fondamentales

> [!abstract]+ Lois Logiques Principales
> **Lois de De Morgan** :
> - $\neg(A \land B) \equiv \neg A \lor \neg B$
> - $\neg(A \lor B) \equiv \neg A \land \neg B$
>
> **Implication** :
> - $A \rightarrow B \equiv \neg A \lor B$
>
> **Équivalence** :
> - $A \leftrightarrow B \equiv (A \rightarrow B) \land (B \rightarrow A)$
>
> **Double négation** :
> - $\neg\neg A \equiv A$
>
> **Lois d'absorption** :
> - $A \land A \equiv A$
> - $A \lor A \equiv A$
>
> **Lois de distributivité** :
> - $A \land (B \lor C) \equiv (A \land B) \lor (A \land C)$
> - $A \lor (B \land C) \equiv (A \lor B) \land (A \lor C)$

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Validité]]** : Une équivalence est une formule valide
> - **[[Déduction Naturelle]]** : Système pour prouver les équivalences
> - **[[Formes Normales]]** : Utilise les équivalences pour transformer les formules
> - **[[Sémantique]]** : Définition de la valeur de vérité
