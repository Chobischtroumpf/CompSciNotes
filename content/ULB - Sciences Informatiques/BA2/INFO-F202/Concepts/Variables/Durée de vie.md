---
title: Durée de vie
authors: Alessandro Dorigo
tags:
  - LDP2
  - Progra
---


> [!info]+ Variable globale
> La variable existe pour la durée de vie du programme. Il n'y a qu'une seule variable pour chaque déclaration. Elle est créée au début du programme et détruite à la fin du programme. Si le programme se termine anormalement, elle peut ne pas être correctement détruite.

> [!info]+ Variable locale
> La variable existe pour la durée de vie du bloc dans lequel elle se trouve. Ce bloc est une fonction / méthode ou un bloc interne défini avec des accolades `{ }`.
>
> Elle est créée lorsque l'exécution atteint l'endroit où elle est déclarée et détruite lorsque l'exécution atteint la fin du bloc.
>
> Les paramètres des fonctions et des méthodes sont aussi des variables locales.

> [!info]+ Variable d'instance
> Une variable d'instance est définie dedans une classe. Elle est associée à une instance particulière d'une variable de sa classe et a la même durée de vie que cette instance.

> [!info]+ Variable temporaire
> Créée lorsqu'elle est renvoyée par une fonction utilisant return-by-value ou par un appel direct à un constructeur. Détruite à la fin de l'expression.
## Helper struct
```cpp
struct C {
	string st;
	C(string s): st(s) { cout << " Created: " << st << endl; }
	C(C &c): st{c.st} { cout << " Created via copy: " << st << endl; }
	~C() { cout << " Destroyed: " << st << endl; }
};
```
