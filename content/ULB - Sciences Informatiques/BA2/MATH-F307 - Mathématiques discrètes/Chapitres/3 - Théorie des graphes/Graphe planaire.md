---
title: Graphe planaire
authors: Alessandro Dorigo
tags:
  - Graphe
---


> [!info]+ Définition
> Un graphe est dit **planaire** s’il peut être représenté dans le plan sans qu’aucune arête n’en croise une autre.
> - Plus précisément: Un graphe est **planaire** ssi chacun de ses composants sont planaires.
^5fdfb5

> [!example]+ Exemples
> ![[f3a181b072bd18b40b2f3bbb4cd82d03.png]]![[9e2c36d58ac3c3aba84c3587b383da8f.png]]![[b7b82eb76d8cbf24c94d506d30883e02.png]]

- Il existe une manière simple pour prouver la non-planarité d'un graphe: On montre qu'il y a "trop" de sommets.

> [!abstract]- Lemme 3.3.1
> Si on a un graphe [[Graphe planaire#^5fdfb5|planaire]] $G$ avec $\vert E \vert \geq 3$ arêtes et $\vert V \vert$ sommets, on a alors $\vert V \vert \leq 3\vert E \vert −6$.
> Ceci peut être utilisé pour prouver qu'un graphe n'est **pas** planaire.

> [!abstract]- Lemme 3.3.2
> Si $G$ est un graphe [[Graphe biparti#^bff5b9|biparti]] [[Graphe planaire#^5fdfb5|planaire]] avec $\vert E \vert \geq 3$ arêtes et $\vert V \vert$ sommets, alors $\vert V \vert \leq 2\vert E \vert −4$.
> Ceci est aussi utilisé pour prouver qu'un graphe n'est **pas** planaire.

> [!abstract]- Lemme 3.3.3
> Le [[Degré#^3c01ed|degré]] moyen des sommets d'un graphe [[Graphe planaire#^5fdfb5|planaire]] doit être plus petit que 6.

> [!abstract]- Théorème 3.3.4 - Formule d'Euler
> Dans un graphe [[Graphe planaire#^5fdfb5|planaire]] [[Graphe connexe#^942c76|connexe]], on a toujours: $$s-a+f=2 =\vert V \vert - \vert E \vert + f$$
> - $f$ étant le nombre de faces du graphe
>
> **2 cas à montrer:**
>
> 1. On ajoute une arête au graphe sans rajouter de sommet mais en connectant 2 existants
> $$s = s \ \ \ \ \underset{\text{on ajoute 1 arête connectant 2 sommets}}{a = a + 1} \ \ \ \ \underset{\text{on coupe 1 face déjà existante}}{f = f + 1}$$
> $$s-(a+1)+(f+1)=s-a-1+f+1 =s-a+f=2$$
>
> 2. On ajoute une arête en rajoutant un sommet et le connectant a un autre
> $$\underset{\text{on ajoute 1 sommet}}{s = s +1} \ \ \ \ \underset{\text{on ajoute 1 arête}}{a = a + 1} \ \ \ \ f = f$$
> $$(s+1)-(a+1)+f=s+1-a-1+f=2 \ \ \ \ \square$$

> [!abstract]- Théorème 3.3.5 - Théorème de Kuratowski
> Un graphe est [[Graphe planaire#^5fdfb5|planaire]] ssi il ne contient pas une sous-division des arêtes de $K_{3,3}$ ou $K_5$ comme sous-graphe.
