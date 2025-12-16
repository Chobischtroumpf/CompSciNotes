---
title: théorème de Kleene
authors: Mihai Bors
tags: []
---

# théorème de Kleene
- tout langage est reconnaissable par un automate
	- $\Leftrightarrow$ il est définissable par une expression rationnelle

### autre formulation
- si $L \subseteq \Sigma^*$ est un langage
	- → alors il existe un automate $A$ tel que $L=L(A)$
		- $\Leftrightarrow$ il existe une expression rationnelle $E$ tq $L = L(E)$
### implication théorème
- il existe
	- un algo qui transforme tout automate en expression rationnelle
	- un algo qui fait inversément

## preuve
_car elle est pas du tout compliquée (je pleure)_
- idée
	- construction se fait par induction sur les expressions
	- pour tte expression $E$, on va construire un AFN $A_E$ tq $L(E) = L(A_E)$
		- → suffit de déterminer et minimiser $A_E$ avec la construction des sous-ensembles

- si $E = \epsilon$
	- → $A_E = (\set{q_0}, q_0, \set{q_0}, \delta := \emptyset)$
	- $A_E$ accepte uniquement $\epsilon$
	$$
	L(\to \circledcirc) A_{\epsilon} = L(\epsilon) = \set{\epsilon}
	$$
	![[Pasted image 20251127175642.png]]
- si $E = a$ avec $a \in \Sigma$
	- → $A_E = (\set{q_0,q_1}, q_0, \set{q_1}, \delta := \set{(q_0,a,q_1)})$
	- $A_E$ accepte uniquement $a$
	$$
	L(a) = \set{a} = L(\to \circ \to_a \circledcirc)
	$$
	![[Pasted image 20251127175706.png]]
- Si $E = \emptyset$
	- → $A_E = (\set{q_0}, q_0, \emptyset, \emptyset)$
	$$
	L(\emptyset) = \emptyset = L(\to \circ)
	$$
	![[Pasted image 20251127180356.png]]

### dans le cas $E = F+G$
- idée
	- construire $A_F,A_G$ par induction apd
		- → construire $A_E : L(A_E) = L(A_F) \cup L(A_G)$
		- → clôture par union (déjà dans AF mais plus simple avec AFN)
- en lisant la première lettre $\sigma$, on va soit
	- dans le premier automate
	- dans le deuxième
		- → utilisant le non-déterminisme
- → $A_E$ a un état initial $q_0$
	- $q_0^F$ état initial de $A_F$
	- $q_0^G$ celui de $A_G$
	- pour toute lettre $\sigma$, pour toute transition $q_0^F, \sigma, q) \in \Delta_F$
		- on ajoute la transition $(Q_0, \sigma, q)$
		- on fait la même pour $\Delta_G$
	- → on rend le nouvel état initial acceptant si $q_0^F$ ou $q_0^G$ étaient acceptant
		- pour accepter le mot vide

![[Pasted image 20251203145709.png]]

### dans le cas $E = F \cdot G$
- idée de la construction
	- quand on lit un mot $w$, c'est d'abord de lire un préfixe $w_1$ dans $A_F$
	- puis choisir de lire le suffixe restant $w_2$ dans $A_G$
		- non-déterministiquement
		- dans le cas où $w_1$ est accepté par $A_F$
	- → lorsque $A_F$ est sur le point d'aller vers un de ses états acceptants
		- on ajoute la possibilité à l'automate $A_{F\cdot G}$ d'aller vers l'état initial de $A_G$
			- via une transition non-déterministe
![[Pasted image 20251203150033.png]]

#### cas problématique
- décomposition de $w$ en $w_1w_2$ ne soit que
	- $w_1 \in L(F), w_1 = \epsilon$
	- $w_2 \in L(G)$
	- → pas possibilité de passer dans la partie $A_G$ en lisant $w$
- → quand $\epsilon \in L(F)$ ou quand $\epsilon \in L(G)$
	- → $L(F \cdot G) = (L(F) \backslash \set{\epsilon})\cdot L(G) \cup (L(F) \cap \set{\epsilon})\cdot L(G)$
		- $(L(F) \cap \set{\epsilon})\cdot L(G) = L(G)$ si $\epsilon \in L(F)$, sinon ensemble vide
- idée
	- construction comme au-dessus avec automate qui accepte $(L(F)\backslash \set{\epsilon})$
		- →états acceptants de $A_F$ plus acceptants dans $A_{F \cdot G}$
		- + utiliser opérations booléenes sur les automates pour obtenir un automate qui accepte $L(F\cdot G)$

- construction
	- soit
		- $A_F = (Q_F, q_0^F, F_F, \Delta_F)$
		- $A_G  = (Q_G, q_0^G, F_G, \Delta_G)$
		- en supp  $Q_F \cap Q_G = \emptyset$
		- → $B_{F\cdot G} = (Q_F \cup Q_G, q_0^F, F_G, \Delta_{F \cdot G})$
			- $\Delta_{F \cdot G} = \Delta_F \cup \Delta_G \cup \set{(q,\sigma,q_0^G) | \exists p \in F_F : (q \sigma, p) \in \Delta_F}$

![[Pasted image 20251203151154.png]]


#### résumé rapide
- cas
	- si $\epsilon \not \in L(F)$
		- → $A_{F \cdot G} = B_{F\cdot G}$
	- si $\epsilon \in L(F)$
		- $A_{F \cdot G} = B_{F \cdot G} \cup A_G$
			- → construction produit ou même chose que $E +F$

### cas $E = G^*$
-  si $\epsilon \in L(E)$
	- → $E = \epsilon + G^+$
		- $G^+ = G \cdot G^*$ donc au moins une itération
		- $L(G^+) : \set{u_1u_2..u_k : k \geq 1, u_i \in L(G) \forall i}$
- → construction $A_{\epsilon}, A_G$ par induction
	- $A_{G^+}$ : similaire à la concaténation sauff qu'on ajoute des transition vers l'état initial de $G$
	- $A_E$ : clôture de $A_{\epsilon} \cup A_{G^+}$
![[Pasted image 20251203153801.png]]
