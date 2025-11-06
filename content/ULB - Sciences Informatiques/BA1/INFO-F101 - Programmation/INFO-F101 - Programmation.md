---
title: INFO-F101 - Programmation
authors: Alessandro Dorigo
tags:
  - ULB
  - BA1
---


[Notions pas comprises](https://www.notion.so/Notions-pas-comprises-9832a23c46894abca8efb620d1491786?pvs=21)

## Chapitre 5: Chaines de characteres, tuples, listes

Exemple de slicing – si on découpe une liste `s = [1, 5, 9, [7, 4]]`

```python
>>> t = s[:]
t[0] = 1, t[1] = 5, …, t[3] = [7, 4]
```

Donc on fait référence a un objet type `liste` pour `t[3]`.

Comme le slicing (quand utilise avec une sous-liste) fait référence a une même sous-liste, si on fait :

```python
>>> s = [1, 5, 9, [7, 4]]
>>> t = s[:]
>>> s[2] = 16
>>> s[3][0] = 888
>>> print(s)
[1, 5, 16, [888, 4]]
>>> print(t)
[1, 5, 9, [888, 4]]
```

On appelle ce genre de copie un `shallow copy` car s et t font référence a la même sous-liste `s[3]`.

Donc pour résoudre ce problème, on introduit (importe) une méthode nommée `deepcopy`.

Cette méthode fait en sorte que `t` pointe vers une totalement sous-liste séparée de `s` et donc nous permet de modifier `s[3]` / `t[3]` indépendamment.

```python
>>> from copy import deepcopy
>>> s = [1, 5, 9, [7, 4]]
>>> t = deepcopy(s)
>>> s[2] = 16
>>> s[3][0] = 888
>>> print(s)
[1, 5, 16, [888, 4]]
>>> print(t)
[1, 5, 9, [7, 4]]
```

Parlons de référence cyclique. Une référence cyclique apparaît quand on fait référence a une même liste dedans une sous-liste, cest-a-dire :

```python
>>> s = list(range(3))
>>> s[0] = s
>>> print(s)
[[…], 1, 2]
```

Les … font référence a une valeur sans précision pourvu qu’on appelle s dedans s.

Un exemple plus élaboré d’une référence cyclique pourrait être:

```python
>>> s = list(range(3))
>>> t = list(range(2))
>>> s[0] = t
>>> t[0] = s
>>> t[1] = t
>>> s[1] = s
>>> print(s)
[[[…], […]], […], 2]
```

Pour finir, toute liste ou dictionnaire s’appellent des conteneurs.

Maintenant nous abordons ce que sont les `argv`.

Chaque commande a des arguments qui peuvent être récupérés par l’input de l’utilisateur.

Par exemple:

```python
cd Directory # ici l’argument est ‘Directory’, récupéré par argv
```

Un autre exemple peut-être :

`(fichier arg.py)`

```python
import sys
print(sys.argv)

>>> python3 arg.py un deux trois 1 2 (1, 2)
[‘arg.py’, ‘un’, ‘deux’, ‘trois’, ‘1’, ‘2’, ‘(1, 2)’]
```

– Polynômes (pas compris)

– Traçage des polynômes avec Turtle (turtle étant une librairie de dessin sur Python)

Les matrices en Python sont représentées par des listes de listes `[[x1, y1], [x2, y2]]`.

On peut donc faire une commande qui multiplie deux matrices:

```python
def matrix_mult(a, b):
	c = [[0 for i in range(len(b[0]))] for j in range(len(a))]

	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(a[0])):
				c[i][j] += a[i][k] * b[k][j]
		return c

x = [[1, 2, 3], [4, 5, 6]]
y = [[1, 2], [4, 5], [7, 0]]
print(‘Le produit vaut: ’, matrix_mult(x, y))
```

Il s’agit d’une implémentation de la multiplication de matrices. La matrice
résultat `c` est initialisée avec des valeurs 0 et sa taille est déterminée en fonction de la taille de `a` et de `b`.

Pour chaque couple de lignes et de colonnes `(i, j)` de `c`, on calcule le produit des éléments de la ligne `i` de `a` et de la colonne `j` de `b`, et on ajoute le résultat à la valeur actuelle de `c[i][j]`.

Le code permet de calculer le produit de deux matrices `a` et `b`, sous réserve que `a` et `b` aient des dimensions compatibles pour la multiplication de matrices (le nombre de colonnes de `a` doit être égal au nombre de lignes de `b`).

Une fonction peut également définir une valeur formelle de quelque chose dans la définition et ce quelque chose peut ensuite être modifié, car il est déclaré que lors de la définition de la fonction.

Exemple:

```python
def f(a, s = []):
	s.append(a)
	return s

>>> f(1)
>>> f(2)
>>> f(3)
>>> print(s)
[1, 2, 3] # on remarque donc que s n’est pas réinitialisé a [] mais donc modifié à chaque fois
```

On peut également remarquer qu’on peut donner des arguments par mots-clés dans des fonctions dans des ordres différents, par exemple avec une fonction `fun(a, b, c)`:

```python
fun(a=393, c=493, b=3.0)
fun(55, b=44) # a = 55
```

Mais `a` est un argument obligatoire! Par exemple :

```python
fun(c=493, 55)
```

Ne marchera pas, car aucun argument positionnel ne peut suivre un argument par mot-clé.

On peut aussi annoter des fonctions avec les types des valeurs données:

```python
def name(s : str=’Man’) → str :
	return ‘Hello’ + s
```

En informatique, il y a un certain nombre d’algorithmes comme:

- les algorithmes de recherche de l’élément minimum (ou maximum) dans une séquence
- les algorithmes de recherche d’un élément dans un ensemble représenté sous une forme ou une autre (séquence, séquence	triée, structure plus élaborée)
- les algorithmes de tri des éléments d’une séquence

En Python, les algorithmes de tri et recherche sont déjà implémentés, avec des fonctions comme `sort()` **ou `for x in liste`, etc.

Cependant, on peut quand même coder ces algorithmes en Python.

**Algorithmes de recherche – recherche de l’élément minimum dans une séquence**

```python
def indice_min(s):
	res = 0
	for i in range(1, len(s)):
		if s[i][0] < s[res][0]:
			res = i
	return res
```

Ce code renvoie l’indice de la valeur minimale dans une séquence.

**Algorithmes de recherche – recherche séquentielle**

```python
def recherche(s, x):
	i = 0
		while i < len(s) and s[i][0] != x:
			i = i + 1
	if i == len(s):
		i = None
	return i
```

Ce code-ci renvoie l’indice `i` dans `s` ou la première instance de `x` est trouvée.

On peut améliorer le code au-dessus si `s` est modifiable en rajoutant `x` dans la liste et en l’enlevant a la fin s’il n’y a aucune instance de `x` trouvée auparavant.

```python
def recherche(s, x):
	i = 0
	s.append(x)
	while s[i][0] != x:
		i = i + 1
	if i == len(s):
		return None
	return i
```

**Algorithmes de recherche – recherche dichotomique**

La recherche dichotomique consiste à diviser une séquence *triée* par ordre *croissant* au milieu et regarder si la valeur recherchée est plus petite ou plus grande que celle de gauche/droite, puis refaire la même étape en fonction de cela par la gauche ou par la droite.

```python
def recherche_dicho(s, x):
	bi, bs = 0, len(s)
	m = (bi + bs) // 2
	while bi < bs and x != s[m][0]:
		m = (bi + bs) // 2
	if s[m][0] < x:
		bi = m + 1
	else:
		bs = m
	if len(s) ≤ m or s[m][0] != x:
		m = None
	return m
```

Les algorithmes de tri peuvent être ou soit croissants ou soit décroissants. On considère que les algorithmes de tri travaillent également avec des listes d’éléments qui contiennent chacune une clé et une information qui correspond (aussi appelée information satellite).

**Tri par sélection:**

Le tri par sélection est un algorithme qui ordonne de maniere croissante une liste – c’est-à-dire a l’étape 0, donc la première valeur, il compare `s[0]` avec tous les autres éléments de la liste, `s[n - 1]` inclus.

S’il y a plusieurs minimales, l’algorithme choisit le plus petit et le remplace avec `s[0]`.

Pour les prochaines étapes, le minimum dans l’intervalle `1` et `n - 1` de `s` est échange avec `s[1]` jusqu’à quand tous les autres éléments ont pris leur place définitive et que toutes les valeurs de `s[i]` jusqu’à `s[n - 1]` sont supérieures ou égales a toutes les valeurs `s[0]` jusque `s[i - 1]`.

## Chapitre 6: Ensembles et Dictionnaires

### **6.1** *Comprehension d’ensembles et de dictionnaires*

```python
s = {i for i in range(2, 12, 2)}
{2, 4, 6, 8, 10}

dico = {cle: valeur for cle, valeur in zip(range(2, 20, 2), 'bonjour')}
{2: 'b', 4: 'o', 6: 'n', 8: 'j', 10: 'o', 12: 'u', 14: 'r'}
```

## Chapitre 7: Notion de Complexite et grand O

### ********7.1******** **********Motivation**********

Grand O sert a pouvoir classer un programme par rapport a son efficacite pour la plupart des cas possibles.

---

### ************7.1.1************ *Criteres de choix d’un algorithme*

On a deux grands criteres de choix:

- La simplicite
- L’efficacite

Souvent, un programme ******************efficace****************** n’est pas simple, ou bien un programme qui doit travailler avec une quantite de donnees imposante doit etre ****************efficace****************.

L’utilisateur a donc le choix entre un programme simple ou efficace.

On categorise donc un programme par sa complexite et non simplicite - c’est-a-dire par rapport au nombre de variables ou calculs qui utiliseront donc la memoire.

---

### ************7.1.2************ *Exemple*

```python
res = 0
i = 1
while i < n:
	if s[i][0] < s[res][0]:
		res = i
	i = i + 1
return res
```

Ici, chaque ligne a une complexite differente, enfin, temps d’execution.

Par exemple, la ligne 1, 2 et 7 durent chaque qu’une unite de temps.

`T_min(n)` **est donne quand le if n’est jamais verifie.**

`T_max(n)` **est donne quand le if est a chaque fois verifie.**

`T_moyen(n)` **est calcule d’une maniere assez complexe, c’est-a-dire:**

$$
C(n)=\frac{1}{n}+\frac{1}{n-1}+...+1=\sum_{i=1}^n \frac{1}{i}
$$

$C(n)=$ le nombre moyen d’assignations a ******res****** pour une liste de taille n

---

### ************7.2************ *Le grand O*

Comme on a prouve que calculer `T_moyen` est tres complique et ne prend pas en compte le temps d’interpretation, du langage, du processeur ou IDE, etc, on prend donc une nouvelle variable, O.

On peut donc prendre 4 formules avec n, par exemple:

$A = 100\times{n}$

$**B=15\times{n^2}**$

$**C=n^4**$

$**D=2^n**$

Sachant que les micro-processeurs de nos jours peuvent calculer 10 ^ 9 operations par seconde, c’est a dire 10 ^ 12 par jour, pour les algorithmes suivants, on peut resoudre:

A, un probleme taille $n=10^{12}$

B, un probleme taille $n=10^{7}$

C, un probleme taille **$n = 3000$**

D, un probleme taille $n = 50$

O peut donc:

1. Determiner si un algorithme a une chance de s’executer pour un n donne
2. Connaissant le temps d’execution pour n, faire une approximation de ce temps pour une autre valeur de n

---

### 7.2.1 **********Definition**********

`O(n)` est defini de la maniere suivante:

**Une complexite** `T(n)` **est dite en grand O de** `f(n)` **s’il existe un entier** `N` **et une constante** `c ****> 0` **tels que pour tout entier** `n > N` **nous avons** `T(n) ≤ c * f(n)`**.**

Donc cela nous permet de simplifier les calculs car:

- Les facteurs constants n’affectent pas `O(n)`, si on a `T(n) = n` ou `T(n) = 100 * n`,  `T(n)` est toujours en `O(n) = n`
- On prend toujours l’ordre le plus grand, par exemple, avec `T(n) = n ^ 3 + 4n ^ 2 + 2n + 4`, on remarquera toujours que `T(n)` est en `O(n ^ 3)` car `n ^ 3 > 4n ^ 2 + 2n + 4`

---

### 7.2.2 Calcul du grand O

Quand on evalue O, on cherche la meilleure estimation “simple”.

On peut donc classer les complexites d’algorithmes selon leur grand O:

| O | Classe d’algorithmes |
| --- | --- |
| O(1) | Constant |
| O(log n) | Logarithmique |
| O(n) | Lineaire |
| O(n log n) | n log n |
| O(n^2) | Quadratique |
| O(n^3) | Cubique |
| O(2^n) | Exp base 2 |
| O(3^n) | Exp base 3 |
| O(n^n) | Exp base n |

Remarque: Pour tout $a,b>0: log_a n=(log_ab)\times(log_bn)$

Si `T(n)` est en `O(log_a n)`, il est egalement en `O(log_b n)` donc la base du logarithme n’a pas d’importance pour exprimer un grand O.

---

**Regles de calcul du grand O**

![yOEbMzp.jpg](INFO%20F-101%20Programmation%207f50dedb52e64c5aaf64867e71e884f9/yOEbMzp.jpg)

**Regle 1: Unite**

Tout ce qui ce qui concerne l’assignation, l’ecriture comme print, input, etc prend `O(1)` temps. Si l’input ou le print ont des valeurs plus complexes, cela ne serait plus `O(1)` mais `O(n)`.

**Regle 2: Sequence**

Si un traitement prend `T_1(n)` en `O(f_1(n))` et un autre `T_2(n)` en `O(f_2(n))`, alors le traitement 1 suivi par le traitement 2 est egal a `O(f_1(n)) + O(f_2(n)) = O(max(f_1(n) , f_2(n)))`. Max prend la fonction qui croit le plus vite (ou autrement dit du plus grand ordre).

**Regle 3: If**

Pour un `if` condition: `instruction_1 else: instruction_2`:

Avec `instruction_1` en `O(f_1(n))` et `instruction_2` en `O(f_2(n))` et le traitement en `O(g(n))`:

`O(max(f_1(n), f_2(n), g(n)))`

*Generalement,* `O(g(n)) = O(1)`

**Regle 4: While**

Le corps de la boucle est en `O(f_1(n))`, l’evaluation est en `O(f_2(n))`. Si on a une fonction en `O(g(n))` qui donne une borne superieure du nombre de fois que le corps sera execute, alors while est en `O(f(n) * g(n))` avec `f(n) = max(f_1(n), f_2(n))`

**Regle 5: For**

Pour les for, il suffit de “traduire” le for en while, par exemple:

```python
for i in range(n):
	print(i)
```

Devient:

```python
i = 0
while i < n:
	i += 1
```

Si on a:

```python
for i in range(10):
	# traitement
```

Ici le for est en `O(10 * f(n))` ou `O(f(n))` est la complexite d’une execution du traitement, donc le code complet serait en `O(f(n))`.

Si on a:

```python
for i in range(n):
	# traitement
```

Ici le for est en `O(n * f(n))` ou `O(f(n))` est a nouveau la complexite d’une execution du traitement.

**Regle 6: Fonction**

L’appel a une fonction se fait en `O(f(n))` qui correspond a la complexite du traitement de cette fonction. Si on veut la complexite min, max ou moyenne, on raffine les calculs avec le nombre de fois qu’une instruction sera repetee, avec des hypotheses sur la probabilite que des conditions de if ou de boucles sont verifiees.

---

### 7.3 ********************************Application des regles de calcul********************************

Le calcul du grand O se fait en partant des complexites des instructions simples et en calculant de proche en proche les complexites des instructions non simples a partir des resultats deja calcules.

---

### 7.3.1 ************************Complexite de la recherche du minimum************************

```python
res = 0
i = 1
while i < n:
	if s[i][0] < s[res][0]:
		res = i
	i = i + 1
return res
```

Ce code peut etre decompose en noeuds, c’est a dire chaque noeud correspond a une ou des instructions (dependant si c’est une boucle ou non).

Avec cette idee en tete, on peut remarquer que les lignes 1, 2, 5, 6 et 7 sont, d’apres la regle 1 en `O(1)`.

D’apres la regle 3, le noeud 4 - 5, qui correspond a l’instruction `if`, est en `O(1)`.

D’apres la regle 2, la sequence d’instructions 4 - 6 sont donc aussi en `O(1)`.

On peut donc evaluer la complexite du while (3 - 6). Il s’execute `n - 1` fois et la complexite du corps est `O(1)`. Donc, d’apres la regle 4, la complexite du while est en `O(n)`.

Finalement, tout le code se resume a `O(1 + 1 + n + 1)` ce qui equivaut a `O(n)`.

- Si un algorithme A est en `O(n)` et un algorithme B est en `O(n ^ 2)`, l’algorithme A est meilleur par rapport a la complexite.
- Par contre si les deux algorithmes sont en `O(f(n))`, il faudrait detailler les 2 complexites pour savoir lequel est meilleur.

---

### 7.3.2 *****************Complexite de la recherche sequentielle et dichotomique*****************

Pour la recherche sequentielle, on peut facilement deduire qu’elle est en `O(n)` ou n est la longueur de la liste, en supposant que les elements sont testes en `O(1)`.

Pour la recherche dichotomique, on peut remarquer que peut importe la valeur de n / x prise en compte, au pire des cas possibles, le champ de recherche est divise par deux. Par exemple dans une liste triee ou l’on cherche 41 parmi 100 nombres, on va devoir diviser cette liste 7 fois pour trouver 41.

Donc, au pire des cas, la recherche dichotomique est en `O(log n)`, puisqu’on divise par deux le champ de recherche a chaque etape de la recherche.

---

### 7.3.3 *******************Complexite du tri par selection*******************

En decomposant le code en parties comme pour 7.3.1, on a la complexite en `O(n ^ 2)`.

---

### 7.3.4 ****Complexite du tri par insertion****

La complexite maximale est en `O(n ^  2)` et la complexite minimale est en `O(n)` quand la liste est deja triee.

---

### 7.3.5 ***********************Complexite du tri Bulle***********************

La complexite maximale et minimale est en `O(n ^ 2)`.

---

### 7.3.6 *****Complexite du tri par enumeration*****

Si m < n, la complexite de ce tri est en `O(n)`.

---

### 7.3.7 ***************Autres exemples***************

Ces exemples font partie d’autres anciens examens:

```python
	i = 1 # O(1)
while i < n**3: # O(log n)
	i = i * 2 # O(1)
```

La complexite de ce code est en `O(log n)` d’apres la regle 4.

```python
for i in range(n): # O(n * m * l)
	for j in range(m): # O(m * l)
		for k in range(l): # O(l)
			print('hello') # O(1)

i = 0 # O(1)
while i < n: # O(n * m * l)
    j = 0 # O(1)
    while j < m: # O(m * l)
        k = 0 # O(1)
        while k < l: # O(l)
            print('hello') # O(1)
            k += 1 # O(1)
        j += 1 # O(1)
    i += 1 # O(1)
```

La complexite de ce code est en `O(n * m * l)` d’apres la regle 5.

```python
i = 2 # O(1)
while i < n: # O(log n)
	i = i * i # O(1)
```

La complexite de ce code est en `O(log n)` d’apres la regle 4.

---

### 7.4 ******************************************Complexite des methodes de manipulation de sequence******************************************

Chaque methode de manipulation de sequence peut etre differente, c’est a dire:

Pour les listes on peut avoir des durees plus ou moins longues en dependant de la liste (en memoire), une liste peut avoir (ou pas) de l’espace pour rajouter des valeurs, etc.

Ces operations peuvent durer beaucoup plus longtemps si cet espace n’est pas present, comme un simple `.append(x)` qui necessitera une copie totale de la liste.

Pour les operations sur les ensembles, tout depend majoritairement des longeurs de ces ensembles, car il faudrait iterer a traver l’ensemble le plus long.

Pour les dictionnaires, on fait aussi appel a comment un dictionnaire est accede en memoire (avec du hashage). S’il y a des collisions (valeur pas trouvee via le hashage du 1er coup), ces durees peuvent etre plus longues. Il n’y donc pas de valeur minimale mais moyenne, car on hypothese qu’il n’y a pas de collision.

## Chapitre 8: Logique, invariant et verification d’algorithme

9:03 - Begin Read

10:33 - Done Read

10:41 - Begin Notes

12:08 - Done Notes

Il est nécessaire de tester des algorithmes avec toutes les données possibles pour être sûr qu'ils fonctionnent correctement dans tous les cas. Cela est pratiquement impossible à faire en pratique en raison du nombre énorme de données possibles. (s'applique seulement aux algorithmes séquentiels et déterministes)

