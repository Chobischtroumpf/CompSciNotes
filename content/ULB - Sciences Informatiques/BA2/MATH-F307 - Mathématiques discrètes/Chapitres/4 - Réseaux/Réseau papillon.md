---
title: Réseau papillon
authors: Alessandro Dorigo
tags:
  - MathDis
  - Network
  - Graphe
---


> [!info]+ Définition
> Un **réseau papillon** est un [[Réseaux de communication#^026870|réseau de communication]] structuré de manière à optimiser la [[Taille (commutateur)#^507117|taille]], le [[Nombre de commutateurs#^7a99a9|nombre de commutateurs]] et la [[Congestion#^5c306c|congestion]]. Il s'agit d'un [[Réseaux de communication#^026870|réseau]] à plusieurs niveaux où chaque entrée $x$ est reliée à chaque sortie $y$ par un [[Chemin#^377ffc|chemin]] unique et dirigé.

^5e9ebc

On peut décrire la forme du réseau:
- Au premier niveau, chaque entrée est connectée à deux commutateurs du niveau suivant.
- À chaque niveau, les commutateurs répartissent les chemins de manière croisée, permettant de diriger les données vers différents commutateurs du niveau suivant.
- Finalement, chaque entrée est connectée à une sortie unique via un seul chemin dirigé, ce qui permet un routage efficace.

> [!note]
> Le réseau papillon est souvent utilisé dans les problèmes de communication parallèle ou de routage, en raison de ses propriétés efficaces en termes de chemins uniques et de faible congestion.

> [!info]+ Proprietés
> ![[b49ea37dec7c5dfc552dcdce319a8c1e.png]]
> ![[ce3973181ace2e384bc19672d58d6f13.png]]

> [!example]+ Exemples
> ![[c49e02a1fef0eeca9fc777aba4d1522f.png]]
> ![[c20ccb6016ca2b586c704d755e0b52e1.png]]
