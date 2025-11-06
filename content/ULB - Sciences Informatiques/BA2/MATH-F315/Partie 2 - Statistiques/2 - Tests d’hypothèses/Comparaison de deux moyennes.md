---
title: Comparaison de deux moyennes
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Énoncé
> Nous considérons deux échantillons indépendants.
>
> Un premier échantillon $X_1, \dots, X_{n_1}$ i.i.d. avec $\mathbb{E}[X_i] = \mu_1$ et $\text{Var}(X_i) = \sigma_1^2 < \infty$. La [[Moyenne (sample mean)|moyenne]] et [[Variance|variance]] empirique des $X_i$ sont données par
>
> $$\overline{X} = \frac{1}{n_1} \sum_{i=1}^{n_1} X_i \quad \quad s^2_X = \frac{1}{n_1} \sum_{i=1}^{n_1} (X_i - \overline{X})^2$$
>
> Un second échantillon $Y_1, \dots, Y_{n_2}$ i.i.d. avec $\mathbb{E}[Y_i] = \mu_2$ et $\text{Var}(Y_i) = \sigma_2^2 < \infty$. La [[Moyenne (sample mean)|moyenne]] et [[Variance|variance]] empirique des $Y_i$ sont données par
>
> $$\overline{Y} = \frac{1}{n_2} \sum_{j=1}^{n_2} Y_j \quad \quad s^2_Y = \frac{1}{n_2} \sum_{j=1}^{n_2} (Y_j - \overline{Y})^2$$
>
> Un [[Estimateur|estimateur]] naturel de $\mu_2 - \mu_1$ est clairement la différence $\overline{Y} - \overline{X}$ des [[Moyenne (sample mean)|moyennes]] empiriques. Nous considérons ici la comparaison des deux [[Moyenne (sample mean)|moyennes]] $\mu_1$ et $\mu_2$.

> [!abstract]- Tests
> **1. Problèmes de test:**
> $$(i) \
> \begin{cases} \mathcal{H}_0 : \mu_1 - \mu_2 \leq d_0 \\ \mathcal{H}_1 : \mu_1 - \mu_2 > d_0 \end{cases}
> \quad (ii) \
> \begin{cases} \mathcal{H}_0 : \mu_1 - \mu_2 \geq d_0 \\ \mathcal{H}_1 : \mu_1 - \mu_2 < d_0 \end{cases}
> \quad (iii) \
> \begin{cases} \mathcal{H}_0 : \mu_1 - \mu_2 = d_0 \\ \mathcal{H}_1 : \mu_1 - \mu_2 \neq d_0 \end{cases}$$
>
> pour un certain $d_0$ fixé.
>
> **2. Statistiques de test:**
> - Si l'on peut supposer que $\sigma_1^2 = \sigma_2^2$, nous utiliserons:
>   $$T_1 = \frac{\overline{X} - \overline{Y} - d_0}{S \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$
>   avec
>   $$S^2 := \frac{n_1 s_X^2 + n_2 s_Y^2}{n_1 + n_2 - 2}$$
>
> - Si l’homogénéité des [[Variance|variances]] ne peut pas être supposée, on utilise:
>   $$T_2 = \frac{\overline{X} - \overline{Y} - d_0}{\sqrt{\frac{s_X^2}{n_1} + \frac{s_Y^2}{n_2}}}$$
>
> **3. Règle de décision:**
> **Cas gaussien** (lorsque $\mu_1 - \mu_2 = d_0$ et $T_1 \sim t_{n_1 + n_2 - 2}$)
> - $(i) \ RH_0$ au niveau $\alpha$ si $T_1 > t_{n_1 + n_2 - 2; 1-\alpha}$
> - $(ii) \ RH_0$ au niveau $\alpha$ si $T_1 < t_{n_1 + n_2 - 2; \alpha}$
> - $(iii) \ RH_0$ au niveau $\alpha$ si $T_1 > t_{n_1 + n_2 - 2}; 1-\alpha/2$ ou $T_1 < t_{n_1 + n_2 - 2; \alpha/2}$, ou plus simplement $d_0 \in [X - Y \pm t_{n_1 + n_2 - 2; 1 - \alpha/2} \cdot S \cdot \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}]$
>
> **Cas général**
> - $(i) \ RH_0$ au niveau $\alpha$ si $T_2 > z_{1-\alpha}$
> - $(ii) \ RH_0$ au niveau $\alpha$ si $T_2 < z_{1-\alpha}$
> - $(iii) \ RH_0$ au niveau $\alpha$ si $T_2 > z_{1-\alpha/2}$ ou $T_2 < z_{\alpha/2}$
