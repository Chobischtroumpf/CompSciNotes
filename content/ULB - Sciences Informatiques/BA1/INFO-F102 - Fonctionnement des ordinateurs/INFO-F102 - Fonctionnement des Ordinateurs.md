---
title: INFO-F102 - Fonctionnement des Ordinateurs
authors: Alessandro Dorigo
tags:
  - ULB
  - BA1
---


## Chapitre 2: Representation de l’information

Code de Hamming:

- Tous les bits d’indice $i$, tel que $i = 2^k$:
    - Bits de controle
- Le reste - donnees

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- |
| C1 | C2 | D3 | C4 | D5 | D6 | D7 |

C1 → D3, D5, D7 → D3 XOR D5 XOR D7

C2 → D3, D6, D7 → D3 XOR D6 XOR D7

C3 → D5, D6, D7 → D5 XOR D6 XOR D7

- Si 2 ou + bits de controle problematiques = donnee fausse
- Si 1 bit de controle problematique = bit de controle faux

## Chapitre 6: Le langage machine

Le langage machine est un langage simple (ou plutot au niveau le plus bas) qui agit directement sur le processeur. Chaque processeur a son propre langage machine, ou plutot a son propre syntaxe.

Dans ce chapitre, nous verrons en detail le langage machine propre au micro-processeur intel i486.

Egalement, ce langage systeme est ecrit de maniere textuelle pour pouvoir aider les programmeurs a coder et ensuite faire le lien plus facilement entre hardware et code.

Qu’est-ce qu’une architecture? Une architecture de processeurs se refere a une famille de microprocesseurs comme intel, amd ou arm par exemple, qui a part la syntaxe, ont egalement des differences sur les types de donnes qu’il peuvent traiter, la memoire libre, etc.

Le processeur 6502, qui est beaucoup plus simple que celui d’intel, pourvu qu’il est egalement plus ancien, possede des registres qui tiennent sur 8 bits:

- `A`, `X`, `Y`, `SP` et `P` avec `A` qui accumule et sert aux operations arithmetiques, `X` et `Y` qui servent a calculer des adresses, `SP` qui est le pointeur du stack et `P` le registre des flags.
- Ses adresses tiennent sur 16 bits, ce qui lui permet d’avoir 64 ko de memoire.
- Ses instructions tiennent sur un, deux ou trois octets, dont le 1er octet sert d’opcode.

Dans le cas du 6502, son modele memoire (modele memoire = comment le processeur voit/interprete la memoire) est tres simpliste:

Toutes les adresses memoire font reference a une adresse physique et tiennent sur 8 bits, c’est a dire de 0 a 255.

Pour le processeur intel i486, cela est plus complexe:

Celui-ci fonctionne en 2 modes, le mode reel et le mode protege.

Le mode reel sert essentiellement pour des raisons de compatibilite avec les precedents processeurs dans la meme architecture. Ce mode laisse le processeur travailler qu’avec 1 Mo de memoire, qui est vue comme un ensemble de segments qui sont des portions de memoire de 64 ko. Un segment peut commencer peu importe ou si l’adresse est un multiple de 16. Ces adresses possedent:

- un numero de segment S sur 16 bits
- une adresse dans le segment O sur 16 bits

L’adresse reelle est donc calculee par la formule - $S \times 2^4 + O$

Le mode protege par contre, travaille sur 32 bits, ce qui veut dire qu’un segment peut a present faire jusqu’a 4 Go, ce qui correspond a la taille de la memoire physique, puisque le processeur a un bus d’adresse de 32 bits et peut donc adresser que $2^{32}$ octets.

Les processeurs peuvent utiliser des nombreux registres, mais ces nombreux registres existent essentiellement en 2 types:

- les registres de travail qui contiennent des valeurs interchangables pour des operations
- les registres de controle qui servent au bon fonctionnement d’un programme et ne contiennent pas de donnees

