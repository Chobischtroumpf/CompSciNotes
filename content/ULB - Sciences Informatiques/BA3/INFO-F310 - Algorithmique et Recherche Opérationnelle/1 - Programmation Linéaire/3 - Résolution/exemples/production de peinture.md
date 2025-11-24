---
title: production de peinture
authors: Mihai Bors
tags: []
---

# production de peinture
## méthode graphique avec programme linéaire
$\max z = 5x_1 + 4x_2$
1. $6x_1 + 4x_2 \leq 24$
2. $x_1 + 2x_2 \leq 6$
3. $x_2 \leq 2$
4. $x_1 + x_2 \leq 1$
5. $x_1 \geq 0$
6. $x_2 \geq 0$
![[6d9878ead273d7f1f9e76ddea82a4e60.png]]
### géométrie des solutions
- ensemble des solutions admissibles = polyèdre convexe ABCDEF non-vide
- sommets du polyèdre ABCDEF = points candidates à solution(s) optimale(s)

### recherche de la solution optimale

| point extrême sommet | coordonnées | $z = 5x_1 + 4x_2$ |
| -------------------- | ----------- | ----------------- |
| A                    | (0,0)       | 0                 |
| B                    | (0,1)       | 4                 |
| C                    | (1,2)       | 13                |
| D                    | (2,2)       | 18                |
| E                    | (3,1.5)     | 21                |
| F                    | (4,0)       | 20                |
→ solution optimale est le sommet E du polyèdre

## courbe de niveau
![[84d3fb400821e559169191dc5b4aa8bd.png]]

## méthode du simplexe
$\max z = 5x_1 + 4x_2$
1. $6x_1 + 4x_2 + s_1 = 24$
2. $x_1 + 2x_2 + s_2 = 6$
3. $x_2 + s_3 = 2$
4. $-x_1 + x_2 + s_4 = 1$
5. $x_1, x_2, s_1, s_2, s_3, s_4 \geq 0$
→ Ax = b : système de 4 équations à 6 inconnues
#### base $B = \set{s_1, s_2,s_3,s_4}$
$z = 0 + 5x_1 + 4x_2$
1. $s_1 = 24 - 6x_1 - 4x_2$
2. $s_2 = 6 - x_1 - 2x_2$
3. $s_3 = 2 - x_2$
4. $s_4 = 1 + x_1 - x_2$

→ si $x_1 = x_2 = 0$ ($x_1, x_2$ hors base) alors $s_1 = 24, s_2 = 6, s_3 = 2, s_4 = 1$
- toutes les valeurs des variables en base (ie de B) sont non-négatives
- la solution de base (0; 0; 24; 6 ; 2 ; 1) = solution de base réalisable
- correspond au sommet A du polyèdre ABCDEF
	- puisque toute solution de base réalisable correspond à un sommet du polyèdre défini par les contraintes
### algorithme du simplexe
**forme standard en rep indicielle**
vu plus haut avec système de 4 équations à 6 inconnues

 **forme standard en rep matricielle**
- $\max z = c^T x$
	- $Ax = b, x \geq 0$
$$
c = \begin{pmatrix} 5 \\ 4 \\ 0 \\ 0 \\ 0 \\ 0\end{pmatrix}, x = \begin{pmatrix} x_1 \\ x_2 \\ s_1 \\ s_2 \\ s_3 \\ s_4\end{pmatrix}, A = \begin{pmatrix} 6 & 4 & 1 & 0 & 0 & 0 \\ 1 & 2 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ -1 & 1 & 0 & 0 & 0 & 1\end{pmatrix}, b = \begin{pmatrix} 24 \\ 6 \\ 2 \\ 1 \end{pmatrix}
$$
**étape 0 : base initiale**
$z = 0 + 5x_1 + 4x_2$
1. $s_1 = 24 - 6x_1 - 4x_2$
2. $s_2 = 6 - x_1 - 2x_2$
3. $s_3 = 2 - x_2$
4. $s_4 = 1 + x_1 - x_2$

