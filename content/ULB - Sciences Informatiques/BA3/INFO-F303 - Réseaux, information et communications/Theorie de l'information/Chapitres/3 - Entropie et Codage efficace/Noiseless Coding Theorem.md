---
title: Noiseless Coding Theorem
authors: Alessandro Dorigo
tags:
  - ThInfo
---

> [!note]+ Noiseless Coding Theorem
>
> La longueur moyenne minimum $L_{min}(S)$ d'un code pour une source $S$ de distribution $p_1, p_2, \ldots, p_q$ satisfait :
>
> $$ H_r(S) \leq L_{min}(S) \leq H_r(S) + 1 $$
>
> - Borne supérieure atteinte uniquement pour une source dégénérée ($\exists i : p_i = 1$), pour laquelle $H = 0$ et $L = 1$
> - De plus,
>
> $$ \lim_{n \to \infty} \frac{L_{min}(S^n)}{n} = H_r(S) = \frac{H(S)}{\log_q r} $$

> [!tip]+ signification
>
> Si l'on choisit un code _efficace_ pour une source étendue, la longueur moyenne _par symbole_ est _asymptotiquement_ celle de l'entropie de la source :
>
> $$ \lim_{n \to \infty} \frac{L_{min}(S^n)}{n} = H_r(S) $$

> [!tip]+ Démonstration
>
> - $H_r(S) \leq L_{min}(S) \leq H_r(S) + 1$ prouvé ci-dessus
> - Borne supérieure atteinte si $\exists i : p_i = 1$
> - Si $\forall i : p_i < 1$ la borne supérieure est stricte pour le code de Shannon
> - On construit un code pour $S^n$ :
>
> $$ H(S^n) \leq L_{min}(S^n) \leq H(S^n) + 1 $$
>
> $$ nH(S) \leq L_{min}(S^n) \leq nH(S) + 1 $$
>
> $$ H(S) \leq \frac{L_{min}(S^n)}{n} \leq H(S) + 1/n $$
>
> et donc $\lim_{n \to \infty} \frac{L_{min}(S^n)}{n} = H(S)$, par le théorème du sandwich
