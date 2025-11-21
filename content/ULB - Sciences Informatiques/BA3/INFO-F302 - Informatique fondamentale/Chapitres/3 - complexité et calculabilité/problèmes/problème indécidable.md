# problème indécidable 
- un problème de décision $P$ sur un alphabet $\Sigma$ est indécidable 
	- s'il n'existe pas d'algorithme $A$ prenant un mot sur $\Sigma$ 
		- et retournant, en un nb fini d'étapes de calcul
			- la valeur 0 ou 1 
		- tel que pour tout mot $x$ sur $\Sigma, A(X)$ retourne 1 $\leftrightarrow x \in P$ 

- problème indécidable s'il n'existe pas d'algorithme pour le résoudre 
	- algo = programme dans un langage de programmation 
## exemple : problème de l'arrêt
`while(true) print "bonjour" ;`

### théorème (Turing, 1936)
- le problème de l'arrêt est indécidable 

#### preuve
par l'absurbe 
- en sup qu'il existe un programme HALT($c_p,x$) qui décide le problème de l'arrêt 
	- pour tout programme $P$ donné par son code $c_p$, et toute chaîne de caractère $x$ 
	- apd HALT, on définit le programme PARADOX
```
PARADOX(c : string)
	if HALT(c,c) then
		loop forever
	else 
		stop
```
- On appelle $PARADOX(c_{PARADOX}$)
	- où le paramètre est la code source du programme PARADOX 
→ Que se passe-t-il ? 
- deux situations 
	- si le programme s'arrête 
		- → c'est que $HALT(c_{PARADOX}, c_{PARADOX}) = 0$ 
		- donc $PARADOX(c_{PARADOX})$ ne s'arrête pas 
	- si le programme ne s'arrête pas 
		- → c'est que $HALT(c,c) = 1$
		- donc $PARADOX$ s'arrête
- → dans les deux cas, contradiction 
	- c'est que le programme HALT n'existe pas 

#### problème de la correspondance de Post 
- Soit $\Sigma = \set{0,1}$ 
	- un mot $u$ sur $\Sigma$ est une s"quence finie d'éléments de $\Sigma$ 
- $u,v$ peuvent être concaténés pour former un nouveau mot 
	- $uv$ 
- l'élément neutre $\epsilon$ (mot vide)

**énoncé**
 - entrée
	 - $(u_1,v_1),...,(u_n,v_n), n \geq 1$ 
		 - $n$ paires de mots (possibles vides) sur $\Sigma$ 
- sortie 
	- $1 \leftrightarrow$ 
	- il existe une séquence finie d'indices 
		- $i_1,...,i_k \in \set{1,...,n}, k \geq 1$
		- $u_{i_1}u_{i_2}...u_{i_k} = v_{i_1}v_{i_2}...v_{i_k}$ 

**exemples**
- instance : 
	- $(u_1,v_1)=(100,00)$
	- $(u_2,v_2) = (0,01)$ 
	- solution possible : 2,1
		- $u_2u_1 = 0100 = v_2v_1$ 
- instance 
	- $(u_1,v_1) = (0,100)$
	- $(u_2,v_2) = (01,00)$ 
	- $(u_3,v_3) = (110,11)$ 
	- solution : 
		- $u_3u_2u_3u_1 = (110)(01)(110)(0)$
		- $= (11)(00)(11)(100) = v_3v_2v_3v_1$ 

#### théorème
- le prb de Correspondance de Post est indécidable 
## autres problèmes indécidables 
- 10é problème de Hilbert 
	- résolution d'équation diophantiennes (à solution entière)
	- indécidabilité prouvée en 1971 (Matiyasevic)
	- prb 
		- entrée : $p(x_1,...,x_n)$ - polynôme à coeff entiers
		- sortie : $\exists i_1... \exists i_n \in \mathbb{Z} \cdot p(i_1,...,i_n) = 0 ?$ 
		- → décidable dans les réels 
- complexité de Kolmogorov 
	- étant donné un mot binaire $w$ et un entier $k \in \mathbb{N}$ 
		- décider s'il existe un programme Java qui écrit $w$ et dont le code est un fichier d'au plus $k$ bits
	- _rq : le choix du formalisme qui écrit le mot influe sur la complexité_
		- formalisme : Java, Lisp, C, machine de Turing,...
- PCP avec $n = 7$ 
	- variante où on se donne 7 paires de mots $(u_1,v_1),...,(u_7,v_7)$ 
	- _rq : décidable pour $n\leq 2$ et ouvert pour $3 \leq n \leq 6$_
- castor affairé 
	- étant donné un programme (donné par son code source,_ex. Java_) qui écrit des 0 et des 1 et qui s'arrête
	- → on veut décider s'il est maximal 
		- ie. qu'il n'existe pas un autre programme dont le code source n'est pas plus grand, mais qui écrit un mot strictement plus grand 
- _rq : notion de réduction = démontrer que NP-dureté d'un prb_
	- _différence, on ne demande pas que l'algo qui calcule la réduction le fasse en tps poly_
