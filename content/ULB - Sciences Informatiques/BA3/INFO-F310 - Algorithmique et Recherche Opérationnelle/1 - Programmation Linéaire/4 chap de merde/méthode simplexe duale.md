---
title: méthode simplexe duale
authors: iamscrambledeggs
tags: []
---

# méthode simplexe duale
- soient
	- $\min c^Tx$
		- $Ax = b$
		- $x \geq 0$
	- $\max b^Ty$
		- $A^T y \leq c$

## théorème 1
- Si
	- $x (x^*)$ solution admissible qlcq (respectivement optimale) du primal
	- $y$ solution admissible du dual
- alors
	1. dualité faible : nécessairement $b^T y \leq c^Tx^* \leq c^Tx$
	2. dualité forte : $\exists$ nécessairement $y^* : b^Ty \leq b^T y^* = c^Tx^*$
	3. écarts : CNS pour $x$ et $y$ soient optimales simultanément
		- $j = 1:n$
		- $x_j \gt 0 \implies a_j^Ty = c_j$
		- $a_j^Ty \leq c_j \implies x_j = 0$


## motivation
imaginons un primal avec $m = 1000$ contraintes et $n = 100$ inconnues

| formes         | primal                                               | dual                                                                  |
| -------------- | ---------------------------------------------------- | --------------------------------------------------------------------- |
| forme standard | m = 1000 contraintes et m+n = 1100 inconnues         | n = 100 contraintes et m = 1000 inconnues donc m + n = 1100 inconnues |
| simplexe       | résoudre à chaque étape un sys de taille 1000 X 1000 | résoudre à chaque étape un système de taille 100 X 100                |
→ préférence pour la version duale (possède moins de contraintes)

## relations
**à partir d'un exemple**
- problème primal
	- $\max z = 5x_1 + 4x_2$
		- $6x_1 + 4x_2 \leq 24$
		- $x_1 + 2x_2 \leq 6$
		- $x_2 \leq 2$
		- $-x_1 + x_2 \leq 1$
		- $x_1,x_2 \geq 0$
- problème dual
	- $\min w = 24y_1 + 6y_2 + 2y_3 + y_4$
		- $6y_1 + y_2 - y_4 \geq 5$
		- $4y_1 + 2y_2 + y_3 + y_4 \geq 4$
		- $y_1,y_2,y_3,y_4 \geq 0$

- identifier relations primal-dual dans la méthode du Simplexe
![[Pasted image 20251205153605.png]]
- toutes les contraintes dans le primal et le dual sont des inéglaités
- correspondance entre variables
	- variables originales primal $\set{x_1,x_2}$
	- variables d'écart du dual $\set{t_1,t_2}$
	- variables originales du dual $\set{y_1,y_2,y_3,y_4}$
	- variables d'écart du primal $\set{s_1,s_2,s_3,s_4}$
- observations
	- valeurs des variables duales sont égales à l'opposé des profits marginaux des variables correspondantes du prb primal $\set{s_1,s_2}, \set{y_1,y_2}$
	- valeurs des variables primales sont égales aux coûts réduits des var correspondantes du prb dual $\set{x_1,x_2},\set{t_1,t_2}$
	- → conséquence de la complémentarité des solutions primale et duale

## théorème 2
- soient
	- $\max c^Tx$
		- $Ax = b$
		- $x \geq 0$
	- $\min b^Ty$
		- $A^T y \geq c$
- pour toute solution de base non dégénérée $x$ du problème primal
	- → il existe exactement UNE solution $y$ du dual complémentaire à $x$
- la solution $x$ est admissible
	- $\leftrightarrow y$ satisfait les conditons d'optimalité (coûts réduits non neg)
- la solution $y$ est admissible
	- $\leftrightarrow x$ satisfait les conditions d'otpimalité (profits marginaux négatifs ou nuls)

**preuve** je ne la fais pas, faut pas croire wesh

## principe
- cas
	- une solution en base non-admissible satisfaisant les conditions d'optimalité peut être facilement identifiable
		- _ex. var d'écart associées aux contraintes d'inégalités_
	- cette base correspond à une solution admissible du dual

**méthode**
- idée
	- résoudre implicitement le dual par la meth du simplexe mais en travaillant sur le tableau primal
		- débuter avec une solution de base satisfaisant les conditions d'optimalité
			- = base admissible pour le dual
		- chercher à rendre cette solution optimal
			- = dual optimale

### règles de pivotage

**choix de variable sortante**
- choisir la var $l$ en base (dans B) avec la valeur minimum (négative)
- si $\forall l \in B, \overline{b_l} \geq 0$
	- → solution admissible
	- STOP

**choix de la variable entrante**
- choisir la variable $k$ hors base (dans $N$) :
	- $k = \arg \min_{i \in N: \overline{a}_{li} \lt 0} -\frac{|\overline{c_i}|}{\overline{a}_{li}}$
	- si $\forall i \in N :\overline{a}_{li} \geq 0$
		- → pas de solution admissible
		- STOP
