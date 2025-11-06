---
title: Coloration
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
  - Algo
---


Étant donné un graphe $G$ et un entier $k > 0$, est-il possible d’assigner une couleur $\phi(v) \in \{1, 2, \dots, k\}$ à chaque sommet $v$, c-à-d $\exists \phi : V(G) \rightarrow \{1, 2, \dots, k\}$, de telle sorte que
$$\forall uv \in E(G) : \phi(u) \neq \phi(v) \ \ ?$$

> [!note]
> Ceci est un problème **NP-complet**.
> - P = polynomial (résolubles en temps polynomial)
> - NP = non déterministe polynômial (“vérifiables” en temps poly)
>
> ![[Pasted image 20241001120558.png]]

On a pour cela un simple algorithme: **L'algorithme glouton**.
1. On choisit un ordre pour les sommets $v_1, \dots, v_n$
2. Pour chaque sommet $i = 1 \dots n$:
	- On prend la plus petite couleur disponible: $\phi(v_i) = \min \left\{ j \mid \neg \left( \exists k \in \{ 1, 2, \dots, i-1 \} : \phi(v_k) = j \land v_i v_k \in E \right) \right\}$

- Algorithme naturel et efficace, optimal à condition de connaître un bon ordre!

> [!info]+ Définition
> Le plus petit $k$ pour lequel il existe une $k$-coloration est le nombre chromatique $\chi(G)$.
