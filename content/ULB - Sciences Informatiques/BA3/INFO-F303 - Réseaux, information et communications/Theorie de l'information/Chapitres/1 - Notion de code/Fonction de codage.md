---
title: Fonction de codage
authors: Alessandro Dorigo
tags:
  - ThInfo
---


> [!info]+ Définition
> Une **fonction de codage** est une fonction qui associe à chaque symbole d'information un mot de code dans un alphabet donné.
> $$K : S \to C^* : s \mapsto c_1c_2...c_\ell$$
> où:
> - $S = \{ s_1, s_2, \dots, s_q \}$: ensemble des symboles d'information
> - $C$: alphabet du code de taille $r = \vert C \vert$
> - $C^*$: ensemble des chaînes non vides de $C$
> - $\ell \geq 1$: longueur du mot de code
> - $K(S) \subset C^*$: le **code** ou ensemble des **mots du code**
> - $\ell_i = \vert K(s_i) \vert$: longueur du mot de code pour le symbole $s_i$
> - $\ell_{\max} = \max_{i=1,...,q} \{ \vert K(s_i)\vert \}$: longueur maximale des mots

^0a7213

> [!abstract]- Extension naturelle
> La fonction de codage s'étend naturellement aux suites de symboles:
> $$K : S^* \to C^* : s_1s_2 \dots s_n \mapsto K(s_1)K(s_2)...K(s_n)$$

- On suppose souvent $r = 2$ (alphabet binaire $C = \{ 0,1 \}$) car c'est le plus utilisé en informatique.

> [!example]+ Exemples
> **Exemple simple**:
> - $S = \{ \text{non}, \text{oui} \}$, $C = {0,1}$
> $$\begin{cases} K(\text{non}) = 0 \\ K(\text{oui}) = 1 \end{cases}$$
>
> **Exemple avec perte d'information**:
> - $S = \{ \text{lun}, \text{mar}, \text{mer}, \text{jeu}, \text{ven}, \text{sam}, \text{dim} \}$
> - $C = \{ \text{semaine}, \text{weekend} \}$
> $$K(x) = \begin{cases} \text{semaine si } x \in \{ \text{lun}, \text{mar}, \text{mer}, \text{jeu}, \text{ven}, \text{sam}, \text{dim} \} \\ \text{weekend si } x \in \{\text{sam}, \text{dim} \} \end{cases}$$
