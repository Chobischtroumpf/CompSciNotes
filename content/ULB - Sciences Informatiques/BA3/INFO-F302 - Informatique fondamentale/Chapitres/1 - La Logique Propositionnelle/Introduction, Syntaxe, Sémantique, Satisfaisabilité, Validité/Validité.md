---
title: Validité
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> Une formule propositionnelle $\phi$ est **valide** si et seulement si pour toute fonction d'interprétation $V$ pour les propositions de $\phi$, on a $V \models \phi$.
>
> Une formule valide est aussi appelée **tautologie**.

## Notation

> [!abstract]+ Symboles
> - $\models \phi$ signifie "$\phi$ est valide"
> - $V \models \phi$ signifie "$\phi$ est vraie sous l'interprétation $V$"

## Relation avec la Satisfaisabilité

> [!abstract]+ Théorème Fondamental
> Une formule propositionnelle $\phi$ est valide si et seulement si sa négation $\neg \phi$ n'est pas satisfaisable.
>
> **Démonstration** :
>
> 1. **($\Rightarrow$)** Supposons que $\phi$ est valide. Alors pour toute interprétation $V$, on a $V \models \phi$. Donc $V \not\models \neg \phi$. Comme c'est pour toute interprétation quelconque $V$, cela signifie que $\neg \phi$ n'est pas satisfaisable.
>
> 2. **($\Leftarrow$)** Réciproquement, supposons que $\neg \phi$ ne soit pas satisfaisable. Alors pour toute interprétation $V$ quelconque, $V \not\models \neg \phi$, donc $V \models \phi$. De nouveau, comme c'est pour toute interprétation quelconque $V$, on en déduit que $\phi$ est valide.

## Conséquence Algorithmique

> [!tip]+ Application Pratique
> Si on dispose d'un algorithme qui décide si une formule est satisfaisable ou non, on obtient un algorithme qui décide si la formule est valide : il suffit de tester la (non-)satisfaisabilité de sa négation.

## Exemples

> [!example]+ Formules Valides
> - $x \lor \neg x$ (tiers exclu)
> - $(x \rightarrow y) \leftrightarrow (\neg y \rightarrow \neg x)$ (contraposition)
> - $((x \rightarrow y) \land x) \rightarrow y$ (modus ponens)

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Satisfaisabilité]]** : Concept dual de la validité
> - **[[Fonction d'Interprétation]]** : Définition de $V \models \phi$
> - **[[Problème SAT]]** : Décision de la satisfaisabilité
> - **[[Déduction Naturelle]]** : Méthode pour prouver la validité
