---
title: Test à Puissance Uniformément Maximale
authors: Alessandro Dorigo
tags:
  - Stats
---


> [!info]+ Définition
> Un **[[Test (stats)#^4bc46e|test]]** $\phi^*$ est dit **à [[Puissance d'un test#^038d20|puissance]] uniformément maximale ($PUM$)** dans la classe des [[Test (stats)#^4bc46e|tests]] de niveau $\alpha$ (pour $H_0$ contre $H_1$) si les deux conditions suivantes sont satisfaites:
>
> 1. **Contrainte de niveau ($\alpha$)**:
> 	$$\mathbb{E}_\theta[\phi^*] \leq \alpha, \quad \forall \theta \in H_0$$
> 	Cela garantit que $\phi^*$ respecte le niveau de significativité fixé.
>
> 2. **Maximisation de la puissance**:
> 	$$\mathbb{E}_\theta[\phi^*] \geq \mathbb{E}_\theta[\phi], \quad \forall \theta \in H_1$$
> 	pour tout autre [[Test (stats)#^4bc46e|test]] $\phi$ respectant la contrainte de niveau ($\mathbb{E}_\theta[\phi] \leq \alpha, \forall \theta \in H_0$).
