---
title: Sémantique
authors: Alessandro Dorigo
tags:
  - InfoFond
---


> [!info] Définition
> La valeur de vérité d'une formule propositionnelle $\phi$ formée a partir des propositions d'un ensemble $X$, évaluée avec la fonction d’interprétation $V$, est notée $⟦ \phi ⟧_V$. En particulier, on a $⟦ \phi ⟧_V \in \{ 0, 1 \}$.
>
> La fonction $⟦ \phi ⟧_V$ est définie par induction sur la syntaxe de $\phi$ de la façon suivante:
> - $⟦ \top ⟧_V = 1; ⟦ \bot ⟧_V = 0; ⟦ x ⟧_V = V(x)$.
> - $⟦ \neg \phi ⟧_V = 1 - ⟦ \phi ⟧_V$
> - $⟦ \phi_1 \lor \phi_2 ⟧_V = \max(⟦ \phi_1 ⟧_V, ⟦ \phi_2 ⟧_V)$
> - $⟦ \phi_1 \land \phi_2 ⟧_V = \min(⟦ \phi_1 ⟧_V, ⟦ \phi_2 ⟧_V)$
> - $⟦ \phi_1 \rightarrow \phi_2 ⟧_V = \max(1 - ⟦ \phi_1 ⟧_V, ⟦ \phi_2 ⟧_V)$
> - $⟦ \phi_1 \leftrightarrow \phi_2 ⟧_V = \min(⟦ \phi_1 \rightarrow \phi_2 ⟧_V, ⟦ \phi_2 \rightarrow \phi_1 ⟧_V)$

> [!tip] Syntaxe minimale
> On peut se passer des opérateurs $\land, \rightarrow, \leftrightarrow$ car pour toute formule $A, B$:
> - $A \lor B \equiv \neg (\neg A \land \neg B)$
> - $A \rightarrow B \equiv \neg A \lor B \equiv \neg (A \land \neg B)$
> - $A \leftrightarrow B \equiv \neg (A \land \neg B) \land \neg (B \land \neg A)$
