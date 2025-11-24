# conséquence de la complétude 
## théorème 
	- Si un problème $X$ est $NP$-complet 
	- → alors il n'existe pas d'algo de décision pour $X$ en tps polynomial 
		- Sauf si $P = NP$

### preuve
- Supposons qu'il existe un algo $A$ pour résoudre $X$ en tps polynomial 
	- idée : on va en déduire que $P = NP$
- on a
	- $X \in P$
	- on sait $P \subseteq NP$
	- → faire preuve double inclusion (montrer que $NP \subseteq P$)
- Soit $Y$ un problème dans $NP$ 
- Comme X est $NP$-complet, $Y$ se réduit à $X$ en tps polynomial 
	- notons $f$ une telle réduction  
- On peut en déduire que $Y$ peut être résolu en tps polynomial 
	- étant donnée une instance $I$ de $Y$
		- l'algo construit d'abord $f(I)$ en tps polynomial 
		- puis applique l'algo $A$ sur $f(I)$ 
	- → on a bien que $I$ a une solution 
		- $\Leftrightarrow f(I)$ a une solution (car $f$ une réduction)
		- $\Leftrightarrow A$ exécuté sur $f(I)$ retourne 1 (car $A$ résout $X$)
	- → algo en 2 étapes est bien correct
		- + en tps polynomial 
			- (car les polynomes pour $f, A$ se composent)
	- donc $Y \in P$ 
- donc $P = NP$ 

### conséquences pratiques
- si pas d'algo "efficace" pour résoudre un prb → ptt il est $NP$-complet
	- à moins que $P = NP$ mais sinon ça ne sert à rien de continuer à chercher 
- si vous trouver un algo en temps polynomial pour un prb $NP$-complet 
	- → alors soit votre algo est incorrect
	- → vous avez démontré que $P = NP$ (et tu gagnes 1 million d'euros)