Le problème de la vérification complète d'un algorithme est complexe et ne possède pas de méthode automatisable.

On presente par la suite la notation BNF, qui nous permet d’initier les expressions logiques comme `p $\land$ q` par exemple.

Une formule logique est consistente si elle est vraie pour au moins une interpretation et valide si elle est vraie pour toutes interpretations.

Il y a egalement un ordre dans les operateurs logiques:

$\neg < \land,\lor < \gets,\to, \leftrightarrow$

(Rappels de logique)

Invariant = affirmation ou assertion vraie

## Chapitre 9: Recursivite

15:12 - Begin Read

15:48 - Done Read

16:00 - Begin Notes

18:10 - Done Notes

La recursivite est une maniere de voir un probleme base sur le concept de recurrence en maths qui consiste a prouver que s(n) = f(n) pour n + 1, etc.

Cette maniere de decouper un probleme peut simplifier beaucoup la difficulte d’un probleme.

Par exemple si on prend la factorielle `n! = n * (n - 1)`, on a une maniere iterative de resoudre ce probleme avec une boucle qui prend toutes les valeurs allant de 1 jusqu’a n + 1 et on a une maniere recursive qui consiste a re-utiliser la fonction quand on veut trouver n - 1, c’est a dire

```python
def fact(n):
	return 1 if n == 0 else n * fact(n - 1)
```

