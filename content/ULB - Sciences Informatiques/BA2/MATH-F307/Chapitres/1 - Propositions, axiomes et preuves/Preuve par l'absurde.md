---
title: Preuve par l'absurde
authors: Alessandro Dorigo
tags:
  - MathDis
  - Logique
---


> [!info]+ Définition
> Une **preuve par l'absurde** est un type de preuve indirecte ou l'on suppose que la [[proposition#^80e81d|proposition]] est fausse puis on montre que cette supposition mène à une contradiction.
>
> Elle a 3 étapes:
> 1. On suppose que $\neg P$ (la négation de $P$) est vraie;
> 2. On montre que cette supposition conduit à une contradiction;
> 3. On conclut que $P$ doit être vraie.

^9d7784

> [!example]+ Exemple de l'absurde (L'irrationalité de $\sqrt{2}$)
> Supposons que $\sqrt{2}$ est rationnel, c'est-à-dire qu'il existe deux entiers $a$ et $b$ tels que $\sqrt{2} = \frac{a}{b}$ avec $b \neq 0$ et $a$ et $b$ premiers entre eux.
>
> En élevant les deux membres au carré, nous obtenons $2 = \frac{a^2}{b^2}$, donc $a^2 = 2b^2$. Ainsi, $a^2$ est pair, donc $a$ est pair.
>
> En posant $a = 2k$, nous obtenons $4k^2 = 2b^2$ donc $b^2 = 2k^2$, ce qui implique que $b$ est également pair, contredisant le fait que $a$ et $b$ sont premiers entre eux.
>
> Donc, $\sqrt{2}$ est irrationnel.
