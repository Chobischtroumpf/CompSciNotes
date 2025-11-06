---
title: Ensemble ordonné
authors: Alessandro Dorigo
tags:
  - MathDis
  - Relations
---


> [!info]+ Définition
> Un **ensemble (partiellement) ordonné** est un couple $(X , \preceq)$ où $\preceq$ est un [[Ordre partiel#^632685|ordre partiel]] sur $X$.
>
> Deux éléments $x \neq y$ dans $X$ sont dits:
> - Comparables si $x \preceq y$ ou $y \preceq x$;
> - Incomparables sinon.

^f247ff

> [!abstract]- Théorème 5.4.1
> Si $(X , \preceq)$ est un [[Ensemble ordonné#^f247ff|ensemble ordonné]] et soit
> $$\prec \ := \ \preceq \ \backslash \ \{(x,x)\mid x \in X \}$$
> alors $(X, \prec)$ est un [[Graphe dirigé (théorie des graphes)#^29385c|graphe dirigé]] acyclique.
>
> ![[Pasted image 20241021093956.png]]

> [!info]+ Définition
> Une **chaîne** dans un ensemble ordonné $(X , \preceq)$ est un sous-ensemble $C \subseteq X$ d’éléments deux à deux comparables.

> [!info]+ Définition
> Une **antichaîne** dans un ensemble ordonné $(X , \preceq)$ est un sous-ensemble $A \subseteq X$ d’éléments deux à deux incomparables.

> [!abstract]- Théorème de Mirsky 5.4.2
> Pour tout ensemble ordonné $(X , \preceq)$,
> $$\min \left\{ k \mid \exists \text{ partition de } X \text{ en } k \text{ antichaînes} \right\}$$
> $$X = A_1 \uplus A_2 \uplus \cdots \uplus A_k$$
> $$= \max \left\{ |C| \mid C \subseteq X \text{ chaîne} \right\}$$
>
> ![[Pasted image 20241021101854.png]]
> ![[Pasted image 20241021101908.png]]

> [!abstract]- Théorème de Dilworth 5.4.3
> Pour tout ensemble ordonné $(X , \preceq)$,
> $$\min \left\{ k \mid \exists \text{ partition de } X \text{ en } k \text{ chaînes} \right\}$$
> $$X = C_1 \uplus C_2 \uplus \cdots \uplus C_k$$
> $$= \max \left\{ |A| \mid A \subseteq X \text{ antichaîne} \right\}$$

> [!example]+ Exemple
> ![[Pasted image 20241021102048.png]]
