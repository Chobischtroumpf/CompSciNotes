---
title: exemple 2
authors: Mihai Bors
tags: []
---

# exercice 2
- Soient
	- $\mathcal{L}= \set{f}$
		- $f$ fonction binaire
	- $\phi$ formule de $\mathcal{L}$ tq $\phi \equiv \exists y \cdot z = f(x,y)$
- → $\phi$ vraie dans la structure de $\mathcal{M}$ en utilisant la valuation $v$

1. soient
	- $\mathcal{M}=(D\equiv \mathbb{N}, f \equiv +)$
	- $v \equiv (x \mapsto 5, z \mapsto 3)$
	→ réponse : $\exists y \in \mathbb{N} \cdot 3 = 5 + y$ ? NON ($y = -2 \not \in \mathbb{N}$)
2. soient
	- $\mathcal{M}=(D\equiv \mathbb{Z}, f \equiv +)$
	- $v \equiv (x \mapsto 5, z \mapsto 3)$
	→ réponse : oui car $y=-2 \in \mathbb{Z}$
3. soient
	- $\mathcal{M}=(D\equiv \mathbb{N}, f \equiv \times)$
	- $v \equiv (x \mapsto 5, z \mapsto 3)$
	→ réponse : $\exists y \in \mathbb{N} \cdot 3 = 5 \times y$ ? NON ($y = 3/5 \not \in \mathbb{N}$)
4. soient
	- $\mathcal{M}=(D\equiv \mathbb{Z}, f \equiv \times)$
	- $v \equiv (x \mapsto 5, z \mapsto 3)$
	→ réponse : même chose que pour la question 3
5. soient
	- $\mathcal{M}=(D\equiv \mathbb{Z}_6, f \equiv \times)$
	- $v \equiv (x \mapsto 5, z \mapsto 3)$
	→ réponse : $\exists y \in \mathbb{Z}_6 \cdot 3 =_6 5 \times y$ ? OUI ($y = 3$ car $5 \times 3 =_6 3$)
		vérifier car $\mathbb{Z}_6$ n'est pas un corps
