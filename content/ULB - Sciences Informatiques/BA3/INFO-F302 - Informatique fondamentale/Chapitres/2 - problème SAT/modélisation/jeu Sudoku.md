---
title: jeu Sudoku
authors: Alessandro Dorigo
tags:
  -
---

![[cd12dd69298f888f9de06ebec4b75b98.png]]
### choix des variables

- On cherche une fonction $f : \underbrace{\set{1,...,9}^2}_{\text{coordonnées des cases}} \to \underbrace{\set{1,...,9}}_{\text{valeurs}}$
- On peut voir cette foncytion comme une fonction
	- $g : \set{1,...,9}^3 \to \set{0,1}$
	- définie par $g(i,j,v) = 1 \leftrightarrow f(i,j) = v$
- → donc on peut prendre une varaible par triplet $(i,j,v) \in \set{1,...,9}$
- $X = \set{x_{i,j,v} | i,j,v \in \set{1,...,9}}$

#### jamais deux valeurs différentes dans une même case
- si la case (5,7) contient 3 alors elle ne contient pas 6
	- $\neg (x_{5,7,3} \wedge x_{5,7,6}) \equiv \neg x_{5,7,3} \vee \neg x_{5,7,6} \equiv x_{5,7,3} \to \neg x_{5,7,6}$
- la case (5,7) ne contient pas deux valeurs différentes
	- $\bigwedge_{v=1}^9 \bigwedge_{v' = v+1}^9 (\neg x_{5,7,v} \vee \neg x_{5,7,v'})$
→ $$
\bigwedge_{(i,j) \in \set{1,...,9}^2} \bigwedge_{v=1}^9 \bigwedge_{v' = v+1}^9 (\neg x_{i,j,v} \vee \neg x_{i,j,v'})
$$

#### au moins une valeur par case
Pour toute case (i,j), il existe une valeur v dans (i,j)
→ $$
\bigwedge_{(i,j) \in \set{1,...,9}^2}(\bigvee_{v \in {1,...,9}} x_{i,j,v})
$$

#### jamais deux fois la même valeur sur une même ligne
Pour toute ligne i, pour toute colonne j, pour toute valeur v, si (i,j) contient v, alors pour toute colonne k $\neq$ j, (i,j) ne contient pas v
$$
\bigwedge_{\begin{gather} v \in \set{1,...,9} \\ i \in \set{1,...,9} \\ j \in \set{1,...,9} \end{gather}} x_{i,j,v} \to \bigwedge_{k \in \set{1,...,9}, k \neq j} \neg x_{i,k,v}
$$
→ après simplification
$$
\equiv \bigwedge_{\begin{gather} v \in \set{1,...,9} \\ i \in \set{1,...,9} \\ j \in \set{1,...,9} \\ k \in \set{j+1,...,9}\end{gather}} ( \neg x_{i,j,v} \vee \neg x_{i,k,v})
$$
- peut être marquée comme
Soit $C \subseteq \set{1,...,9}^2$
Dans $C$, il n'existe pas deux fois la même valeur
$$
\bigwedge_{\begin{gather} (i,j) \in C \\ (i', j') \in C \\ (i,j) \neq (i',j') \\ v \in \set{1,...,9}\end{gather}} (\neg x_{i,j,v} \vee \neg x_{i',j',v})
$$
#### jamais deux fois la même valeur sur une même colonne
$$
\bigwedge_{\begin{gather} v \in \set{1,...,9} \\ j \in \set{1,...,9} \\ i \in \set{1,...,9} \\ i' \set{i+1,...,9}\end{gather}} (\neg x_{i,j,v} \vee \neg x_{i',j,v})
$$

#### jamais deux fois la même valeur dans un même sous-carré 3x3
$$
\bigwedge_{\text{C : sous-carré de la grille}} \bigwedge_{\begin{gather} (i,j) \in C \\ (i',j') \in C \\ (i,j) \neq (i',j') \\ v \in \set{1,...,9}\end{gather}} (\neg x_{i,j,v} \vee \neg x_{i',j',v})
$$

### la grille est pré-remplie
en entrée, on se donne une fonction $G : \set{1,...,9}^2 \to \set{1,...,9} \cup \set{\text{NULL}}$
→ on doit exprimer l'existence des valeurs prédéfinies
$$
\bigwedge_{\begin{gather} (i,j) \in \set{1,...,9}^2 \\ G(i,j) \neq \text{NULL}\end{gather}} x_{i,j,G(i,j)}
$$
- remarque
	- la contrainte "jamais deux valeurs différentes sur une même case" inutile car impliquée par toutes les autres
	- → lors des tests, il apparaît qu'elle permet de mieux guider le solveur et donc être plus efficace
