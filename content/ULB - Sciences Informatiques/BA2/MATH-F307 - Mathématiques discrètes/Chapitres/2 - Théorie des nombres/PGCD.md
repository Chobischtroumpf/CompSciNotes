---
title: PGCD
authors: Alessandro Dorigo
tags:
  - MathDis
  - TheorieDesNombres
---


> [!info]+ Définition
> Le **pgcd** (plus grand commun diviseur) de $a$ et $b$, noté $\text{pgcd}(a, b)$, est le plus grand entier positif qui divise simultanément $a$ et $b$.
>
> $$\text{pgcd}(a, b) = \max\{d \in \mathbb{N}^+ \mid d \mid a \text{ et } d \mid b\}$$

^86c2aa

> [!tip]+ Corollaires
> - Si $a$ divise $bc$, et que $\text{pgcd}(a, b) = d$, alors $\frac{a}{d}$ divise $c$.
> - $\text{pgcd}(m \cdot a, m \cdot b) = m \cdot \text{pgcd}(a, b), \ \forall m \in \mathbb{Z^+}$.
> - $\text{pgcd}(a + m \cdot b, b) = \text{pgcd}(a, b), \ \forall m \in \mathbb{Z}$.
> 	- $\text{pgcd}(a \mod b,b)=\text{pgcd}(a,b)$.
> - Si $d \mid a$ et $d \mid b$, alors $d \mid \text{pgcd}(a, b)$.
> - Si $a$ et $b$ sont premiers entre eux ($\text{pgcd}(a, b) = 1$), alors $\text{pgcd}(a \cdot c, b) = \text{pgcd}(a, b) \cdot \text{pgcd}(c, b)$.
> - Si $m$ est un diviseur commun positif de $a$ et $b$, alors:
>   $$\text{pgcd}\left(\frac{a}{m}, \frac{b}{m}\right) = \frac{\text{pgcd}(a, b)}{m}$$
>
> **Propriétés:**
> - $\text{pgcd}(a, b) = \text{pgcd}(b, a)$ (commutativité).
> - $\text{pgcd}(a, \text{pgcd}(b, c)) = \text{pgcd}(\text{pgcd}(a, b), c)$ (associativité).
> - Si $a_1$​ et $a_2$​ sont premiers entre eux, alors:
>   $$\text{pgcd}(a_1 \cdot a_2, b) = \text{pgcd}(a_1, b) \cdot \text{pgcd}(a_2, b)$$

> [!abstract]- Théorème 2.2.1 - Algorithme d'Euclide
> Le pgcd de deux entiers $a$ et $b$ peut être calculé en utilisant l'algorithme d'Euclide:
> $$\text{pgcd}(a, b) = \text{pgcd}(b \mod a, a),$$
> où $b \mod a$ est le reste de la division de $b$ par $a$.
>
> **Démonstration**:
> Supposons que $m$ soit un diviseur commun de $a$ et $b$. Alors, par définition, $m \mid a$ et $m \mid b$, ce qui implique aussi que $m$ divise toute combinaison linéaire de $a$ et $b$. En particulier, $m$ divise $b - q \cdot a$, où $q$ est le quotient de la division de $b$ par $a$, c'est-à-dire que:
> $$m \mid (b - q \cdot a)$$
>
> Ainsi, $m$ divise $b \mod a$, ce qui montre que les diviseurs communs de $a$ et $b$ sont les mêmes que ceux de $a$ et $b \mod a$. Donc, $\text{pgcd}(a, b) = \text{pgcd}(b \mod a, a)$.

> [!abstract]- Méthode originelle d'Euclide
> La méthode introduite par Euclide pour calculer le $\text{pgcd}$ repose sur le fait que:
> - Étant donnés deux entiers positifs $a$ et $b$ avec $a > b$, les diviseurs communs de $a$ et $b$ sont les mêmes que ceux de $a - b$ et $b$.
>
> Ainsi, la méthode de calcul du $\text{pgcd}$ consiste à:
> 1. Remplacer le plus grand des deux nombres par la **différence** des deux nombres.
> 2. Répéter ce processus jusqu’à ce que les deux nombres deviennent égaux.
> 3. Ce nombre commun est alors le **plus grand commun diviseur**.

> [!abstract]- Théorème 2.2.2 - Identité de Bézout
> Pour tous $a, b \in \mathbb{Z}$, il existe des entiers $p$ et $q$ tels que:
> $$\text{pgcd}(a, b) = a \cdot p + b \cdot q$$
>
> ![[d0b2b52d05b34efd9320567884b2515f.png]]

> [!tip]+ Corollaire
> Pour tous $a, b \in \mathbb{Z}$:
> $$a\mathbb{Z} + b\mathbb{Z} = \text{pgcd}(a, b)\mathbb{Z},$$
> c'est-à-dire que l'ensemble des combinaisons linéaires entières de $a$ et $b$ est l'ensemble des multiples de $\text{pgcd}(a, b)$.
>
> ![[006569e5c5c67bfbeb96297b47f40e86.png]]

> [!abstract]- Théorème 2.2.3 - Lemme d'Euclide
> Si $p$ est premier et $p \mid ab$, alors $p \mid a$ ou $p \mid b$.
> - Si $\text{pgcd}(a,p) = p$, alors $p \mid a$.
> - Si $\text{pgcd}(a,p)=1$, alors $\exists s,t \in \mathbb{Z}$ tels que
>
> $$1=s\cdot a+t\cdot p$$
>
> Il suit que
> $$b=sab+tpb$$
> Or,
> $$p\mid ab \text{ et } p \mid p \text{, donc } p\mid b$$
>
> ![[330848f1ada888b5729199c4ce8c2f88.png]]![[c767f1eb5e9c6335585e019c2de06c02.png]]
