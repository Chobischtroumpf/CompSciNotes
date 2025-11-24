---
title: méthode du simplexe
authors: iamscrambledeggs
tags: []
---

# méthode du simplexe

- résumé des théorèmes que nous avons besoin
	- théorème fondamental de programmation linéiare
		- suffisant de considérer uniquement les solutions de base réalisable dans la recherche d'une solution réalisable optimale
	- théorème de l'alternative
		- critère de terminaison et prévoir un double certificat pour qu'une solution de base réalisable soit optimale
			- certificat = démarche pourquoi un système linéaire est faisable ou infaisable

- idée fondamentale
	- se déplacer d'une solution de base réalisable (ie. un point extrême du polyèdre) de l'ensemble de contraintes à un autre  problème de PL (**sous forme standard**)
	- se déplacer de manière à améliorer cntinuellement la valeur de la fonction objectif jusqu'à ce qu'une solution réalisable optimale soit atteinte

- principe
	- se déplacer de sommet en sommet adjacent (solution de base réalisable adjacente ou voisine) de manière à améliorer la valeur de l'objectif
- → fournit une méthode efficace pour passer des solutions de base réalisables à la solution optimale

## solutions de base réalisables adjacentes
- idée : considérer deux solution de base dont les variables de base sont les mêmes sauf une qui est en base dans la première et hors base dans la seconde
- définition
	- deux solutions de base réalisables sont dites adjacentes si elles ne diffèrent que d'une (seule) variable en base
	- → puisque toute solution de base réalisable correspond à un sommet du polyèdre
	- → deux sommets du polyèdre sont dits adjacents si les variables en base ne diffèrent que d'un seul élément

**implications**
- + : génération d'une nouvelle solution de base àpd une ancienne en remplaçant une variable en base par une variable hors base
- - : impossible de spécifier arbitrairement/simultanément la paire de variables dont les rôles doivent être intervertis tout en maintenant la condition de non-négativité
	- spécifier quelle variable hors base doit devenir variable en base
	- déterminer quelle variable en base devrait devenir hors base
	- → dès qu'une variable hors base est sélectionnée comme variable entrante, il reste à sélectionner la variable en base sortant (pour maintenir la faisabilité du modèle)

## algorithme du simplexe
- principe
	- apd solution de base réalisable (tq ttes variables ont valeurs non-négatives)
	- passer par changement d'une variable en base (pour cette solution) à une solution de base adjacente qui améliore la valeur de l'objectif

- trois étapes
	- déterminer la variable entrante $\equiv$ variable entrant dans la base
		- variable hors base → variable en base
	- déterminer la variable sortant $\equiv$ variable sortant de la base
		- variable en base → variable hors base
	- pivotage vers une solution de base adjacente admissible

**règle**
- pour un problème de maximization
	- choisir comme indice $j \in \set{1,...,n}$ de la variable $x_j$ celui qui augmente le plus rapidement de $z$
- pour un problème de minimization
	- l'inverse de ce qui a été cité plus haut

### tableau indiciel
- procédure
	0. former tableau initial
	1. choix de la colonne $j$ du pivot
	2. choix de la ligne $i$ du pivot
	3. pivotage
		1. procédure d'élimination autour du pivot situé à l'intersection de la ligne $i$ et de la colonne $j$
			1. méthode Gauss-Jordan
		2. diviser la ligne $i$ par le pivot (ainsi déterminé) pour le mettre égal à 1
- Soit le système de contraintes (sous forme canonique) $\set{Ax\leq b | x \geq 0}$
	- $A \in \mathbb{R}^{m\times n}$
	- $x \in \mathbb{R}^n$
	- $b \geq 0, b \in \mathbb{R}^m$
- et le problème
	- $\max z = \sum_{j=1}^n c_jx_j$

**étape 0**
- reformulation sous forme standard
	- parmi $n+m$ variables
		- $n$ var $\set{x_1,...,x_n}$ hors-base
		- $m$ var $\set{x_{n+1} = s_1,..., x_{n+m} = s_m}$ en base
	- choix toujours possible si $b \geq 0, (b_i \geq 0, i = 1,...m)$
