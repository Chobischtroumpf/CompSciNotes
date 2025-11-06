---
title: Intervalle de confiance
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> Un **intervalle de confiance** au niveau de confiance $(1-\alpha)$ pour $\theta$ est un intervalle $[I_-(\mathbf{X}), I^+(\mathbf{X}))]$ tel que:
>
> 1. $I^-(\mathbf{X})$ et $I^+(\mathbf{X})$ sont des [[Statistique#^92a060|statistiques]];
> 2. $\mathbb{P}_\theta[I^-(\mathbf{X}) \leq \theta \leq I^+(\mathbf{X})] \geq 1-\alpha \quad \forall \theta \in \Theta$

^5071ba

## IC pour un [[Test unilatéral avec variance spécifiée|test unilatéral avec variance spécifiée]] (loi gaussienne)
> [!abstract]- Énoncé
> ![[Test unilatéral avec variance spécifiée#^280dee]]
> On sait grâce au [[Information de Fisher#^c6b970|lemme de Fisher]] que:
>
> $$\overline{X}^{(n)} \sim \mathcal{N}(\mu_0, \frac{\sigma^2}{n}) \Rightarrow \frac{\overline{X}^n - \mu}{\frac{\sigma}{\sqrt{n}}} \sim \mathcal{N}(0,1)$$
>
> $$\implies \mathbb{P}_\mu \left[ z_{\alpha/2} \leq \frac{\overline{X}^{(n)} - \mu}{\sigma / \sqrt{n}} \leq z_{1-\alpha/2} \right] = 1 - \alpha \quad \forall \mu$$
>
> $$\mathbb{P}_\mu \left[
> \underbrace{\overline{X}^{(n)} - z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}}_{=:I^-(\mathbf{X})}
> \leq \mu
> \leq
> \underbrace{\overline{X}^{(n)} + z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}}_{=:I^+(\mathbf{X})} \right]
> = 1 - \alpha \quad \forall \mu$$
>
> et $\left[I^-(\mathbf{X}), I^+(\mathbf{X})\right] = \left[\overline{X} \pm z_{1-\alpha/2} \frac{\sigma}{\sqrt{n}}\right]$ est un intervalle de confiance pour $\mu$ au niveau de confiance $(1 - \alpha)$.

## IC pour un [[Test unilatéral sans variance spécifiée|test unilatéral sans variance specifiée]] (loi gaussienne)
> [!abstract]- Énoncé
> ![[Test unilatéral sans variance spécifiée#^393696]]
> On sait grâce au [[Information de Fisher#^c6b970|lemme de Fisher]] que:
>
> $$\overline{X}^{(n)} \sim \mathcal{N}(\mu, \frac{\sigma^2}{n}) \quad \text{et} \quad \frac{ns^2}{\sigma^2} \sim \chi_{n-1}^2$$
>
> $$ \implies \mathbb{P}_{\mu, \sigma^2} \left[ t_{n-1; \alpha/2} \leq \frac{\overline{X}^{(n)} - \mu}{S / \sqrt{n}} \leq t_{n-1; 1-\alpha/2} \right] = 1 - \alpha \quad \forall \mu, \sigma^2 $$
>
> $$ \mathbb{P}_{\mu, \sigma^2} \left[
> \underbrace{\overline{X}^{(n)} - t_{n-1; 1-\alpha/2} \frac{S}{\sqrt{n}}}_{=:I^-(\mathbf{X})}
> \leq \mu
> \leq
> \underbrace{\overline{X}^{(n)} + t_{n-1; 1-\alpha/2} \frac{S}{\sqrt{n}}}_{=:I^+(\mathbf{X})} \right]
> = 1 - \alpha \quad \forall \mu, \sigma^2 $$
>
> et $\left[I^-(\mathbf{X}), I^+(\mathbf{X})\right] = \left[\overline{X} \pm t_{n-1; 1-\alpha/2} \frac{S}{\sqrt{n}} \right]$ est un intervalle de confiance pour $\mu$ au niveau de confiance $(1 - \alpha)$.

## IC pour la moyenne d’un échantillon de loi quelconque
> [!abstract]- Énoncé
> Soient $X_1, \dots, X_n$ [[Indépendantes et Identiquement Distribuées#^1a45cf|i.i.d.]] où $\sigma^2 = \text{Var}[X_i] < \infty$. Posons $\mu = \mathbb{E}[X_i]$ et $\overline{X}^{(n)} = \frac{1}{n} \sum_{i=1}^n X_i$.
> On sait grâce au [[Théorème central limite#^3800c6|TCL]] que $\frac{\overline{X}^{(n)} - \mu}{\frac{S}{\sqrt{n}}} \to \mathcal{N}(0,1)$. On a donc que:
>
> $$\mathbb{P}_\mu \left[z_{\alpha/2} \leq \frac{\overline{X}^{(n)} - \mu}{S / \sqrt{n}} \leq z_{1-\alpha/2}\right] \simeq 1 - \alpha \quad \forall \mu$$
>
> $$ \mathbb{P}_\mu \left[
> \underbrace{\overline{X}^{(n)} - z_{1-\alpha/2} \frac{S}{\sqrt{n}}}_{=:I^-(\mathbf{X})}
> \leq \mu
> \leq
> \underbrace{\overline{X}^{(n)} + z_{1-\alpha/2} \frac{S}{\sqrt{n}}}_{=:I^+(\mathbf{X})} \right]
> = 1 - \alpha \quad \forall \mu, \sigma^2 $$
>
> et $\left[I^-(\mathbf{X}), I^+(\mathbf{X})\right] = \left[\overline{X} \pm z_{1-\alpha/2} \frac{S}{\sqrt{n}} \right]$ est un intervalle de confiance pour $\mu$ au niveau de confiance $(1 - \alpha)$.