**étape 1 : sélection de la variable entrante dans la base**
- en s'orientant vers un sommet adjacent pour lequel la valeur de la fonction objectif $z$ en ce sommet est supérieure à la valeur actuelle

- si $x_1$ ou $x_2$ augmente (entre en base)
	- → alors la valeur de la fonction objectif $z$ augmente
- la fonction objectif $z$ augment plus rapidement en fonction de la variable $x_1$ que de $x_2$

**étape 2 : sélection de la variable sortante de la base**
- puisque $x_2 = 0$ (variable hors base) ET les autres variables doivent rester positives
1. $s_1 = 24 - 6x_1 - 4x_2 = 24 - 6x_1 \geq 0$
2. $s_2 = 6 - x_1 - 2x_2 = 6 - x_1 \geq 0$
3. $s_3 = 2 - x_2 = 2 \geq 0$
4. $s_4 = 1 + x_1 - x_2 = 1 + x_1 \geq 0$

Donc
1. $s_1 = 24 - 6x_1 \geq 0 \to x_1 \leq 4$
2. $s_2 = 6 - x_1 \geq 0 \to x_1 \leq 6$
3. $s_3 = 2 \geq 0 \to 2 \geq 0$
4. $s_4 = 1 + x_1 \geq 0 \to x_1 \geq -1$
- observation
	- les deux dernières inégalités sont tjr vérifiées
	- si $x_1 = 4, x_2 = 0 \to s_1 = 0$
- conséquence
	- variable $x_1$ entre en base et $s_1$ sort de la base
	- nouvelle base $B = \set{x_1, s_2, s_3, s_4}$
- _NB : les contraintes de non-négativité guident le choix de la variable sortante_

**étape 3 : pivotage**
- de l'étape 1 : la variable $x_1$ entre dans la base
- de l'étape 2 : la variable $s_1$ sort de la base
- → expression déduite de la base initiale
	- $s_1 = 24 - 6x_1 - 4x_2$
	- $x_1 = 4 - \frac{1}{6}s_1 - \frac{2}{3}x_2$
donc nous obtenons le nouveau système
1. $z = 20 - \frac{5}{6}s_1 + \frac{2}{3}x_2$
2. $x_1 = 4 - \frac{1}{6}s_1 - \frac{2}{3}x_2$
3. $s_2 = 2 + \frac{1}{6}s_1 - \frac{4}{3}x_2$
4. $s_3 = 2 - x_2$
5. $s_4 = 5 - \frac{1}{6}s_1 - \frac{5}{3}x_2$

**structure en tableau**

| B(ase) | $z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | solution |
| ------ | --- | ----- | ----- | ----- | ----- | ----- | ----- | -------- |
| $z$    | -1  | 5     | 4     | 0     | 0     | 0     | 0     | 0        |
| $s_1$  | 0   | 6     | 4     | 1     | 0     | 0     | 0     | 24       |
| $s_2$  | 0   | 1     | 2     | 0     | 1     | 0     | 0     | 6        |
| $s_3$  | 0   | 0     | 1     | 0     | 0     | 1     | 0     | 2        |
| $s_4$  | 0   | -1    | 1     | 0     | 0     | 0     | 1     | 1        |
- $c_1 = \max_{k=1,2}\set{c_k|c_k \gt 0} = 5$
	- → $x_1$ entre dans la base
- $i  = 1 : \max_{1 \leq k \leq m=4}\set{\frac{b_k}{a_{k,j=1}}|a_{i,j=1}\gt 0}$

**étape 3**

| B(ase) | $z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | solution |
| ------ | --- | ----- | ----- | ----- | ----- | ----- | ----- | -------- |
| $z$    | -1  | 5     | 4     | 0     | 0     | 0     | 0     | 20       |
| $x_1$  | 0   | 1     | 2/3   | 1/6   | 0     | 0     | 0     | 4        |
| $s_2$  | 0   | 0     | 2     | 0     | 1     | 0     | 0     | 6        |
| $s_3$  | 0   | 0     | 1     | 0     | 0     | 1     | 0     | 2        |
