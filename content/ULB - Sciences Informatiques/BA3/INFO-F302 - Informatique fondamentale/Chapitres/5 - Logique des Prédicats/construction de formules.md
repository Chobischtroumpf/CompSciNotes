---
title: construction de formules
authors: Mihai Bors
tags: []
---

# construction des formules
- ensembles des formules d'un langage $\mathcal{L}$
	- ensemble des formules de la forme
		- $p(t_1,...,t_n)$
			- $p$ = prédicat d'arité $n$
			- $t_1,...,t_n$ = termes du langages $\mathcal{L}$
	- noté $\mathcal{F(L)}$
	- défini par la grammaire suivante
$$
\phi ::= p(t_1,...,t_n) | phi \lor \phi | phi \land \phi | \neg \phi | \phi \to \phi | \phi \leftrightarrow \phi | \exists x\cdot \phi | \forall x \cdot \phi | (\phi)
$$
- où
	- $t_1,...,t_n$ : termes
	- $p$ symbole de relation
	- $\exists x$ : quantificateur existentiel
	- $\forall x$ : quantificateur universel

- lorsque $p$ est le prédicat $=$
	- → noter $t_1 = t_2$ au lieu de $= (t_1,t_2)$

## exemples
- $r(c) \lor \neg \exists x \cdot r(x)$ : formule de $\mathcal{L}_1$
	- exemples de formules de $\mathcal{L}_2$
		- $\forall x \cdot \exists y (g(x,y) = c \land g(y,x) = c)$
		- $\forall x \cdot \neg(f(x) = c)$
- langage $\mathcal{L}_3 = \set{p}$ où $p$ = symbole de prédicat binaire
	- $\forall x \cdot \forall y \cdot (p(x,y) \to p(y,x))$
	- $\forall x \cdot \forall y \cdot \forall z \cdot (p(x,y) \land p(y,z) \to p(x,z))$
	- comment pour que $p$ interprété par une fonction  ?
		- $\forall x \cdot \forall y \cdot \forall z \cdot (p(x,y) \land p(x,z) \to y = z)$
		- → fonction totale (def partout) : $\forall x \cdot \exists y \cdot p(x,y)$
