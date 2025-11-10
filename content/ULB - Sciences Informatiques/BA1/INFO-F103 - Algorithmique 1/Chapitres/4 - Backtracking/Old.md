---
title: Old
authors: Alessandro Dorigo
tags:
  -
---

Le backtracking permet de trouver une solution à un problème en essayant différentes voies.
Si le choix d’une voie s’avère incorrect pour mener à la solution, l’algorithme repart en arrière *(backtrack)* et repart du point où il a fait le choix de cette voie afin d’en choisir une autre.
## Recherche exhaustive
La génération exhaustive (ou recherche exhaustive) consiste en l’écriture de programmes qui énumèrent toutes les structures possibles appartenant à un ensemble donné. Plus généralement, l’ensemble à générer pourra être vu comme l’ensemble des *solutions possibles* d’un problème informatique donné.

[[Chap 04 - slides_backtracking.pdf#L’énumération de tous les mots de cinq lettres]]
## Génération exhaustive
Nous aimerions remplir une liste `s` de `n` booléens avec toutes les affectations booléennes possibles.

Une implémentation récursive résolvant le problème par backtracking peut utiliser une fonction `generate_words` qui remplit la liste `s` avec tous les mots booléens possibles, mais seulement entre les positions `i` et `n - 1`.

[[Chap 04 - slides_backtracking.pdf#Mots booléens]]

Nous voyons donc que la valeur de `i` n’a cessé d’osciller entre 0 et 2, ceci est dû à la structure du programme récursif, qui après l’appel récursif à `i + 1`, revient à l’ancien `i` pour continuer son travail.

[[Chap 04 - slides_backtracking.pdf#Mots alphabétiques]]

De ces exemples nous pouvons déduire un canevas réalisant une génération exhaustive par backtracking:
```
def essai(i):
	if terminé:
		if solution trouvée:
			afficher solution
	else:
		for choix in choix possibles:
			construire solution partielle
			essai(i + 1)
			démolir solution partielle
```
Nous y procédons par *filtrage*, en générant de façon exhaustive directe un sur-ensemble de l’ensemble recherché, et en veillant, dans le test d’arrêt, à éliminer les éléments n’appartenant finalement pas à la solution.

Certaines des constructions doivent parfois être défaites au retour de l’appel récursif, avant que l’on puisse réitérer la boucle et construire la solution partielle correspondant au cas suivant.
## Canevas de recherche d’une solution
```
def essai(i):
	if terminé:
		if solution trouvée:
			afficher solution
			return True
	else:
		for choix in choix possible:
			if choix admissible:
				construire solution partielle
				if essai(i + 1):
					return True
				démolir solution partielle
	return False
```
## Canevas de recherche de la meilleure solution
```
def essai(i):
	if terminé:
		if solution trouvée et solution meilleure:
			sauvegarder solution
	else:
		for choix in choix possibles:
			if choix admissible:
				construire solution partielle
				essai(i + 1)
				démolir solution partielle
```
## Canevas de branch and bound
```
def essai(i):
	if terminé:
		if solution trouvée et solution meilleure:
			sauvegarder solution
	else:
		for choix in choix possibles:
			if choix admissible:
				construire solution partielle
				if solution semble meilleure:
					essai(i + 1)
				démolir solution partielle
```
## Canevas d’une recherche non récursive d’une solution
```
def essai:
	i = 0
	ok = False
	initialisation du premier choix
	while i >= 0 and not ok:
		while not ok and choix possible:
			if choix admissible:
				ok = True
			else:
				choix suivant
		if ok:
			sauvegarder choix
			construire solution partielle
			i += 1
			ok = solution trouvée
			if not ok:
				initialisation du choix i
		else:
			if i != 0:
				i -= 1
				démolir solution partielle
				retrouver choix
				choix suivant
			else:
				i -= 1
		return ok
```
