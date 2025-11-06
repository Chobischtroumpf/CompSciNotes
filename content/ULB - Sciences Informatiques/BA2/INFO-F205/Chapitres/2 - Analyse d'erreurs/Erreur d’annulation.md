---
title: Erreur d’annulation
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> Un cas particulier [[Erreur de propagation#^0d8961|d’erreur de propagation]] est l’**erreur d’annulation** survient lorsqu’on **soustrait deux nombres proches**, entraînant une **perte de précision** dans les chiffres significatifs.
>
> **Problème**: Si $x = F(d) = d - a$ et que $d \approx a$, alors:
> $$ \frac{\text{erreur relative sur } d}{\text{erreur relative sur } x} \approx \frac{|d|}{|d - a|} \gg 1 $$
> L'erreur initiale est amplifiée!

^29c241

> [!example]+ Exemple: Annulation catastrophique
> Calcul de $x = d - 1$ pour $d = 1.00098$ et $t = 4$ chiffres significatifs:
> - $d$ arrondi en machine: $1.001$
> - $x$ devient $1.001 - 1 = 0.001$
> - L’erreur passe de **$10^{-5}$ à $10^{-2}$**, donc **amplifiée 1000 fois**.
