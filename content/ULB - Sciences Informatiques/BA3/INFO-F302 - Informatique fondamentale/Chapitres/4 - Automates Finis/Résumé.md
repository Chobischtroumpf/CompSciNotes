---
title: Résumé
authors: Mihai Bors
tags:
  - InfoFond
---
## Automates

Ce chapitre parle des automates, en réintroduisant ce que sont un alphabet, mots, lettres et langages. On introduit d'abord les automates finis (déterministes), qui sont un ensemble d'états avec un alphabet, une fonction de transition, un état initial et un ensemble d'états finaux. On nous montre comment les automates sont lus (de gauche à droite), comment on vérifie l'appartenance d'un mot dans le langage (en regardant si le mot mène vers un état final, ou plutôt s'il finit sur un).

On nous parle ensuite des intersections/unions (produit d'automates) entre des automates, où on voit les propriétés essentielles comme les états finaux résultants des intersections (l'état doit contenir les états finaux des deux en même temps) et des unions (soit les états finaux du 1er soit 2ème). On voit aussi des propriétés pour regarder si un automate est un sous-ensemble d'un autre (ou plutôt le langage d'un est le sous-ensemble d'un autre).

Finalement, on voit le test du vide, qui nous permet de voir si un automate a au moins un chemin vers un état final depuis l'état initial ou pas.

La 2ème partie s'intéresse aux automates finis non-déterministes. La notion de non-déterminisme ici veut dire qu'on a plusieurs destinations possibles pour un même couple (état, lettre). On voit que les tests d'appartenance se basent sur l'exploration de tous les chemins possibles : si au moins un chemin termine dans un état final, le mot est accepté. On utilise une fonction nommée $\text{Post}_A$ qui à partir d'un sous-ensemble d'états et une lettre, nous permet de savoir l'union des états accessibles avec la lettre depuis tous les états du sous-ensemble.

Finalement, on voit que le test du vide marche de manière identique aux AF et qu'on peut convertir un AFN en AF en utilisant l'algorithme de déterminisation (ou algorithme des sous-ensembles), où on doit prendre en compte tous les ensembles d'états trouvés par la fonction $\text{Post}_A$ comme nouveaux états de l'AF résultant.

## Expressions Rationnelles

Ce court chapitre porte sur les expressions rationnelles, des expressions définies par induction avec des règles de construction syntaxiques. Leur sémantique est définie par un langage $\mathcal{L}(E)$ où $E$ est une expression rationnelle. On a plusieurs règles, notamment $\mathcal{L}(E_1 + E_2)$ étant l'union de deux langages, $\mathcal{L}(E_1.E_2)$ étant la concaténation de deux langages et $\mathcal{L}(E^*)$ qui est l'ensemble de 0 ou plus concaténations de mots de $\mathcal{L}(E)$.

Finalement, on voit le théorème de Kleene, qui stipule qu'un langage est reconnaissable par un automate si et seulement si il est définissable par une expression rationnelle, donc on peut faire expression → automate et inversement.
