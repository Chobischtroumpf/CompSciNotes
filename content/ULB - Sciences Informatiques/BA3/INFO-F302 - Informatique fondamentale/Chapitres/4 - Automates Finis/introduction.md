---
title: introduction
authors: Mihai Bors
tags: []
---

- automates finis
	- modèle de calcul abstrait
	- accepte ou rejette des séquences de symboles (= mots)
	- nb fini d'états
	- nombreuses applications
	- nombreuses extensions
## exemples
- automate fini
	- lit séquence des lettres de gauche à droite
	- possède un nb fini d'états
	- en fonction de l'état courant et de la lettre lue
		- se déplace vers un autre état
	- possède un état initial
		- rep par une flèche sans source
	- possède états finaux ou acceptants
		- rep par des doubles cercles
	- il accepte le mot ssi lorsqu'il arrive à la fin du mot : il se trouve dans un état final
![[2ca184c171a2f1a8dee7f427fb19b91b.png]]
![[a0856ec7d4c45c39d59c9e5d2acc2ace.png]]
### exercice 1
![[0ce8e1687d9591f0d4545bd393d5344b.png]]
- quel est l'automate qui accepte l'ensemble des mots sur l'alphabet $\Sigma = \set{a,b}$ qui contiennent au moins un lettre ?
	- donc tous les autres mots sont rejetés

- réponse
	1. l'automate rejette uniquement $\epsilon$, le seul mot de longeur 0
		- accepte tous les autres
		- → réponse
	2. l'automate accepte uniquement les mots de longueur $1$
		- rejette tous les autre mots
	3. l'automate accepte tous les autres mots
		- y compris le mot vide de longueur 0

### exercice 2
![[5d32cf9b26a24cf3902d50ee174030c8.png]]
- quel est l'ensemble des mots reconnus par l'automate suivant ?
	- sur l'alphabet {0,1}
- réponse
	- c'est l'ensemble des mots  sur l'alphabet {0,1} qui possède 00 pour facteur

### exemple : recherche textuelle
- on veut trouver toutes les occurences de $101$ dans une séquence de bits
- on va construire un automate avec un état spécial tel qu'à chaque fois qu'on entrera dans cet état
	- c'est qu'on vient de lire $101$

- **revoir cette merde car j'ai  pas compris le diagramme de l'automate**
![[8b133a7e7cce8e071d122d8343f7e2f9.png]]

## applications possibles
- en informatique théorique
- modélisation de protocoles réseau
- analyse de texte, recherche textuelle
- compilation (analyseur lexicaux)
- preuve automatique de programme (théorie du model-checking)
- ...

## avantages/inconvénients des automates
- avantages
	- classe de programmes simples mais ayant de nombreuses applications
	- bien compris, nb résultats, nb algo pour les analyser
	- robustes
		- bcp de caractérisations
			- expressions rationnelles
			- logique
			- régularité
			- algébrique
			- ...
		- clotûre par opérations booléennes

- inconvénients
	- peu puissants
	- peu compacts
