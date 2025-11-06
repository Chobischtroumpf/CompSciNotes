---
title: Analyse de Mergesort
authors: Alessandro Dorigo
tags:
  - Algo
---


Cette note concerne l'analyse de complexité de [[Mergesort]], initialement vu en `INFO-F103`. Pour les details mathématiques, voir [[Mergesort (maths discrètes)]].
## Relation de récurrence
Lorsque nous analysons le tri fusion, nous obtenons une relation de récurrence caractéristique. Si nous notons $D(n)$ le nombre de comparaisons nécessaires pour trier $n$ éléments, nous avons:

> [!abstract]- Formule
> $$D(n) = 2D(n/2) + n$$
> où $D(1) = 0$

Cette relation s'explique par:
- $2D(n/2)$: les deux appels récursifs sur des tableaux de taille $n/2$
- $n$: le coût de la fusion des deux sous-tableaux triés

On peut se rendre compte que $D(n) = \mathcal{O}(n \log n)$.
## Visualisation de la complexité
Une autre manière intuitive de comprendre cette complexité est de visualiser l'arbre des appels récursifs:

- **Hauteur de l'arbre:** $\log_2(n)$ niveaux
- **Coût par niveau:** $n$ comparaisons
- **Coût total:** $n \log_2(n)$ comparaisons

> [!tip]+ Remarque
> Cette complexité est asymptotiquement optimale pour un algorithme de tri par comparaisons, comme nous le démontrerons plus tard avec la borne inférieure.
## Analyse en espace
Il est important de noter que le tri fusion a également une complexité en espace significative:

> [!abstract]- Complexité en Espace
> $$S(n) = O(n)$$

Cette complexité provient du tableau auxiliaire nécessaire pour la fusion. Ce coût en espace supplémentaire est le prix à payer pour obtenir un tri stable et une complexité optimale en nombre de comparaisons.
### Cas particuliers et extensions
> [!note]+ Optimisations Possibles
> - La constante multiplicative de $n \log_2(n)$ peut être améliorée dans certains cas
> - Des optimisations sont possibles pour les petits tableaux
> - Le tri fusion bottom-up peut réduire les constantes cachées

Cette complexité de $\mathcal{O}(n \log n)$ reste vraie même quand $n$ n'est pas une puissance de 2. La démonstration précédente peut être étendue à tous les entiers positifs, mais la preuve est plus technique.
