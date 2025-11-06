---
title: Fonction de transformation de sortie
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition mathématique
> La fonction de sortie $h$ détermine la sortie du système à partir de son état. Elle est définie comme :
> $$y(t) = h(t,x(t))$$
> où :
> - $y(t)$ est la sortie du système à l'instant $t$
> - $x(t)$ est l'état du système à l'instant $t$

> [!abstract]- Propriétés importantes
> 1. Pour un système invariant dans le temps, la fonction de sortie ne dépend pas explicitement du temps :
> $$y(t) = h(x(t))$$
> 2. La fonction de sortie est en général plus simple que la fonction de transition d'état car elle n'implique pas d'évolution temporelle

> [!example]+ Exemple
> Pour un réservoir d'eau cylindrique de rayon $R$ :
> $$y(t) = \frac{x(t)}{\pi R^2}$$
> où :
> - $x(t)$ est le volume d'eau (variable d'état)
> - $y(t)$ est le niveau d'eau (sortie)

> [!tip]+ Remarque
> La fonction de sortie représente l'interface observable du système avec l'extérieur. Elle définit ce qui peut être mesuré ou observé directement.
