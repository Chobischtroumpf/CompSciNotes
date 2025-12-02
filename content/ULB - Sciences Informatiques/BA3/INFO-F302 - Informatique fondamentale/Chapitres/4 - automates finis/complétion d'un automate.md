---
title: complétion d'un automate
authors: Mihai Bors
tags: []
---

# complétion d'un automate
- un automate est dit complet si sa fonction de transition est totale
	- ie. sa fonction de transition est définie pour toutes les combinaisons d'états et de symboles

## lemme
- on peut toujours transformer un automate $A$ en un automate $B$ complet qui accepte le même langage
	- tq $L(A) = L(B)$
	- il faut définir les couples (état, symbole) pas compris dans la fonction de transition définie pour l'automate $A$

- idée de la preuve
	- ajouter un état supplémentaire (= état puits) non final
	- ajouter les transitions manquantes vers cet état

**exemple**
![[76e66301a1e6309dd515e2d591a1a1fc.png]]
