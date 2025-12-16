---
title: exemple 1
authors: Mihai Bors
tags: []
---

# exemple 1
- Soient
	- $\mathcal{L} = (p,q,r,s,t,f)$
		- $p,q$ prédicats unaires
		- $r,s,t$ prédicats binaires
		- $f$ une fonction unaire
- modéliser
	1. prédicat $s$ contient le produit cartésien de $p,q$
	2. prédicat $t$ est égal au produit cartésien de $q,p$
	3. fonction $f$ est surjective
- correction
	1. $\forall x \forall y ( p(x) \land p(q) \to s(x,y))$
	2. $\forall x \forall y (q(x) \land p(y) \leftrightarrow t(x,y))$
	3. $\forall x \exists y (f(x) = y)$
