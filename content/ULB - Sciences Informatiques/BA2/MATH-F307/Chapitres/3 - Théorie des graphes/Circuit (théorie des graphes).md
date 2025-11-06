---
title: Circuit (théorie des graphes)
authors: Alessandro Dorigo
tags:
  - MathDis
  - Graphe
---


Formellement appris en `MATH-F307`. Pour les circuits vus de manière algorithmique, voir *link*.

> [!info]+ Définition
> Un **circuit** dans un graphe $G$ est une promenade qui peut passer plusieurs fois par chaque sommet qui débute et termine au même endroit.
> $$ W = v_0 \ e_1 \ v_1 \ e_2 \ \cdots \ e_{k-1} \ v_{k-1} \ e_k \ v_0$$

^07846b

> [!abstract]- Lemme 3.6.1 - Circuit Eulérien
> Un [[Circuit (théorie des graphes)#^07846b|circuit]] est dit **eulérien** s’il emprunte chaque arête une et une seule fois.
> - Un graphe est dit **eulérien** s’il admet un circuit eulérien.
>

> [!abstract]- Corollaire 3.6.2
> Une [[Promenade#^81c9d2|promenade]] est dite **eulérienne** si elle emprunte chaque arête du graphe une et une seule fois.
> - Une promenade eulérienne ne nécessite pas de revenir au point de départ.

> [!abstract]- Corollaire 3.6.3
> Un graphe $K_{m,n}$ (graphe [[Graphe biparti#^bff5b9|biparti]] [[Graphe complet#^673d8c|complet]]) possède un circuit eulérien si et seulement si $m$ et $n$ sont pairs.
>
> Le graphe $K_{m,n}$ est déjà connexe et sans sommet isolé. Les $m$ sommets de la première partie sont connectés à chacun des $n$ sommets de la deuxième partie, et vice versa.
>
> Donc, si $m$ est pair, les sommets dans la deuxième partie (qui ont un degré $m$) auront un degré pair. Si $n$ est pair, les sommets dans la première partie (qui ont un degré $n$) auront un degré pair.

> [!abstract]- Théorème 3.6.4
> Un graphe $G$ sans sommet isolé est eulérien ssi:
> 1) $G$ est [[Graphe connexe#^942c76|connexe]] et
> 2) $G$ n'a pas de sommet de [[Degré#^3c01ed|degré]] impair.
>
> ![[Pasted image 20241009111803.png]]
> ![[Pasted image 20241009111811.png]]
> ![[Pasted image 20241009111819.png]]
