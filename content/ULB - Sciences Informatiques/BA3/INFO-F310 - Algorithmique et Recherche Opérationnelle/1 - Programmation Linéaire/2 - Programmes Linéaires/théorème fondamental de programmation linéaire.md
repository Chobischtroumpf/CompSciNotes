# théorème fondamental
- PL (program lin) sous forme standard
	- minimize $c^Tx$
	- subject to $Ax = b, x \geq 0$
		- var x : vect col de dim $n$
		- coef $c^T$ : fonction obj, vect ligne de dim $n$
		- coef A : contraintes, mat dim $m \times n$
		- coef b : contraintes, vec col de dim $m$
## énoncé
Soit un programme linéaire, sous forme standard, ou matrice A est de dim $m \times n, m \lt n$ de rang $m$
- si l'ensemble des sol réalisables pas vide → il existe une sol de base réalisable dans cet ensemble (**Théorème de Carathéodory**)
- s'il existe une sol réalisable optimable → il existe une sol de base réalisable optimale (**recherche de solutions de base réalisables**)
	- lors de la résolution du programme, restreindre notre attention au sous-ensemble des solutions de base réalisable de l'ensemble
		- $\set{x | Ax = b, x \geq 0}$
	- Pour programme P avec $n$ variables et $m$ contraintes, au plus
		- $\binom{n}{m}$ solution de base (nb de façons de séléctionner $m$ parmi $n$ colonnes) → nb fini de possibilités
- → technique de recherche finie évidente mais terriblement inefficace

- en gros
	- s'il y a des solutions réalisables dans un tel ensemble → alors il y a une solution de base réalisable dans cet ensemble (surprise mf)
	- si y a une solution réalisable optimale → alors il existe une solution de base réalisable
		- résolution
			- avec n var et m contraintes = $\binom{n}{m}$ solution de base
			- horriblement pas efficace

## interprétation
- considérer uniquement les sol de base réalisables lors de la recherche d'une sol réalisable optimale (la val optimale est toujours atteinte pour une telle solution)
- si cette sol = sol de base → c'est une sol de base réalisable optimale

### interprétation géométrique
- lien entre interprétation algébrique et géométrique : relation formelle entre solutions de base réalisable et points extrêmes des polyèdres
	- polyèdre : intersection d'un nb fini de demi-espaces fermés
		- $\set{x | a^T x \leq b}$
	- polyèdre convexe
		- demi-espace fermé $\set{x | a^T x \leq b}$ = convexe
		- intersection d'une famille quelconque d'ensembles convexes forme un ensemble convexe
- en gros
	- si tu représentes graphiquement toutes tes contraintes
	- → tu te retrouves avec un polyèdre
	- et selon le sommet que tu prends, tu auras une solution de base réalisable (ou pas, car why not)
