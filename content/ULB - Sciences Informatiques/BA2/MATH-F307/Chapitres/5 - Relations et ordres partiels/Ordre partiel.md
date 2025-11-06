---
title: Ordre partiel
authors: Alessandro Dorigo
tags:
  - MathDis
  - Relations
---


> [!info]+ Définition
> Un **ordre partiel** sur $X$ est une [[ULB - Sciences Informatiques/BA2/MATH-F307/Chapitres/5 - Relations et ordres partiels/Relation#^bbecb9|relation]] $R$ qui est
> 1. [[Relation réflexive#^33ed77|Réflexive]]
> 2. [[Relation antisymétrique#^313899|Antisymétrique]]
> 3. [[Relation transitive#^28003e|Transitive]]
>
> On écrit, par simplicité $R = \ \preceq$

^632685

> [!example]+ Exemples
> - $\mid$ sur $\mathbb{N}$ ("divise")
> - $\leq$ sur $\mathbb{Q}$ ("est plus petit ou égal")

> [!info]+ Définition
> Un élément $x$ dans un ordre partiel $(X , \preceq)$ est dit **minimal** s’il n’existe pas un $y \in X$ tel que $y \prec x$.

^f0a218

> [!info]+ Définition
> Un élément $x$ dans un ordre partiel $(X , \preceq)$ est dit **maximal** s’il n’existe pas un $y \in X$ tel que $x \prec y$.

^1660da

> [!abstract]- Lemme 5.6.1
> Tout ordre partiel fini possède un [[Ordre partiel#^f0a218|élément minimal]].
>
> ![[Pasted image 20241021100659.png]]
> ![[Pasted image 20241021100707.png]]
>
> Avec la même preuve, on peut montrer que $X$ possède aussi un [[Ordre partiel#^1660da|élément maximal]].

^59e650
