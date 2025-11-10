---
title: Modèle statistique
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> Un **modèle statistique** est défini comme une famille de distributions de probabilité:
> $$\mathcal{P} = \{\mathbb{P}_\theta \mid \theta \in \Theta\}$$
>
> où:
> - $\Theta \subseteq \mathbb{R}^k$ est l'espace des **paramètres**,
> - Chaque $P_\theta$ est une loi de probabilité décrivant le comportement d'un vecteur aléatoire $\mathbf{X} = (X_1, \dots, X_n)$, qui représente l'objet d'étude.

^3e66f8

> [!example]+ Exemples
> 1. L’âge de $n$ personnes sélectionnées en Belgique;
> 2. La présence ou absence d’un virus chez $n$ individus.

- Dans le cadre de ce modèle, les $X_i$ sont supposés **[[Indépendantes et Identiquement Distribuées#^1a45cf|indépendants et identiquement distribués (i.i.d.)]]**, avec une loi commune $P_\theta$. La loi commune est obtenue comme le produit des [[Fonction de masse marginale (discrète)#^40b83b|lois marginales]] grâce à l’indépendance.

Un **modèle statistique** permet d'étudier les relations entre les observations et les paramètres $\theta$, par exemple pour estimer $\theta$, une caractéristique de la distribution sous-jacente comme l’[[Espérance (expected value)#^c716f7|espérance]] ou la [[Variance#^4c0c18|variance]].