On peut utiliser cette methode pour simplifier d’autres choses (comme la conjecture de syracuse (que je connais pas)).

Ou par exemple (mon favoris), la recherche dichotomique (binary search), que je sais pas faire 100% sans recursion:

```python
def rech_dicho(s, x, g, d):
	if g >= d:
		return -1
	else:
		m = (g + d) // 2
		if s[m][0] > x:
			rech_dicho(s, x, m + 1, d)
		elif s[m][0] < x:
			rech_dicho(s, x, g, m)
		elif s[m][0] == x:
			return m
```

Prenons une fonction foo qui fait quelque chose pour le cas `n = 0`:

```python
def foo1(n):
	if n == 0:
		print(f"cas de base: {n}")
	else:
		print(f"pre-traitement: {n}")
		foo(n - 1)
```

On peut observer qu’on peut avoir des verifications / conditions, pre / post trairement (avant / apres la recursion).

```python
def foo2(n):
	if n == 0:
		print(f"cas de base: {n}")
	else:
		foo(n - 1)
		print(f"post-traitement : {n}")
```

On aurait donc deux cas qui peuvent etre combines:

```python
foo1(5)
>> pre-traitement: 5
>> pre-traitement: 4
>> pre-traitement: 3
>> pre-traitement: 2
>> pre-traitement: 1
>> cas de base: 0

foo2(5)
>> cas de base: 0
>> post-traitement: 1
>> post-traitement: 2
>> post-traitement: 3
>> post-traitement: 4
>> post-traitement: 5
```