En outre, le i486 possede 4 registres de travail 32 bits `eax` `ebx` `ecx` et `edx` et 8 de travail 80 bits pour les nombres flottants. Il possede 4 registres index `esi` `edi` `ebp` et `esp` qui servent a faire des calculs d’adresse, le registre `eip` qui est pointeur de programme, 6 registres 16 bits qui permettent de selectionner des segments `cs` `ds` `es` `fs` `gs` et `ss` et 1 registre de flags.

Pour etre compatible avec ses ancetres 16 bits, les 8 bits de poids faible de `eax` sont appeles `al` et les bits de 8 at 15 `ah` .

Le langage machine permettra donc de manipuler:

- des donnees booleennes
- des donnees numeriques
- des donnees non-numeriques (mais plus rare)

Le coeur du langage machine, c’est son jeu d’instructions. Une instruction est en general caracterisee pas un opcode qui identifie celle ci. Plus un processeur est complexe, plus le jeu d’instruction est plus etendu.

Ces jeux d’instructions peuvent etre classifies:

- mouvement de donnees - elles servent a deplacer des donnees/travailler avec la memoire
- instructions arithmetiques, logiques - elles servent a faire des operations de tout type
- instructions de saut, comparaison et branchement - elles servent a modifier l’adresse dans le pointeur d’instruction PC via l’ajout d’une autre valeur soit l’ajout d’une valeur negative pour sauter a une autre etape/instruction dans le code (cela peut egalement etre execute si des conditions sont remplies)
- appels de procedures - elles servent a faire des appels de fonctions, en sauvegardant les valeurs en memoire a chaque appel via des push et pop vers le stack
- boucles - elles servent a pouvoir faire des boucles en comparant des registres
- entrees/sorties - elles servent a gerer les peripheriques et communiquer avec

Les instructions machine sont categorisees par 2 types:

- les instructions privilegiees, c’est a dire celles qui sont plus sensibles, par exemple celles qui communiquent ou travaillent sur les peripheriques
- les instructions non-privilegiees, c’est a dire celles qui ecrivent en memoire primaire ou qui font des simples calculs

Le processeur peut aussi avoir 2 types de modes:

- le mode superviseur, qui peut executer tout type d’instructions, inclus celles privilegiees
- le mode utilisateur, qui ne peut executer les instructions privilegiees et declenchera des erreurs

Dans notre cas, avec le processeur i486, on a 3 types d’instructions cette fois:

- les instructions privilegiees
- les instruction sensibles - elles gerent les entrees et sorties
- le reste

On a egalement 4 types de modes d’execution:

- type 0, utilise par le systeme d’exploitation, soit le plus privilegie
- type 1, utilise par le mode superviseur
- type 2, utilise par le mode superviseur
- type 3, utilise par le mode utilisateur

Les instructions ont egalement besoin d’etre adressees, et cela se passe avec les opcodes, mais on a un probleme: certains opcodes tiennent sur 8 bits car ils ont besoin des operandes plus longues, certains tiennent sur 16 bits donc les operandes sont plus courtes, etc.

On a 2 manieres pour resoudre le probleme entre les adressages: ou soit on veut rester sur 32 bits et on fait une lecture en memoire pour avoir les operandes, ou soit on decide d’avoir des tailles **********variables********** pour les adressages, c’est a dire avoir une representation specifique pour chaque opcode en binaire, avec une allant de `0000 0000` a `1111 1110` pour les opcodes a 8 bits, et une allant de `1111 1111 0000 0000` a  `1111 1111 1111 1111` pour ceux a 16 bits, qui nous permettra d’avoir 511 differents opcodes qui peuvent etre de taille variable.

L’adressage peut egalement etre divise en plusieurs types:

- adressage immediat - permet de stocker une valeur instantanement dans un registre
- adressage directe - permet de stocker une valeur qui se trouve dans la case memoire indiquee comme parametre
- adressage par registre - permet de stocker une valeur qui se trouve dans le registre indique comme parametre
- adressage par registre avec indirection - permet de stocker une valeur qui se trouve dans la case memoire a l’adresse du registre donne en parametre
- adressage indexe avec base - comme celle d’avant, sauf que le registre indique est lui meme donne par une valeur qui correspond a la case memoire de celui-ci

