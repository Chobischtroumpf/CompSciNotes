---
title: Règles de précédence
authors: Alessandro Dorigo
tags:
  - InfoFond
---


> [!info] Ordre de précédence $\prec$ sur les opérateurs:
> $$\leftrightarrow \ \prec \ \rightarrow \ \prec \ \lor \ \prec \ \land \ \prec \ \neg$$
> et associativité a gauche pour $\leftrightarrow, \lor, \land$ et a droite pour $\rightarrow$

> [!example] Exemples
> - $x \lor y \land z$ se lit $x \lor (y \land z)$
> - $x \rightarrow y \rightarrow x$ se lit $x \rightarrow (y \rightarrow x)$
> - $x \lor y \rightarrow z$ se lit $(x \lor y) \rightarrow z$
> - $\neg x \land y$ se lit $(\neg x) \land y$
> - $x \rightarrow y \land z \rightarrow t$ se lit $x \rightarrow ((y \land z) \rightarrow t)$
> 	- ![[Pasted image 20251001115823.png]]

> [!tip] Remarque
> Les parenthèses permettent de contrecarrer ces règles, si elles ne conviennent pas. Elles permettent aussi de rendre une formule plus lisible, ou de ne pas devoir retenir les règles de précédence.
