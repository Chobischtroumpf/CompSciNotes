---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

## Exemple: L’énigme des bidons de Die Hard 3
On dispose de deux bidons: l'un de 5 litres et l'autre de 3 litres. Le défi consiste à mesurer exactement 4 litres en utilisant uniquement ces deux bidons.
### Réforme mathématique du problème
Pour analyser ce problème, nous allons le reformuler en termes mathématiques. Généralisons le problème avec deux bidons de capacités $a$ litres et $b$ litres, où $a, b \in \mathbb{N}$ et $a \leq b$ sans perte de généralité.
#### Modélisation par une machine à états
- **États**: Les couples $(x, y)$ où $x$ et $y$ représentent les quantités d'eau dans les bidons de $a$ litres et $b$ litres respectivement. Ainsi, $0 \leq x \leq a$ et $0 \leq y \leq b$.
- **État initial**: $(0, 0)$ (les deux bidons sont vides).
- **Transitions possibles**:
  1. **Remplissage**:
     - Remplir le bidon de $a$ litres:  $(x, y) \rightarrow (a, y)$.
     - Remplir le bidon de $b$ litres:  $(x, y) \rightarrow (x, b)$.
  2. **Vidage**:
     - Vider le bidon de $a$ litres:      $(x, y) \rightarrow (0, y)$.
     - Vider le bidon de $b$ litres:      $(x, y) \rightarrow (x, 0)$.
  3. **Transvasement**:
     - Verser du bidon de $a$ litres dans celui de $b$ litres:
		- Si $x + y \leq b$:                    $(x, y) \rightarrow (0, x + y)$.
		- Sinon:                              $(x, y) \rightarrow (x + y - b, b)$.
     - Verser du bidon de $b$ litres dans celui de $a$ litres:
		- Si $x + y \leq a$:                   $(x, y) \rightarrow (x + y, 0)$.
		- Sinon:                             $(x, y) \rightarrow (a, x + y - a)$.




# Théorèmes
- Pour tout état atteignable $(x, y)$, les quantités $x$ et $y$ appartiennent à l'ensemble $a\mathbb{Z} + b\mathbb{Z}$, c'est-à-dire qu'elles peuvent s'écrire sous la forme $x = ap + bq$ avec $p, q \in \mathbb{Z}$.
![[Pasted image 20240930144212.png]]
![[Pasted image 20240930144227.png]]

- Tout nombre $z \in a\mathbb{Z} + b\mathbb{Z}$ tel que $0 \leq z \leq b$ est un résultat possible.
![[Pasted image 20240930144415.png]]
![[Pasted image 20240930144425.png]]
![[Pasted image 20240930144451.png]]
![[Pasted image 20240930144531.png]]

- Les résultats possibles sont tous les nombres de $a\mathbb{Z} + b\mathbb{Z}$ dans l’intervalle $[0, b]$.
