---
title: union, intersection
authors: Mihai Bors
tags: []
---

## union, intersection
- Soient $L_1,L_2 \subseteq \Sigma^*$ deux langages
	- $L_1 \cup L_2 = \set{w \in \Sigma^* | w \in L_1 \lor w \in L_2}$
	- $L_1 \cap L_2 = \set{ w \in \Sigma^* | w \in L_1 \land w \in L_2}$

### théorème
- Soient $A, A_1, A_2$ des automates finis sur un alphabet $\Sigma$
- il existe des automates $A_c, U, I$ tq
	- $L(A_c) = \overline{L(A)}$
	- $L(U) = L(A_1) \cup L(A_2)$
	- $L(I) = L(A_1) \cap L(A_2)$

#### clotûre par complément
- si $A = (Q,q_0,F,\delta)$ est complet
	- alors il suffit de prendre $A_c = (Q,q_0, Q \backslash F, \delta)$
- Si $A$ pas complet
	- → il faut le compléter avant

**exercice 1**
![[28bcac389587b429e4dfcf4f1d569f51.png]]
