---
title: Logique
authors: Alessandro Dorigo
tags:
  - MathDis
  - Logique
---


> [!info]+ Définition
> Le **prédicat** est une expression dont la vérité dépend d'une ou plusieurs variables. Par exemple, $P(x)$ pourrait représenter "$x$ est un nombre pair". Lorsque la variable $x$ est spécifiée, le prédicat devient une proposition qui est soit vraie, soit fausse.

^d2e40c

> [!info]+ Définition
> L'**implication**, notée $p \implies q$ (lire « si $p$ alors $q$ ») est *fausse* uniquement lorsque $p$ est *vrai* et $q$ est *faux*. Dans tous les autres cas, elle est *vraie*.

^35b977

> [!info]+ Définition
> La **double implication** (ou **équivalence**), notée $p \iff q$ est *vraie* si $p$ et $q$ ont la même valeur de vérité (tous deux _vrais_ ou tous deux _faux_), et *fausse* sinon.

^8c7f1d

> [!info]+ Définition
> La **négation** $\neg p$ est *vraie* lorsque $p$ est *fausse*, et *fausse* lorsque $p$ est *vraie*.

^6cf484
## Tables de Vérité

|      ![[c488fb00eb4f4f1a27a4e74b29f64e8c.png]]       |    ![[4f14214a05b075c9ea18fe67e84faff2.png]]     |
| :---------------------------------------------: | :-----------------------------------------: |
| [[Logique#^35b977\|Implication]] $p \implies q$ | [[Logique#^8c7f1d\|Équivalence]] $p \iff q$ |
### Exemples de Négation

| [[Proposition#^80e81d\|Proposition]] $P$  | [[Logique#^6cf484\|Négation]] $\neg P$          |
| ----------------------------------------- | ----------------------------------------------- |
| "Tous les oiseaux volent."                | "Il existe au moins un oiseau qui ne vole pas." |
| "Il existe un nombre pair supérieur à 5." | "Tous les nombres supérieurs à 5 sont impairs." |
| ![[7eaa7f58dd1c17d9db84b497b840b8f6.png]]      | ![[d6354f7acf82084e4486eb5e22d65e9f.png]]            |
