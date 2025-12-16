---
title: structure
authors: Mihai Bors
tags: []
---

# structure
- structure $\mathcal{M}$ pour un langage $\mathcal{L}$
	- un ensemble non vide $M$
		- _domaine_
	- une interprétation des sumboles de prédicats par des relations sur $M$
	- des symboles de fonctions par des fonctions de $M$
	- des constantes par des éléments de $M$

donc
- structure composée
	- un sous-ensemble $M^n$ pour chq symbole de prédicat $r$ d'arité $n$ dans $\mathcal{L}$
		- noté $r^{\mathcal{M}}$
	- une fonction totale de $M^m$ dans $M$ pour chaque symbole de fonction $f$ d'arité $m$ dans $\mathcal{L}$
		- noté $f^{\mathcal{M}}$
	- un élément de $M$ pour chaque symbole de constante $c$ dans $\mathcal{L}$
		- noté $c^{\mathcal{M}}$

## exemples
- pour $\mathcal{L}_1 = (r|_1,c)$
	- structure $\mathcal{M}_1 = (\mathbb{N}, r^{\mathcal{M}_1}, c^{\mathcal{M}_1})$
		- $r^{\mathcal{M}_1}$ : ensemble des nb premiers
		- $c^{\mathcal{M}_1} = 2$
	- → structure est une interprétaiton de $\mathcal{L}_1$
- pour $\mathcal{L}_2 = (r|_2,f|_1,g|_2, h|_2,c,d)$
	- possibilité de prendre structure sur les réeles
		- $\mathcal{M}_2 = (\mathbb{R}, \leq, +1,+,\times,0,1)$
		- $+1$ : la fonction $x \mapsto x+1$
	- → écrit directement les interprétations dans le n-uplet
		- parfois uniquement
