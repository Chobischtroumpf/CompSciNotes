---
title: structures et satisfaction des formules
authors: Mihai Bors
tags: []
---

# structures et satisfaction des formules
- lorsque $\mathcal{M}, v \vDash \phi$
	- → on dit que $\mathcal{M}, v$ satisfait $\phi$
	- → $\equiv (\mathcal{M},v)$ est un modèle de $\phi$
- lorsque $\phi$ est une formule close
	- → alors sa valeur de vérité dans un couple $(\mathcal{M},v)$ ne dépend pas de $v$
		- pas mention de $v$ alors

## exemples
- prenons $\mathcal{L}_1 = \set{r|_2,c}$
	- formule close suivante
		- $\forall x \cdot r(x,x)$
		- $\land \forall x \cdot \forall y \cdot (r(x,y)\to r(y,x))$
		- $\land \forall x \cdot \forall y \cdot \forall z \cdot (r(x,y) \land r(y,z) \to r(x,z))$
	- → exprime qu'une structure $(D,R,a)$ = modèle de la formule
		- $\Leftrightarrow$ si $R$ est une relation d'équivalence
- $\exists x \cdot \forall y \cdot r(x,y)$ vraie dans $(\mathbb{N},\leq)$ ?
	- oui en prenant $x=0$
- sur le langage $\mathcal{L}_2 = (r|_2,f|_1,g|_2,h|_2,c,d)$
	- formule close
		- $\forall x \cdot \forall z \cdot \exists y \cdot (x = c \lor g(h(x,y),z)=c)$
	- $(\mathbb{R}, \leq, +1, + , \times, 0, 1)$ en est modèle ?
		- oui car nous avons $x = c \lor (x \times y + z = c)$
		- → $x,y,z$ sont dans les réels donc peuvent avoir des valeurs négatives
	- $(\mathbb{N}, \leq, +1, + , \times, 0, 1)$ en est modèle ?
		- pas possible car pas de valeurs négatives possibles
