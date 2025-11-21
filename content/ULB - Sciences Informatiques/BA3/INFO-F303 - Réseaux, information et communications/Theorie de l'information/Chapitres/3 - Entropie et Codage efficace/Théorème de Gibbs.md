---
title: Théorème de Gibbs
authors: Alessandro Dorigo
tags: []
---

> [!abstract]+ Théorème de Gibbs
>
> Pour toute source $S$ de $q$ symboles suivant une loi de probabilité ${p_i}$ et pour toute fonction $f(s_i) = f_i$ réelle positive définie sur ces mêmes symboles, on a :
>
> $$ \sum_{i=1}^{q} f_i \leq 1 \quad \Rightarrow \quad \sum_{i=1}^{q} p_i \log_b \frac{f_i}{p_i} \leq 0 $$
>
> NB : on peut réécrire l'inégalité de droite comme :
>
> $$ -\sum_{i=1}^{q} p_i \log_b f_i \geq -\sum_{i=1}^{q} p_i \log_b p_i = H_b({p_i}) $$
>
> (entropie est le minimum de $-\sum_{i=1}^{q} p_i \log_b f_i$ sur les fonctions $f$ de $L_1$ norme bornée par 1)
## Démonstration (théorème de Gibbs)

> [!tip]+ Remarque
>
> - Il suffit de prouver le résultat pour $b = e$
> - Lemme : $\ln x \leq x - 1$
> - On développe :
>
> $$ \sum_{i=1}^{q} p_i \log_b \frac{f_i}{p_i} \leq \sum_{i=1}^{q} p_i \left(\frac{f_i}{p_i} - 1\right) = \sum_{i=1}^{q} f_i - \sum_{i=1}^{q} p_i \leq 1 - 1 = 0 $$
