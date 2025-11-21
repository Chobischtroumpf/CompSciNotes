---
title: Propriétés de l'Entropie
authors: Alessandro Dorigo
tags: []
---


> [!abstract]+ Propriétés de l'entropie
>
> 1. $H$ est **positive** : $H(p_1, \ldots, p_q) \geq 0$
> 2. $H(p_1, \ldots, p_q) = H(p_1, \ldots, p_q, 0)$
> 3. $H(p_1, \ldots, p_q)$ est **continue et symétrique** en ses $q$ variables
> 4. $H(p_1, \ldots, p_q) \leq H\left(\frac{1}{q}, \ldots, \frac{1}{q}\right)$
> 5. $H$ est **cohérente** : $H(p_1, \ldots, p_q) = H((p_1 + p_2), p_3, \ldots, p_q) + (p_1 + p_2)H\left(\frac{p_1}{p_1 + p_2}, \frac{p_2}{p_1 + p_2}\right)$
> 6. On a $0 \leq H_b(S) \leq \log_b q$ ; entropie nulle ssi $\exists i : p_i = 1$ ; entropie maximale ssi $\forall i : p_i = \frac{1}{q}$
>
> NB : propriétés 1-5 définissent l'entropie
