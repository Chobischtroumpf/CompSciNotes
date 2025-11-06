---
title: Indépendantes et Identiquement Distribuées
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> En statistiques, des [[Variable aléatoire#^dcd8d2|variables aléatoires]] sont dites **i.i.d.** (*independent and identically distributed*) lorsqu'elles remplissent deux conditions:
>
> 1. **Indépendance**: Chaque [[Variable aléatoire#^dcd8d2|variable aléatoire]] est **indépendante** des autres. Cela signifie que la réalisation d'une variable n'affecte pas la probabilité des réalisations des autres.
>
> - Formellement, si $X_1, X_2, \dots, X_n$ sont i.i.d., alors pour tout $x_1, x_2, \dots, x_n$:
>   $$\mathbb{P}(X_1 = x_1, X_2 = x_2, \dots, X_n = x_n) = \mathbb{P}(X_1 = x_1) \cdot \mathbb{P}(X_2 = x_2) \cdots \mathbb{P}(X_n = x_n)$$
>
> 2. **Identiquement distribuées**: Toutes les [[Variable aléatoire#^dcd8d2|variables aléatoires]] suivent la **même distribution**. Cela signifie qu'elles ont la même [[Fonctions de probabilités#Fonction de densité (Probability Density Function - PDF)|fonction de densité]] (ou de [[Fonctions de probabilités#Fonction de masse (Mass Function)|masse]]) de probabilité, ainsi que les mêmes paramètres, comme l'[[Espérance (expected value)#^c716f7|espérance]] et la [[Variance#^4c0c18|variance]].

^1a45cf

- Si les [[Variable aléatoire#^dcd8d2|variables aléatoires]] sont **i.i.d.**, elles garantissent des propriétés asymptotiques (comme la convergence vers la vraie valeur).

> [!tip]
> Les [[Variable aléatoire#^dcd8d2|variables]] ne sont **pas indépendantes** si, par exemple, deux événements sont liés (comme le tirage de cartes sans remise). Elles ne sont pas **identiquement distribuées** si les [[Variable aléatoire#^dcd8d2|variables aléatoires]] suivent des distributions différentes.
