---
title: construction des termes
authors: Mihai Bors
tags: []
---

# construction des termes
- ensembles des termes d'un langage $\mathcal{L}$
	- = plus petit ensemble qui contient les symboles de constantes et de variables
		- + qui est clos par application des fonctions
	- noté $\mathcal{T}$
	- satisfaisant
		- tout symbole de constante ou variable = un terme
		- si
			- $f$ = un symbole de fonction d'arité $n$
			- $t_1,t_2,..,t_n$ = termes
		- alors
			- → $f(t_1,t_2,...,t_n)$ = terme
- terme _clos_ s'il est sans variables
	- _ex.$f(c)$_

- NB : prédicats ne fournissent pas des termes
	- → ils serviront pour construire les formules

## exemples
 - les seuls termes du langage $\mathcal{L}_1$
	 - la constantes $c$
	 - les variables
- termes du langage $\mathcal{L}_2$
	- f(c)
	- f(h(f(c),d))
	- f(y)
	- f(h(f(x),f(d)))
