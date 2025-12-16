---
title: variable libre, liée
authors: Mihai Bors
tags: []
---

# variables libres et liées
- idée
	- occurence d'une variable dans une formule = couple constitué de cette variable et d'une place effective
		- càd qui ne suit pas un quantificateur
## exemple
- $r(x,z) \to \forall \cdot (r(y,z) \lor y = z)$
	- $x$ une occurence
		- → libre dans $r(x,z)$
	- $y$ deux occurences
		- → libre dans $r(y,z)$ et $y = z$
	- $z$ trois occurences
		- → libre dans $r(x,z)$
		- → liée dans $\forall z \cdot r(y,z)$ et $\forall z \cdot y = z$

## définition
- une occurence d'une variable $x$ dans une formule $\phi$
	- occurence libre si elle ne se trouve dans aucune sous-formule de $\phi$ qui commence par une quantification $\forall x$ ou $\exists x$
		- sinon occurence dite _liée_
- variable _libre_ dans une formule
	- → si elle a au moins une occurence libre dans cette formule
