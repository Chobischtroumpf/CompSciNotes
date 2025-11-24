---
title: Entropie
authors: Alessandro Dorigo
tags:
  - ThInfo
---

> [!info]+ Définition
>
> L'entropie en base $b$ d'une source / variable aléatoire $S$ de distribution $p_1, p_2, \ldots, p_q$ est la **quantité d'information moyenne** :
>
> $$ H_b(S) = H_b(p_1, p_2, \ldots, p_q) = -\sum_{i=1}^{q} p_i \log_b p_i $$
>
> Par continuité, on pose $0 \cdot \log 0 = 0$

> [!abstract]+ Formule : Fonction d'Entropie généralisée
>
> $$ \mathcal{H}_q(p) = -p \log_q \frac{p}{q-1} - (1-p) \log_q(1-p) $$

> [!abstract]+ Entropie d'une source binaire
>
> Pour une source binaire $p_1 = p$ et $p_2 = 1 - p$, on a :
>
> $$ \mathcal{H}_2(p) = -p \log_2 p - (1-p) \log_2(1-p) $$

> [!abstract]+ Longueur moyenne minimum
>
> La longueur moyenne minimum $L_{min}(S)$ d'un code pour une source $S$ de distribution $p_1, p_2, \ldots, p_q$ satisfait :
>
> $$ H_r(S) \leq L_{min}(S) \leq H_r(S) + 1 $$
>
> (rappel : $r$ = taille de l'alphabet)2

> [!tip]+ Borne superieure
>
> La borne superieure d'un code est satisfaite par le [[Code de Shannon]] $\ell_i = \lceil -\log_2 p_i \rceil$. La longueur moyenne vaut :
>
> $$ \sum_{i=1}^{q} p_i \cdot \lceil -\log_2 p_i \rceil \leq \left(-\sum_{i=1}^{q} p_i \log_2 p_i\right) + 1 = H_2({p_1, p_2, \ldots, p_q}) + 1 $$
>
> En particulier, la longueur moyenne minimum d'un code est bornée supérieurement par cette valeur

> [!abstract]+ Borne inférieure
>
> Pour toute source $S$ et pour tout code univoque $K$, la longueur moyenne du code $L_K(S)$ satisfait :
>
> $$ H_r(S) \leq L_K(S) $$
>
> Démonstration (borne inférieure)
> - Notons $\ell_i$ les longueurs des mots de $K$
> - De $\ell_i = -\log_r r^{-\ell_i}$, on a :
>
> $$ H_r(S) - L_K(S) = -\sum_{i=1}^{q} p_i \log_r p_i - \sum_{i=1}^{q} p_i \ell_i $$
>
> $$ = -\sum_{i=1}^{q} p_i \log_r p_i + \sum_{i=1}^{q} p_i \log_r r^{-\ell_i} $$
>
> $$ = \sum_{i=1}^{q} p_i \log_r \frac{r^{-\ell_i}}{p_i} $$
>
> - On a $\sum_{i=1}^{q} r^{-\ell_i} \leq 1$ par l'inégalité de Kraft
> - L'inégalité de Gibbs donne le résultat
