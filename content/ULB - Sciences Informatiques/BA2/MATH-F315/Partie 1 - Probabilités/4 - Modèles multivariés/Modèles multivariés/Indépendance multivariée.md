---
title: Indépendance multivariée
authors: Alessandro Dorigo
tags:
  - Proba
---


> [!info]+ Définition
> Les [[Variable aléatoire#^dcd8d2|variables aléatoires]] sont **indépendantes** si leur [[Fonction de répartition jointe multivariée#^e93253|fonction de répartition jointe]] peut s'écrire comme le produit de leurs [[Fonction de répartition marginale (discrète)#^cb4dc6|fonctions de répartition marginales]].
>
> Cette propriété s'étend aux densités / probabilités et aux [[Espérance (expected value)#^c716f7|espérances]], permettant de simplifier de nombreux calculs.

^03df8d

> [!abstract]- Formules
> On peut donc écrire leur [[Fonction de répartition jointe multivariée#^e93253|fonction de répartition]]:
> $$F_{X_1,X_2, \dots,X_n}(x_1, \dots,x_n) = F_{X_1}(x_1) \cdot \ \cdots \ \cdot F_{X_n}(x_n)$$
>
> Impliquant que la [[Fonction de densité jointe multivariée (continue)|densité jointe]] peut donc être simplifiée comme:
> $$f_{X_1,X_2, \dots,X_n}(x_1, \dots,x_n) = f_{X_1}(x_1) \cdot \ \cdots \ \cdot f_{X_n}(x_n)$$
>
> Ou dans le cas discret la [[Fonction de masse jointe multivariée (discrète)|fonction de masse]]:
> $$p_{X_1,X_2, \dots,X_n}(x_1, \dots,x_n) = p_{X_1}(x_1) \cdot \ \cdots \ \cdot p_{X_n}(x_n)$$
>
> L'[[Espérance (expected value)|espérance]] peut se calculer comme la multiplication de l'[[Espérance (expected value)#^c716f7|espérance]] de chaque [[Variable aléatoire#^dcd8d2|v.a.]] composant le vecteur:
> $$\mathbb{E}[X_1 \cdot X_2 \cdot \ \cdots \ \cdot X_n] = \mathbb{E}[X_1] \cdot \mathbb{E}[X_2] \cdot \ \cdots \ \cdot \mathbb{E}[X_n]$$
>
> Et plus généralement, pour toute fonction $g$:
> $$\mathbb{E}[g_{X_1}(X_1) \cdot g_{X_2}(X_2) \cdot \ \cdots \ \cdot g_{X_n}(X_n)] = \mathbb{E}[g_{X_1}(X_1)] \cdot \mathbb{E}[g_{X_2}(X_2)] \cdot \ \cdots \ \cdot \mathbb{E}[g_{X_n}(X_n)]$$

> [!tip]+ Résultat utile
> $$F_{X_1,X_2, \dots, X_n}(x_1, \dots,x_n) = H_{X_1}(x_1) \cdot \ \cdots \ \cdot H_{X_n}(x_n)$$
>
> Ce résultat établit une condition nécessaire et suffisante pour l'indépendance des variables aléatoires $X_1, X_2, \dots, X_n$:
> - Elles sont indépendantes **si et seulement si** leur [[Fonction de répartition jointe multivariée#^e93253|loi de répartition jointe]] peut s'écrire comme un produit de fonctions $H_{X_i}$, où chaque fonction $H_{X_i}$ dépend exclusivement de la variable $x_i$ correspondante.
>
> **Important**: les fonctions $H_{X_i}$ ne sont pas nécessairement égales aux [[Fonction de répartition marginale (discrète)#^cb4dc6|fonctions de répartition marginales]] $F_{X_i}(x_i)$.
