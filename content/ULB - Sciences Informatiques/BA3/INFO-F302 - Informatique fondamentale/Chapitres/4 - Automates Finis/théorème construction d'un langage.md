---
title: théorème construction d'un langage
authors: Mihai Bors
tags: []
---

# $L(B_{F\cdot G}) = (L(F) \backslash \set{\epsilon})\cdot L(G)$

## preuve
svp je veux foutre en l'air ce cours

- idée de la preuve : double inclusion
	- sens direct
		- pour exécution acceptante de $L(B_{F \cdot G})$, décomposition en deux parties (une dans $F$ et une autre dans $G$ avec état acceptant)
		- → transition pour aller de la partie $A_F$ à $A_G$
		- → donc il y a une transition depuis $q_i$ en lisant $\sigma_i$ vers un état acceptant de $F$
		- → comme mot différent du mot vide, on a bien $w \in (L(F) \backslash \set{\epsilon})\cdot L(G)$
	- sens indirect
		- existence de $w_1,w_2 : w = w_1w_2, w_1 \in L(F), w_2 \in L(G), w_1 \neq \epsilon$
		- → existence exécution acceptante de $A_F$ sur $w_1$ vers état acceptant de $A_F$
			- même chose pour $A_G$
		- → donc exécution acceptante de $w$
		- → $w \in L(B_{F\cdot G})$
