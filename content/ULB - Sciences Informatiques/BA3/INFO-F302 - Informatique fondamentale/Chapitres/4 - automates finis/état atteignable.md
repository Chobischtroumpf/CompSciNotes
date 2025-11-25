# états atteignables
- soit $A = (Q, q_0, F, \delta)$ un automate sur un alphabet $\Sigma$ 
- un état $q \in Q$ est dit atteignable 
	- s'il existe un mot $w \in \Sigma^*$ et une exécution de $A$ sur $w$ qui se termine en $q$ 

- rq : l'ensemble des états atteignables d'un graphe peut être calculer en temps $O(n+m)$ 
	- par algo de graphe classiques
		- _ex. parcours en largeur_
	- $n$ : nb détats de l'automate 
	- $m$: nb de transitions
## théorème 
- Étant donné un automate $A$ avec $n$ états, $m$ transitions
	- on peut tester en $O(n+m)$ si $L(A) = \emptyset$ 
### algorithme 
1. calculer l'ensemble des états atteignables $R$ de $A$ 
2. tester si $R \cap F = \emptyset$ 