- → si $b \geq 0$, point de départ
	- base initial consistuée des variables d'écart
		- $\set{x_{n+1}=s_1,...,x_{n+m} = s_m}$
	- solution de base admissible
		- $(x_1=0,...,x_n = 0, s_1,...,s_m)$
	- puisque $c^Tx + (-1)z = 0$ donc coefficient = -1

| B(ase)          | $z$ | $x_1$    | $x_2$    | ... | $x_n$    | $s_1$ | $s_2$ | ... | $s_m$ | solution |
| --------------- | --- | -------- | -------- | --- | -------- | ----- | ----- | --- | ----- | -------- |
| $z$             | -1  | $c_1$    | $c_2$    | ... | $c_n$    | 0     | 0     | ... | 0     | 0        |
| $x_{n+1} = s_1$ | 0   | $a_{11}$ | $a_{12}$ | ... | $a_{1n}$ | 1     | 0     | ... | 0     | $b_1$    |
| $x_{n+2} = s_2$ | 0   | $a_{21}$ | $a_{22}$ | ... | $a_{2n}$ | 0     | 1     | ... | 0     | $b_2$    |
| ...             | ... | ...      | ...      | ... | ....     | ....  | ...   | ... | ...   | ...      |
| $x_{n+m} = s_m$ | 0   | $a_{m1}$ | $a_{m2}$ | ... | $a_{mn}$ | 0     | 0     | ... | 1     | $b_m$    |


**étape 1**
- choix de la colonne du pivot $j$
	- $c_k$ : coefficient des vairbales (hors base) dans la fonciton objectif $z$
		- max : $c_j = \max_{1\leq k \leq n}\set{c_k | c_k \gt 0}$
		- min : $c_j =\min_{1 \leq k \leq n}\set{c_k | c_k \lt 0}$
	- → si aucun choix $j$ possible
		- solution optimale attenite et l'algorithme se termine
**étape 2**
- choix de la ligne du pivot
	- soit indice de la colonne $j$ du pivot obtenu à l'étape 1
	- si $a_{kj} \leq 0, \forall k = \set{1,...,m}$ alors problème non-borné
	- sinon indice de la ligne $i$ du pivot est celui varifiant le critère du quotient
		- $\frac{b_i}{a_{ij}} = \min_{1\leq k \leq m}\set{\frac{b_k}{a_{kj}}|a_{ij}\gt 0}$
		- → assure l'admissibilité de la nouvelle solution de base
- _notes_
	- _Si $a_{kj}\leq 0, \forall k$, alors on peut augmenter $x_k$ indéfiniment, la non-négativité du vecteur de variable de base $x_B$ est toujours satisfaite_
	- → problème non borné

**étape 3**
- pivotage
	- appliquer une procédure délimination autour du pivot situé à l'intersection de la ligne $i$ et de la colonne $j$
	- diviser la ligne $i$ par le pivot pour le mettre égal à 1
→ et puis on recommence jusqu'à qu'on ne puisse plus
### représentation matricielle
- Soit le système de contraintes (sous forme standard) $\set{Ax\leq b | x \geq 0}$ avec dictionnaire
	- $A \in \mathbb{R}^{m\times n}$
	- $x \in \mathbb{R}^n$
	- $b \geq 0, b \in \mathbb{R}^m$
- et le problème
	- $\max z = \sum_{j=1}^n c_jx_j$
 **dictionnaire**
 - sys d'équations linéaires liant $x_1,...,x_m,x_{m+1}, ..., x_{m+((n-m)-1)}, x_n$ et $z$
	 - satisfant prop 1, 2
1. les équations consistuant un dico doivent exprimer
	1. $z$ et les $m$ variables en fonctions des $n-m$ aurtes variables hors-base
