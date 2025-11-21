#InfoFond 

# lemme (composition de réductions)
	la composition de deux réductions polynomiale est une réduction polynomiale
## preuve
- Soient 
	- A,B,C trois prb 
	- $f$ une réduction de A vers B en temps $O(n^c)$ 
	- $g$ une réduction de B vers C en temps $O(n^d)$ 
	- $n$ taille des instances prises en entrée 
- alors $g \circ f$ est une réduction de $A$ vers $C$ 
	- en effet, prenons une instance $I_A$ de $A* : on a lors que $I_A$ a une solution 
		- $\Leftrightarrow f(I_A)$ a une solution (car $f$ est une réduction)
		- $\Leftrightarrow g(f(I_A))$ a une solution (car $g$ est une réduction)
- de plus si on note $n_A$ : la taille de $I_A$
	- → la taille de l'instance $f(I_A)$ est dans $O(n_A^c)$ 
	- et donc le temps pour construire $g(f(I_A))$ à partir de $I_A$ est dans $O((n^c_A)^d) = O(n_A^{cd})$ : ce qui est polynomial