## Chapitre 7: Le mecanisme d’interruption

Dans ce chapitre, nous verrons la resolution d’un probleme observe jusqu’a present: on remarque qu’un ordinateur doit faire plusieur taches en meme temps. Pour ca, on doit rajouter donc un mecanisme d’interruption pour chaque action, comme quand une touche est pressee, la souris est deplacee, etc.

Mais ceci n’est pas le role du programmeur; de coder ca dans chaque probleme, donc faut voir comment integrer ca dans l’OS. Comment fonctionne un mecanisme d’interruption?

Grosso modo, ce mecanisme doit interrompre l’instruction en cours du processeur pour qu’il passe a la prochaine car la 1ere a ete finie avant que l’information est arrivee au processeur (un peripherique n’est pas aussi ‘rapide’ qu’un processeur).

En etapes, ca donne:

- le programme/peripherique renvoie un signal d’interruption
- le cpu detecte ce signal (sinon il attend que ce signal arrive a chaque tour de boucle)
- le gestionnaire d’interruption arrete le programme en cours, sauvegarde les donnees necessaires et passe la machine en mode superviseur
- le CPU modifie `PC` pour qu’il pointe vers la 1ere instruction du gestionnaire d’interruption, souvent nomme vecteur d’interruption
- le gestionnaire s’execute et doit sauvegarder les autres registres, traiter l’interruption, restaurer les registres sauves, le registre `PC`, les registres de controle et remettre la machine en mode utilisateur

Du coup le mecanisme d’interruption permet a un peripherique de demander au CPU de s’interrompre temporairement dans son traitement pour executer un gestionnaire d’interruption. Une fois le gestionnaire termine, le processeur reprend son execution de maniere transparente pour le programme interrompu.

Cependant, il faut qu’on met le gestionnaire d’interruption en mode superviseur, sinon il pourrait etre lui aussi a son tour interrompu, car c’est egalement un programme. On suppose donc que le mode utilisateur est le seul a pouvoir etre interrompu.

Pour realiser ce mecanisme d’interruption, il nous faut donc un test qui verifie si `IRQ` (le flag qui correspond a interruption request) est a 1 ou 0 ******************entre****************** deux programmes (on n’arrete pas au milieu d’un programme) puis passer l’ordinateur en mode superviseur, modifier dans `PC` la valeur du vecteur d’interruption et ensuite remettre `IRQ` a 0 et l’ordinateur en mode utilisateur. `IR` va ensuite recevoir l’adresse presente dans `PC` et demarrer le gestionnaire d’interruption.

On doit s’assurer que passer l’ordinateur en mode utilisateur et restaurer `PC` ont lieu en meme temps, sinon la protection offerte par les differents modes n’existera plus.

Le mecanisme d’interruption est utile dans plusieurs cas:

- les peripheriques - interruption quand une touche est appuyee, un click de la souris est present, etc
- les exceptions - interruption cree par le processeur lui-meme
- les defauts de page - interruption essentielle pour la pagination
- les appels superviseur - interruption qui a lieu quand un programme en mode utilisateur a besoin de passer en mode superviseur (par exemple ecrire sur le disque)

Le mecanisme peut avoir des extensions pour etre meilleur - comme pour l’interruption interruptible. Jusqu’a present, si on arrete un programme, puis on met un autre en mode superviseur, on ne peut pas arreter celui-ci, ce qui devient complique quand on envoie plusieurs interruptions, comme plusieurs touches en meme temps par exemple. On introduit donc un systeme de ************************PRIORITE************************ qui nous permettra d’arreter des gestionnaires de priorite plus basse pour en executer d’autres.

Il existe egalement des ‘ameliorations’ au niveau de la restauration des registres - surtout quand un programme envoie une interruption - ou soit qu’une partie des registres est restauree ou soit une sauvegarde a part est cree pour stocker ceux dont on a pas besoin

Comment fonctionne donc tout ca sur notre processeur Intel i486DX?

Ce processeur a deux types d’interruptions:

