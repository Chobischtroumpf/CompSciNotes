---
title: Erreur de propagation
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> L'**erreur de propagation** est l'erreur introduite dans la solution d'un problème numérique en raison d'une **perturbation des données d’entrée**. Elle dépend du **[[Conditionnement|conditionnement]] du problème**.
>
> **Formule**: Si $x = F(d)$ est la solution exacte et que $d$ est approchée par $\hat{d} = d(1 + \rho_d)$, alors la solution numérique devient:
> $$ F(\hat{d}) \approx F(d)(1 + \kappa(d)\rho_d) $$
> où $\kappa(d)$ est le **[[Conditionnement|conditionnement]]** du problème et $\rho_d$ [[Erreur relative#^c60666|l’écart relatif]].

^0d8961

- L'[[Erreur relative#^8fa3af|erreur relative]] **peut être amplifiée** si $\kappa(d) > 1$. Si la solution obtenue $F(\hat{d})$ ne peut pas être représentée exactement en machine, l'ordinateur retourne une version arrondie $\hat{x}$: $$ \hat{x} = fl(F(\hat{d})) = x(1 + \kappa(d) \rho_d)(1 + \rho_{F(\hat{d})}) \approx x(1 + \kappa(d) \rho_d + \rho_{F(\hat{d})}) $$

où $\rho_{F(\hat{d})}$ est l’**[[Erreur d’arrondi#^ac2136|erreur d’arrondi]]** sur le résultat final.

> [!example]+ Exemple: Sensibilité aux erreurs d’entrée
> Considérons $F(d) = d - 1$ et une entrée perturbée $\hat{d} = 1.00098$ (arrondi à 4 chiffres).
> L’erreur relative sur les **données** est petite, mais l’erreur sur le **résultat** est amplifiée d’un facteur $\approx 1000$, illustrant le **mauvais [[Conditionnement|conditionnement]]** du problème.
