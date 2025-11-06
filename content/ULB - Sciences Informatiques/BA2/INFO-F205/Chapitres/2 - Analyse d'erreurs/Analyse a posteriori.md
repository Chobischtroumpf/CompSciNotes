---
title: Analyse a posteriori
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> L’**analyse a posteriori** mesure **l’erreur après exécution**, en comparant la solution numérique $\hat{x}$ avec la vraie solution $x$.
>
> **Approche**:
> - Calcul du **résidu**: $r = F(\hat{x}) - d$
> - Si $r$ est petit, la solution est proche de la vraie.
> #### Relation entre résidu et erreur
> Pour une solution approchée $\hat{x}$, le résidu est défini par :
> $$r = b - A\hat{x}$$
> On peut montrer que l'erreur $e = x - \hat{x}$ est liée au résidu par :
> $$e = A^{-1}r$$
> Ce qui implique :
> $$|e| \leq |A^{-1}||r| \leq \kappa(A)\frac{|r|}{|A|}$$
> Cette relation montre qu'un petit résidu ne garantit pas nécessairement une petite erreur si le conditionnement $\kappa(A)$ est grand.

> [!example]+ Exemple: Vérification de la précision
> On résout $Ax = b$ en machine et obtient $\hat{x}$.
> - Si $A \hat{x} \neq b$, on calcule $r = A \hat{x} - b$.
> - Si $||r||$ est petit, alors $\hat{x}$ est une bonne approximation.
