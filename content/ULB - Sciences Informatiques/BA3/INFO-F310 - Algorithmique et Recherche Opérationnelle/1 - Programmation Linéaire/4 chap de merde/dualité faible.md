---
title: dualité faible
authors: iamscrambledeggs
tags: []
---

# dualité faible
- idée : le dual fournit un moyen de déduire des limites (bornes) sur le primal

- si
	- $x$ une solution admissible (qlcq) du prb primal de maximisation
	- $y$ une solution admissible (qlcq) du prb dual
- alors
	- $c^Tx \leq b^Ty$
**bref**: tte solution admissible du prb dual correspond à une limite sup de tte solution admissible du prb primal

## preuve
- problème primal
	- $n$ var primales et $m$ contraintes ($m \lt n$)
		- $c,x \in \mathbb{R}^{n}$
		- $b \in \mathbb{R}^{m}$
		- $A \in \mathbb{R}^{m \times n}$
	- $\max c^T x$
		- $Ax \leq b$
		- $x \geq 0$
- problème dual
	- $m$ variable duales et $n$ contraintes ($m \lt n$)
		- $c \in \mathbb{R}^{n}$
		- $b,y \in \mathbb{R}^{m}$
		- $A \in \mathbb{R}^{m \times n}$
	- $\min b^T y$
		- $A^T y \geq c$
			- $y \geq 0$

- contrainte $A^Ty \geq c$ (dual)  permet d'écrire puisque $x \geq 0$
	- $A^Ty \geq c \Leftrightarrow c \leq A^Ty$
	- $c^T x \leq y^TAx$
		- base de l'inégalité de dualité faible
- contrainte $Ax \leq b$ (primal) permet d'écrire puisque $y \geq 0$
	- $y^TAx \leq y^Tb$
- → donc
	- $c^Tx \leq y^TAx \leq y^Tb = b^Ty$
		- quel que soit $y \geq 0 : A^Ty \geq c$
- → $c^Tx \leq b^Ty$

### conséquence du théorème
- pour obtenir une borne sup sur la valeur optioamle de fonction objectif du primal
	- → il suffit de connaître une solution réalisable de son dual
- si $y$ solution réalisable du dual et $x^*$ solution optimale du primal
	- alors : $c^Tx^* \leq b^Ty$
	- donc $b^Ty$ : borne sup sur la valeur optimale du primal
### problème de minimisation
- si
	- $x$ une solution réalisable/admissible du prb primal de minimisation
	- $y$ une solution réalisable/admissible du prb dual
- alors
	- → $b^Ty \leq c^Tx$
