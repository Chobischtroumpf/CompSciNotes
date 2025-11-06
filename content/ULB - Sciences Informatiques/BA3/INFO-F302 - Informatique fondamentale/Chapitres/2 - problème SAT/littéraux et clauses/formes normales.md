---
title: formes normales
authors: Alessandro Dorigo
tags:
  - InfoFond
---

# forme normale conjonctive (FNC)

> [!info] Définition
> formule en _forme normale conjonctive_ (FNC) ssi c'est une conjonction de disjonctions de littéraux
	>- $\wedge_i(\vee_j(\neg)x_{i,j})$
# forme normale disjonctive (FND)

> [!info] Définition
>- formule en _forme normale disjonctive_(FND) ssi c'est une disjonction  de conjonctions de littéraux
	>- $\vee_i(\wedge_j(\neg)x_{i,j})$
# mise sous FNC et FND
## lemme de merde
- lemme
	- tt ensemble non-vide de clauses $A = \set{C_1,...,C_n}$ est équivalent à la formule en FNC $\phi_A = \wedge_{i=1}^n C_i$
	- pour toute valuation, $V \vDash A \leftrightarrow V \vDash \phi_A$
- → Pour mettre formule sous forme de clauses, il suffit de la mettre en FNC

## fonctionnement
- utilisation des transformations successives suivantes pour obtenir les formes normales
	- élimination des connecteurs $\to, \leftrightarrow$
		- $(\phi \to \psi) \equiv (\neg \phi \vee \psi)$
		- $(\phi \leftrightarrow \psi) \equiv (\neg \phi \vee \psi) \wedge (\phi \vee \neg \psi)$
	- entrer les négations le plus à l'intérieur possible
		- $\neg(\phi \wedge \psi) \equiv (\neg \phi \vee \neg \psi)$
		- $\neg \neg \phi \equiv \phi$
		- $\neg(\phi \vee \psi) \equiv (\neg \phi \wedge \neg \psi )$
	- utilisation des distributivité de $\vee, \wedge$
**exemple**
$\neg (x \leftrightarrow (y \to r))$
- retirer les équivalences et implications : $\neg((\neg x \vee \neg y \vee r) \wedge (\neg(\neg \vee r) \vee x))$
- pousser les négations à l'intérieur : $(x \wedge y \wedge \neg r) \vee ((\neg \vee r)\wedge \neg x)$
- distributions : $((x \wedge y \wedge \neg r) \vee (\neg y \vee r)) \wedge ((x \wedge y \wedge \neg r) \vee \neg x)$
- distributions : $(x \vee \neg y \vee r) \wedge (y \vee \neg y \vee r) \wedge(\neg r \vee \neg y \vee r) \wedge (x \vee \neg x) \wedge (y \vee \neg x) \wedge ( \neg r \vee \neg x)$
-  retirer les formules équivalentes à $\top$ : $(x \vee \neg y \vee r) \wedge (y \vee \neg x) \wedge ( \neg r \vee \neg x)$
