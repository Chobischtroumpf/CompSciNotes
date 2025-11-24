# algorithme de vérification 
- informellement, un algo de vérification = algo étant donnée une solution "candidate" à un prb de décision, décide si  oui ou non cette solution est valide 
	- _ex. coloriage de graphe avec au plus $k$, une solution candidate avec coloriage $c$_
- algo de vérification pour un prb $P \subseteq \Sigma^*$ = algo de décision $A$
	- prenant deux mots en argument 
	- qui termine pour toute entrée tel que 
		- $P = \set{u \in \Sigma^* | \exists v \in \Sigma^*, A(u,v) = 1}$ 
		- qd $A(u,v) = 1$ : $v$ est appelé un certificat pour $u$ 
