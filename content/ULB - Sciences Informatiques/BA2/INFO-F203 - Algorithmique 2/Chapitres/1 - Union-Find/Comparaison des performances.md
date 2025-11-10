---
title: Comparaison des performances
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!abstract]- Tableau Comparatif
> Voici les complexités des différentes versions pour $n$ éléments :
> - Méthode naïve: $\mathcal{O}(n)$ pour union, $O(1)$ pour find
> - Union rapide simple: $\mathcal{O}(h)$ pour union et find, où $h$ peut être $\mathcal{O}(n)$ dans le pire cas
> - Union rapide pondérée: $\mathcal{O}(\log n)$ pour union et find
> - Union rapide pondérée avec compression: $\mathcal{O}(\alpha(n))$ amorti pour union et find

> [!tip]+ Choix de l'implémentation
> En pratique, l'implémentation recommandée est l'union rapide pondérée avec compression de chemin car:
> - Elle offre les meilleures garanties théoriques
> - Sa complexité est quasiment constante en pratique
> - Le surcoût de la compression est largement compensé par l'amélioration des performances
### Applications
La structure Union-Find avec ces optimisations est utilisée dans de nombreux algorithmes:
- Détection de cycles dans un graphe
- Calcul des composantes connexes
- Algorithme de Kruskal pour l'arbre couvrant minimal
- Regroupement de pixels en imagerie numérique

> [!example]+ Exemple
> Dans l'algorithme de Kruskal, Union-Find permet de maintenir efficacement les composantes connexes de l'arbre en construction. Chaque fois qu'une arête est ajoutée, une opération `union` fusionne deux composantes.
