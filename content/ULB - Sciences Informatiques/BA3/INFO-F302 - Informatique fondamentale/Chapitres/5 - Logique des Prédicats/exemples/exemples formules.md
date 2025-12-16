---
title: exemples formules
authors: Mihai Bors
tags: []
---

# exemples de formules
- $\forall x, p(x,x)$
	- quelque soit le domaine d'interprétation de cette formule, elle sera vraie dès lors que $p$ nest interprétée par une relation binaire réflexise
	- $p(x,x) \Leftrightarrow (x,x) \in p$
- $\forall x \forall y, p(x,y) \to p(y,x)$
	- vraie dès lors que $p$ est interprétée par une relation symétrique
- $\forall x \forall y, f(x) = f(y) \to x = y$
	- vraie dès lors que $f$ est interprétée par une fonction injectie
- $\forall x, [(p(x) \to \neg p(S(x)) \land (\neg p(x) \to p(S(x)))]$
	- vraie _ex1_ : dans $\mathbb{N}$ où on interpète $p$ par "être pair" et S par la fonction qui retourne $n+1$ pour tout $n$
	- vraie _ex2_ : dans {0,1} où on interprète p par "être pair" et S par la fonction
		- $0 \mapsto 1$
		- $1 \mapsto 0$
- $\exists x \forall y, \neg(S(y) = x)$
	- vraie _ex1_ : dans $\mathbb{N}$ où $S$ est interprétée par la fonction $n \in \mathbb{B} \mapsto n+1$
		- en prenant $x = 0$
	- faux _ex1_ : dans $\mathbb{Z}$ où $S$ est la fonction $n \in \mathbb{Z} \mapsto n+1$
- $\forall y, \neg (S(y) = c)$
	- $c$ : symbole de constrante, doit être interprété par un élément du domaine
	- vraie dans $\mathbb{N}$ avec $c$ interprétée par $0$ et $S$ par $n \mapsto n+1$
- $\forall x \forall y, [f(x,y) = f(y,x) \land f(x,S(y)) = S(f(x,y)) \land f(x,c) = x]$
	- vraie dans $\mathbb{N}$ avec
		- _ex1_
			- c = 0
			- f : +
			- s : + 1
		- _ex2_
			- c = 1
			- f : $\times$
			- s: $\times 2$ (ou tout multiple)
