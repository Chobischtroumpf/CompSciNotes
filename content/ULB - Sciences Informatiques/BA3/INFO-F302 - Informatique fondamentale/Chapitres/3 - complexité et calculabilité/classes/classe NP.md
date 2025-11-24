#InfoFond 
#  classe $NP$ 
- un prb $P$ est dans $NP$ s'il existe 
	- un algo de vérification $A$ de complexité polynomiale en temps 
	- une constante $k$ 
	- → tq pour toute entrée $u$ :
		- $u \in P$ 
		- il existe un certificat $v$ de longueur polynomiale dans $u : (|v| = O(|u|^k))$ 
			- tq $A(u,v) = 1$ 

(autre def bizarre)
- c'est la classe des prb pouvant être décidés en tps polynomial par un algo non-déterministe
	- cet algo doit s'arrêter après un nb d'étapes polynomial
		- il a le droit de faire des choix aléatoires
		- si rep au prb est OUI → il doit exister une exécution de l'algo après laquelle l'algo répondra OUI
	- certificat = suite de tirages
- _Exemple : SAT choisit aléatoirement une valeur de vérité pour chaque variable, vérifier en tps linéaire qu'elles satisfont la formule_

**exemples de problèmes**
- décider qu'un ensemble de clauses est satisfaisable 
	- certificat = valuation 
- _voyageur de commerce_ 
	- certificat = cycle 
- _coloriage de graphes_
	- certificat = coloriage
- 2-partition 
	- certificat = partition 
- bin packing 
	- certificat = rangement 
- _non-primalité_ : entier $n$ en binaire pas premier ?
	- certificat = un diviseur 
- primalité : entier $n$ en binnaire primaire ? 
	- certificat non triviale 
	- → 2002, démo que prb dans $P$ 
- ts les problèmes de la classe $P$ ($P \subseteq NP$) 
	- algo $A$ qui décide le prb en tps polynomial : changer algo de vérification qui ignore le certificat 

## $NP \subseteq$ ExpTime 
- tt prb de $NP$ peut être décidé par un algo de complexité exponentielle en temps 
	- → why ? (_tell me why ?_)
	- étant donné un mot $u$ en entrée 
		- → il suffit d'énumérer ts les certificats de longueur au plus $a. |u|^k$ (pour $a$ de la notation $O(|u|^a)$)
		- et d'appeler algo de vérification 
			- _ex. SAT : énumérer ttes interprétations possibles et tester_
## $NP$- dur ou $NP$-difficiles
- un problème de décision $P$ est $NP$- dur si 
	- tout problème $P'$ de $NP$ se réduit à $P$ en tps polynomial 
	- ie. il existe un algo $T$ de complexité polynomial en temps, qui transforme 
		- tout mot $u'$ en un mot $T(u')$ tq $u' \in P'$
		- $\leftrightarrow T(u') \in P$
- prb à la fois dans $NP$ est $NP$-dur est dit $NP$-complet
	- ce sont les prb les "plus difficiles" de $NP$

**exemples de prb $NP$-complets**
- SAT 
	- 3-SAT (exactement 3 variables par clauses)
- voyageur de commerce 
- coloriage de graphes 
- bin-packing
- couverture d'arête
	- étant donné un graphe et un entier $k$ : peut-on trouver un sous-ensemble $S$ de sommets tels que chaque arête a au moins une de ses extrémités dans $S$ 