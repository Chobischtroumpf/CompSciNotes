---
title: Analyse a priori
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> L’**analyse a priori** évalue comment les erreurs initiales (arrondi, conditionnement) se propagent **avant** d’exécuter un algorithme.
>
> **Méthodes**:
> 1. **[[Analyse directe]]**: Étudier comment les erreurs d’entrée affectent la sortie ($\delta d → \delta x$).
> 2. **[[Analyse rétrograde]]**: On suppose que la solution numérique est exacte, mais pour un problème légèrement modifié ($x̂ = F(d + δd)$).

> [!example]+ Exemple: Analyse directe
> Pour $F(d) = \sqrt{d} - \sqrt{a}$:
> - **Conditionnement**: $\kappa(d) = \frac{\sqrt{d}(\sqrt{d} + \sqrt{a})}{2|d - a|}$
> - Si $d \approx a$, $\kappa(d)$ devient grand $\Rightarrow$ **problème mal conditionné**.
