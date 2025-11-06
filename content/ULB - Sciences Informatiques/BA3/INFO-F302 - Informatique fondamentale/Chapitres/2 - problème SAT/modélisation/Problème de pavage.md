---
title: Problème de pavage
authors: Alessandro Dorigo
tags:
  -
---

### intitulé
étant donnés $\dim \in \mathbb{N}$ et
![[Pasted image 20251017140412.png]]
peut-on paver le carré de dimension $\dim \times \dim$ ?
![[Pasted image 20251017140918.png]]
### formalisation du problème
- entrée
	- un ensemble fini T de "types" d'arêtes
	- un ensemble fini $C \subseteq T^4$ de carreaux
	- une dimension $\dim \in \mathbb{N}$
- sortie
	- une fonction totale $f : \set{1, ..., \dim}^2 \to C$ tq
		- $\forall 1 \leq i \leq \dim, 1 \leq j \leq \dim, f(i,j) . \text{ nord } = f(i,j-1).\text{ sud }$
		- $\forall 1 \leq i \lt \dim, 1 \leq j \leq \dim, f(i,j).\text{ est } = f(i+1,j). \text{ ouest }$
- choix des variables
	- $X_{i,jc}$
		- $\forall i,j \in \set{1,...,\dim}^2$
		- $\forall c$, carreau de $C$
		- → $X_{i,j,c}$ vraie $\leftrightarrow$ (i,j) contient c
#### contraintes
- $\forall (i,j) \in \set{1,...,\dim}^2, j \gt 1, \forall c$
- si (i,j) contient $c$ → il existe un carreau $c'$ tq
	- $(i,j-1)$ contient $c'$
	- $c.\text{ nord } = c'. \text{ sud }$
	- $\land_{(i,j) \in \set{1,...,\dim}^2, j \gt 1} \land_{c \in C}(X_{i,j,c} \to \lor_{c' \in C, c.nord = c'.sud} X_{i,j-1,c'})$
	- autre solution possible : $\land_{1 \leq i \leq \dim, 1 \lt j \leq \dim, c_1,c_2 \in C, c_1.nord \neq c_2.sud}(\neg X_{i,j,c_1} \lor \neg X_{i,j-1,c_2})$

- pour les contraintes est/ouest
	- $\land_{(i,j) \in \set{1,...,\dim}^2, i \lt \dim} \land_{c \in C}(X_{i,j,c} \to \lor_{c' \in C, c.est = c'.ouest} X_{i+1, j, c'})$

- il faut au moins un carreau par case
	- $\land_{(i,j) \in \set{1,...,\dim}^2}(\lor_{c \in C} X_{i,j,c})$

- il faut au plus un carreau par case
	- $\land_{(i,j) \in \set{1,...,\dim}^2, c_1, c_2 \in C, c_1 \neq c_2}(\neg X_{i,j,c_1} \lor \neg X_{i,j,c_2})$
## comment choisir les propositions
- souvent, un prb de décision demande l'existence d'une relation binaire d'un ensemble fini A vers un ensemble fini B, qui satisfait certaines contraintes
	- coloriage de graphe
		- A : ensemble des sommets
		- B : ensemble des couleurs
	- $n$ reines à placer sur un échiquier $n \times n$
		- A = {1,...,n}^2 : ensemble des cases
		- B = {0,1}
	- Sudoku
		- A = {1,...,9}^2 : ensemble des cases
		- B = {1,...,9} : ensemble des valeurs
- → on peut alors tenter d'utiliser
	- pour tout $a \in A, b \in B$
	- " a est en relation avec b" $\equiv x_{a,b}$

- si on veut que la relation soit une fonction
	- exemples précédents, relation = fonction totale de A vers B
- → exprimer les contraintes suivantes
	- **au moins une** : $\wedge_{a \in A}(\vee_{b \in B} x_{a,b})$
	- **au plus une** : $\wedge_{a \in A, b, b' \in B, b \neq b'} \neg x_{a,b} \vee \neg x_{a,b'}$
