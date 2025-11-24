---
title: solution de base
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---
# Solution de base

> [!info]+ Définition
>
> Une **solution de base** d'un programme linéaire est une solution unique du système de $m$ équations à $m$ inconnues obtenu en fixant $(n-m)$ variables à zéro, pourvu que la matrice $A_B \in \mathbb{R}^{m \times m}$ du système soit inversible.
>
> Dans une solution de base, les variables fixées à zéro sont appelées **variables hors-base** et les autres variables sont appelées **variables en base**.

> [!info]+ Solution de base réalisable
>
> Une **solution de base réalisable** est une solution de base telle que toutes les variables prennent des valeurs non-négatives.

^503980

> [!info]+ Solution de base dégénérée
>
> Si une ou plusieurs variables de base d'une solution de base ont une valeur nulle, cette solution est appelée **solution de base dégénérée**.

^2d600c

> [!info]+ Solution de base réalisable dégénérée
>
> Si une solution de base réalisable est également une solution de base dégénérée, on parle de **solution de base réalisable dégénérée**.

^199e43

> [!info]+ Solution réalisable optimale
>
> Une **solution réalisable optimale** est une solution réalisable satisfaisant le système de contraintes et atteignant la valeur minimale (ou maximale) de la fonction objectif.

^50a468

> [!info]+ Solution réalisable
>
> Un vecteur $x$ satisfaisant les contraintes $Ax = b, x \geq 0$ est dit **réalisable** (ou **admissible**) pour ces contraintes.

^af92a8

> [!tip]+ Remarque
>
> Pour un système de $m$ équations à $n$ inconnues ($m < n$), il existe une infinité de solutions.
