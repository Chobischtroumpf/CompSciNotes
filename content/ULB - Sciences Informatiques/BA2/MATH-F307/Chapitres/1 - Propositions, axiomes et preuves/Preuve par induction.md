---
title: Preuve par induction
authors: Alessandro Dorigo
tags:
  - MathDis
  - Logique
---


> [!info]+ Définition
> Une **preuve par induction** est un type de preuve indirecte puissante qui prouve qu'une propriété est vraie $\forall n \in \mathbb{N}$. Elle fonctionne par récurrence:
>
> **Axiome d'induction**: Soit $P(n)$ un prédicat avec $n \in \mathbb{N}$. Si:
> 1. **Cas de base**: $P(0)$ est vraie.
> 2. **Hérédité**: $\forall n \in \mathbb{N},\ P(n) \implies P(n+1)$ est vraie.
>
> Alors, $\forall n \in \mathbb{N},\ P(n)$ est vraie.
>
> Si ces deux étapes sont validées, alors $P(n)$ est vraie pour tout $n \in \mathbb{N}$.

^33574a

 > [!tip]+ Induction à partir d'un entier $b$
 > Si $P(b)$ est vraie et que $\forall n \geq b,\, P(n) \implies P(n+1)$, alors $P(n)$ est vraie pour tout $n \geq b$.

> [!example]+ Exemple d'induction (somme des $n$ premiers entiers)
> Prouvons que $\forall n \in \mathbb{N},\ \sum_{i=1}^{n} i = \frac{n(n+1)}{2}$.
> 1. **Cas de base ($n=1$)**:
> $$\sum_{i=1}^{1} i = 1 = \frac{1(1+1)}{2}$$
> 2. **Hérédité**: Supposons la formule vraie pour $n$, démontrons-la pour $n+1$ :
> $$\sum_{i=1}^{n+1} i = \left( \sum_{i=1}^{n} i \right) + (n+1) = \frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}$$
>
> Donc, la formule est vraie pour $n+1$, ce qui complète la preuve par induction.

> [!note]+ Limites de l'induction
> L'induction ne fournit pas toujours une intuition sur le résultat.
> Il est crucial de vérifier la validité de la base et de l'étape inductive pour éviter les erreurs.

> [!abstract]- Théorème 1.1.1
> $\forall n \in \mathbb{N}$:
> $$3 \mid (n^3 - n)$$
>
> ![[Pasted image 20240923152324.png]]

> [!abstract]- Théorème 1.1.2
> $\forall n \geq 1$, $\exists$ un pavage d'un carré de taille $2^n \times 2^n$ par des $L$, laissant exactement un carré $1 \times 1$ non couvert **dans le centre**.
>
> ![[Pasted image 20240923153926.png]]
>
> **Idée**: changer l’hypothèse inductif:
> - $P(n)$ : $\forall n \geq 1$, $\exists$ un pavage d'un carré de taille $2^n \times 2^n$ par des $L$, laissant exactement un carré $1 \times 1$ non couvert **n'importe où**.

> [!abstract]- Faux théorème 1.1.x
> ![[Pasted image 20240923152612.png]]
> ![[Pasted image 20240923152620.png]]
>
> **Erreur!!!** Bien que $P(1)$ affirme que "tous les chats de l'ensemble $\{c_1\}$ ont la même couleur", et que $P(2)$ affirme que "tous les chats de l'ensemble $\{c_2\}$ ont la même couleur", cela ne garantit pas que ces deux ensembles partagent la même couleur.
>
> Il n'y a **pas de transitivité** entre les ensembles de chats, et rien n'assure que $c_1$ et $c_2$​ sont de la même couleur. C'est précisément à ce point qu'il faut faire attention:
> - Les $n$ points $\{c_1,c_2, \dots ,c_n\}$ masquent cette absence de lien direct entre les différents ensembles. Le détail crucial se cache dans cette étape, car c'est là que l'argument inductif échoue: la généralisation à $n+1$ chats suppose implicitement une transitivité qui n'est pas justifiée.
