---
title: Problème de routage
authors: Alessandro Dorigo
tags:
  - MathDis
  - Algo
  - Network
---


> [!info]+ Énoncé
> John veut envoyer un paquet à Bob à travers un [[Réseaux de communication#^026870|réseau de communication]] constitué de $N$ points d'entrée et $N$ points de sortie, reliés par des commutateurs.
>
> Le paquet de John part du terminal de John (point d'entrée $\text{in}_k$) et doit atteindre le terminal de Bob (point de sortie $\text{out}_{\pi(k)}$) en suivant un [[Chemin#^377ffc|chemin]] à travers le [[Réseaux de communication#^026870|réseau]].
>
> Le défi est de trouver $N$ [[Chemin#^377ffc|chemins]] distincts, chacun reliant un point d'entrée à un point de sortie spécifique, en minimisant les conflits ([[Congestion#^4df71b|congestion]]) et la [[Chemin#^dd07e6|longueur]] des trajets, tout en garantissant que chaque paquet arrive à sa destination correcte sans interférence.

^fe8a80

> [!info]+ Définition
> Une **instance du problème de routage** sur un [[Réseaux de communication#^026870|réseau de communication]] de taille $N \times N$ consiste en une permutation $\pi$ *bijective* des indices ${0, 1, ..., N-1}$. Chaque permutation représente l'association entre les points d'entrée et de sortie du réseau.

> [!info]+ Définition
> Une **solution** à un problème de routage est la sélection de $N$ [[Chemin#^377ffc|chemins]] $P^\pi_0, P^\pi_1, ..., P^\pi_{N-1}$, où chaque $P^\pi_k$ est un [[Chemin#^377ffc|chemin]] dirigé allant du point d'entrée $\text{in}_k$ au point de sortie $\text{out}_{\pi(k)}$, pour tout $k \in {0, 1, ..., N-1}$.
