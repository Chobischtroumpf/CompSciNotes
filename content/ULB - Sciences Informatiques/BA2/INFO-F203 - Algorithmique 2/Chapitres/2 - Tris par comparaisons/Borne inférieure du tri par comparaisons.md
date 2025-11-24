---
title: Borne inférieure du tri par comparaisons
authors: Alessandro Dorigo
tags:
  - Algo
---

# Introduction au Problème

Une question fondamentale se pose : les algorithmes comme le tri fusion et le tri rapide, qui atteignent une complexité de $O(n\log n)$, sont-ils optimaux ? Peut-on faire mieux ?

## Le Résultat Fondamental

> [!abstract]- Théorème "Borne Inférieure"
> Aucun algorithme de tri par comparaisons ne peut trier un ensemble de $n$ éléments en utilisant moins de $\log_2(n!) \sim n\ln n$ comparaisons.

Cette borne remarquable nous montre que nos algorithmes précédents sont asymptotiquement optimaux.

## La Démonstration

La preuve utilise une approche élégante basée sur les arbres de décision.

### L'Arbre de Décision

> [!info]+ Définition "Arbre de Décision Binaire"
> Pour un algorithme de tri par comparaisons :
> - Chaque nœud représente une comparaison
> - Les branches représentent les résultats possibles
> - Les feuilles représentent les permutations finales triées

### Structure de la Preuve

La démonstration se décompose en trois étapes clés :

1. **Représentation des Sorties**
> [!info]+ Propriété
> Chaque feuille de l'arbre correspond à une permutation possible des éléments d'entrée dans leur ordre trié.

2. **Nombre de Permutations Possibles**
> [!abstract]- Formule
> Pour $n$ éléments distincts, il y a $n!$ permutations possibles.
> Donc l'arbre doit avoir au moins $n!$ feuilles.

3. **Relation Hauteur-Feuilles**
> [!abstract]- Formule "Relation Fondamentale"
> Pour un arbre binaire avec $m$ feuilles :
> $$\text{hauteur} \geq \log_2(m)$$

### La Conclusion Mathématique

En combinant ces éléments :
- L'arbre a au moins $n!$ feuilles
- Sa hauteur est donc au moins $\log_2(n!)$
- Le nombre de comparaisons est au moins égal à la hauteur

> [!abstract]- Formule "Approximation de Stirling"
> $$\log_2(n!) \sim n\log_2(n) - \frac{n}{\ln(2)} + O(\log n) \sim n\log_2(n)$$

## Implications Pratiques

Cette borne inférieure nous apprend plusieurs choses importantes :

4. **Optimalité des Algorithmes**
  - Le tri fusion et le tri rapide (en moyenne) sont asymptotiquement optimaux
  - On ne peut pas espérer trouver un algorithme de tri par comparaisons fondamentalement plus rapide

5. **Limites du Modèle**
  - Pour faire mieux que $O(n\log n)$, il faut sortir du modèle des comparaisons
  - Cela explique l'existence d'algorithmes comme le tri par dénombrement ou le tri par base qui peuvent atteindre $O(n)$ dans certains cas

> [!tip]+ Remarque "Au-delà des Comparaisons"
> Cette borne ne s'applique qu'aux algorithmes de tri par comparaisons. D'autres modèles de calcul peuvent permettre des performances supérieures pour des cas spécifiques.

## Conclusion

Cette borne inférieure est un résultat fondamental qui :
- Justifie l'optimalité de nos meilleurs algorithmes
- Illustre la puissance des arguments de théorie de l'information
- Montre les limites intrinsèques du modèle des comparaisons
