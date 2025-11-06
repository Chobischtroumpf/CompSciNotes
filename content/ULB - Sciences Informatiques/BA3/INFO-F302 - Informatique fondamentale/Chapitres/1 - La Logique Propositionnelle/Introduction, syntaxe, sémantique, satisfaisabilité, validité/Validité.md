---
title: Validité
authors: Alessandro Dorigo
tags:
  - InfoFond
---


> [!info] Définition
> Une formule propositionnelle $\phi$ est valide ssi pour toute fonction d’interprétation $V$ pour les propositions de $\phi$, on a $V \models \phi$.

> [!abstract] Théorème 1.0.1
> Une formule propositionnelle $\phi$ est valide ssi sa négation $\neg \phi$ n'est pas satisfaisable.
>
> **Démonstration**:
> 1. Supposons que $\phi$ est valide. Alors pour tout interprétation $V$, on a $V \models \phi$. Donc $V \not\models \neg \phi$. Comme c'est pour toute interpretation quelconque $V$, cela signifie que $\neg \phi$ n'est pas satisfaisable.
> 2. Réciproquement, supposons que $\neg \phi$ ne soit pas satisfaisable. Alors pour tout interprétation $V$ quelconque, $V \not\models \neg \phi$, donc $V \models \phi$. De nouveau, comme c’est pour tout interprétation quelconque $V$, on en déduit que $\phi$ est valide.

Par conséquent, si on dispose d’un algorithme qui décide si une formule est satisfaisable ou non, on obtient un algorithme qui décide si la formule est valide, il suffit de tester la (non-)satisfaisabilité de sa négation.
