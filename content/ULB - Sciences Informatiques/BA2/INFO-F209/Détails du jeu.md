---
title: Détails du jeu
authors: Alessandro Dorigo
tags:
  -
---

## Description
**Tetris Royale** est une version multijoueur compétitive du célèbre jeu **Tetris**.

- Lorsqu'une ligne est complétée, elle disparaît et le joueur gagne des points.
- **Tetris Royale** se distingue des autres versions de **Tetris**, en ce que chaque joueur peut envoyer des [[Détails du jeu#^08f910|malus]] à ses adversaires sous forme de **lignes incomplètes** supplémentaires lorsqu'il réussit à compléter plusieurs lignes en un seul coup.

- Le but du jeu est de survivre **le plus longtemps possible**. Le dernier joueur en vie, **après que tous les autres aient perdu**, est déclaré **vainqueur**.

> [!info]+ Malus Classique
> Un **malus** est une ligne supplémentaire ajoutée en bas de la grille d’un joueur adverse. Elle contient des *blocs gris avec un espace vide*, qui force les autres lignes à monter, rapprochant le joueur de la défaite.

^08f910

> [!note]
> Si plusieurs lignes de malus sont rajoutées, le bloc manquant est le même pour toutes les [[Détails du jeu#^08f910|malus]] d'un même combo.

## Partie
Chaque joueur commence avec une **grille vide** de taille $10 \times 20$.

*Les pièces tombent du haut de la grille et doivent être déplacées et tournées par le joueur. Si un joueur complète une ligne, elle disparaît de sa grille.*

Chaque fois qu'un joueur fait un **combo** (complète plusieurs lignes à la fois), il envoie des malus à un autre joueur:
- 1 ligne complétée n'envoie **pas de [[Détails du jeu#^08f910|malus]]**,
- 2 lignes complétées envoient **1 ligne de [[Détails du jeu#^08f910|malus]]**,
- 3 lignes complétées envoient **2 lignes de [[Détails du jeu#^08f910|malus]]**,
- 4 lignes complétées (Tetris) envoient **4 lignes de [[Détails du jeu#^08f910|malus]]**.

Des **règles spéciales** peuvent être ajoutées pour rendre la partie plus dynamique: par exemple, un joueur peut **déclencher un envoi de malus en série** ou **bloquer temporairement les commandes d'un adversaire** (cf. modes de jeu).

## Modes
### Endless
Mode de jeu à un **seul joueur**. Le joueur **gagne des points** en **fonction de ses combos**. Les pièces **tombent de plus en plus vite**. Son score final finit dans un **classement en ligne** (?).
### Classic
Se joue en **groupe de 3 à 9 joueurs**, où les groupes s'affrontent dans des **parties simples** avec uniquement les **[[Détails du jeu#^08f910|malus basiques]]**. Le **dernier joueur en vie** est le **gagnant**.

- Bien que les malus soient envoyés automatiquement lorsqu'ils sont disponibles dans ce mode, le **joueur doit être capable de changer le joueur actuellement ciblé par ses malus**.
### Duel
Suit les mêmes règles que le mode **Classic** mais se joue en **un contre un**.
## Royal Competition (Tricky Towers)
Les **malus ne sont plus envoyés automatiquement**, les joueurs reçoivent de l'énergie lorsqu'ils détruisent des blocs et lorsqu'ils ont suffisamment d'énergie peuvent choisir d'envoyer un malus (`K`) ou de s'octroyer un bonus (`J`).

- Il se joue par groupe de 3 à 9 joueurs.
### Bonus
- Réduire la vitesse de chute des pièces de son propre plateau pendant un moment.
- Vos 2 prochaines pièces se transforment en blocs de $1 \times 1$.

- *Removes your last placed brick.*
### Malus
- Bloquer les commandes du joueur ciblé pour la pose du prochain bloc.
- Inverser les commandes du joueur ciblé pour la pose des trois prochains blocs.
- Envoyer un éclair qui supprime les blocs dans une zone de $2 \times 2$ chez le joueur ciblé.
- Éteindre la lumière, le joueur ciblé ne voit plus son tableau pendant un court moment.
- Augmenter la difficulté pour un adversaire en accélérant la chute de ses pièces.

- *Bricks rotate on their own. ($\approx 3$ sec per rotation)*
## Fonctionnalités de l'application
**IMPORTANT!!!!!!!!!!!!**
Toutes les fonctionnalités doivent être accessibles et pleinement fonctionnelles sur les deux interfaces (terminal et GUI).

**Les joueurs utilisant une interface en mode terminal doivent pouvoir jouer contre ceux utilisant la GUI, et inversement, sans problème de compatibilité.**
### Touches

| ![[Pasted image 20241108123939.png]] | ![[Pasted image 20241108124706.png]] |
| :----------------------------------: | :----------------------------------: |

### Menu Local

| ![[Pasted image 20241108124424.png]] | ![[Pasted image 20241108124434.png]] |
| :----------------------------------: | :----------------------------------: |
### Menu En-ligne

| ![[Pasted image 20241108124501.png]] | ![[Pasted image 20241108124508.png]] |
| :----------------------------------: | :----------------------------------: |
| ![[Pasted image 20241108124550.png]] | ![[Pasted image 20241108124608.png]] |
### Network
- Créer un compte associé à un pseudonyme et un mot de passe
- Se connecter à son compte
- Gérer une liste d'amis
- Discuter avec ses amis
	- Le chat devra être accessible dans tous les menus du jeu, permettant aux joueurs de communiquer facilement avant et après les parties.
	- Cependant, durant une partie active, vous n'êtes pas obligés de rendre le chat accessible.
	- Assurez-vous néanmoins que la transition entre l'accès au chat et la désactivation pendant une partie soit fluide.

- Configurer et créer une partie
	- Mode de jeu;
	- Le nombre maximum de joueurs (pour Classic et Royal Competition).
	- Dans les modes multijoueurs, chaque joueur doit pouvoir voir les tableaux des autres joueurs.
	- Ces tableaux devront être cachés idéalement en version réduite pour ne pas encombrer l'interface principale tout en fournissant une vue d'ensemble claire de l'état des autres joueurs.
	- Le tableau du joueur actif doit rester en taille normale et être bien discernable des autres.
- Rejoindre une partie déjà créée
- Inviter un ou plusieurs amis à sa partie en tant que joueur ou observateur

- Consulter le classement des meilleurs joueurs du mode Endless
### Options

| ![[Pasted image 20241108124631.png]] | ![[Pasted image 20241108124638.png]] | ![[Pasted image 20241108124651.png]] |
| :----------------------------------: | :----------------------------------: | :----------------------------------: |
