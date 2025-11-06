---
title: Comparaison de deux proportions
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Énoncé
> L’expérience considérée ici se compose de deux [[Loi Bernoulli|schémas de Bernoulli]] indépendants
>
> $$X_1, \dots, X_{n_1} \ \text{i.i.d.} \ \text{Bin}(1;p_1); p_1 \in (0,1)$$
> $$Y_1, \dots, X_{n_2} \ \text{i.i.d.} \ \text{Bin}(1;p_2); p_2 \in (0,1)$$
>
> Dans ce schéma, nous considérons la comparaison des deux proportions $p_1$ et $p_2$.

> [!abstract]- Tests
> **1. Problèmes de test:**
> $$(i) \
> \begin{cases} \mathcal{H}_0 : p_1 - p_2 \leq 0 \\ \mathcal{H}_1 : p_1 - p_2 > 0 \end{cases}
> \quad (ii) \
> \begin{cases} \mathcal{H}_0 : p_1 - p_2 \geq 0 \\ \mathcal{H}_1 : p_1 - p_2 < 0 \end{cases}
> \quad (iii) \
> \begin{cases} \mathcal{H}_0 : p_1 - p_2 = 0 \\ \mathcal{H}_1 : p_1 - p_2 \neq 0 \end{cases}$$
>
> **2. Statistiques de test:**
> - Avec un [[Estimateur|estimateur]] "naturel", sans biais de la différence $p_1 - p_2$ donné par $\hat{p_1} - \hat{p_2}$, où $\hat{p_1} = n_1^{-1} \sum_{i=1}^{n_1} X_i$ et $\hat{p_2} = n_2^{-1} \sum_{j=1}^{n_2} Y_j$, on a:
>
>   $$T = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1 - \hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$$
>
>   avec
>
>   $$\hat{p} := \frac{\sum_{i=1}^{n_1} X_i + \sum_{j=1}^{n_2} Y_j}{n_1 + n_2} = \frac{n_1 \hat{p}_1 + n_2 \hat{p}_2}{n_1 + n_2}$$
>
> **3. Règle de décision (sous $p_1 = p_2, T \approx \mathcal{N}(0,1)$ avec $n_1$ et $n_2$ grands):**
> - $(i) \ RH_0$ au niveau $\alpha$ si $T > z_{1-\alpha}$
> - $(ii) \ RH_0$ au niveau $\alpha$ si $T < z_\alpha$
> - $(iii) \ RH_0$ au niveau $\alpha$ si $T \notin [\pm z_{1-\alpha/2}]$
