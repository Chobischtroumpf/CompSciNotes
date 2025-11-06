---
title: Estimateur efficace
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition (Variance)
> Un estimateur $\hat{\theta}$ de $\theta$ est dit **efficace** si:
>
> 1. Son [[Biais#^74266c|biais]] est nul, et
> 2. Sa [[Variance#^4c0c18|variance]] atteint uniformément la borne de [[Théorème de Cramér-Rao (Inégalité)#^767ee4|Cramér-Rao]]:
>
> $$\text{Var}_\theta(\hat{\theta}) = \frac{1}{\mathcal{I}(\theta)}, \quad \forall \theta \in \Theta$$

^2d1207
> [!info]+ Définition ($\text{EQM}$)
> Un estimateur $\hat{\theta}$ de $\theta$  est dit **efficace** si son [[Écart quadratique moyen#^091951|écart quadratique moyen]] atteint uniformément la borne de [[Théorème de Cramér-Rao (Inégalité)#^767ee4|Cramér-Rao]]:
>
> $$\mathbb{E}_\theta[(\hat{\theta} - \theta)^2] = \frac{1}{\mathcal{I}(\theta)} \quad \forall \theta \in \Theta$$

> [!tip]+ Remarques
> 1. La borne de [[Théorème de Cramér-Rao (Inégalité)#^767ee4|Cramér-Rao]] impose: $\frac{1}{\mathcal{I}(\theta)} \leq \text{Var}_\theta(\hat{\theta}) \leq \text{EQM}_\theta(\hat{\theta})$. Ainsi, si $\text{EQM}_\theta(\hat{\theta}) = \frac{1}{\mathcal{I}(\theta)}$, alors $\text{EQM}_\theta(\hat{\theta}) = \text{Var}_\theta(\hat{\theta})$. Par conséquent, **un estimateur biaisé ne peut pas être efficace.**
> 2. Un estimateur efficace de $\theta$ est à [[Variance#^4c0c18|variance]] **uniformément minimale** dans la classe des [[Estimateur sans biais#^a4d3b2|estimateurs sans biais]] de $\theta$.
> 3. **Attention**: La réciproque n’est pas vraie. Il arrive que la borne de [[Théorème de Cramér-Rao (Inégalité)#^767ee4|Cramér-Rao]] soit inatteignable, même pour un [[Estimateur sans biais#^a4d3b2|estimateur sans biais]].

> [!example]+ Exemples
> ![[Pasted image 20241125104902.png]]
> ![[Pasted image 20241125104918.png]]
> ![[Pasted image 20241125104928.png]]
