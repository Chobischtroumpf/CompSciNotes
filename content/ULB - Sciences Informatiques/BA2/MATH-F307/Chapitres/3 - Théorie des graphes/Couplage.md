---
title: Couplage
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
---


> [!info]+ Définition
> Un **couplage** d’un graphe est un sous-ensemble d’arêtes tel que chaque sommet est [[Incidence#^a96a3d|incident]] à **au plus une arête** de ce sous-ensemble.

- Autrement dit, un couplage est un ensemble d’arêtes qui ne partagent aucun sommet entre elles.

> [!note]
> Le sous-graphe formé est souvent nommé $M$.

> [!info]+ Taille d'un couplage
> La **taille d’un couplage** est le nombre d’arêtes qui composent ce couplage. Si $M$ est un couplage, sa taille est $\vert E(M) \vert$.

> [!info]+ Couplage maximal
> Un **couplage maximal** est un couplage auquel on ne peut ajouter aucune arête sans violer la condition de couplage (aucun sommet partagé entre deux arêtes).

- Autrement dit, chaque arête restante du graphe partage au moins un sommet avec une arête déjà dans le couplage.

> [!info]+ Couplage maximum
> Un **couplage maximum** *(couplage de taille maximale dans le cours)* est un couplage qui contient le plus grand nombre possible d’arêtes dans le graphe.
> - **Remarque**: Tout couplage maximum est aussi un couplage maximal, mais l’inverse n’est pas toujours vrai.

> [!example]+ Exemples
> **Couplage de taille 4**
>
> ![[1E2D1963-C633-40A3-BBD3-1B2BDE5CB49A.png]]
>
> **Couplage de taille 5**
>
> ![[DF567FED-E578-4FCF-9AE9-8F48F8683928.png]]

| ![[B0C694AA-3BEB-4500-A621-FEA910083B69.png]] | $\{x_1, x_2, x_5, x_6\}$ | $\bigl\{\{x_1,x_6\}, \{x_2,x_5\}\bigl\}$ |
| :-------------------------------------------: | :----------------------: | :--------------------------------------: |
|                  Graphe $G$                   |          $V(M)$          |                  $E(M)$                  |
> [!info]+ Couplage parfait
> Un **couplage parfait** est un couplage qui couvre **tous les sommets** du graphe $G$. Autrement dit, chaque sommet de $G$ est [[Incidence#^a96a3d|incident]] à une et une seule arête du couplage.
> - Si $M$ est un couplage parfait, alors $\vert E(M) \vert = \vert V(G) \vert / 2$.
> - Un couplage parfait ne peut exister que si $G$ contient un **nombre pair de sommets**, car chaque arête connecte deux sommets.

> [!note]
> - Tout couplage parfait est automatiquement **maximum** et **maximal**, car il ne peut contenir plus d’arêtes et aucune autre arête ne peut être ajoutée sans violer les conditions de couplage.
> - Un couplage parfait correspond également à une **couverture d'arêtes minimale**, c'est-à-dire qu'il minimise le nombre d'arêtes nécessaires pour couvrir tous les sommets du graphe.

> [!info]+ Poids d'un couplage
> Le **poids** d’un couplage $M$ est la somme des poids des arêtes appartenant à $M$.
> - Si le graphe $G$ est un graphe pondéré (avec des poids associés aux arêtes), le poids total d’un couplage $M$ est donné par: $$\text{Poids}(M) = \sum_{e \in M} \text{Poids}(e)$$
## Fait:
- Il existe un algorithme efficace (= polynomial) pour trouver un couplage de taille maximum dans un graphe et;
- Il existe un algorithme efficace pour trouver un couplage parfait de poids minimum dans un graphe pondéré.

> [!info]+ Définition
> Un **couple rebelle** pour un couplage (parfait) $M$ est une arête $xy \in E(G) \setminus E(M)$ t.q:
> 1. $x$ "préfère" $y$ à son partenaire $x'$ dans $M$;
> 2. $y$ "préfère" $x$ à son partenaire $y'$ dans $M$.
>
>  ![[{B9A05696-02A5-4C84-9A23-A88F8CC7163B}.png]]
>
>  La notion de préférence est mieux reformulée comme **le couple restant si on enlève** $M$ de $G$.

> [!info]+ Couplage stable
> Un couplage est dit **stable** s'il n'existe pas de couple rebelle.
