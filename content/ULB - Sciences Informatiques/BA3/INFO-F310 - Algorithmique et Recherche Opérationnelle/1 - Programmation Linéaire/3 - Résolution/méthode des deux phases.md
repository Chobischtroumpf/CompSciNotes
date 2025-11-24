---
title: méthode des deux phases
authors: iamscrambledeggs
tags: []
---

- cas problématique
	- solution de base admissible pas toujours connue a priori
	- certains prb n'admettent pas de solution admissible
		- → impossible de trouver une base de départ
- → algorithme du simplexe ne peut être appliqué directement

- idée générale
	- utiliser une première étape d'initialisation (phase 1)
	- algorithme du simplexe (phase 2)
	- permet de déterminer une base admissible ou prouver que le problème impossible à résoudre
		- faire apparaître une matrice identité
		- introduction de variables artificielles (ou var auxiliaires)
#### exemple
considérons le problème de PL
- $\min z = 4x_1 + x_2$
	- $3x_1 + x_2 = 3$
	- $4x_1 + 3x_2 \geq 6$
	- $x_1 + 2x_2 \leq 4$
	- $x_1,x_2 \geq 0$
- introduction des variables $x_3,x_4 \geq 0$
	- $3x_1 + x_2 = 3$
	- $4x_1 + 3x_2 - x_3 = 6$
	- $x_1 + 2x_2 + x_4 = 4$
	- $x_1,x_2,x_3,x_4 \geq 0$
- → pas de base admissible "triviale"

- introduction des var artificielles :$R_1,R_2$
	- $\min z = 4x_1 + x_2$
	- $3x_1 + x_2 + R_1 = 3$
	- $4x_1 + 3x_2 + R_2 - x_3 = 6$
	- $x_1 + 2x_2 + x_4 = 4$
	- $x_1,x_2,R_1,R_2,x_3,x_4 \geq 0$
	- → $R_1, R_2, x_4$ utilisées comme base de départ admissible
- → obtenir une solution de base réalisable initiale pour le problème (P)
	- procédure : éliminer var $R_1,R_2$ de l'ensemble des var de base
		- tq $R_1 = R_2 = 0$ (var hors base)

**étape 1**
- remplacer la fonction objectif $z$ par la ffonction objectif $r$ définie comme la somme des var artificielles $R_1, R_2$

- $\min r = R_1 + R_2$
	- $3x_1 + x_2 + R_1 = 3$
	- $4x_1 + 3x_2 + R_2 - x_3 = 6$
	- $x_1 + 2x_2 + x_4 = 4$
	- $x_1,x_2, R_1,R_2,x_3,x_4 \geq 0$

**étape 2**
- exprimer la fonction objectif $r$ en fonction des var hors base $\set{x_1,x_2,x_3}$

- $3x_1 + x_2 + R_1 = 3 \Leftrightarrow R_1 = 3 - 3x_1 - x_2$
- $4x_1 + 3x_2 - x_3 + R_2 = 6 \Leftrightarrow R_2 = 6-4x_1 -3x_2 + x_3$

**problème auxiliaire (Pa)**
- $\min r = -7x_1 - 4x_2 + x_3 + 9$
	- $3x_1 + x_2 + R_1 = 3$
	- $4x_1 + 3x_2 - x_3 + R_2 = 6$
	- $x_1 + 2x_2 + x_4 = 4$
	- $x_1,x_2,x_3, R_1,R_2,x_4 \geq 0$

- ensuite résoudre (Pa) par la méthode de la **Phase II** (sortir de la base toutes les var artificielles)
	- si la valeur de la fonction obj du (Pa) est strictement positive
		- → alors l'ensemble des solutions admissibles pour (P) est vide : STOP
	- sinon (le prb est consistant) : on obtient une base admissible pour (Pa) où les var artificielles sont hors-base et cette base admissible l'est également pour (P)
## résumé
- la résolution du prb auxiliaire (Pa) permet soit
	- de montrer que le modèle (P) ne possède aucune solution admissible
	- de trouver une solution de base initiale
		- selon que la valeur minimale de $r$ est 0 ou non
- (P) admet une solution admissible
	- ssi le prb auxiliaire (Pa) admet une solution de base optimale avec R = 0

- _notes_:
	- le dico obtenu en éliminant les var artificielles est un dico initiale pour la Phase II
		- → explication : dans l'exécution de la Phase I, on cherche à éliminer ces var de l'ensemble des var de base
