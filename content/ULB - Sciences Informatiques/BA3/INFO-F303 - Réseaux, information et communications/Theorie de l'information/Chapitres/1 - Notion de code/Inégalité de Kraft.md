---
title: Inégalité de Kraft
authors: Alessandro Dorigo
tags:
  - ThInfo
---


> [!abstract]- Inégalité de Kraft (1948)
> Pour tout ensemble de longueurs de mots du code $\{ \ell_1, \ell_2, \dots, \ell_q \}$ donné, il existe **au moins** un [[Code sans préfixe#^392e5f|code univoque sans préfixe]] correspondant **si et seulement si** l'inégalité suivante est satisfaite:
> $$\sum_{i=1}^{q} r^{-\ell_i} \leq 1$$
> où $r$ est la taille de l'alphabet du code.

^f120a9

> [!abstract]- Interprétation
> L'inégalité de Kraft caractérise complètement les ensembles de longueurs réalisables par un [[Code sans préfixe#^392e5f|code sans préfixe]]:
> - **Condition nécessaire**: tout [[Code sans préfixe#^392e5f|code sans préfixe]] satisfait cette inégalité
> - **Condition suffisante**: si l'inégalité est satisfaite, on peut construire un [[Code sans préfixe#^392e5f|code sans préfixe]]
## Démonstration
**Preuve constructive** (pour $r = 2$):
 1. **Cas de base**: $q = 1$, évident avec $2^{-\ell_1} \leq 1$
 2. **Récurrence**: Supposons le code construit pour $q-1$ symboles
 3. **Étape inductive**:
     - On a $2^{\ell_q}$ mots possibles de longueur $\ell_q$
     - Chaque mot existant $K(s_i)$ "exclut" $2^{\ell_q - \ell_i}$ mots
     - ![[1f788a9a2b3620159144e54c66edef93.png]]

> [!example]+ Exemples d'application
> **Alphabet binaire** ($r = 2$):
> - Longueurs $\{ 1, 1 \}$: $2^{-1} + 2^{-1} = 1$ ✓ (réalisable)
> - Longueurs $\{ 2, 2, 2, 2 \}$: $4 \times 2^{-2} = 1$ ✓ (réalisable)
> - Longueurs $\{ 1, 2, 3, 3 \}$: $2^{-1} + 2^{-2} + 2 \times 2^{-3} = 1$ ✓ (réalisable)
> - Longueurs $\{ 1, 2, 4, 4, 4, 4, 4 \}$: $2^{-1} + 2^{-2} + 5 \times 2^{-4} > 1$ ✗ (impossible)

> [!abstract]- Égalité dans Kraft
> **Borne atteinte** si et seulement si l'[[Arbre de code#^4606d7|arbre de code]] est **localement complet**:
> - Tous les nœuds internes ont exactement $r$ fils
> - Chaque feuille au niveau $\ell_i$​ a un "poids" $r^{-\ell_i}$