- les interruptions, qui proviennent de l’exterieur du processeur et peuvent etre ou soit masquables (ignorees) ou non-masquables
- les exceptions, qui proviennent cette fois de l’interieur du processeur et sont de 3 types:
    - les *******faults -******* erreurs de calcul, opcode invalide, page fault
    - les *****traps***** - demandes par un programme utilisateur de faire des operations qui necessitent d’etre superviseur
    - les ****aborts -**** erreurs graves et la continuation du programme n’est pas assuree

Ces interruptions possedent egalement des vecteurs d’interruption entre 0 et 255, qui est stocke dans `idtr` la table des vecteurs d’interruption.

Le code des interruptions doit etre place dans un segment de privilege 0 pour avoir acces aux instructions privilegiees.

Finalement, le processeur i486DX possede l’instruction `iret` qui effectue le retour d’interruption.

## Chapitre 8: Le systeme d’exploitation

Les premiers ordinateurs pouvaient seulement avoir un utilisateur / programme en cours. Ils avaient egalement pas de notion de fichier ou de répertoire, et les utilisateurs devaient présenter des cartes perforées ou des rubans perforés pour exécuter leur programme. Les programmes avaient un accès total à tous les périphériques.

Pour étendre le système pour qu'il puisse exécuter plusieurs programmes appartenant à plusieurs utilisateurs, il faut trouver des réponses à certaines questions. Les questions les plus importantes sont comment faire pour qu'un ordinateur avec un seul processeur puisse exécuter plusieurs programmes en même temps, comment éviter que ces programmes n'utilisent les mêmes zones de la mémoire primaire, et comment faire pour que l'accès à la mémoire secondaire soit plus structuré et partagé par tous les programmes.

Nous allons introduire deux techniques: le multitâche (et en particulier le temps CPU partagé), et la mémoire paginée. Il faut expliquer comment implémenter un système de fichiers, et que toutes ces tâches sont dévolues au système d'exploitation.

Les systèmes d'exploitation (OS) sont des composants logiciels d'un système informatique qui ont pour but de gérer de manière équitable et sûre les ressources matérielles du système.

L’OS constitue une interface entre le matériel et les applications qui s'exécutent sur l'ordinateur. Toutes les requêtes sont analysées et traduites par l'OS avant d'être effectuées par le matériel.

![Principe general de fonctionnement de l’OS](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled.png)

Principe general de fonctionnement de l’OS

Pour que l’OS soit securise (empecher l’acces direct au materiel), il nous faut un mecanisme de protection. Ce mecanisme peut etre divise en etapes:

- CPU en mode maitre si l’instruction provient du kernel
- Les programmes sont executes en mode utilisateur
    - S’il y a une tentative d’instruction privilegiee - erreur declenchee par le CPU
- Appel systeme quand une requete est presente
- Interruption pour le programme
    - Handler dans l’OS qui permet une interruption 100% transparente car celui-ci retourne les donnees suite a la requete

Pour exploiter les principes et mecanismes, il y a donc une serie de taches confiees a l’OS:

- Gestion de la memoire primaire
    - Stocke les programmes et leurs donnees - repartit la memoire entre les programmes qui s’executent → pagination a la demande
- Gestion des processus
    - Nombre des coeurs du CPU < programmes a executer en meme temps, donc l’OS a un module pour repartir le CPU en fonction des besoins → ordonnanceur
- Gestion des peripheriques
    - Acces a travers des appels de l’OS qui traduit les demandes
- Gestion des differents utilisateurs
    - Identifiants, mots de passe (avec un super-utilisateur / **********ADMIN**********)
    - Donne l’autorisation ou la restriction aux actions de l’utilisateur (acces a des fichiers / repertoires, limite temps CPU, quota de memoire, ressources)
- Gestion de la memoire secondaire
    - Demande rd / wr dans les fichiers → OS → adresses sur la memoire + mecanisme de controle d’acces
- Gestion de l’interface utilisateur
    - Systemes en traitement par lots - non interactif, on donne une sequence d’instructions que la machine execute
    - Interface en ligne de commande - textuelle avec invite pour les commandes (terminal) + interpreteur de commande (OS)
    - Interface graphique utilisateur (GUI) - uniformiser l’affichage des fenetres
        - Bibliotheque de fonctions appelee par les programmes utilisateurs