2. tout dico est algébriquement équivalent au dico définissant les variables d'écart et la fonction objectif
$$
\begin{cases}\tilde{x_i} = b_i - \sum_{j=1}^n a_{ij}x_j,\text{ pour } i = 1,...,m \\ z = \sum_{j=1}^n c_j x_j\end{cases}
$$
→ _solution réalisable exprimée à l'aide d'un dictionnaire = solution de base réalisable_

**initialisation**
 - soit
	 - B = indices des var en base
	 - N = indices des var hors base
- décomposition des données et variables (réarrangeant ordre des var)
	- $A = ( A_B A_N), A_B \in \mathbb{R}^{m\times m}, A_N \in \mathbb{R}^{m\times (n-m)}$
	- $c = \begin{pmatrix} c_B \\ c_N \end{pmatrix}, C_B \in \mathbb{R}^{m}, c_N \in \mathbb{R}^{n-m}$
	- $x = \begin{pmatrix} x_B \\ x_N \end{pmatrix}, x_B \in \mathbb{R}^{m},x_N \in \mathbb{R}^{n-m}$
		- $x_B$ : vecteur des var en base
		- $x_N$ : vecteur des var hors-base

**relations**
- si $A_B \in \mathbb{R}^{m\times m}$ inversible
	- $Ax = b \Leftrightarrow A_Bx_B + A_bx_N = b$
		- $\Leftrightarrow x_B + A_b^{-1}A_Nx_N = A_B^{-1}b$
		- $\Leftrightarrow x_B = A_B^{-1}b - A_B^{-1}A_Nx_N$
			- équation 13
	- → permet d'éliminer $x_B$ de l'expression de $z$
	- → expression de $z$ en fonction des variables hors-base ($x_N$ uniquement)
- $z = c^T x \Leftrightarrow  c_B^T x_B + c_N^T x_N$
	- $\Leftrightarrow c^R_B(A_B^{-1}b - A_B^{-1}A_Nx_N)+c_N^Tx_N$
	- $\Leftrightarrow c_B^TA_B^{-1}b + \underbrace{(c_N^T - c_B^TA_B^{-1}A_N)}_{\text{profits marginaux ou coûts réduits}}x_N$
		- équation 14

- _notes_
	- coûts réduits d'une var en base est 0
	- couts réduits $\overline{c} := c^T_N - c_B^TA_B^{-1}A_N$
		- → coefficients des variables hors-base $x_N$

donc on obtient avec équations 13,14
- $Ax = b \Leftrightarrow x_B = A_B^{-1}b - A_B^{-1}A_Nx_N$
- $z = c^T x \Leftrightarrow  c_B^TA_B^{-1}b + (c_N^T - c_B^TA_B^{-1}A_N)x_N$

- pour une solution de base réalisable $\overline{x} = (\overline{x_B}, \overline{x_N})$
	-  $\overline{x_B} = A_B^{-1}b - A_B^{-1}A_N\overline{x_N}$
	- $c^T\overline{x}= c_B^TA_B^{-1}b + (c_N^T - c_B^TA_B^{-1}A_N)\overline{x_N}$
		- équation 15
- → puisque $\overline{x_N} = 0$
	- $\overline{x_B} = A_B^{-1}b$
	- $c^T\overline{x} = c_B^T\overline{x}_B^T + c_N^T\overline{x}_B^T = c_B^T\overline{x}_B^T$
		- équation 16
- finalement on a
	- $\overline{x}_B = A_B^{-1}b → \overline{x}_B$
	- $c_B^T\overline{x}_B = c_B^TA_B^{-1}b → \overline{z}$
		- équation 17
- en substituant  17 en partant de 13,14
	- $z = c_B^Tx_B + c_N^Tx_N$
		- $= c_B^TA_B^{-1}b + (c_N^T - c_B^T - c_B^TA_B^{-1}A_N)x_N$
		- $= c_B^TA_B^{-1}b + \overline{c}_N^Tx_N$
		- $= \overline{z} + \sum_{k \in N}\overline{c}_k x_k$
			- équation 18
	- $x_B = A_B^{-1}b - A_B^{-1}A_Nx_N$
		- $= \overline{x}_B - A_B^{-1}A_Nx_N$
		- $\Leftrightarrow x_l = \overline{b}_l - \sum_{k \in N}\overline{a}_{lk}x_k, \forall l \in B$
			- équation 19
