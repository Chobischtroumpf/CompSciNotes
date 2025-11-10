---
titled: Définitions
authors: Alessandro Dorigo
tags:
  - InfoFond
---

# clause

> [!info] Définition
> - clause = disjonction de littéraux $l_1 \vee ... \vee l_n$
	>>- satisfaite par valuation $V$ s'il existe $i$ tq $V(l_i) = 1$
	>>- → clause _vide_, $\bot$ insatisfaisable
# satisfaction d'ensemble de clauses

> [!info] Définition
>- satisfaction d'ensemble de clauses
	>>- un ensemble de clauses $A = \set{C_1,...,C_n}$ est satisfait par une valuation $V$, noté $V \vdash A$
		>>>- si pour tout $i, V \vDash C_i$
		>>>- en particulier, tout valuation satisfait l'ensemble vide $A = \emptyset$
