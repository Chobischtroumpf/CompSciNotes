---
title: alphabet
authors: Mihai Bors
tags: []
---

# alphabet
- alphabet d'un langage 1er ordre comportes les symboles (communs à tous ces langages)
	- connecteurs
		- $\neg, \land, \lor, \to, \leftrightarrow$
	- parenthèses
		- $(,)$
	- quantificateurs universel et existentiel : $\forall, \exists$
	- ensemble infini $V$ de symboles de variables $x,y,z,...$

- langage $L$ de la logique du premier ordre est caractérisé par
	- symboles de relations (= prédicats)
		- $p,r,s,...$
	- symboles de fonctions
		- $f,g,h,...$
	- symboles de constantes
		- $c,d,e,...$
- → chaque prédicat $p$, on associe un entier st positif (= _arité_ de $p$)
	- càd le nb d'arguments de $p$
		- $p|_n$ : $p$ symbole de relation d'arité $n$
	- même chose pour une fonction $f$ d'arité $n$
- prédicat "$=$" : dénoter égalité
	- on suppose qu'il est toujours présent (même si pas indiqué dans $L$ )

## exemples de langages
- $L_1 = \set{r|_1,c}$
	-  un prédicat unaire $r$
	- une constante $c$
- $L_2 = \set{r|_2, f|_1, g|_2, h|_2, c,d}$
	- prédicat  binaire $r$
	- une fonction unaire $f$
	- deux symboles de fonctions binaire $g,h$
	- deux constantes $c,d$
