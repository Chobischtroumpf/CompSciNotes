# théorème équivalence entre points extrêmes et solutions de base réalisable
- Soit
	- A, matrice réelle de dimension $m \times n$ et de rang $m$, et un vecteur réel $b$ de dimension $m$
	- $P$ un polytope convexe défini par tous les vecteurs $x$ de dimension $n$ satisfaisant les contraintes (sous-forme standard)
- $Ax = b, x \geq 0$
	- vecteur $x$ = point extrême de P $\leftrightarrow x$ = solution de base réalisable pour le système défini par l'ensemble de contraintes
	- _condition  de non-négativité permet l'équivalence avec solutions de base réalisables_

- jpp des mathématiciens, ils ont 3000 théorèmes pour la même chose là
	- bref juste une manière d'officialiser qu'on peut trouver la solution de base réalisable graphiquement
## preuve
### preuve $\leftarrow$
- Supp $x = (x_1,x_2, ..., x_m, 0, 0, ..., 0)$ = solution de base réalisable pour l'ensemble de contraintes
	- → $x_1a_1 + ... + x_ma_m = b$
		- $m$ premières cols de A sont linéairement indep
- Supp $x$ = combinaison convexe de deux autres points $y, z \in P$
	- $x = \alpha y + (1 - \alpha)z, 0 \lt \alpha \lt 1, y \neq z$
- toutes les compo de $x,y,z \gt 0$ et $0 \lt \alpha \lt 1, \to (n-m)$ composantes de $y, z$ sont nulles
	- $y_1a_1 + ... + y_ma_m = b$
	- $z_1a_1 + ... + z_ma_m = b$
- les vecteurs de A étant linéairement indep, il s'en suit que $x = y = z$ et donc que $x$ = point extrême de P

### preuve $\rightarrow$
- supp $x$ = point extrême de P
- supp les composantes non-nulles de $x$ sont les $k$ premières compo
	- $x_1a_1 + ... + x_ka_k = b, x_i \gt 0, i = 1,...,k$
- démontrer x = solution de base  réalisable → démontrer les vecteurs $a_1,...,a_k$ sont linéairement indep (on fait par contradiction)
- supp vecteurs $a_1,..., a_k$ linéairement indép. Dans ce cas, il existe un CL (non-triviale) tq
	- $y_1a_1 + ... + y_ka_k = 0$
- définissons le vecteur $y = (y_1,..., y_k, 0, ..., 0) \in \mathbb{R}^n$
	- puisque $x_i \gt 0, 1 \leq i \leq k,$ il est possible de choisir $\varepsilon$ vérifiant les contraintes de non-négativités :
		- $x + \varepsilon y \geq 0$
		- $x - \varepsilon y \geq 0$
- dans ce cas, $x = \frac{1}{2}(x + \varepsilon y) + \frac{1}{2}(x - \varepsilon y)$ serait une combinaison convexe de deux vecteurs (distincts) de P
	- → impossible puisque $x$ est un point extrême de $P$
- → $a_1,...,a_k$ sont linéairement indep
