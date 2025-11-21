# problème de maximisation non-borné supérieurement
- $\max z = x_1 + 2x_2$ 
	- $x_1 - x_2 \leq 1$ 
	- $x_1 \leq 2$
	- $x_1,x_2 \geq 0$ 
- → $\max z = x_1 + 2x_2$
	- $x_1 - x_2 + s_1 = 1$ 
	- $x_1 + s_2 = 2$
	- $x_1, x_2, s_1, s_2 \geq 0$ 

| var en base | z   | $x_1$ | $x_2$ | $s_1$ | $s_2$ | solution |
| ----------- | --- | ----- | ----- | ----- | ----- | -------- |
| $z$         | -1  | 1     | 2     | 0     | 0     | 0        |
| $s_1$       | 0   | 1     | -1    | 1     | 0     | 1        |
| $s_2$       | 0   | 1     | 0     | 0     | 1     | 2        |
- tous les coefficients (sauf le profit marginal) dans la colonne $x_2$ sont négatifs ou nuls
	- → critère du quotient ne s'applique pas 
- toutes les contraintes de non-négativité son satisfaites
	- quelle que soit la valeur de $x_2$ 
- valeur de la fonvtion objectif peut donc augmenter indéfiniment

_NB : si prb de minimisation non borné inférieurrement, pas de solution optimale_

# problème non-borné
- $\max z = x_1 + 2x_2$ 
	- $-2x_1 + 6x_2 \leq 6$
	- $x_1 \geq 1$
	- $x_1,x_2 \geq 0$ 
- → polyèdre non borné n'implique pas nécessairement pas que le prb soit borné 
	- nécessaire de vérifier  que la valeur de la fonction objectif est non bornée
- → $\min z = x_1 + 2x_2$ 
	- $-2x_1 + 6x_2 \leq 6$ 
	- $x_1 \geq 1$ 
	- $x_1,x_2 \geq 0$ 