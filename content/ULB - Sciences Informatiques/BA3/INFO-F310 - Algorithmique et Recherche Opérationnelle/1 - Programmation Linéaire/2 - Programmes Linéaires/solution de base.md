---
title: solution de base
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---

# solution de base
solution de base d'un programme linéaire : solution unique du sys de m équation à m inconnues obtenu en fixant (n-m) var à zéro
- pourvu que mat $A_B \in R^{m \times m}$ du sys soit inv

→ dans sol de base, var fixées à zéro == variables **hors-base** et autres var = variables en-base
## solution de base réalisable
solution de base tq ttes les var prennent des valeurs non-nég = solution de base réalisable

## solution de base dégénérée
Si une ou plusieurs var de base d'une solution de base ont une valeur nulle, cette sol = solution de base dégénérée

## solution de base réalisable dégénérée
Si solution de base réalisable est également une soltuion de base dégénérée → solution de base réalisable dégénérée

## solution réalisable optimale
sol réalisable satisfaisant au sys de contraintes et atteignant la val minimale de la fonction objectif

## solution réalisable
vecteur $x$ satisfaisant les contraintes $Ax = b, x \geq 0$ est dit réalisable (/ admissible) pour ces contraintes
- → pour un sys de **m** eq à **n** inconnues ($m \lt n$ ) : infinité de solutions
