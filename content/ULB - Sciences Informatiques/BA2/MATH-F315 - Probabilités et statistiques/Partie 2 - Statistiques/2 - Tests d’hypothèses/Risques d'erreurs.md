---
title: Risques d'erreurs
authors: Alessandro Dorigo
tags:
  - Stats
---


Soit $\phi$ un [[Test (stats)#^4bc46e|test statistique]] associé à un paramètre $\theta$, une [[Hypothèse (stats)#^0a3543|hypothèse]] nulle $H_0$, et une contre-hypothèse $H_1$. Deux types d'erreurs peuvent survenir lors du test d'hypothèse:
#### 1. **Erreur de première espèce**
L'**erreur de première espèce** consiste à **rejeter l'[[Hypothèse (stats)#^0a3543|hypothèse]] nulle** alors qu'elle est correcte ($\theta \in H_0$).

> [!info]+ Définition (Risque de première espèce)
> Le risque de première espèce, noté $\alpha$, est la probabilité de commettre cette erreur:
>
> $$\mathbb{P}_\theta[RH_0] = \mathbb{P}_\theta[\phi(\mathbf{X}) = 1] = \mathbb{E}_\theta[\phi], \quad \theta \in H_0$$
#### 2. **Erreur de seconde espèce**
L'**erreur de seconde espèce** consiste à **ne pas rejeter l'[[Hypothèse (stats)#^0a3543|hypothèse]] nulle** alors qu'elle est fausse ($\theta \in H_1$).

> [!info]+ Définition (Risque de seconde espèce)
> Le risque de seconde espèce, noté $\beta$, est la probabilité de commettre cette erreur:
>
> $$\mathbb{P}_\theta[NRH_0] = 1 - \mathbb{P}_\theta[\phi(\mathbf{X}) = 1] = 1 - \mathbb{E}_\theta[\phi], \quad \theta \in H_1$$

![[0a46924d3705152a71633d750439aeba.png]]

La probabilité de commettre une erreur de première ou de seconde espèce dépend de la **valeur inconnue** de $\theta$. Ces probabilités sont appelées **risques** associés au [[Test (stats)#^4bc46e|test]].
