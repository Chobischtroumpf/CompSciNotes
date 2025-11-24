---
title: théorème fondamental de programmation linéaire
authors: iamscrambledeggs
tags:
  - Maths
  - Algo
---
# Théorème fondamental

> [!info]+ Définition
>
> Soit un programme linéaire sous forme standard :
>
> $$ \begin{align} &\text{minimize} \quad c^T x \\ &\text{subject to} \quad Ax = b, \quad x \geq 0 \end{align} $$
>
> où :
>
> - la variable $x$ est un vecteur colonne de dimension $n$
> - les coefficients $c^T$ représentent la fonction objectif, un vecteur ligne de dimension $n$
> - les coefficients $A$ représentent les contraintes, une matrice de dimension $m \times n$
> - les coefficients $b$ représentent les contraintes, un vecteur colonne de dimension $m$

> [!abstract]- Théorème "Théorème fondamental de la programmation linéaire"
>
> Soit un programme linéaire sous forme standard, où la matrice $A$ est de dimension $m \times n$ avec $m < n$ et de rang $m$.
>
> 1. Si l'ensemble des solutions réalisables n'est pas vide, alors il existe une solution de base réalisable dans cet ensemble (**Théorème de Carathéodory**).
>
> 2. S'il existe une solution réalisable optimale, alors il existe une solution de base réalisable optimale (**recherche de solutions de base réalisables**).
>
>
> Lors de la résolution du programme, on peut restreindre notre attention au sous-ensemble des solutions de base réalisables de l'ensemble :
>
> $$ {x \mid Ax = b, x \geq 0} $$
>
> Pour un programme avec $n$ variables et $m$ contraintes, il y a au plus :
>
> $$ \binom{n}{m} $$
>
> solutions de base (nombre de façons de sélectionner $m$ parmi $n$ colonnes), soit un nombre fini de possibilités.

> [!tip]+ Remarque
>
> Ce théorème suggère une technique de recherche finie évidente mais terriblement inefficace.
>
> En résumé :
>
> - S'il existe des solutions réalisables dans un tel ensemble, alors il existe une solution de base réalisable dans cet ensemble.
> - S'il existe une solution réalisable optimale, alors il existe une solution de base réalisable optimale.
> - Pour la résolution avec $n$ variables et $m$ contraintes, il y a $\binom{n}{m}$ solutions de base à examiner, ce qui est horriblement inefficace.
## Interprétation

> [!tip]+ Remarque
>
> Il suffit de considérer uniquement les solutions de base réalisables lors de la recherche d'une solution réalisable optimale (la valeur optimale est toujours atteinte pour une telle solution).
>
> Si cette solution est une solution de base, alors c'est une solution de base réalisable optimale.

### Interprétation géométrique

> [!tip]+ Remarque
>
> Il existe un lien entre interprétation algébrique et géométrique : une relation formelle entre solutions de base réalisables et points extrêmes des polyèdres.
>
> Un **polyèdre** est l'intersection d'un nombre fini de demi-espaces fermés :
>
> $$ {x \mid a^T x \leq b} $$
>
> Un polyèdre est convexe car :
>
> - Un demi-espace fermé ${x \mid a^T x \leq b}$ est convexe
> - L'intersection d'une famille quelconque d'ensembles convexes forme un ensemble convexe
>
> **Interprétation :** Si l'on représente graphiquement toutes les contraintes, on obtient un polyèdre. Selon le sommet choisi, on aura une solution de base réalisable (ou pas).
