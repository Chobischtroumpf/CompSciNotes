---
title: Etat d'un système
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Définition Fondamentale
> Les variables d'état sont un ensemble de variables internes qui permettent de caractériser complètement l'état d'un [[Systèmes dynamiques|système dynamique]] à un instant donné. Elles constituent la "mémoire" du système.

> [!abstract]- Théorème Fondamental des Variables d'État
> La connaissance de l'état à l'instant $t_1$, noté $x(t_1)$, couplée à celle de l'entrée sur l'intervalle $[t_1,t_2]$, est suffisante pour déterminer l'état (et donc la sortie) à l'instant $t_2$.

> [!example]+ Exemple
> Prenons l'exemple d'un réservoir d'eau :
> - La variable d'état est le volume d'eau $x(t)$ dans le réservoir
> - Les entrées sont le débit d'entrée $u_1(t)$ et la section du trou de sortie $u_2(t)$
> - La sortie est le niveau d'eau $y(t)$
>
> Le comportement futur du système dépend :
> - De son état actuel (volume actuel)
> - Des entrées futures (débits futurs)
> - Mais pas de l'historique passé une fois l'état actuel connu

> [!tip]+ Remarque
> L'état d'un système peut être représenté par plusieurs ensembles différents de variables d'état. Le choix des variables n'est pas unique, mais doit être suffisant pour caractériser complètement le système.

La dynamique du système peut alors être décrite par deux fonctions fondamentales :
1. La [[Fonction de transition d'état]]
2. La [[Fonction de transformation de sortie]]

> [!abstract]- Propriétés importantes
> 1. **Causalité** : L'état actuel ne dépend que du passé et du présent, pas du futur
> 2. **Mémoire** : Les variables d'état "résument" toute l'histoire passée du système
> 3. **Prédictibilité** : La connaissance de l'état actuel et des entrées futures permet de prédire l'évolution du système

> [!example]+ Exemple Concret
> Pour une voiture :
> - Variables d'état : position, vitesse, accélération
> - Entrées : position de l'accélérateur, angle du volant
> - Sortie : mouvement de la voiture
>
> Pour prédire où sera la voiture dans 5 secondes, il faut connaître :
> - Son état actuel (position, vitesse, accélération actuelles)
> - Les actions du conducteur pendant ces 5 secondes
> - L'historique avant l'instant présent n'est pas nécessaire une fois l'état actuel connu

Cette représentation d'état est fondamentale car elle permet :
- D'analyser le comportement dynamique du système
- De concevoir des systèmes de contrôle
- De simuler numériquement l'évolution du système

> [!tip]+ Remarque importante
> Plus le système est complexe, plus le nombre de variables d'état nécessaires pour le décrire augmente. C'est ce qu'on appelle la dimension du système.

Cette description par variables d'état est particulièrement puissante car elle permet de traiter de manière unifiée des systèmes très différents (mécaniques, électriques, thermiques, etc.) et de mettre en évidence des propriétés communes comme la stabilité ou la contrôlabilité.
