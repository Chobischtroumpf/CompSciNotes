---
title: interprétation des termes dans une structure
authors: Mihai Bors
tags: []
---

# interprétation des termes dans une structure
- étant données
	- $\mathcal{V}$  : ensemble de variables
	- $M$ : un domaine
	- une _valuation_  pour les variables de $\mathcal{V}$ dans $M$
		- → une fonction $v:\mathcal{V} \to M$ qui attribue à chq variable $x \in \mathcal{V}$
	- une valeur $v(x) \in M$
 → l'interprétation d'un terme $t$ (dont les variables sont dans $\mathcal{V}$) dans une structure de domaine $M$
- + selon une valuation $v$ = un élément $t^{\mathcal{M},v} \in M$
	- → définition inductivement :
		- si $t=c$
			- → $t^{\mathcal{M},v} = c^{\mathcal{M}}$
		- si $t=x$
			- → $t^{\mathcal{M},v} = v(x)$
		- si $t = f(t_1,...,t_n)$
			- → $t^{\mathcal{M},v} = f^{\mathcal{M}}(t_1^{\mathcal{M},v}, ..., t_n^{\mathcal{M},v})$
## exemples
- soient
	- $\mathcal{L}_2 = (r|_2,f|_1,g|_2,h|_2,c,d)$
	- $\mathcal{M}_3 = (\mathbb{N},\leq, +1, +, \times, 0,1)$
- l'interprétation dans $\mathcal{M}_3$ de
	- $t_1 \equiv g(y,h(c,x))$
		- $v(x) = 3$
		- $v(y) = 4$
		- $v(z) = 6$
	- → $t_1^{\mathcal{M}_3,v} = g^{\mathcal{M}_3}(v(y), h^{\mathcal{M}_3}(c^{\mathcal{M}_3},v(x)))$
		- $= v(y) + h^{\mathcal{M}_3}(c^{\mathcal{M}_3},v(x))$
		- $=v(y) + c^{\mathcal{M}_3}\times v(x)$
		- $= 4 + 0 \times 3$
		- $= 4$
	- $t_2 \equiv f(g(d,h(y,z)))$
		- $v(x) = 3$
		- $v(y) = 4$
		- $v(z) = 6$
	- → $t_2^{\mathcal{M}_3,v} = (1+(4 \times 6)) + 1 = 26$