## Chapitre 9: Gestion de la memoire primaire

L’OS, si dans un environnement multitache, doit pouvoir executer plusieurs programmes stockes en memoire primaire simultanement.

Il nous faut egalement un mecanisme de protection des donnes entre les differentes pages.

**Adresses virtuelles ≠ Adresses reelles**

Les adresses virtuelles sont relatives au debut du programme et sont connues lors de l’execution de celui-ci → adresse en memoire inconnue

Les adresses reelles sont relatives au debut de la memoire (correspondent plus precisement au numero de la case memoire)

Probleme d’adressage et de relocation:

- Lors du chargement du programme, il faut ajouter a toutes les adresses virtuelles l’adresse reelle du debut du programme en memoire + la table de relocation (l’ensemble des positions du programme ou se trouve une adresse a modifier)

Ceci est la relocation - l’operation qui consiste a ajuster toutes les adresses virtuelles d’un programme en fonction de sa position en memoire, pour transformer celles-ci en adresses reelles.

Probleme de fragmentation:

- Relocation pas efficace
- Espace libre et fragmentation difficile a exploiter
- Les adresses virtuelles ne correspondent pas aux adresses reelles - les programmes etant de tailles differentes, ne pourront pas etre charges d’un seul bloc car cela risque d’entrainer la fragmentation qui rend la memoire libre inutilisable

![Ici, un programme S de taille 3 ne pourrait pas etre introduit car il y aurait un probleme de fragmentation](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Screenshot_from_2023-01-17_09-57-40.png)

Ici, un programme S de taille 3 ne pourrait pas etre introduit car il y aurait un probleme de fragmentation

## Pagination

Pages

Programmes a charger en memoire decoupes en portions de taille $l$

Page frames

Memoire primaire decoupee en portions de taille $l$

MMU

Circuit qui traduit les adresses virtuelles en adresses reelles

Puisque taille page = taille page frame

- N’importe quel programme peut etre charge dans n’importe quel page frame, pas forcemment de maniere contigue ni dans l’ordre original du programme

![Exemple etudie pour les prochaines parties](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%201.png)

Exemple etudie pour les prochaines parties

Les page frames sont de longeur unique et fixee $l$, numerotes a partir de 0. Le page frame $i$ est constitue de $l$ cases de memoire primaire d’adresses allant de $i \times l$ → $(i + 1) \times l - 1$

La taille memoire n’est pas forcement un multiple de $l$, donc les dernieres cases ne fassent partie d’aucun page frame et soient inutilisables.

![Meme exemple, mais avec les page frames](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%202.png)

Meme exemple, mais avec les page frames

Les pages sont aussi decoupees en taille $l$.

Si la taille d’un programme n’est pas un multiple de $l$, alors on rajoute un octet vide a la derniere case de la page pour la completer.

Les pages sont egalement numerotes a partir de 0 et la page $i$ est constituee de la plage d’adresses virtuelles allant de $i \times l$ → $(i + 1) \times l - 1$.

![Les pages des programmes P et Q avec leurs tables des pages](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%203.png)

Les pages des programmes P et Q avec leurs tables des pages

On peut donc maintenant charger une page dans un page frame libre, c’est-a-dire coincider le debut de la page avec le debut du page frame.

- On est plus obliges de respecter un ordre car chaque page frame libre peut etre directement exploite
    - Le probleme de fragmentation est regle (sauf pour les dernieres cases vides, mais cela est negligeable par rapport au gain)
- Cependant, le probleme du calcul des adresses est encore + complique car les programmes ne sont plus charges d’un bloc ni dans l’ordre d’origine
    - Il faut donc trouver une solution pour faire la traduction de maniere efficace

![Apres l’execution de Q, le programme R est charge en memoire](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%204.png)

Apres l’execution de Q, le programme R est charge en memoire

Le MMU doit donc etre implemente efficacement et faire une traduction d’adresse.

