---
title: interprétation partielle
authors: Alessandro Dorigo
tags:
  - InfoFond
---

# interprétation partielle
> [!info] Définition
> - interprétation partielle = assignement
	>>- noté $x/1, x/0$
	>>- signifie qu'on assigne la valeur 1 ou 0 à $x$

## simplification sous une interprétation partielle
- Etant donnée une clause $C$ et une interprétation partielle $x/b$
	- $b \in \set{0,1}$
	- la formule $C[x/b]$ est obtenue selon
		- si $C$ ne contient pas $x$ ou $\neg x$ → $C[x/b] = C$
		- sinon si $C$ ne contient que $x$ ou que $\neg x$ → on considère les cas suivants
			- $C = x, b = 1 → C[x/b] = \top$
			- $C = x, b = 0 → C[x/b] = \bot$
			- $C = \neg x, b = 0 → C[x/b] = \top$
			- $C = \neg x, b = 1 → C[x/b] = \bot$
		- sinon si $C$ contient $x, b =1$ ou $C$ contient $neg x, b = 0$ → $C[x/b] = \top$
		- sinon, on retire &de $C$ les occurences de $x$ ou de $\neg x$
	- Si $\phi = \wedge_{i=1}^n$ est une conjonction de clauses
		- alors
			- $\phi[x/b] = \bot$
				- s'il existe une clause $C_i$ telle que $C_i$ telle que $C_i[x/n] = \bot$
			- sinon $\phi[x/b] = \wedge_{i : C_i[x/nb] \neq \top}C_i[x/b]$
	- Si toutes les clauses se simplifient en $\top$ → $\phi[x/b] = \top$
**exemple**
$a = x \vee y \vee z, b = x \vee \neg y \vee \neg z$
- $a[x/1] = \top, b[x/1] = \top, (a \wedge b)[x/1] = \top$
- $b[y/1] = x \vee \neg z$
- $b[z/1] = x \vee \neg z$
- $a[x/0] = y \vee z$
- $b[x / 0] = \neg y \vee \neg z$
- $(a \wedge b)[x/0] = (y \vee z) \wedge(\neg y \vee \neg z)$
- $(a \wedge b)[x/0][y/0] = z$
- $(a\wedge b) [x/0][y/0][z/1] = \top$
