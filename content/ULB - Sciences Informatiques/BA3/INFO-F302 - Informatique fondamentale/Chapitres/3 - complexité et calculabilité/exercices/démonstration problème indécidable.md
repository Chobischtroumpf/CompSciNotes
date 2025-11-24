Mq le prb suivant est indécidable 
- Étant donnés deux programmes P et Q qui retournent tous les deux une valeur bool
	- est-ce que les 2 programmes sont équivalents? 
		- $\forall x, P(x) = Q(x) ?$ 

**réponse**
- réduction apd prb de l'arrêt (indécidable)
- étant donné un programme $R$ et une entrée particulière $x_0$ de $R$, on considère les deux programmes 
	- procedure AUX(x) : 
		- r := R(x0)
		- return 1
	- procedure CONST(x) : 
		- return 1
- la différence fondamentale entre les deux programme 
	- AUX(x) ne retourne rien qd l'exécution de R sur $x_0$ ne s'arrête pas
	- → CONST(x) s'arrête tjr et retourne 1 
- → Donc AUX(x) = 1 pour toute entrée x 
	- $\Leftrightarrow$ R s'arrête sur l'entrée $x_0$ 
- → on en déduit que AUX et CONST sont équivalents 
	- $\Leftrightarrow R$ s'arrête sur l'entrée $x_0$ 
- → si le prb d'équivalence était décidable
	- alors le problème de l'arrêt le serait aussi 