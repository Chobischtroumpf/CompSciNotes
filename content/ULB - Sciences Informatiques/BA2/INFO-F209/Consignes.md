---
title: Consignes
authors: Alessandro Dorigo
tags:
  -
---

Tout au long du projet, vous pouvez, et on vous encourage, à prendre rendez-vous avec votre assistant pour vous assurer que votre travail progresse correctement. Aucune réunion régulière n'est imposée si ce n'est celles en fin d'itération, mais il est recommandé d'en organiser suffisamment pour vous assurer que votre produit réponde aux attentes des clients et que le code soit conforme aux exigences du projet.
## Phase 1: SRD + Prototype de base
Nous vous demandons de remettre un prototype primitif de l'application.

Celui-ci devra simplement permettre de faire tourner une version locale de Tetris, sans modes de jeux ou fonctionnalités complexes telles que la gestion d'une base de données ou d'autres éléments avancés.

1. **Architecture Générale**: Décrire les modules principaux (par exemple, gestion des joueurs, gestion du plateau de jeu, logique de jeu, gestion des malus/bonus). Expliquer comment ces modules interagiront et l'architecture globale du programme (ex: modèle MVC ou autre design pattern pertinent).

2. **Diagrammes UML**:
   - **Diagramme de classes**: Montrer les classes principales comme `GameManager`, `Player`, `Tetrimino`, `Grid`, `MalusHandler`. Indiquer leurs relations (associations, dépendances) et les principales méthodes et attributs.
   - **Diagrammes de séquence**: Illustrer des scénarios importants, comme la séquence d'envoi de malus entre joueurs ou l'ajout d'une ligne dans le plateau d'un adversaire lors d'un combo.
   - **Diagramme d'activités**: Expliquer les processus critiques comme l’initialisation d’une partie, l'ajout d'un malus ou l’achèvement d’une ligne.

3. **Description des Fonctionnalités**: Détail des fonctionnalités de base, incluant:
   - **Logique de Tetris**: Placement des pièces, rotation, vérification des lignes complètes, gestion de la fin de partie.
   - **Gestion des Malus/Bonus**: Explication du système de malus (ex. l'ajout de lignes en fonction du nombre de lignes complétées), possibilité de cibler un adversaire dans le mode Classic.
   - **Modes de jeu**: Description des différents modes (Endless, Classic, Duel, Royal Competition) et leurs particularités.

4. **Prototype**: Expliquer le prototype que tu as réalisé, qui sera une version simplifiée de Tetris sans fonctionnalités avancées (ex: base de données, chat).

## Phase 2: Terminal Tetris Royale
Implémenter toutes les règles nécessaires au bon déroulement du Tetris Royale.

Il vous sera également demandé de créer un menu de jeu et de gérer toute la partie réseau, permettant ainsi à plusieurs joueurs de s'affronter via un réseau local (LAN) en mode terminal.

À ce stade, les fonctionnalités de création de compte, gestion d'amis, et autres doivent être opérationnelles.

À la fin de cette phase vous devrez faire une présentation de votre projet. Un feedbak vous sera alors aussi remis avant le début de la prochaine phase.

## Phase 3: GUI Tetris Royale
Implémentation de l'interface graphique (GUI) et aux demandes supplémentaires des clients en début de cette phase.

Cette phase se terminera par une présentation de votre application entière dans les salles du `NO`.

***Votre application doit tourner sur les machines du `NO`. Veillez à vérifier avant chaque remise***
***que ceci est bien le cas.***
