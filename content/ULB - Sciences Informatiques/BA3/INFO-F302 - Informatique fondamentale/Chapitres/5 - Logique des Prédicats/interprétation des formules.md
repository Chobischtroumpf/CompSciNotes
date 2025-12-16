---
title: interprétation des formules
authors: Mihai Bors
tags: []
---

# interprétation des formules
- une formule $\phi$ construite sur un langage $\mathcal{L}$ est satisfaite
	- dans une structure $\mathcal{M}$
	- pour une valuation $v$ donnant une valeur aux variables de l'ensemble $\mathcal{V}$
	- noté $\mathcal{M}, v \vDash \phi$
- $\Leftrightarrow$ ssi

	- si
		- $\phi \equiv r(t_1,...,t_n)$
		- $\forall i=1:n, t_i^{\mathcal{M},v} = b_i$
	- alors
		- $\phi$ vraie
		- $\Leftrightarrow (b_1,...,b_n) \in r^{\mathcal{M}}$

	- si
		- $\phi \equiv \neg \psi_1$
		- $\phi \equiv \psi_1 \lor \psi_2$
		- $\phi \equiv \psi_1 \land \psi_2$
		- $\phi \equiv \psi_1 \to \psi_2$
		- $\phi \equiv \psi_1 \leftrightarrow \psi_2$
	- alors
		- la valeur de $\phi$ est calculée àpd valeurs de $\psi_1$ et $\psi_2$ comme dans le cas propositionnel

	- si
		- $\phi \equiv \exists x \cdot \psi$
	- alors
		- $\phi$ vraie $\Leftrightarrow$ il existe une valutation $v'$ tq $\mathcal{M}, v' \vDash \psi$ et $v'$ est d'accord avec $v$ sur $Libres(\phi)$
			- $v'(x) = v(x), \forall x \in Libres(\phi)$
