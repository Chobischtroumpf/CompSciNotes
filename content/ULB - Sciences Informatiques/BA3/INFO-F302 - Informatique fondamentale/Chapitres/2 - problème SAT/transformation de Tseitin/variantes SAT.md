---
title: variantes SAT
authors: Alessandro Dorigo
tags:
  - InfoFond
---

# 2SAT
- 2-SAT : les clauses ne contiennent qu'au plus deux littéraux
	- _ex: $(x_1 \vee \neg x_2) \wedge x_3 \wedge (x_4 \vee \neg x_1)$_
	- solvable en temps polynomial
		- 3-SAT est NP complet
# QSAT
- QSAT : décider la satisfaisabilité de formules de la forme
	- $\forall x_1 \exists q_1 \forall x_2 \exists q_2 ... \forall x_n \exists q_n \phi$
		- $\phi$ : formule en FNC construite sur les prop $x_1,q_1,...,x_n, q_n$
	- PSPACE-complet
		- peut être résolu en espace polynomial
		- tous les problèmes pouvant être résolus en espace polynomial peuvent se réduire au problème QSAT en temps poly
		- ie. QSAT est aussi difficile que tous les problèmes pouvant être résolu en espace poly
# WEIGHTED-MAX-SAT
- WEIGHTED-MAX-SAT : on attribue des poids à chaque clause, on se donne un entier $r$, et on veut savoir si on peut satisfaire un ensemble de clauses dont la somme des poids est au moins $r$
	- _ex  $x \wedge y \wedge (\neg x \vee \neg y)$ avec poids(x) = 1, poids(y) = 1 et poids($\neg x \vee \neg y$)_
		- avec $V(x) = 1,  V(y) = 1$, on ne satisfait pas la dernière clause → poids total $=2$
		- en mettant $V(x) = 1, V(y) = 0$, on satisfait al première et dernière clause → poids total $1 + 2 = 3$
## MAX-SAT
- MAX-SAT : étant donnée une formule $\phi$ en FNC et un entier $k \in N$, peut-on satisfaire au moins $k$ clauses ?
	- _ex. $x \wedge y \wedge (\neg x \vee \neg y)$ - on peut satisfaire au plus deux clauses
