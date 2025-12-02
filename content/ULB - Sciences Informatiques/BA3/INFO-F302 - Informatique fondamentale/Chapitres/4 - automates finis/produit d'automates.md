---
title: produit d'automates
authors: Mihai Bors
tags: []
---

# Produit d'automates
- _pré-automate_ sur $\Sigma (Q,q_0,\delta)$
	- $Q$ : un ensemble fini
	- $q_0 \in Q$
	- $\delta : Q \times \Sigma \to Q$ une fonction

- Soient $A_1 = (Q_1,q_0^1,F_1,\delta_1), A_2 = (Q_2,q_0^2, F_2, \delta_2)$ sur $\Sigma$
	- $A_1 \otimes A_2 = (Q_1 \times Q_2, (q_0^1, q_0^2), \delta_{12})$
		- $(q_1,q_2) \in Q_1 \times Q_2$
		- $\forall \sigma \in Sigma$
			- $\delta_{12}((q_1,q_2), \sigma) = \begin{cases} \text{indef si } \delta_1(q_1,\sigma) \text{ pas def } \\ \text{indef si } \delta_2(q_2,\sigma) \text{ pas def }\\ (\delta_1(q_1,\sigma), \delta_2(q_2, \sigma)) \text{ sinon } \end{cases}$
## exemple 1
![[524d4b1205b553a4ed4d58c9ceadc456.png]]
- Soient
	- $L(A_1)$ : ensemble des mots qui contiennent un nb pair de $b$
	- $L(A_2)$ : ensemble des mots qui contiennent un nb pair de $a$
- toute exécution de $A_1 \otimes A_2$ sur un mot $w$ simule en parallèle l'exécution de $w$ ainsi que celle de $A_2$
	- ex. $w= abba$
		- $A_1: e_1 = p_0 ap_0bp_1bp_0ap_0$
		- $A_2 : e_2 = q_0aq_1bq_1bq_1aq_0$
		- $A_1 \otimes A_2 : (p_0,q_0)a(p_0,q_1)b(p_1,q_1)b(p_0,q_1)a(p_0,q_0)$
- → comment définir apd du produit, un automate qui accepte
	- $L(A_1) \cap L(A_2)$
		- → $F_{\cap} = F_1 \times F_2$ pour états finaux
	- $L(A_1) \cap L(A_2)$
		- → $F_{\cup}=(F_1 \times Q_2) \cup (Q_1 \times F_2)$ pour états finaux

### clôture par intersection
![[275ad7e1ccfe561716d006728038b72b.png]]

### clôture par union
![[1b1a29e704dd29d04b7ad59a8dea1d30.png]]
## cloture par union et intersection
- Soient
	- $A_1 = (Q_1,q_0^1,F_1,\delta_1), A_2 = (Q_2,q_0^2, F_2, \delta_2)$ sur $\Sigma$
	- $A_1 \otimes A_2 = (Q_1 \times Q_2, (q_0^1, q_0^2), \delta_{12})$, pré-automate produit
- Si
	- $A_1,A_2$ sont complets
	- $U = (Q_1 \times Q_2, (q_0^1, q_0^2), (F_1 \times Q_2) \cup (Q_1 \times F_2), \delta_{12})$
- alors
	- $L(U) = L(A_1) \cup L(A_2)$
- Si
	- $I = (Q_1 \times Q_2, (q_0^1, q_0^2), F_1 \times F_2, \delta_{12})$
- alors
	- $L(I) = L(A_1)\cap L(A_2)$
