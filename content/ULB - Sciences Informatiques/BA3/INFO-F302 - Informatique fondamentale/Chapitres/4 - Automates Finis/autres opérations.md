---
title: autres opérations
authors: Mihai Bors
tags: []
---

# autres opérations
- Soient $L,L_1,L_2 \subseteq \Sigma^*$ trois langages
	- $L_1\cdot L_2 = \set{u_1u_2 | u_1 \in L_1 \land u_2 \in L_2}$
		- $\equiv L_1L_2$
	- $L^* = \set{u_1...u_k | k \geq 0, \forall i= 1:k, u_i \in L}$
		- $\epsilon \in L^*, k = 0$
## exemples
- PAIR : mots qui contiennent un nombre pair de 'a'
	- $PAIR = PAIR \cdot \set{\epsilon} \subseteq PAIR\cdot PAIR$ car $\set{\epsilon} \subseteq PAIR$
- Si $L_1 = PAIR$
	- → $L_1L_1 = L_1$
- Si $L_1 = \set{a,b}, L_2 = {a,bb}$
	- → $L_1L_2 = \set{aa,abb,ba,bbb}$
- Si $L = \set{a}$
	- → $L^* = \set{a^n | n \geq 0}$
	- ensemble des mots qu'on peut former avec des lettres de $\Sigma$