Donc ici le concepte est qu’on peut, pour des problemes plus complexes, verifier, faire des operations, etc **AVANT** et **APRES** la recursion, comme dans la recherche dichotomique ou l’appel a la fonction etait juste pour modifier les valeurs donnees a la fonction.

On peut noter qu’une fonction foo peut etre appelee fonction ***pere*** `foo` qui fait appel a la fonction ***fils*** `foo` dedans.

Pour des recursions avec pre-traitement, on a deux exemples:

1. Permutations
2. Tri rapide (quicksort)

Les permutations comptent avec un prefixe, dans une sequence, toutes les permutations possibles avec les symboles de cette sequence (pas trop compris)

Le tri rapide est une maniere de trier une liste qui consiste a avoir un pivot (par exemple, le premier element) et aller a gauche et a droite de cet element pour ensuite trier les elements. On applique recursivement la meme chose pour chaque element a gauche et a droite jusqu’au moment ou la longueur de la liste devient 0 ou 1, qui implique que la liste a bien ete triee.

Les fonctions recursives avec post-traitement on a besoin d’avoir la valeur fils avant de pouvoir avoir la valeur pere, ou la valeur finale.

On a une fonction `eval`, qui, comme son nom l’indique, evalue une expression. Par exemple, si on a `4 + 5 * 7`, pour avoir la valeur finale, on a `4` (qui est obtenu instantanement) et puis `5 * 7`, qui doit doit etre egalement evalue recursivement pour avoir la valeur de la multiplication.

