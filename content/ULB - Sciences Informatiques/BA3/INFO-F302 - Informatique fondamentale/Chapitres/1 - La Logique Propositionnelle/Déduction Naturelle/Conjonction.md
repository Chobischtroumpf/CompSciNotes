---
title: Conjonction
authors: Alessandro Dorigo
tags:
  - InfoFond
---


Les règles pour la conjonction:
- Règle d'introduction: $$\frac{\phi \quad \psi}{\phi \land \psi} \land_i$$ (si j'ai une preuve de $\phi$ et une preuve de $\psi$, alors j'ai une preuve de $\phi \land \psi$)
- Règle d’élimination: $$\frac{\phi \land \psi}{\phi} \land_{e_1} \frac{\phi \land \psi}{\psi} \land_{e_2}$$ (si on a $\phi \land \psi$, on peut extraire que $\psi$)

> [!example] Exemples
> $x \land y, z \vdash y \land z$
> 1. $x \land y$ **prémisse**: on a $x$ et $y$ donnés comme vrais.
> 2. $z$ **prémisse**: on a $z$ donné comme vrai.
> 3. $y \land_{e_2}, 1$ **règle de l’élimination**: on extrait $y$ de $x \land y$
> 4. $y  \land z \land_i, 3,2$ **règle d'introduction**: on a $y$ de l’étape 3 et $z$ de l’étape 2, donc on peut les combiner pour avoir $y \land z$
>
> $(x \land y) \land z, t \land h \vdash y \land t$
> 1. $(x \land y) \land z$ **prémisse**: $(x \land y) \land z$ vrai
> 2. $t \land h$ **prémisse**: vrai
> 3. $x \land y \land_{e_1}, 1$ **règle d’élimination**: on extrait $x \land y$ de $(x \land y) \land z$
> 4. $y \land_{e_2}, 3$ **règle d’élimination**: on extrait $y$ de $x \land y$
> 5. $t \land_{e_1}, 2$ **règle d’élimination**: on extrait $t$ de $t \land h$
> 6. $y \land t \land_i, 4,5$ **règle d'introduction**: on a $y$ de l’étape 4 et $t$ de l’étape 5, donc on peut les combiner pour avoir $y \land t$