- Numero de page: $av \div l$ (division entiere)
- Decalage: $av \mod{l}$ (cb de fois l rentre dans av)
- Numero de page frame: trouver dans la table des pages
- Adresse reelle: $pf \times l + ∆$

****Adresse Virtuelle:****

| n - 1 → k | k - 1 → 0 |
| --- | --- |
| numero page p | decalage ∆ |

****************Adresse Reelle:****************

| n - 1 → k | k - 1 → 0 |
| --- | --- |
| numero page frame | decalage ∆ |

La longeur des pages est en binaire - le decalage est dans le poids faible, le numero de page frame et le numero des pages est dans le poids fort.

![Pagination du programme P avec l = 2**2](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%205.png)

Pagination du programme P avec l = 2**2

## Pagination a la demande

La pagination a la demande nous offre des ameliorations importantes:

- On charge en memoire primaire que la page necessaire a un moment donne (au lieu de charger l’ensemble des pages / tous les programmes)
- Les pages qui ne sont pas charges en memoire primaire vont dans la memoire secondaire
    - Donc le temps de chargement + rapide
    - On peut executer un ensemble de programmes plus grand que la memoire physique

Le defaut de page se resume en 2 parties:

- L’ajout d’une colonne bit de presence dans TDP que le MMU va consulter apres le calcul
    - Si n = 1: la page est en memoire primaire, on connait donc le page frame
    - Si n = 0: la page n’est pas en memoire primaire, et le MMU declenche une interruption ***Page Fault***
- L’OS s’occupe de charger la page manquante durant l’interruption ( le stockage des pages en memoire secondaire depend de l’OS)

On introduit egalement l’echange et le choix de victime:

- OS determine la page manquante (aide par la sauvegarde de `PC` lors de l’interruption)
- OS determine si la page existe dans le programme et ou elle se trouve en memoire secondaire
- OS charge la page en memoire primaire et met a jour la TDP
    - S’il y a un page frame libre - page chargee + bit de presence = 1 (notion de ***Swap In***)
    - S’il y a aucun page frame libre - choix d’une page victime (apres avoir sauvegarde cette page entierement en memoire secondaire) qu’on enleve de la memoire primaire + bit de presence = 0 + charger nouvelle page (notion de ***************************Swap Out***************************)

![Pages des programmes P et Q chargees en memoire avec leurs tables des pages](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%206.png)

Pages des programmes P et Q chargees en memoire avec leurs tables des pages

![R1 chargee en memoire primaire](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%207.png)

R1 chargee en memoire primaire

![R0 chargee a la place de P0 (P0 etant donc la victime)](INFO%20F-102%20Fonctionnement%20des%20Ordinateurs%20680037d901f94fdd8a4175a685148fcf/Untitled%208.png)

R0 chargee a la place de P0 (P0 etant donc la victime)

Le choix de la victime depend de l’OS: conserve en memoire secondaire les pages dont l’usage dans un futur proche est le plus probable.

Si les pages sont de plus en plus petites, la TDP est de plus en plus grande (si les pages sont plus grandes, la fragmentation interne augmente). Il n’y aura egalement plus assez de place dans le MMU, mais cela pourrait etre resolu via plusieurs niveaux de page et / ou avec la mise en memoire primaire des pages qui ne peuvent pas etre Swap Out.

Les Swap In et Swap Out sont des mecanismes tres couteux en temps, qui peuvent prendre 1 instruction machine entiere et donc surcharger le systeme avec trop de processus et trop peu de memoire primaire libre. Ce phenomene s’appelle le thrashing.

Tous les processeurs modernes ont un MMU qui est necessaire pour la pagination. Cependant, les processeurs sans MMU s’appellent donc des micro-controleurs (pas de OS necessaire, par exemple l’electro-menager, systemes de controle de vehicules).

## Chapitre 10: Gestion des processus et de la memoire secondaire

Comment on execute plusieurs processus en meme temps / parallele ?

Qu’est-ce qu’un processus? Un processus est un programme en cours d’execution avec ses propres donnees. Ce programme est en general ecrit en langage machine.

