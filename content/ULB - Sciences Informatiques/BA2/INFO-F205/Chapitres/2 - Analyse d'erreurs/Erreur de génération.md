---
title: Erreur de génération
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> L'**erreur de génération** est l’erreur introduite **au fil des calculs** lors de la résolution d’un problème numérique. Elle dépend de **l’algorithme utilisé** et de la manière dont les [[Erreur d’arrondi#^ac2136|erreurs d’arrondi]] se propagent.
>
> **Propagation dans un algorithme en plusieurs étapes**:
> $$ x_n = F_n(F_{n-1}(\dots F_1(d) \dots )) $$
>
> Si chaque opération génère une [[Erreur d’arrondi#^ac2136|erreur d’arrondi]] $\rho_i$, alors l’erreur finale est amplifiée selon:
> $$ \hat{x} \approx x(1 + \rho_n + \kappa_n \rho_{n-1} + \dots + \kappa_n \dots \kappa_2 \rho_1) $$
>
> ![[Pasted image 20250221115102.png]]

^d42576

> [!tip]+ Remarque
> Cette erreur est liée avec la [[Stabilité#^f6ba30|stabilité]] de l’algorithme.

> [!example]+ Exemple: Mauvaise propagation des erreurs
> Supposons qu’on veut calculer $e^d - 1$ avec:
> 1. **Algorithme direct**: $F(d) = e^d - 1$
> 2. **Algorithme en étapes**: $x_1 = e^d$, puis $x_2 = x_1 - 1$
>
> Le second algorithme produit une erreur plus grande car la **soustraction de 1** amplifie l’erreur d’arrondi accumulée sur $e^d$.
