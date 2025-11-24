---
title: Fonction de transition d'état
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition mathématique
> La fonction de transition d'état $\varphi$ décrit l'évolution de l'état du système dans le temps. Elle est définie comme :
> $$x(t) = \varphi(t,t_0,x^0,u(·))$$
> où :
> - $x(t)$ est l'état du système à l'instant $t$
> - $t_0$ est l'instant initial
> - $x^0$ est l'état initial à l'instant $t_0$
> - $u(·)$ est la fonction d'entrée sur l'intervalle $[t_0,t]$

> [!abstract]- Théorème des propriétés fondamentales
> Une fonction de transition d'état doit satisfaire deux propriétés :
> 1. Propriété identité : $\varphi(t_0,t_0,x^0,u(·)) = x^0$
> 2. Propriété semi-groupe : $\varphi(t_2,t_0,x^0,u(·)) = \varphi(t_2,t_1,\varphi(t_1,t_0,x^0,u(·)),u(·))$

> [!example]+ Exemple
> Pour un réservoir d'eau avec débit d'entrée $u_1$ et section de sortie $u_2$ :
> $$x(t) = max(0, x(t-\Delta) + (u_1(t-\Delta) - u_2(t-\Delta)\sqrt{2g\frac{x(t-\Delta)}{\pi R^2}})\Delta)$$
> où $x(t)$ est le volume d'eau à l'instant $t$

> [!tip]+ Remarque
> La fonction de transition définit entièrement la dynamique du système : connaissant l'état initial et les entrées, on peut déterminer tout état futur.