Il peut y avoir 2 copies d’un programme qui s’execute = 2 processus differents.

La difference majeure est *********le contexte********* (donnees manipulees, info peripheriques, avancement), qui possede:

- Les valeurs `PC`
- Les specifications de la zone memoire appartenant aux programmes
- Le statut du processus
- Les contenus des registres de travail (donnees)

L’OS est donc un arbitre entre les processus qui repartit de maniere egale les ressources materielles de l’ordi.

Un processus comporte un cycle de vie:

- Creation - l’OS cree le processus a la demande d’un autre (avec un appel systeme)
    - Processus fils crees par processus pere
- Actif - le processus s’execute sur un des CPU
- En attente - le processus n’a pas fini son execution ou desire disposer du CPU
- Bloque - le processus n’a pas fini son execution mais n’est pas capable de continuer (ex: il attend un peripherique)
- Termine - signale a l’OS via un appel systeme qu’il est termine puis l’OS libere les dernieres ressources utilisees par le processus

Donc pour pouvoir executer plusieurs processus en meme temps, on introduit la notion de **Time Sharing** qui va faire en sorte que l’OS attend, a chaque processus, un quantum de temps pour s’executer sur le CPU (en gros passsage d’actif a attente continu).

Pour cela, on a un module sur l’OS: l’ordonnanceur qui:

- Decide quel est le prochain processus a etre actif (plus precisement avoir acces au CPU) selon des contraintes
    - OS temps reel → choix processus afin qu’aucun rate son echeance
    - OS classique → donne le CPU aux processus a la suite de maniere circulaire

Pour passer d’un processus a un autre on fait un changement de contexte:

- On sauvegarde le contexte de l’ancien processus
- On charge le contexte du nouveau processus

Cela peut prendre du temps, surtout si les pages du processus sont presentes en memoire secondaire et qu’il faut les recharger.

Il y a donc 2 techniques pour le ************************Time Sharing************************:

- Time sharing cooperatif
    - Le processus consulte l’horloge systeme regulierement
        - Rend la main quand le quantum de temps est epuise
    - Declenche un appel systeme, faisant appel a l’ordonnanceur
    - Methode tres bonne si le programme n’a pas de boucles infinies et surtout si on connait les pages → systemes embarques par exemple
- Time sharing preemptif
    - L’horloge systeme est programmee pour declencher une interruption a intervalle reguliere
        - Le gestionnaire d’interruption fait le meme appel a l’ordonnanceur; designant le prochain processus et sauvegardant l’ancien
    - Probleme de thrashing si trop de processus car le changement de contexte devient trop frequent

La memoire secondaire peut prendre des formes differentes, comme un disque dur, cle USB, CD-ROM, etc.

Neanmoins, ces differentes formes sont toutes divises en cases qui se nomment des ***blocs / clusters***. Ces blocs sont de quelques kilooctets et chaque bloc a une adresse unique.

Nous accedons pas a la memoire secondaire via une adresse mais via une structure en repertoires, fichiers… etc.

On a donc:

- Volume: la memoire secondaire est vue comme un ensemble de volumes, appeles aussi partitions = plage d’adresses physiques
- Repertoire / dossier: a l’interieur d’un volume, on peut creer un ou plusieurs qui offre une structure mais pas l’information
- Fichiers: unite elementaire de donnees, qui est, par convention nommee dans le style nom + extension pour avoir des infos sur le fichier

Pour acceder aux fichiers, qui sont des espaces de stockage qui peuvent s’etendre et sont contigus, on accede d’abord dans l’adresse virtuelle du fichier qui est traduite par l’OS vers une adresse reelle (numero de bloc) pour realiser les operations demandees.

Les fichiers n’ont pas obligatoirement une existence physique sur un des peripheriques, ce sont donc des fichiers virtuels auxquels l’OS associe des noms puis des sources d’information (par exemple: les alias et points d’entree)

**Alias:** nom de fichier qui substitue un autre fichier pour eviter la duplication

**Point d’entree:** “fichier” qui contient de l’information venant de l’OS
