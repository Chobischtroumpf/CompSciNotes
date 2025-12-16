---
title: formule équivalente
authors: Mihai Bors
tags: []
---

# formule équivalente
- deux formules $\phi_1,\phi_2$ sont équivalentes
	- tq $Libres(\phi_1) = Libres(\phi_2)$
- → si la formule $\forall x_1...\forall x_n(\phi_1 \leftrightarrow \phi_2)$ est valide
	- avec $\set{x_1,...,x_n} = Libres(\phi_1)$

## exemples de formules équivalentes
- couple 1
	- $\forall x \cdot (\phi \land \psi)$
	- $(\forall x \cdot \phi) \land (\forall x \cdot \psi)$
- couple 2
	- $\exists x \cdot (\phi \lor \psi)$
	- $(\exists x \cdot \phi) \lor (\exists x \cdot \psi)$
- couple 3
	- $\neg \forall x \cdot \phi$
	- $\exists x \cdot \neg \phi$
- couple 4
	- $\neg \exists x \cdot \phi$
	- $\forall x \cdot \neg \phi$

## à ne pas faire !!!!!
$\forall x ( \phi \lor \psi) \not \equiv (\forall x \phi) \lor (\forall x \psi)$
$\exists x (\phi \land \psi) \not \equiv (\exists x \phi) \land (\exists x \psi)$
 - si $\phi$ : $x$ est pair
 - si $\psi$ : $x$ est impair
 - car $Libres(\phi) \neq Libres(\psi)$ → pas équivalence
