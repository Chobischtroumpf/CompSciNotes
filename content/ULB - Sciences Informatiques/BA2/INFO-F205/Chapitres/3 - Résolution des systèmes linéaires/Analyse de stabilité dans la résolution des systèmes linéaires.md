---
title: Analyse de stabilité dans la résolution des systèmes linéaires
authors: Alessandro Dorigo
tags:
  - CFN
---


> [!info]+ Définition
> L'analyse de stabilité étudie comment les erreurs (d'arrondi, de mesure, etc.) affectent la précision de la solution calculée d'un système linéaire $Ax = b$.
## Types d'analyse de stabilité

### 1.[[Analyse a priori]]
- [[Analyse directe]]
- [[Analyse rétrograde]]
### 2. [[Analyse a posteriori]]
## Facteurs affectant la stabilité
### 1. [[Conditionnement de la matrice]]
### 2. [[Choix des algorithmes]]
### 3. [[Propagation des erreurs d'arrondi]]

## Techniques d'amélioration de la stabilité

### 1. [[Pivotage]]

### 2. [[Raffinement itératif]]

### 3. [[Tests d'arrêt|Tests d'arrêt pour les méthodes itératives]]

## Exemple pratique

> [!example]+ Exemple
> Considérons le système linéaire : $$A = \begin{bmatrix} 1.2969 & 0.8648 \ 0.2161 & 0.1441 \end{bmatrix}, \quad b = \begin{bmatrix} 0.8642 \ 0.1440 \end{bmatrix}$$
>
> La solution exacte est $x = [2, -2]^T$.
>
> Une solution approchée $\hat{x} = [0.9911, -0.4870]^T$ présente une grande erreur malgré un résidu très petit : $$r = b - A\hat{x} = \begin{bmatrix} -10^{-8} \ 10^{-8} \end{bmatrix}$$
>
> Ce phénomène s'explique par le conditionnement très élevé : $$\kappa_{\infty}(A) \approx 3.26 \cdot 10^8$$
>
> Cet exemple illustre qu'un petit résidu ne garantit pas une solution précise si la matrice est mal conditionnée.

> [!tip]+ Remarque
> Le choix d'un algorithme stable et éventuellement l'application de techniques d'amélioration comme le raffinement itératif sont essentiels pour les problèmes mal conditionnés.
