---
title: Code sans préfixe
authors: Alessandro Dorigo
tags:
  - ThInfo
---


> [!info]+ Définition
> Un **code sans préfixe** est un code dans lequel aucun mot du code n'est le préfixe d'un autre mot du code.

^392e5f

> [!abstract]- Propriété fondamentale
> **Décodage unique et à la volée**: comme pour les [[Code en bloc#^b9336a|codes en bloc]], on peut décoder une séquence de gauche à droite sans ambiguïté et sans avoir besoin de regarder en avant.

- Un code sans préfixe peut être représenté sous forme d'[[Arbre de code#^4606d7|arbre de code]].

> [!abstract]- Propriété d'équivalence
> Un code est sans préfixe si et seulement si il peut être représenté par un [[Arbre de code#^4606d7|arbre de code]].
>
> **Preuve**:
> - ($\Rightarrow$) Si code sans préfixe $\rightarrow$ construction de l'arbre possible
> - ($\Leftarrow$) Si arbre existe $\rightarrow$ aucun mot n'est préfixe d'un autre (propriété des feuilles)

> [!note]
> - Tout code sans préfixe est [[Code univoque#^95f169|univoque]]
> - La réciproque n'est pas vraie: le code $\{ 1, 10 \}$ est univoque mais pas sans préfixe
