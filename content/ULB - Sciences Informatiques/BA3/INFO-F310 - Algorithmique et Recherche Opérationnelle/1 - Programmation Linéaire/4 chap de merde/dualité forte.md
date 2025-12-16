---
title: dualité forte
authors: iamscrambledeggs
tags: []
---

# dualité forte
- si le prb primal (P) possède une solution optimale finie $x^*$
	- → alors le prb dual (D) possède une solution optimale finie $y^*$
	- + les valeurs respectives des fonctions objectif sont nécessairement égales
$$
\sum_{j=1}^n c_jx_j^* = \sum_{i=1}^m b_iy^*_i \Leftrightarrow c^Tx^* = b^Ty^*
$$
## interprétation
- combine dualité faible avec the fondamental de PL
- caractère borné de la valeur optimale de la fonction objectif du primal ou du dual
	- → existence d'une solution optimale pour le prb primal ET dual
- prop caractéristique de la PL
	- contrairement à la programmation non-linéaire
## démonstration
- considérons le primal (P) et dual (D)
- idée : suivant théorème de la dualité faible, une solution $y^*$ de (D) telle que $c^Tx^* = b^Ty^*$ implique $y^*$ solution optimale
- éléments
	- introduire variables d'écart $x_{n+1},...,x_{n+m}$ définies par
		- $\forall i = 1,...,m : x_{n+i} = b_i = \sum_{j=1}^n a_{ij}x_j$
	- base de (P) correspondant à la solution optimale $x^*$
	- vecteurs de coûts réduits $\overline{c}$ de $(x_1,...,x_{n+m})$ dans cette base
		- le vecteur $\overline{c} \leq 0$ puisque solution $x^*$ est optimale
- dans base de (P)
	- la fonction obj $z$ du primal s'écrit pour tout $x$
		- $z = \sum_{j=1}^n c_jx_j$
			- $= \sum_{j=1:n} c_j x^*_j + \sum_{j=1:n+m}\overline{c}^*_j x_j$
			- $=z^* + \sum_{j=1:n}\overline{c}^*_j x_j  + \sum_{i=1:m}\overline{c}^*_{n+i} x_{n+i}$
- poser que la solution optimale de (D) est égal (à l'opposé) de la valeur des coûts réduits de $x = (x_n,...,x_{n+m})$
	- $\forall i = 1,...,m : y_i^* = - \overline{c}^*_{n+i}$
	- → $\sum_{j=1:n} c_jx_j = z^* + \sum_{j=1:n}\overline{c}^*_jx_j - \sum_{i=1:m} y_i^*x_{n+i}$
![[./Pasted image 20251124171627.png]]
![[Pasted image 20251124171651.png]]
## autre démonstration (plus courte car why not)
- du théorème de dualité faible
- supp le primal non-borné supérieurement
	- $c^Tx \to \infty$
- si dual était réalisable
	- → alors il existerait
		- $y \in \set{y | A^Ty \geq c, y \geq 0}$
	- dans ce cas, par théorème de la dualité fiable
		- $c^Tx \leq b^Ty$
		- $b^Ty$ : brone supérieure sur la valeur de la fonction objectif du primal $c^Tx$
- → dernière affirmation impossible
