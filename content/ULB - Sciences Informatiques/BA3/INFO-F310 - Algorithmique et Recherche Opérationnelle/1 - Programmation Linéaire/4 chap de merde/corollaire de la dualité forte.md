---
title: corollaire de la dualité forte
authors: iamscrambledeggs
tags: []
---

# corollaire
- si $c^Tx = b^Ty$
	- alors $x$ est une solution optimale du prb primal
		- et $y$ est une solution optimale du prb dual
## preuve
par contradiction
- supp que $x$ ne soit pas la solution maximale pour le primal
	- alors il existe solution $\tilde{x}$ du primal : $c^Tx \lt c^T \tilde{x}$
- si $y$ est une solution du dual
	- par la base de l'inégalité de dualité faible :
		- →$c^T \tilde{x} \leq b^Ty$
- comme $c^Tx = b^Ty$, impossible de vérifier l'inégalité stricte
	- $c^T\tilde{x} \leq b^Ty (= c^Tx) \lt c^T \tilde{x}$
