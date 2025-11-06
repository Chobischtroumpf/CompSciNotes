---
title: Degré
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
---


> [!info]+ Définition
> Le **degré** d'un sommet $v$ d'un graphe $G$ est le nombre d’[[Termes Clés#Arête Une connexion non directionnelle.|arêtes]] incidentes a $v$: $$\text{d}(v) := \vert\{w \in V(G)\vert vw \in E(G)\} = \vert\{e \in E(G) \vert v \in e\}\vert$$

^3c01ed

> [!note]
> Pour les graphes [[Graphe dirigé (théorie des graphes)#^29385c|dirigés]], chaque sommet a un degré **entrant** $\deg^-(v)$ et **sortant** $\deg^+(v)$. Tel que le degré $\text{d}(v)$ total d'un sommet est la somme du degré entrant et du degré sortant
>  $$\text{d}(v) = \deg^+(v) + \deg^-(v)$$

> [!example]+ Exemple
> ![[Pasted image 20241001114821.png]]

> [!abstract]- Lemme 3.1.1
> Dans un graphe [[Graphe complet#^673d8c|complet]], le degré de chaque sommet est égal a $\vert V \vert - 1$ car chaque sommet est connecté à tous les autres sommets.

> [!abstract]- Théorème 3.1.2 - Handshaking Lemma
> Dans tout graphe [[Graphe simple#^4ba691|simple]], la somme des degrés des sommets est égale à deux fois le nombre d’arêtes: $$\sum_{v \in V} \text{d}(v)=2\vert E\vert$$
> **Cas de base**
> Aucune arête ne relie les points:
>- Sommets de degrés $0$
>- $0 = 2 \cdot 0$, donc la relation est vérifiée
>
>**Hypothèse de récurrence**
>Supposons que la relation soit vraie pour tout graphe à $n$ arêtes.
>
>**Étape de récurrence**
>Montrons que cela reste vrai pour $n+1$ arêtes:
>- Lorsque nous ajoutons $1$ arête reliant $2$ nœuds, le degré de ces $2$ nœuds augmente de $1$ tandis que le degré des autres nœuds ne change pas.
>- Ainsi, la somme des degrés de tous les nœuds a augmenté de $2$ (soit $1+1$) tandis que le nombre d’arêtes n’a augmenté que de $1$.
>
>Ainsi, pour chaque arête ajoutée, $\sum_{v \in V} \text{d}(v)$ augmente de $2$ et $2\vert E \vert$ aussi. $\square$

^a3f053

> [!abstract]- Lemme 3.1.3
> La somme des degrés sortants et entrants de tous les sommets $v \in V$ équivaut à la taille du graphe: $$\sum_{v \in V} \deg^+(v) + \sum_{v \in V} \deg^-(v) = |E|$$