résumé :

| var. en base | z   | x                                   | solution          |
| ------------ | --- | ----------------------------------- | ----------------- |
| $z$          | -1  | $c^T - c_B^TA_B^{-1}A=\overline{c}$ | $-c_B^TA_B^{-1}b$ |
| $x_B$        | 0   | $A_B^{-1}A = \overline{a}$          | $A_B^{-1}b$       |

**étape 1 : sélection de la variable entrante**
 - si $\forall k \in N$, profits marginaux $\overline{c}_k \leq 0$ (pour $\max z$) ou coût réduit $\overline{c}_k \geq 0$
	 - → impossible d'augmenter ou de diminuer la fonction objectif
	- solution de base réalisable optimale
- sinon choisir la variable hors base d'indice $k$ (variable entrante)
	- de profit marginal maximum : $k= \arg\max_{i\in N} \overline{c}_i$
	- de coût réduit minimum : $k = \arg\max_{i \in N}\overline{c}_i$
		- équation 20 ^b08bfc

**étape 2 : sélection de la variable sortante**
- si pour tout $l \in B, \overline{a}_{lk} \leq 0$
	- → on peut augmenter $x_k$ indéfiniment
		- problème non borné
- sinon choisir variable en base d'indice $l$
	- $l = \arg\min_{j\in B}\set{\frac{\over{b}_j}{\overline{a}_{jk}}|\overline{a}_{jk}\gt 0}$
		- équation 21 ^c9b20d
	- contrainte de non-négativité du vecteur $x_B$ satisfaite

**étape 3 : pivotage**
- les nouvelles valeurs des coefficients sont obtenues suivant ces règles
$$
\overline{a}'_{ij} = \begin{cases} \frac{\overline{a}_{lj}}{\overline{a}_{lk}}, i = l\\ \overline{a}_{ij} - \overline{a}_{ik}\frac{\overline{a}_{lj}}{\overline{a}_{lk}}, i \neq l \end{cases}
$$
$$
\overline{b}'_i = \begin{cases}\frac{\overline{b}_l}{\overline{a}_{lk}}, i = l \\ \overline{b}_i - \overline{a}_{ik}\frac{\overline{b}_l}{\overline{a}_{lk}}, i \neq l \end{cases}
$$
- _notes_
	- $\overline{a}_{lk}$ : valeur du pivot
	- $\overline{c}_k$ : coefficient de la variable entrante d'indice $k$
	- mÀj
		- $\overline{c}'_j = \overline{c}_j - \overline{c}_k \frac{\overline{a}_{lj}}{\overline{a}_{lk}}, j \neq k$
		- $\overline{c}'_j = \overline{c}'_j = \overline{c}_k - \overline{c}_k \frac{\overline{a}_{lk}}{\overline{a}_{lk}} = 0, j = k$

### théorème fondamental de l'algo du simplexe
 - si on peut déterminer
	 - variable entrante d'indice $k$ vérifiant
		 - [[#^b08bfc|équation 20]]
	- variable sortante d'indice $l$ vérifiant
		- [[#^c9b20d|équation 21]]
- alors
	- la nouvelle base $B'$ obtenue par pivot = base réalisable et inversible
		- $(A_{B'}^{-1})$
	- la nouvelle solution de base réalisable $x_B'$ est telle que
		- $z_B' \geq z_B$ (max z)
		- ou $z_B' \leq z_B$ (min z)
	- si $B'$ est telle que $A_{B'}^{-1}b$ ne possède aucune composante non nulle
		- $z_B' \gt z_B$ (max z)
		- ou $z_B' \lt z_B$ (min z)
### tableau synthétique
te fous pas de ma gueule c'est la même chose que le tableau indiciel
