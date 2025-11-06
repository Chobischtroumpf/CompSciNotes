---
title: Systèmes dynamiques
authors: Alessandro Dorigo
tags:
  -
---

Je vais vous donner une définition complète et structurée d'un système dynamique.

> [!info]+ Définition mathématique
> Un système dynamique est un t-uple $S = (T,U,\Omega,X,Y,\Gamma,\varphi,h)$ où :
> - $T$ est l'ensemble ordonné des temps
> - $U$ est l'ensemble des entrées possibles
> - $\Omega$ est l'ensemble des fonctions d'entrée admissibles
> - $X$ est l'ensemble des [[Etat d'un système|états]] possibles
> - $Y$ est l'ensemble des sorties possibles
> - $\Gamma$ est l'ensemble des fonctions de sortie
> - $\varphi$ est la [[Fonction de transition d'état|fonction de transition d'état]]
> - $h$ est la [[Fonction de transformation de sortie|fonction de transformation de sortie]]

Cette définition formelle peut être expliquée plus intuitivement :

> [!info]+ Définition intuitive
> Un système dynamique est un système dont l'état évolue au cours du temps selon des règles déterminées, en fonction :
> - De son état actuel
> - Des entrées qu'il reçoit
> - De sa dynamique interne (décrite par les fonctions $\varphi$ et $h$)

Les caractéristiques fondamentales d'un système dynamique sont :
1. La présence d'une mémoire : l'état futur dépend de l'état présent
2. L'évolution temporelle : le système change au cours du temps
3. La causalité : les effets ne peuvent pas précéder les causes

> [!example]+ Exemple Simple
> Un pendule simple est un système dynamique où :
> - Les variables d'état sont la position angulaire $\theta$ et la vitesse angulaire $\dot{\theta}$
> - L'entrée peut être une force extérieure appliquée
> - La sortie peut être la position de la masse
> - Le système évolue selon les lois de la mécanique newtonienne

> [!example]+ Exemple Concret
> Une population de bactéries est un système dynamique où :
> - L'état est le nombre de bactéries
> - Les entrées sont les conditions environnementales (température, nutriments)
> - La sortie peut être la biomasse totale
> - Le système évolue selon des lois de croissance biologique

> [!tip]+ Remarque
> Un système dynamique peut être :
> - À [[Système à temps continu et discret|temps continu ou discret]]
> - [[Systemes linéaires|Linéaire]] ou [[Systèmes non linéaires|non linéaire]]
> - Déterministe ou stochastique
> - Autonome (pas d'entrée externe) ou non autonome

Cette définition met en évidence que les systèmes dynamiques sont un cadre mathématique puissant pour modéliser de nombreux phénomènes naturels, techniques, ou sociaux qui évoluent dans le temps.
