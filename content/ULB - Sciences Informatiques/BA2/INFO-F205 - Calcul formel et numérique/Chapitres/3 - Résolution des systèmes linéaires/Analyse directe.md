---
title: Analyse directe
authors: Alessandro Dorigo
tags:
  -
---


L'analyse directe suppose que les perturbations des données $\delta A$ et $\delta b$ introduisent des modifications dans la matrice $A$ et le vecteur $b$ : $$A \rightarrow A + \delta A, \quad b \rightarrow b + \delta b$$

Ces perturbations entraînent une modification de la solution : $$(A + \delta A)(x + \delta x) = b + \delta b$$

> [!abstract]- Analyse directe à priori
> Si $A$ est une matrice inversible et $|A^{-1}||\delta A| < 1$, alors : $$\frac{|\delta x|}{|x|} \leq \frac{\kappa(A)}{1 - \kappa(A)\frac{|\delta A|}{|A|}}\left(\frac{|\delta b|}{|b|} + \frac{|\delta A|}{|A|}\right)$$ où $\kappa(A) = |A||A^{-1}|$ est le conditionnement de $A$.
> Dans le cas particulier où $\delta A = 0$ (seul le second membre est perturbé), on obtient la relation simplifiée : $$\frac{1}{\kappa(A)}\frac{|\delta b|}{|b|} \leq \frac{|\delta x|}{|x|} \leq \kappa(A)\frac{|\delta b|}{|b|}$$
