---
title: Arbre équilibré
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!info]+ Définition
> Un arbre est dit **équilibré** si, pour tout nœud de l’arbre, la hauteur de ses sous-arbres gauche et droit diffère d’au plus une unité.
### Types d’arbres équilibrés:
Il existe plusieurs variantes d'arbres équilibrés en fonction des contraintes spécifiques appliquées:
1. **Arbre AVL**
    - Un [[ABR|arbre binaire de recherche]] (BST) où la **balance factor** de chaque nœud (différence entre les hauteurs du sous-arbre gauche et droit) est **au plus 1**.
    - Requiert des rotations pour maintenir l'équilibre après chaque insertion ou suppression.
2. **Arbre Rouge-Noir**
    - [[ABR|BST]] équilibré approximativement en limitant la hauteur à $\mathcal{O}(\log n)$.
    - Les nœuds suivent une contrainte de coloration (rouge ou noir) qui garantit l'équilibre sans nécessiter un équilibrage strict à chaque nœud.
3. **Arbre B (B-tree)**
    - Utilisé principalement pour les bases de données et systèmes de fichiers.
    - Chaque nœud peut contenir plusieurs clés et enfants, ce qui réduit la profondeur de l'arbre.
4. **Arbre 2-3 (ou 2-3-4)**
    - Variante où chaque nœud peut contenir **2 ou 3 clés** pour limiter la profondeur.