On peut aussi avoir la fonction du tri par fusion, qui trie une liste qui est decoupee en 2 et triee recursivement, PUIS fusionne recursivement les 2 listes dans l’ordre. (pas compris 100%)

Les representations graphiques ou les arbres binaires sont egalement des fonctions recursives.

Par exemple S = (V, E) avec S etant une structure de donnees avec V ensembles de E elements (ou paire d’elements (aussi appeles couples)). Si E sont que des elements, S est non oriente. Si E sont des couples, S est oriente.

En Python, ca pourrait donner, pour S etant des gens V qui ont pour relation E = ‘connait’:

```python
s = {"Jean": ["Michel", "Charlotte"],
		 "Michel": ["Jean"],
		 "Charlotte": ["Jean", "Luc"],
		 "Luc": []
}
```

Les arbres binaires sont ou soit vides ou soit composes de noeuds, et ces noeuds sont egalement a leur tour des arbres binaires. On peut appeler les 2 noeuds ‘noeud gauche’, ‘noeud droit’.

Par exemple `4 + 5 * 7`, ca donne en Python (et arbre binaire du coup)

```python
eval = [4, '+', [5, '*', 7]]
```

En Python, tout est objet (ou fait reference a un). Cela veut dire qu’une variable, nommee `a` par exemple est un objet. Cet objet a un type, donne par `type(a)`, une adresse, donnee par `id(a)` et un contenu.

