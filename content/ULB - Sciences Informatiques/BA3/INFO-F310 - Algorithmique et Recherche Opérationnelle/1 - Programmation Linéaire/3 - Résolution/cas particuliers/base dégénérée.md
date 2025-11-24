# base dégénérée
- base dégénérée 
	- base $B$ telle que sa solution de base associée possède au moins une var en base nulle 
		- ie. au moins une des compo de $x_B = 0$ 
	- pour var sortante 
		- si plusieurs choix sont possibles, alors une des variables en base sera nulle à l'itération suivante 
	- dégénérescence 
		- lors des itérations de l'algo du Simplexe, une op de pivot peut atteindre une base dégénérée
		- pivotage vers une nouvelle base correspondant à la même solution sans que la fonction objectif $z$ ne change de valeur
			- on reste sur le même point 
		- ce pivot est dégénéré : il change de base mais reste sur la même solution 

- _rappel_ : la terminaison de l'algo du Simplexe n'est assurée que si l'on améliore strictement la valeur des solutions de base à chaque pivot 

- règle lexicographique 
	- choix de la variable hors-base entrante : var hors-base du plus petit indice 
		- parmi var hors-base 
			- couts réduit : st négatifs
			- profits marginaux : st positifs
	- choix de la var sortante : var en base de plus petit indice 
		- parmi celles possible pour le pivot

### en général 
- difficile de donner une technique simple qui permettrait de choisir celle des variables candidates (sortantes) qui conduit à l'optimum par le plus petit nb d'itérations
	- en cas de dégénérescence
	- sinon impossible

- conséquences (possibles)
	- lors d'exécution du Simplexe, on retrouve un tableau correspondant à une étape préalable
		- plusieurs pivots successifs ramènent à la base dégénérée
	- si on poursuit l'exécution alors mêmes étapes que déjà exécutées
	- → cyclage

### cyclage 
- au bout d'un nb fini d'itération, on retrouve un dico déjà rencontré
	- on retrouve une même partition des $n+m$ var
		- $m$ var en base 
		- $n$ var hors base 
### en pratique 
- cause = contrainte redondante dans le modèle 
- même si dégénérescence observée, cyclage plus rarement et se recontre dans les modèles de grande taille très dégénérés
	- difficile de trouver des modèles de petite teille où le phénomène de cyclage se présente
- si cyclage se produit → algo du simplexe ne se termine pas 

## éviter cyclage
### théorème de Bland
- cyclage ne peut pas se produit lorsqu'à chaque itération effectuée apd dico dégéné
	- → choisir variables entrantes et sortantes comme celle du plus petit indice parmi les candidats possible 
	- → _empêche cyclage mais peut avoir dégénérescence_
- en pratique
	- → empêche les cycles de pivots dégénérés
	- n'empêche pas nécessairement de longues séquences de pivots dégénérés ne formant pas un cycle 
		- inhibe performance 

### méthode des perturbations
- modifier de manière infinitésimale le vecteur $b = (b_1,b_2,...,b_m)$ 
	- _ex. $b_i \to b_i + \varepsilon_i, 0 \lt \varepsilon_i \ll 1$  
- → transformation entrâine les sommets du polydre uniquement à l'intersection de $m$ inégalités et non davantage
- → bonne approximation de la solution 

- en pratique 
	- une bonne anlyse a priori pour éliminer les redondances = meilleur moyen d'éviter ces prb de cyclage 
		- redondances cachées !! 
