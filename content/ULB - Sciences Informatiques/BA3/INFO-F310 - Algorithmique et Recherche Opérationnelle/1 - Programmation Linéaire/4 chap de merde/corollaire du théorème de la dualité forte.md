---
title: corollaire du théorème de la dualité forte
authors: iamscrambledeggs
tags: []
---

# corollaire du théorème de la dualité forte
- soient
	- $x^*$ : solution optimale du primal (P) sous forme standard avec les variables d'écart $\set{x_{n+1},...,x_{n+m}}$
	- $\overline{c}^*_j, j \in \set{1,...,n+m}$: coûts réduits dans l'écriture de base optimale de (P)
- soient les définitions suivantes
	- en maximisation : $y_i^* = - \overline{c}^*_{n+i}, i = 1:m$
	- en minimisation :  $y_i^* = \overline{c}^*_{n+i}, i = 1:m$
- → alors $y^*$ solution optimale du dual (D)

## interprétation économique
- les valeurs duales optimales $y_i^*$
	- ~ coûts marginaux (shadow price)
	- désignent augmentation de l'objectif 'a la marge"
		- augemntationunitaire d'une borne d'une contrainte
- → égalité au signe prêt entre coûts réduits et marginaux
	- utilisation l'un ou l'autre pour les désigner
- gén : coûts marginaux indiquent la tendance eco permettant de prévoir ajustements ou améliorations d'un modèle