Par exemple:

```python
a = 1
a = a + 4
```

Ici, on fait un objet nomme `a` qui est de type `int` et qui pointe vers une valeur `1`.

Ensuite on modifie l’adresse de `a` en rajoutant un autre objet de type `int` et de valeur `4`.

Egalement, en Python, une variable peut etre globale, c’est a dire une valeur en memoire qui est en dehors de tout, soit locale, c’est a dire une valeur qui n’est en memoire que pendant l’appel d’une fonction.

Pour la gestion en memoire, sont presents 2 types de … , runtime stack et runtime heap. Le runtime stack sert a stocker les espaces de noms globales et les espaces de nom locaux.

(Vraiment complique)

Pour les noms locaux, on rajoute a runtime stack, temporairement la/les variables pendant qu’on fait appel a une fonction foo (dans ce qu’on appelle des trames). Par la suite, lorsqu’il y a un return ou qu’on veut utiliser la variable locale, celle ci est enlevee de runtime stack et rajoutee en haut de runtime stack de la fonction qui fait appel a cette variable.

Un objet reste tout le temps en memoire et pour cela on introduit le terme ‘garbage collector’, une fonction, mais pas vraiment qui est utilise quand on veut utiliser l’adresse en memoire d’un objet. Ceci est fait de maniere transparente et cela prend un peu de temps qui n’est pas remarquable quand on tourne un code, sauf pour quelque milliers de seconde.

