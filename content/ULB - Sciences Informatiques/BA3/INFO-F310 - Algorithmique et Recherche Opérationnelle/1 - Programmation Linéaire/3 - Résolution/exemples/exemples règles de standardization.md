# (P) PL
- $\min z = x_1 + x_2 + x_3$
	- $x_1 + 2x_2 + x_3 \geq 110$
	- $x_1 + 3x_2 + 2x_3 = 140$
	- $x_1 + x_2 + 4x_3 = 180$
	- $x_1,x_2,x_3 \geq 0$

## étape 1
- introduction de la var de surplus $s_1 \geq 0$ pour la contrainte ("$\geq$")
- $\min z = x_1 + x_2 + x_3$
	- $x_1 + 2x_2 + x_3 - s_1 = 110$
	- $x_1 + 3x_2 + 2x_3 = 140$
	- $x_1 + x_2 + 4x_3 = 180$
	- $x_1,x_2,x_3,x_1 \geq 0$

- lors de la première itération de la méthode du Simplexe
	- les var $x_1,x_2,x_3$ ne sont pas en base
		- $x_1 = 0, x_2 = 0, x_3 = 0$
	- → la variable de surplus $s_1 = -110$
		- ne satisfait pas la condition de non-négativité
	- → nécessaire d'ajouter dans la contrainte correspondante un var artificielle $R_1 \geq 0$
		- avec un coef nul dans la fonction objectif
- → la première contrainte est modifiée comme suit
	- $x_1 + 2x_3 + x_3 - s_1 = 110$
	- → $x_1 + 2x_2 + x_3 - s_1 + R_1 = 110$

## étape 2
 - pour les deux autres contraintes d'égalité "="
	 - également nécessaire d'ajouter les var artificielles

- $R_2 \geq 0$ à la 2e contrainte
	- pour éviter la contradiction $0 = 140$ lorsque $x_1 = x_2 = x_3 = 0$
- $R_3 \geq 0$ à la 3e contrainte
	- pour éviter la contradiction $0 = 180$ lorsque $x_1 = x_2 = x_3 = 0$
- → leur coeff respectif sera nul dans la fonction objectif

- donc
	- $x_1 + 3x_2 + 2x_3 = 140 →x_1 + 3x_2 + 2x_3 + R_2 = 140$
	- $x_1 + x_2 + 4x_3 = 180 → x_1 + x_2 + 4x_3 + R_3 = 180$

## étape 3
- $R_1, R_2, R_3$ doivent être éliminées de la base initiale pour prendre une valeur nulle dans la solution obtenue à la terminaison de la phase I

1. remplacer la fontion objectif $z$ par la fonction objectif $r = R_1  + R_2 + R_3$

- $\min r = R_1 + R_2 + R_3$
	- $x_1 + 2x_2 + x_3 - s_1 + R_1 = 110$
	- $x_1 + 3x_2 + 2x_3 + R_2 = 140$
	- $x_1 + x_2 + 4x_3 + R_3 = 180$
	- $x_1,x_2,x_3, s_1, R_1,R_2,R_3 \geq 0$

2. exprimer $r$ en fonction des var hors base $\set{x_1,x_2,x_3,s_1}$
$$
\begin{cases} x_1 + 2x_2 + x_3 - s_1 + R_1 = 110 \Leftrightarrow R_1 = 110-x_1 - 2x_2 -x_3 + s_1 \\ x_1 + 3x_2 + 2x_3 + R_2 = 140 \Leftrightarrow R_2 = 140 - x_1 - 3x_2 - 2x_3 \\ x_1 + x_2 + 4x_3 + R_3 = 180 \Leftrightarrow R_3 = 180 - x_1 - x_2 - 4x-3 \end{cases}
$$

3. Résoudre le problème auxiliare (Pa) par la méthode de la Phase II

- $\min r = 430 - 3x_1 - 6x_2 - 7x_3 + s_1$
	- $s_1 + 2x_2 + x_3 - s_1 + R_1 = 110$
	- $x_1 + 3x_2 + 2x_3 + R_2 = 140$
	- $x_1 + x_2 + 4x_3 + R_3 = 180$
	- $x_1,x_2,x_3,s_1,R_1,R_2,R_3 \geq 0$

**base initiale du Pa**
$B = \set{R_1,R_2,R_3}$ et tableau initial

| var en base | r   | $x_1$ | $x_2$ | $x_3$ | $s_1$ | $R_1$ | $R_2$ | $R_3$ | solution |
| ----------- | --- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | -------- |
| $r$         | 1   | -3    | -6    | -7    | 1     | 0     | 0     | 0     | 430      |
| $R_1$       | 0   | 1     | 2     | 1     | -1    | 1     | 0     | 0     | 110      |
| $R_2$       | 0   | 1     | 3     | 2     | 0     | 0     | 1     | 0     | 140      |
| $R_3$       | 0   | 1     | 1     | 4     | 0     | 0     | 0     | 1     | 180      |
- la résolution de ce Pa donne la solution de base initiale qui est admissible pour P
	- $x_1 = 75, x_2 = 5, x_3 = 25$