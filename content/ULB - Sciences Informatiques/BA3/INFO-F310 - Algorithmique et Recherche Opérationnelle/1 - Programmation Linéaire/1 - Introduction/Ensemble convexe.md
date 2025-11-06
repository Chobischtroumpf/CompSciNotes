---
title: Ensemble convexe
authors: Alessandro Dorigo
tags:
  - Algo
  - Maths
---


> [!info]+ Définition
> Un ensemble $C \subseteq \mathbb{R}^n$ est convexe si toute pair de points $x,y \in C$ vérifie la combinaison convexe $\alpha x + (1-\alpha) y \in C$ pour tout $\alpha \in [0,1]$

- **Interprétation géométrique**: un ensemble $C$ est convexe si toutes paires de points appartenant à $C$ peut être jointe par un segment de droite dont tous les points appartiennent à $C$.

![[Pasted image 20250923112802.png]]

- Un sous-ensemble de $\mathbb{R}$ est convexe si et seulement si ce sous-ensemble est un intervalle.

> [!example]+ Exemples
> - L'ensemble vide $\varnothing$
> - Le singleton $\{x\}$
> - L'espace (n-dim, $n \geq 1$) des nombres réels $\mathbb{R}^n$
> - Un sous-ensemble $I$ de $\mathbb{R}$ est un intervalle si $x, y \in I$ et $x < z < y$ implique $z \in I$
> - La boule unitaire d'une espace vectoriel normé: $\{x \in \mathbb{R}^n \mid \|x\|_p \leq 1, p \geq 1\}$
> - L'ensemble défini par des contraintes d'inégalités linéaires $\{x \in \mathbb{R}^n \mid Ax \leq b\}$, où la matrice $A \in \mathbb{R}^{m \times n}$, et le vecteur $b \in \mathbb{R}^m$
