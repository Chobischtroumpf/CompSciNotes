---
title: Graphe (théorie des graphes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
---


Formellement appris en `MATH-F307`. Pour les graphes vus de manière algorithmique, voir [[Graphe (algorithmique)]].

> [!info]+ Définition
> Un **graphe** est un couple $G = (V,E)$ ou $V$ est un ensemble fini de sommets et $E$ un ensemble fini d’arêtes.

^ca541f

> [!note]+ Incidence & Adjacence
> Chaque arête est une paire de sommets $e = \{u,v\} \Leftrightarrow e = uv$.
> - On dit que $e = \{u,v\}$ et $v$ sont **incidents**;
> - Si $\{u,v\} \in E$, on dit que $u$ et $v$ sont **adjacents**.

^230773

> [!example]+ Exemple
> ![[Pasted image 20241001114539.png]]
## Types de graphes
- [[Graphe simple (théorie des graphes)]]
- [[Graphe dirigé (théorie des graphes)]]
- [[Graphe biparti]]
- [[Graphe planaire]]
- [[Graphe connexe]]
## Représentations d'un graphe (matrices)
- Matrice d'adjacence: [[Matrice d'adjacence#^17ebc9]]
- Matrice d'incidence [[Matrice d'incidence#^3bcff9]]
# Étude d'un cas via les graphes: Statistiques du sexe
**Énoncé:** Dans une population hétérosexuelle donnée, qui a, en moyenne, plus de partenaires (au cours d’une vie)? Les hommes ou les femmes?
- “L’homme moyen a 20 partenaires du sexe opposé (au cours d’une vie), et la femme moyenne seulement 6.”
- Une disparité de 233%!

Modélisons la situation avec un graphe.

|   ![[Pasted image 20241001115421.png]]   | Graphe Biparti<br>------------------------------------------------------------------------------------------------ |
| :--------------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| ![[Pasted image 20241001115428.png]]<br> |                                                                                                                    |
$M_H :=$ degré moyen d'un $H$
$M_F :=$ degré moyen d'une $F$
$$M_H = \frac{\sum_{v \in V_H}d(v)}{\vert V_H\vert} = \frac{\vert E \vert}{\vert V_H \vert}$$
$$M_F = \frac{\sum_{v \in V_F}d(v)}{\vert V_F\vert} = \frac{\vert E \vert}{\vert V_F \vert}$$
$$\frac{M_H}{M_F} = \frac{\vert E \vert / \vert V_H \vert}{\vert E \vert / \vert V_F \vert} = \frac{\vert V_F \vert}{\vert V_H \vert} \approx 1.0325$$
