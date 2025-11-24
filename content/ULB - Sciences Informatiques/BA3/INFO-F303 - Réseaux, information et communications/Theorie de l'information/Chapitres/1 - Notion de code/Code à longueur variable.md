---
title: Code à longueur variable
authors: Alessandro Dorigo
tags:
  - ThInfo
---


> [!info]+ Définition
> Un **code à longueur variable** est un code où les mots peuvent avoir des longueurs différentes, contrairement aux [[Code en bloc#^b9336a|codes en bloc]].

- L'idée clé est d'assigner des mots courts aux symboles fréquents et des mots longs aux symboles rares (coder "E" avec un bit et "Z" avec plusieurs bits).
- Cependant, il y a de l'ambiguïté potentielle lors du décodage de chaînes!

> [!example]+ Exemple problématique
> Considérons $S = \{ a,b,c \}, C = \{ 0,1 \}$ et:
> $$\begin{cases} K(a) = 0 \\ K(b) = 1 \\ K(c) = 01 \end{cases}$$
> **Problème**: La chaîne $01$ peut se décoder soit comme $ab$ ($0$ puis $1$) soit comme $c$ ($01$) car $K(a) = 0$ est un **préfixe** de $K(c) = 01$!
