---
title: exemple base dégénérée
authors: Mihai Bors
tags: []
---

# base dégénérée
- contraintes redondantes
	- $\max z = 3x_1 + 9x_2$
		- $x_1 + 4x_2 \leq 8$
		- $x_1 + 2x_2 \leq 4$
		- $x_1,x_2 \geq 0$
→ choix de la variable sortante :
- $\arg \min_{j \in \set{1,2}}\set{\frac{\overline{b}_j}{\overline{a}_{jk}}|\overline{a}_{jk} \gt 0}$
	- $= \arg\min_{j \in \set{1,2}}\set{\frac{8}{4},\frac{4}{2}}$
- → plusieurs choix possibles pour la variante
![[9286f0643a5a80c4656e6cf3843b0870.png]]