(Fin complique)

Decortiquons ensuite la fonction merge_sort avec une liste `list(”DCBA”)`. On observe comment les valeurs de `t1`, `t2`, `t` et `res` sont gardees dans la memoire avec les trames et vers quelles valeurs globales elles pointent a travers l’execution du programme.

## Chapitre 10: Exceptions

8:44 - Begin Read

8:54 - Done Read

9:00 - Begin Notes

9:31 - Done Notes

Une exception se produit quand un code rencontre une valeur ou une exception qui produit une erreur dans le programme. On peut appeler ca egalement des valeurs anormales. Le probleme principal avec les exceptions c’est qu’elles arretent brutalement l’execution d’un programme, et donc le programme en question ne se finit pas.

Pour gerer ces exceptions, il y a la methode `raise`**.**

```python
def foo(x):
	n = int(x)
	if n is not isInstance(n, int):
		raise TypeError(n, 'is not an integer')
```

On peut donc montrer qu’il y a une erreur et donc pouvoir quand meme executer (ou pas) le programme.

Il y a 4 types communs d’erreurs:

| TypeError | Type de valeur interdit |
| --- | --- |
| ValueError | Valeur interdite |
| IOError | Erreur avec un fichier ou fichier non existant |
| IndexError | L’index est trop grand ou petit par rapport a la liste, ou l’index n’existe pas dans la liste |

Il y a donc deux solutions pour ne pas arreter un programme brutalement avec une exception:

- Ajouter des conditions

On a cependant des problemes avec cette solution. Il y a beaucoup trop de cas a verifier, le code peut prendre du temps a s’executer puisqu’il faut verifier chaque condition / cas, et un cas seul peut avoir des centaines de types d’erreurs a annoter, ce qui n’est pas tres optimal pour un code ET egalement ca peut prendre plus de temps pour chercher chaque cas possible.

- Utiliser la methode `try-except`

Cette solution est la meilleure puisqu’elle fonctionne d’une maniere optimale.

La syntaxe etant:

```python
try:
	# code
except:
	# code a executer en cas d'erreur
```

Cette methode nous permet d’essayer un code et catch tout type d’erreur possible et faire quelque chose en cas d’erreur, sans devoir passer par chaque cas.

On peut egalement modifier la syntaxe pour catch des erreurs specifiques:

```python
try:
	# code
except ValueError:
	# code a executer en cas d'erreur liee a une valeur interdite
```

On peut meme prendre un tuple d’erreurs et regrouper des types d’erreurs, etc. Apres `except` il est aussi possible de faire un `else` si par exemple il n’y aucune erreur qui a etee `catch`.

`except` peut aussi prendre un valeur et etre utilise pour montrer le detail de l’erreur qui a ete `catch`:

```python
try:
	# code
except TypeError as e:
	print('Wrong variable type:', e)
else:
	# continuation du code si aucune exception est produite
```

A ne pas oublier qu’il est possible aussi de rajouter un cas nomme `finally`. Ce cas s’executera meme s’il y a une exception ou pas, ce qui est tres utile par exemple si on veut faire des taches de “clean-up”, ou par exemple sauvegarder un fichier avant qu’il ait une exception.

Une exception est donc, pour resumer, une erreur qui se produit de maniere exceptionnelle et arrete brutalement un programme si elle n’est pas geree correctement.

## Chapitre 11: Objet et classe

9:57 - Begin Read

