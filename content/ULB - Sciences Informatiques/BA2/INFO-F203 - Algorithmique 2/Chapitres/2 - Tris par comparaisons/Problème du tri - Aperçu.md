---
title: Problème du tri - Aperçu
authors: Alessandro Dorigo
tags:
  - Algo
---


Le problème du tri est un problème classique et fondamental en algorithmique: étant
donnés $n$ éléments d’un ensemble, nous souhaitons les ranger dans un certain ordre.

De façon à nous abstraire du type de données particulier manipulé, nous nous restreignons au modèle du **tri par comparaisons:** les seules opérations élémentaires permises sur les données, outre les déplacements en mémoire, sont les comparaisons.

Nous faisons donc simplement l’hypothèse que l’ensemble que nous manipulons est muni d’un [[Ordre total#^3869e6|ordre total]] $\leq$, et qu’il existe une opération de comparaison qui permet, étant donné deux éléments $v$ et $w$, de décider si $v \leq w$.

La mesure typique de la complexité d’un tel algorithme est le **nombre de comparaisons effectuées** pour trier un ensemble de $n$ éléments.
### Concepts clés
---
- [[Bottom-up Mergesort]]
- [[Top-down Mergesort]]
	- [[Analyse de Mergesort]]
- [[Analyse de Quicksort]]
