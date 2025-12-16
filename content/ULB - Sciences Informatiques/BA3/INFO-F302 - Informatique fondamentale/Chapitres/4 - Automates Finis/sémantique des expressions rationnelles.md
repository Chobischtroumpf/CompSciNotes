---
title: sémantique des expressions rationnelles
authors: Mihai Bors
tags: []
---

# sémantiques des expressions rationnelles
- sémantique d'une expression rationnelle $E$ sur $\Sigma$ est donné par un langage, $L(E)$
	- $L(\epsilon) = \set{\epsilon}$
	- $\forall a \in \Sigma, L(a) = \set{a}$
	- $L(\emptyset) = \emptyset$
	- $L(E_1 + E_2) = L(E_1) \cup L(E_2)$
	- $L(E_1\cdot E_2) = L(E_1)\cdot L(E_2)$
		- pour qu'un mot $w$ soit dans $L(E_1\cdot E_2)$, il faut trouver $w_1,w_2$ tq
			- $w = w_1w_2$
			- $w_1 \in L(E_1)$
			- $w_2 \in L(E_2)$
	- $L(E^*) = L(E)^*$
		- $w \in L(E^*)$ si $\forall i \in \mathbb{N}, \forall w_i \in L(E), w = w_1...w_n$

## exemples
- sur $\Sigma = \set{a,b}$
	- $L((a+b)^*a(a+b)^*)$ : ensemble des mots qui contiennent au moins un $a$
		- $L(a+b) = L(a) \cup L(b)$
			- tous les mots où il y a au moins $a$ et $b$
		- $L((a+b)^*) = L(a+b)^*$
			- autant de répétitions qu'on veut
		- $L((a+b)^* \cdot a)$
			- il y a au moins la présence d'un $a$
	- $L(b^* (ab^* ab^*)^*)=PAIR$
		- $PAIR$ : nombre pair de $a$
		- $L(ab^*)$
			- au moins un $a$ et autant de $b$ qu'on veut
		- $L((ab^* ab^*)^*)$
			- autant de fois qu'on veut la chaine $ab^*ab^*$
				- → toujours eux $a$, donc toujours pair
	- $L(aa^*)$ : ensemble des mots qui ne contiennent que des $a$ et au moins un $a$
	- $PAIR\cdot ab^*$ = langage $IMPAIR$
→ ça ressemble un peu à la syntaxe regex
