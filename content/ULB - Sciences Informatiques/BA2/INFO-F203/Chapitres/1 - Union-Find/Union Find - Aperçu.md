---
title: Union Find - Aperçu
authors: Alessandro Dorigo
tags:
  - Algo
---


> [!info]+ Définition
> La structure Union-Find est une structure de données permettant de gérer efficacement les relations d'équivalence dynamiques.
### Concepts clés
---
- [[Arbre équilibré]] <- Prérequis
- [[Relation d'équivalence (algorithmique 2)]]
- [[Méthode naïve]]
- [[Union rapide]]
- [[Union rapide pondérée]]
	- [[Union par nombre d'éléments]] <- extra
- [[Compression de chemin]]
- [[Comparaison des performances]]
### Java
---
```java
// initialise la structure avec n éléments deux à deux non connectés
UF(int n)
// union des classes contenant p et q
void union(int p, int q)
// renvoie l'identifiant de la classe d’équivalence contenant p
int find(int p)
// teste si deux éléments appartiennent à la même classe
boolean connected(int p, int q)
// renvoie le nombre total de classes d’équivalence
int count()
```
