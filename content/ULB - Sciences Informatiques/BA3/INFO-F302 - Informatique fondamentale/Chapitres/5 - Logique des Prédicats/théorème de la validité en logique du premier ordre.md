---
title: théorème de la validité en logique du premier ordre
authors: Mihai Bors
tags: []
---


# théorème de la validité en logique du premier ordre
- le problème de la validité en logique du premier ordre est indécidable
## preuve (pas à l'examen askip)
- idée: réduire problème au PCP

### considérations
- nous considérons
	- $\mathcal{L} = (p, =)$
		- langage du premier ordre
		- $p$ prédicat binaire
	- $f_0,f_1$ : symboles de fonction unaires
	- $a$ : symbole de constante
- étant donné
	- un mot $u$ sur $\Sigma$
	- un terme $g$
- → définit $t_u(g)$ inductivement par
	- $t_{\epsilon}(g)= g$
	- $t_{bv}(g) = f_b(t_v(g)), b \in \set{0,1}, v \in \set{0,1}^*$

- remarque
	- $\forall u,v \in \set{0,1}^*, g : t_{uv}(g) = t_u(t_v(g)) \land t_u(g) = t_v(g) \Leftrightarrow u=v$

- Soit $I = \set{(u_1,v_1),...,(u_n,v_n)}$ une instance de PCP
	- → construire une formule $\phi_I$ de la logique du 1er odre sur le langage $L$
	- → mq $\phi_I$ est valide $\Leftrightarrow$ I a une solution
	- → $\phi_I = (\rho \land \sigma) \to \tau$

### étape 1
$$
\rho \equiv p(t_{u_1}(a), t_{v_1}(a))\land p(t_{u_2}(a),t_{v_2}(a)) \land ... \land p(t_{u_n}(a),t_{v_n}(a))
$$
- → on met dans la relation $p$ les termes qui correspondent aux paires de mots
	- on peut étendre cette relation aux concaténations (paires à paires) de couples de mots de $I$
	- en particulier : si $x$ et $y$ sont en relation
		- → on peut concaténer $u_i$ à $x$ et $v_j$ à $y$, pourvu que $i=j$
		- $\sigma \equiv \forall x \forall y \cdot (p(x,y) \to \wedge_{i=1}^n  p(t_{u_i}(x), t_{v_i}(y)))$
		- $\tau$ : existence  de 2 éléments égaux en relation
		- $\tau \equiv \exists z \cdot p(z,z) \land z \neq a$
- → cette réduction est effective
	- on peut écrire un algo qui l'implémente
- → on doit mq elle est correcte

### étape 2
- en gros, on essaye de mq que si PCP a une solution alors il y a une solution pour le prb de validité de logique du premier ordre associé

- sup que $I$ a une solution $i_1,...,i_k$ et mq $\phi_I$ est valide
- → soit $\mathcal{M}$ une structure sur $L$
- Supp $\mathcal{M} \vDash \rho \land \sigma$
	- par hyp, on sait que : $u_{i_1}...u_{i_k} = v_{i_1}...v_{i_k}$
- → donc $t_{u_{i_1}...u_{i_k}}(a) = t_{v_{i_1}...v_{i_k}}(a)$
- → on en déduit que :
	- $t_{u_{i_1}}(t_{u_{i_2}}(...(t_{u_{i_k}}(a))))=t_{v_{i_1}}(t_{v_{i_2}}(...(t_{v_{i_k}}(a))))$
	- → notons $g$ ce terme
- par hyp
	- $\mathcal{M} \vDash p(t_{u_{i_k}}, t_{v_{i_k}})$
	- $\mathcal{M} \vDash \sigma$
- on obtient
	- $\mathcal{M} \vDash p(t_{u_{i_{k-1}}}(t_{u_{i_k}}(a)), t_{v_{i_{k-1}}}(t_{v_{i_k}}(a)))$
	- → plus généralement : $\mathcal{M} \vDash p(g,g)$
	- → donc $\mathcal{M} \vDash \exists z \cdot p(z,z)$
	- → on peut supposer $z \neq a$ car $k\geq 1$
- → donc $\mathcal{M} \vDash \exists z \cdot p(z,z) \land z \neq a$

### étape 3
- on fait la chose de l'autre sens que de l'étape 2

- supp $\phi_I$ est valide
	- → mq $I$ a une solution
- on définit une structure $H$
	- son domaine : ensemble des termes clos sur $L$
	- fonctions et constantes sont interprétées par elles-mêmes
		- $f^H(t) = f(t)$
	- l'interprétation $p^H$ de $p$ est définit inductivement
		- $p^H(a,a) = 1$ pour tous termes clos $h$ et $g$
		- $p^H(t_{u_i}(g),t_{v_j}(h)) = 1 \Leftrightarrow i = j \land p^H(g,h) =1$
- → $H \vDash \rho \land \sigma$
	- donc $H \vDash \tau$ puisque $\phi_I$ est valide
- Donc il existe un terme clos $t$ tq
	- $H \vDash p(t,t) \land t \neq a$
- par déf de $H$
	- facile de voir que $t$ se décompose nécessaireemnt en
		- $t_{u_{i_1}}(t_{u_{i_2}}(...(t_{u_{i_k}}(a))))=t_{v_{i_1}}(t_{v_{i_2}}(...(t_{v_{i_k}}(a))))$
	- → donc
		- $u_{i_1}...u_{i_k} = v_{i_1}...v_{i_k}$
		- $I$ a une solution
