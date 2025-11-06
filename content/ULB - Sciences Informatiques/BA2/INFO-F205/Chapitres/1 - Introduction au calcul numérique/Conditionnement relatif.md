---
title: Conditionnement relatif
authors: Alessandro Dorigo
tags:
  - Maths
  - CFN
---


> [!info]+ Définition
> Soient $\delta \vec{d}$ une perturbation admissible des données et $\delta \vec{x}$ la modification induite sur la solution du problème $\vec{x} = F(\vec{d})$. On appelle [[Conditionnement#^a58471|conditionnement]] **relatif** de ce problème la quantité:
>
> $$\kappa(\vec{d}) = \lim_{|D|\to 0} \sup_{\delta \vec{d}\in D} \frac{\|\delta \vec{x}\|/\|\vec{x}\|}{\|\delta \vec{d}\|/\|\vec{d}\|}$$
> - **Petit $\kappa(\vec{d})$** → Problème bien conditionné.
> - **Grand $\kappa(\vec{d})$** → Problème mal conditionné.

> [!abstract]- Formule
> Si $F(\cdot)$ est différentiable en $\vec{d}$, on obtient:
> $$\kappa(\vec{d}) = \|F'(\vec{d})\| \frac{\|\vec{d}\|}{\|F(\vec{d})\|}$$

> [!example]+ Exemple
> Considérons $x = d - 1$. Le conditionnement relatif est:
> $$\kappa(d) = \frac{|d|}{|d - 1|}$$
> Ce problème est **mal conditionné** pour $0.999 < d < 1.001$.
