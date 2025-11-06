---
title: Well Ordering Principle
authors: Alessandro Dorigo
tags:
  - MathDis
  - TheorieDesNombres
  - Logique
---


> [!info]+ Définition
> Basé sur l'[[Preuve par induction#^33574a|induction]], le **principe du bon ordre** est un outil fondamental pour démontrer les théorèmes vus en **théorie des nombres**.
>
> Il fonctionne de la manière suivante:
>
> **Prédicat**: On considère un [[Logique#^d2e40c|prédicat]] $P(n)$ dépendant d'un paramètre naturel $n$.
>
> **Ensemble des contre-exemples**: On définit l'ensemble $C := \{ n \in \mathbb{N} \mid \neg P(n) \}$.
> - On suppose par l'[[Preuve par l'absurde#^9d7784|absurde]] que $C$ est non vide.
> - Par le principe du bon ordre, il existe un plus petit élément $n_0$ dans $C$.
>
> **Recherche de la contradiction**:
> - On montre que $P(n_0)$ est vrai, contredisant $\neg P(n_0)$.
> - Ou bien, on trouve un $n_1 < n_0$​ tel que $\neg P(n_1)$ est vrai, contredisant le fait que $n_0$ est le plus petit élément de $C$.
>
> **Conclusion**: La contradiction implique que $C$ est vide, donc $P(n)$ est vrai $\forall n \in \mathbb{N}$.

> [!example]+ Exemple: Le théorème fondamental de l'arithmétique
> Tout entier naturel $n > 1$ peut être décomposé en un produit de nombres premiers. Cette décomposition est unique à l'ordre des facteurs près.
>
> **Prédicat**: $P(n)$ : "L'entier $n$ admet une factorisation en nombres premiers".
>
> **Supposition**: On suppose que l'ensemble $C := \{ n \in \mathbb{N} \mid n > 1 \text{ et } \neg P(n) \}$ est non vide.
>
> **Plus petit contre-exemple**: Soit $n_0$ le plus petit élément de $C$.
>
> **Analyse**:
> - Puisque $n_0 > 1$ et $n_0$ n'est pas premier (sinon $P(n_0)$ serait vrai), $n_0$ n'est pas premier.
> - Donc, il existe $x, y \in \mathbb{N}$ tels que $n_0 = x \cdot y$ avec $1 < x, y < n_0$.
>
> **Contradiction**:
> - Par minimalité de $n_0$, $P(x)$ et $P(y)$ sont vrais.
> - Ainsi, $x$ et $y$ se décomposent en produits de nombres premiers.
> - Donc, $n_0 = x \cdot y$ est également un produit de nombres premiers, contredisant $\neg P(n_0)$.
>
> **Conclusion**: $C$ est vide, donc tout entier naturel $n > 1$ admet une factorisation en nombres premiers. □
