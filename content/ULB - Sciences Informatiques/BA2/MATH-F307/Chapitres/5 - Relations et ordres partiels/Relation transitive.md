---
title: Relation transitive
authors: Alessandro Dorigo
tags:
  - MathDis
  - Relations
---


> [!info]+ Définition
> Une [[ULB - Sciences Informatiques/BA2/MATH-F307/Chapitres/5 - Relations et ordres partiels/Relation#^bbecb9|relation]] $R$ sur $X$ est dite **transitive** si
> $$\forall x,y,z \in X, \quad xRy \land yRz \implies xRz$$
> Donc, une relation entre x et y et entre y et z implique une relation entre x et z

^28003e

> [!example]+ Exemples de relation transitive
> 1. Égalite
> 2. $\leq sur \mathbb{N} est transitive$
> 3. la relation dans un graphe $G=(S,A)$
> 	qui met deux sommets a et b en relation si ils sont dans la meme CFC (Composante Fortement Connexe)

^b93538

### Attention:
![[Pasted image 20250916144252.png]]
Ici, a est en reation avec b, et b est en relation avec c, mais a n'est pas en relation avec c, il faudrait pour cela qu'une arrete relie a et c
