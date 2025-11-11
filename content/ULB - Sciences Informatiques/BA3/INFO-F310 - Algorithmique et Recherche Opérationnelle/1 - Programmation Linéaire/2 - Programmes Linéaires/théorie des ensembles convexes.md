---
title: théorie des ensembles convexes
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---

### combinaison convexe
- Pour un ensemble fini de points $x_1,...,x_n \in \mathbb{R}^d$ et toute famille de réels positifs $\alpha_i \geq 0, i = 1...,n$
	- telles que : $\sum_{i=1}^n \alpha_i = \alpha_1 + ... + \alpha_n = 1$
	- le point def par :
		- $\sum_{i=1}^n \alpha_i x_i = \alpha_1x_1 + ... + \alpha_n x_n$
		- = combinaison convexe des points $x_1,...,x_n$

### ensemble convexe
- un ensemble $X \subseteq \mathbb{R}^n$ est convexe si
	- toute pair de points $y \in X$
	- tout $\alpha \in [0,1]$
	- → vérifie la combinaison convexe $\alpha x + (1 - \alpha)y \in C$
**interprétation**
- X convexe $\leftrightarrow$ pour tout couple de points $x,y$ de $X$
	- le segment de droite $[x,y] = \set{\alpha x + (1 - \alpha)y | \alpha \in [0,1]}$
		- reliant ces deux points est (entièrement) inclus dans $X$
	- un élément $z$ de ce segment [x,y] s'écrit égalemnt sous la forme
		- $z = y + \alpha ( x - y)$

#### exemple ensembles connexe
- ensemble vide, singleton, espace $\mathbb{R}^n$
- sous-ensemble I de $\mathbb{R}$ définit un intervalle si $x,y \in I, x \lt z \lt y \to z \in I$
	- sous-ensemble de $\mathbb{R}$ convexe $\leftrightarrow$ I est un intervalle
- boule unitaire d'un espace vectoriel
	- $\set{x \in \mathbb{R}^n | ||x||_p \leq 1}, p \in [1, \infty [$
- ellipsoïde
	- $\set{x \in \mathbb{R}^n | (x - x_c)^T Q(x - x_c) \leq r}, x_c \in \mathbb{R}^n, r \in \mathbb{R}, Q$ matrice positive semi-définie $\in \mathbb{R}^{n \times n}$
- l'ensemble défini par des contraintes d'inégalités linéaires
	- $\set{x \in \mathbb{R}^n | Ax \leq b} = \set{ x \in \mathbb{R}^n | a_i^T x \leq b_i, i = 1,..., m}$
		- matrice $A \in \mathbb{R}^{m \times n}$
		- vecteur $b \in \mathbb{R}^m$
- hyperplan (intersection de deux demi-espaces fermés)
	- $\set{x \in \mathbb{R}^n | a^T x = b}$

### enveloppe convexe
- Soit un ensemble qlcq $X \subseteq \mathbb{R}^n$
	- conv(X) :  ensemble convexe le plus petit contenant $X$
	- → en dimision finie, conv(X) = ensemble des combinaisons convexe finies d'éléments (points) de $X$
		- conv(X) = $\set{x \in X | x = \sum_{i=1}^m \alpha_i x_i, \sum_{i=1}^m \alpha_i = 1, \alpha_i \geq 0}$
		- → défini comme inteersection de demi-espaces fermés → ensemble lui-même fermé
- algorithmes
	- jarvis march
	- graham scan
	- combination chan's algortihm

### point extrême
- un point $x$ d'un ensemble convexe $X \subseteq \mathbb{R}^n$ est un point extrême de $X$ s'il n'existe pas deux points distincts $y$ et $z \in X$ tq
	- $x = \alpha y + (1 - \alpha)z, \alpha \in ] 0 ; 1 [$
- → point extrême de X : point $x$ qui ne se situe pas strictement à l'intérieur d'un segment de droite reliant deux autres points de l'ensemble
	- $x \in X, x \not \in \text{ conv}(X \setminus \set{x})$

**exemples**
- les points extrêmes d'un polyèdre = ses sommets
