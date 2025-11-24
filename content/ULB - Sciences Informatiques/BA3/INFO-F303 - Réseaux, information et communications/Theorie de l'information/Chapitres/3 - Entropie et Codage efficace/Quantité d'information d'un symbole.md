---
title: Quantité d'information d'un symbole
authors: Alessandro Dorigo
tags: []
---


> [!info]+ Définition
>
> Fonction de la probabilité associée au symbole :
>
> $$\mathcal{I}^*({s_i}) = \mathcal{I}(p_i)$$
>
> que l'on veut :
>
> - Positive : $\mathcal{I}(p_i) \geq 0$
> - Additive : $\mathcal{I}^*({s_i, s_j}) = \mathcal{I}(p_i \cdot p_j) = \mathcal{I}(p_i) + \mathcal{I}(p_j)$
> - Continue

> [!abstract]+ Formule et Démonstration
>
> $$\mathcal{I}(p) = -\log_b p, \quad b > 1$$
>
> On montre $\mathcal{I}(p^\alpha) = \alpha \cdot \mathcal{I}(p)$ pour tout $\alpha \in \mathbb{R}$
>
> - Vrai pour $\alpha = n \in \mathbb{Z}$, par l'axiome d'additivité
> - S'étend à $\alpha = 1/n$ avec $n \in \mathbb{Z}$ par manipulations
> - S'étend à $\alpha \in \mathbb{Q}$
> - S'étend à $\alpha \in \mathbb{R}$ par continuité
>
> On déduit $\mathcal{I}(p) = k \ln p$
>
> - On a $\mathcal{I}(1) = \alpha\mathcal{I}(1)$ $\forall\alpha$ donc $\mathcal{I}(1) = 0$
> - $\mathcal{I}(e^{-1})$ détermine $\mathcal{I}(p) = \mathcal{I}(e^{\ln p}) = -\mathcal{I}(e^{-1}) \cdot \ln p$ $\forall p$
>
> De plus $k < 0$ car $\mathcal{I}(p)$ positif et $p \leq 1$

> [!tip]+ Remarque
>
> Corollaire (Shannon, 1948) :
>
> $$\mathcal{I}(p) = \mathcal{I}_b(p) = -\log_b p$$
>
> avec $b > 1$
>
> Plus d'information dans un "z" (faible probabilité) que dans un "e" (grande probabilité)