10:33 - Done Read

11:35 - Start Notes

12:47 - Done Notes

On a vu qu’en Python tout variable est un objet. Un objet a un type, un identificateur en memoire et une valeur. Ces valeurs, types, etc sont gardees en runtime heap qui contient le runtime stack des valeurs pointees par des variables dans une fonction a un instant precis.

Maintenant on peut voir comment on peut creer nos propres classes d’objets et ensuite creer et manipuler ces objets de cette classe.

Pour definir une classe (un type), on doit instancier ce nouvel type de la maniere suivant:

```python
class Point(object):
	# code
```

Avec `class` etant la definition de ce nouvel type, `Point` etant ecrit avec une majuscule (par convention) et qui contient un objet a l’interieur.

On peut ensuite creer des objets de la classe Point en utilisant Point comme une fonction.

Ce qu’il se passera ensuite c’est que les objets seront de type Point et seront une instance de la classe. L’instance ensuite montrera, quand printee, qu’elle est de type classe et qu’elle pointe vers l’adresse en memoire ou cette instance est stockee (en hexadecimal).

Ces objets auront, ou plutot peuvent avoir eux memes des attributs qui sont definis simplement avec un point.

```python
p = Point()
p.x = 4.0
p.y = 8.0
```

Les attributs peuvent egalement etre des objets a leur tour.

```python
box = Rectangle()
box.w = 100
box.h = 40
box.corner = Point()
box.corner.x = 0
box.corner.y = 0
```

On peut faire une fonction qui cree un objet et qui retourne la reference vers celui-ci.

Maintenant un probleme ressort: on a un point et on souhaite faire un 2eme qui a les memes coordonnees que le 1er. Si on change la valeur d’un ou des coordonnees du 2eme point, on observe que le 1er point changera egalement. Ceci est du au fait qu’un objet peut faire reference aux memes attributs d’un autre objet, et donc se refere au memes valeurs.

Pour regler ce probleme, on peut d’une effectuer un `.copy()`, qui va creer une instance separee de l’objet et donc p1 et p2 ne seront pas le meme objet, MAIS, auront les memes attributs.

Donc maintenant parvient un 2eme “probleme”, qui peut etre resolu en faisant un `.deepcopy()` d’un objet  qui va creer une instance completement independante / separee d’un objet et donc on remarque que les attributs mutables seront eux aussi copies vers cette nouvelle instance.

Maintenant qu’on a vu les attributs des objets de type classe, on remarque qu’il n’y a pas que ca. On parle maintenant de methodes.

Une methode est une fonction qui va travailler sur les objets d’un type defini, en gros une fonction qui travaille uniquement avec les objets dedans une classe.

Egalement, toute methode va faire appel a ces objets avec self (par convention).

Une methode souvent utilisee est la methode `__init__`. Cette methode permet, lors de l'initialisation d'une classe / type, d'avoir des attributs par defaut et ensuite assigner ces attributs a l'objet de type classe.

```python
class Time():
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second
```

On a aussi la methode `__str__`, qui elle va se charger de la representation de l'objet avec les print() etc. Par exemple:

```python
class Time():
	# ...
	def __str__(self):
		print("{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.minute, self.second))
```

Et la methode `__repr__`, qui elle va se charger de la representation entiere de l'objet, c'est a dire si c'est un string, la methode va montrer cela avec des ' ', etc.

Par la suite, on peut surcharger un operateur. Cela veut dire qu’on modifie ***************************************manuellement*************************************** le comportement d’un operateur pour un type. Par exemple ‘+’ peut etre modifie via la methode `__add__` et le programmeur peut ensuite decider ce qu’il se passe quand une operation avec ‘+’ est appelee a un objet.

On peut faire ca pour chaque operateur possible.

Egalement, l’ordre d’une operation peut avoir (ou pas) une importance si le programmeur decide de s’occuper de cela. Par exemple si on veut faire `5 + Time(4, 50, 3)` , on est dans un cas d’erreur sauf si on utilise la methode `__radd__` qui elle s’occupe de gerer une addition si l’objet est a droite.

Introduisons finalement le concept de polymorphisme. Ce concept est base sur le fait qu’on peut appliquer des fonctions sur des objets d’un certain type pour peu qu’on utilise les operations gerees par la classe, donc on peut par exemple utiliser `sum()` sur des objets de type `Time()` .

Finalement, la programmation orientee objet, ou plus court, POO, consiste a coder, comme en Python ou Java ou C++, des objets avec des attributs et des methodes et pouvoir modifier le comportement de ceux-ci.
