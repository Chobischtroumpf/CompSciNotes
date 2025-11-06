---
title: Élimination de Gauss
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition
> L'élimination de Gauss est une méthode directe pour transformer un système linéaire en un système triangulaire équivalent.

> [!tip]+ Remarque
> Deux systèmes linéaires sont équivalents s'ils ont la même solution. On ne change pas la solution du système quand :
> - on inverse deux lignes
> - on multiplie une équation par une constante
> - on ajoute à une équation donnée une combinaison linéaire des autres équations
> Les multiplicateurs sont définis par :
> $$m_{ik} = \frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}, \quad i = k+1, \ldots, n$$
> où $a_{kk}^{(k)}$ est appelé le pivot.

> [!abstract]- "Complexité de Gauss"
> L'élimination de Gauss demande :
>
> - $\frac{n(n-1)}{2}$ divisions
> - $\frac{n^3}{3} - \frac{n}{3}$ multiplications
> - $\frac{n^3}{3} - \frac{n}{3}$ additions (ou soustractions)
>
> Au total, la complexité est de $\frac{2n^3}{3} + \frac{3n^2}{2} - \frac{7n}{6}$ opérations flottantes.
