---
title: Fonction d'Interprétation
authors: Alessandro Dorigo, Mihai Bors
tags:
  - InfoFond
---
> [!info]+ Définition
> La **fonction d'interprétation** (notée $V$) pour un ensemble $X$ de propositions considérées assigne à chaque variable de $X$ la valeur vrai ou faux.
>
> $$V : X \rightarrow \{0, 1\}$$

## Notation

> [!abstract]+ Valeurs de Vérité
> - $V(x) = 1$ signifie que la proposition $x$ est vraie sous l'interprétation $V$
> - $V(x) = 0$ signifie que la proposition $x$ est fausse sous l'interprétation $V$

## Extension aux Formules

> [!note]+ Évaluation de Formules
> La fonction d'interprétation $V$ s'étend aux formules complexes via la [[Sémantique]].
>
> Pour toute formule $\phi$, on note $\llbracket \phi \rrbracket_V$ la valeur de vérité de $\phi$ sous l'interprétation $V$.

## Exemple

> [!example]+ Interprétation Concrète
> Soit $X = \{x, y, z\}$ et l'interprétation $V$ définie par :
> - $V(x) = 1$
> - $V(y) = 0$
> - $V(z) = 1$
>
> Alors pour la formule $\phi = x \land (y \lor z)$ :
> - $\llbracket \phi \rrbracket_V = \llbracket x \land (y \lor z) \rrbracket_V = 1 \land (0 \lor 1) = 1 \land 1 = 1$

## Concepts Associés

> [!note]+ Voir Aussi
> - **[[Sémantique]]** : Extension de l'interprétation aux formules
> - **[[Satisfaisabilité]]** : Existence d'une interprétation satisfaisante
> - **[[Validité]]** : Vérité sous toutes les interprétations
