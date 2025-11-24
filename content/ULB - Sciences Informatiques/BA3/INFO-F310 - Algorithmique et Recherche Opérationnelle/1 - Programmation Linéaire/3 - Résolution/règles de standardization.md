---
title: règles de standardization
authors: iamscrambledeggs
tags: []
---

#### rappel
- le modèle standard du prb impose que toutes les contraintes soient des contraintes d'égalité (Ax = b)
	- à l'exception de la contrainte de non-négativité des variables $x (x \geq 0)$

### pour appliquer l'algo du simplexe
- transformer toutes les contraintes d'inégalités (de type $\leq$ ou $\geq$) du modèle original à l'exception de la condition/contrainte de **non-négativité** des variables $x (x \geq 0)$
- assurer que les contraintes d'égalité du modèle original ou résultants de cette transformation restent valides puisque les coeff indépendants (b) doivent être non négatifs

## contraintes de type $\leq$
- additionner une var d'écart $s$ dans le membre de gauche de cette contrainte
- ajouter une contrainte de non-négativité sur cette var ($s \geq 0$)
	- cette nouvelle var apparaît avec un coeff nul dans la fonction objectif
**exemple**
$a_{11}x_1 + a_{12}x_2 + a_{13}x_3 \leq b_1 \to a_{11}x_1 + a_{12}x_2+a_{13}x_3 + s = b_1, s \geq 0$
## contraintes de type $=$
- nécessaire d'additionner une var artificielle $R \geq 0$ par contrainte d'égalité
	- coeff sera 0 dans la fonction objectif
**exemple**
$a_{11}x_1 + a_{12}x_2 + a_{13}x_3  = b_1 \to a_{11}x_1 + a_{12}x_2+a_{13}x_3 + R = b_1, R \geq 0$
## contraintes de  type $\geq$
- soustraite une var de surplus ou d'excès $s$ dans le membre de gauche de cette contrainte
- ajouter une contrainte de non-négativité sur cette var ($s \geq 0$)
	- cette nouvelle var $s$ apparaît avec unn coeff nul dans la fonction objectif

**exemple**
$a_{11}x_1 + a_{12}x_2 + a_{13}x_3 \geq b_1 \to a_{11}x_1 + a_{12}x_2+a_{13}x_3 - s = b_1, s \geq 0$
**problème avec la contrainte de non-négativité, $s \geq 0$**
- lors de la première itération du Simplexe, les var $x_1,x_2,x_3 = 0$
	- donc $s = -b_1$ violant ainsi la contrainte de non-négativité
		- puisque ($b_1 \geq 0$)
- pour éviter ce prb, additionner une var artificielle $R \geq 0$ dans le membre de fauche de cette contrainte
$a_{11}x_1 + a_{12}x_2 + a_{13}x_3 - s = b_1 \to a_{11}x_1 + a_{12}x_2+a_{13}x_3 - s + R= b_1, s \geq 0, R \geq 0$
## tableau récapitulatif

| contrainte | opération | type de var  | opération | type var     |
| ---------- | --------- | ------------ | --------- | ------------ |
| $\leq$     | +         | écart        |           |              |
| $=$        | +         | artificielle |           |              |
| $\geq$     | -         | excès        | +         | artificielle |
