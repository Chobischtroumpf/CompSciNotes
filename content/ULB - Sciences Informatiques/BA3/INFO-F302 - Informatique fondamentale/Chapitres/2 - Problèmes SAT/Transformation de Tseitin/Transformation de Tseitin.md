---
title: Transformation de Tseitin
authors: Alessandro Dorigo
tags:
  - InfoFond
---

## Idée
 - parfois le problème qu'on cherche à résoudre ne s'exprime pas facilement par une formule en FNC
 - Transfromation de Tseitin : ajout de nouvelles variables et équivalences

**Exemple**
$\phi = (x \wedge q) \vee \neg(y \vee r)$
- Remplacement
	- $x \wedge q \equiv x_1$
	- $\neg(y \vee r) \equiv x_2$
- → $(x_1 \vee x_2) \wedge (x_1 \leftrightarrow x \wedge q) \wedge (x_2 \leftrightarrow \neg(y \vee r))$
- Il reste à mettre  sous FNC
	- $(x_1 \leftrightarrow x \wedge q)$
	- $(x_2 \leftrightarrow \neg (y \vee r))$

Après avoir montré les équivalences pour mettre la formule sous FNC
$$
(x_1 \vee x_2) \wedge (\neg x_1 \vee p) \wedge (\neg x_1 \vee q) \wedge (\neg x \vee \neg y \vee x_1)\wedge (\neg x_2 \vee \neg q) \wedge (\neg x_2 \vee \neg r) \wedge (y \vee r \vee x_1)
$$
→ la satisfaisabilitié est préservée i.e. $\phi$ satisfaisable ssi $\psi$ est satisfaisable

## Transformation de Tseitin
- la technique de Tseitin sera particulièrement intéresante lorqu'on devra mettre sous FNC des formules qui sont sous FND
	- $C_1 \vee C_2 \vee ... \vee C_n$
		- $C_i$ = conjonctions de littéraux
- on va introduire une variable $x_i$ pour chaque $C_i$ et on obtient la formule
	- $(x_1 \vee x_2 \vee ... \vee x_n) \wedge (x_1 \leftrightarrow C_1) \wedge ... \wedge (x_n \leftrightarrow C_n)$
- supposons que $C_i = I_1 \wedge ... \wedge I_k$
	- $I_i$ = littéraux
	- → mettre $x_i \leftrightarrow C_i$ sous FNC est assez simple
		- $x_i \leftrightarrow C_i \equiv (\bigwedge_{j=1}^k (\neg x_i \vee I_j)) \wedge (x_i \vee \bigvee_{j=1}^k \neg I_j)$
		- sous FNC
→ ne pas hésiter à introduire des nouvelles variables pour minimiser le nombre de clauses (même pour les SAT solveurs)
