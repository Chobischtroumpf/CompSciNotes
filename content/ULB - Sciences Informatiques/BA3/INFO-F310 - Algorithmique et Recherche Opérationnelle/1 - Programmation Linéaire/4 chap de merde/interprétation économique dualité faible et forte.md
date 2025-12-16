---
title: interprétation économique dualité faible et forte
authors: iamscrambledeggs
tags: []
---

# interprétation économique
- de la dualité faible
	- $z \leq w$ : profit $\leq$ valeur des ressources
- de la dualité forte
	- profit max est atteint si les ressources ont été exploitées complètement
		- juqu'à épuisement de leur valeur

## exemple
- problème primal
	- $\max z = 5x_1 + 4x_2$
		- $6x_1 + 4x_2 \leq 24$
		- $x_1 + 2x_2 \leq 6$
		- $x_2 \leq 2$
		- $-x_1 + x_2 \leq 1$
		- $x_1,x_2 \geq 0$
	- solution optimale $x_1 = 3, x_2 = 1.5$ → profit $z = 21$
- problème dual
	- $\min w = 24y_1 + 6y_2 + 2y_3 + y_4$
		- $6y_1 + y_2 - y_4 \geq 5$
		- $4y_1 + 2y_2 + y_3 + y_4 \geq 4$
		- $y_1,y_2,y_3,y_4 \geq 0$
	- solution optimale $y=0.75, y_2 = 0.5, y_3 = 0, y_4 = 0$ → valeur $w= 21$
- interprétation du dual
	- profit augmente de $0.75$ par augmentation d'une tonne de $M_1$
	- profit augmente de 0.5 par augmentation d'une tonne de $M_2$
	- ressources 3,4 abondantes → augmenter ces ressources n'apporte aucun profit supplémentaire
- → solution optimale du dual égale (au signe près) la valeur optimale des coûts réduits du primal
