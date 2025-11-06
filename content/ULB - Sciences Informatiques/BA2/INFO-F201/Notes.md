---
title: Notes
authors: Alessandro Dorigo
tags:
  -
---

# 1: Introduction
## 1.1 Les systèmes d'exploitation
Les ordinateurs sont constitués de plusieurs composants clés:

- **RAM (Random Access Memory)**: Elle stocke temporairement les données et les instructions en cours de traitement. La RAM est divisée en cadres (page frames), chacun contenant une plage d'adresses physiques contiguës. Ces adresses sont utilisées par le CPU pour accéder aux données et aux instructions. Typiquement, chaque cadre a une taille de 4096 octets, avec chaque adresse correspondant à un octet.
- **CPU (Central Processing Unit)**: C'est le cerveau de l'ordinateur, où les opérations principales sont traitées. Il exécute les instructions des programmes et gère les opérations logiques et mathématiques. Les ordinateurs peuvent être mono-processeurs ou multi-processeurs, affectant leur capacité à exécuter un ou plusieurs programmes simultanément. La performance du CPU est souvent mesurée en IPS (Instructions Per Second).
- **Le Bus**: Il s'agit du système qui relie les différents composants de l'ordinateur, comme le CPU, la RAM, et les périphériques d'entrée/sortie (E/S) tels que le clavier, la souris et le disque dur.

En termes de logiciels, on distingue généralement les programmes système (comme le système d'exploitation et les compilateurs) et les programmes d'application, qui sont créés par les utilisateurs.

Le **système d'exploitation (OS)** joue un rôle crucial dans la gestion des ressources informatiques. Il:

1. Coordonne l'accès au matériel,
2. Gère les processus et les fichiers et,
3. S'occupe du chargement et de l'exécution des programmes.
4. En outre, il assure la protection et la détection des erreurs.

Le système d'exploitation fournit une interface abstraite, souvent appelée machine virtuelle, et propose des appels système permettant d'accéder à des fonctionnalités du système qui ne sont pas directement visibles pour l'utilisateur.
## 1.2 Evolution des systèmes d'exploitation
#### 1.2.1 Traitement par lots (Batch Processing)
Dans ce mécanisme, les tâches sont traitées les unes après les autres. Chaque tâche est complètement traitée avant de passer à la suivante.

Un inconvénient majeur de ce système est que le processeur reste inactif pendant que les périphériques d'entrée/sortie sont utilisés, ce qui entraîne une utilisation inefficace des ressources.
#### 1.2.2 Multiprogrammation et Spooling
Pour surmonter les limitations du traitement par lots, la multiprogrammation a été introduite, souvent en conjonction avec le **Spooling (Simultaneous Peripheral Operations On-line)**.

Dans ce système, les tâches sont stockées soit sur le disque, soit en mémoire. La mémoire est divisée en plusieurs partitions, chacune contenant une tâche différente, et le système d'exploitation occupe également sa propre partition.

Le processeur passe d'une tâche à l'autre, ce qui permet une utilisation plus efficace des ressources et réduit le temps d'inactivité du processeur.
#### 1.2.3 Multiprogrammation et partage de temps (Time-Sharing)
Cette phase marque l'introduction du partage de temps, permettant à plusieurs utilisateurs de travailler sur leurs tâches en parallèle.

Le processeur partage son temps entre les différentes tâches, en leur allouant un temps prédéterminé avant de passer à la tâche suivante (une tache non finie pouvant être interrompue après ce lapse de temps). Cela améliore l'efficacité et permet aux utilisateurs d'interagir presque simultanément avec leurs programmes.
## 1.3 Interactions utilisateur / système
Les interactions entre l'utilisateur et le système d'exploitation se font principalement à travers des appels système comme `read`, `write`, et `open`. Ces appels, intégrés dans le système d'exploitation et accessibles via des bibliothèques, permettent aux programmeurs d'exécuter des opérations complexes de manière standardisée.

Ils masquent la complexité des opérations de bas niveau et fournissent une interface uniforme pour interagir avec le système.

Le terminal, ou ligne de commande, est l'interface utilisateur principale pour ces interactions, permettant l'exécution de commandes et l'accès aux fonctionnalités du système.
## 1.4 Appels système
Les appels système sont des mécanismes par lesquels un programme demande un service au système d'exploitation. Lorsqu'un appel système est effectué, il génère une interruption logicielle qui transfère le contrôle du mode utilisateur au mode superviseur.

- **Mode Superviseur**: C'est un mode privilégié utilisé par le système d'exploitation pour accéder à l'ensemble du matériel et contrôler les opérations du système. Il permet d'effectuer toutes les opérations nécessaires pour gérer les ressources informatiques.
- **Mode Utilisateur**: Dans ce mode, les programmes ont un accès limité aux ressources et doivent demander des services au système d'exploitation (par des appels système) pour des opérations spécifiques.
#### 1.4.1 Les Processus
- Un processus est une instance d'un programme en cours d'exécution. Chaque processus a son propre espace d'adressage et peut créer des processus fils.
- Les **threads**, ou processus légers, sont des unités d'exécution au sein d'un même processus qui partagent l'espace d'adressage de ce processus principal. Ils permettent l'exécution de multiples tâches en parallèle au sein d'un même processus.
#### 1.4.2 Les Fichiers
- Un fichier est une collection de données stockées. Il peut s'agir de documents, d'images, de programmes, de répertoires, ou même de périphériques représentés sous forme de fichiers.
- Les chemins d'accès aux fichiers peuvent être **absolus**, commençant par la racine du système de fichiers (par exemple, `/home/user/document.txt`), ou **relatifs**, basés sur le répertoire courant (par exemple, `./document.txt` pour un fichier dans le répertoire actuel).
## 1.5 Structure d'un système d'exploitation
#### 1.5.1 Structure en couches
Les systèmes d'exploitation structurés en couches sont organisés hiérarchiquement, où chaque couche repose sur la couche inférieure et fournit des services à la couche supérieure:

- **Niveau 0: Noyau / Kernel** - Gère les interactions de bas niveau avec le matériel.
- **Niveau 1: Mémoire** - Gère l'allocation de la mémoire et son accès.
- **Niveau 2: E/S** - Gère les opérations d'entrée et de sortie.
- **Niveau 3: Fichiers** - Supervise la création, l'organisation et l'accès aux fichiers.
- **Niveau 4: Allocation de Ressources** - Gère l'allocation des ressources systèmes aux différents processus.
#### 1.5.2 Structure monolithique
Dans un OS monolithique, toutes les fonctions du système sont étroitement interconnectées et s'exécutent dans un espace d'adressage unique:

- **Procédure Principale**: Appelle les procédures de service nécessaires.
- **Procédures de Service**: Exécutent les appels système et autres opérations.
- **Procédures Utilitaires**: Assistants des procédures de service.
#### 1.5.3 Micro-Kernel
Le micro-kernel est une approche minimaliste où le noyau contient uniquement les fonctions essentielles au fonctionnement du système, comme la communication entre les processus et la gestion de base de la mémoire. Les autres services du système d'exploitation sont exécutés en tant que processus séparés, souvent en mode utilisateur.
#### 1.5.4 Modèle Client/Serveur
Dans ce modèle, l'OS est divisé en un noyau minimal et plusieurs serveurs. Le noyau gère les communications de base, tandis que les serveurs exécutent des fonctions spécifiques du système d'exploitation. Les clients, généralement des applications, demandent des services aux serveurs.
#### 1.5.5 Machines Virtuelles
Les machines virtuelles sont des émulations de systèmes informatiques qui peuvent exécuter des programmes comme s'ils étaient sur une machine physique. Exemples:

- **IBM VM**: Une des premières implémentations de machine virtuelle.
- **Java VM**: Exécute des programmes Java dans un environnement contrôlé.
- **VirtualBox, VMWare**: Logiciels permettant de créer et de gérer des machines virtuelles sur des ordinateurs hôtes.
- **Nachos**: Un système éducatif pour comprendre les principes des systèmes d'exploitation.
# 2: Processus et threads

## 2.1 Processus
Chaque logiciel sur un OS est constitué de processus. Un processus est représenté par un PCB (Process Control Block), qui est un élément crucial de la gestion des processus.
#### 2.1.1 PCB (Process Control Block)
Le PCB, géré par l'OS, contient des informations détaillées sur chaque processus, notamment:
- Le `PID` (Process IDentifier)
- État du processus (élu, prêt, bloqué)
- Sa priorité
- Ses compteurs de programme
- Son espace d'adressage / allocations mémoire
- Ses fichiers ouverts
- L’état des registres du processeur lors de sa dernière suspension
- Les signaux en attente / masque des signaux et gestionnaire des signaux
- Autres infos (processus père / fils, groupe, variables d'environnement, statistiques, limites d'utilisation des ressources)

La sauvegarde de l'état des registres est essentielle pour la reprise d'un processus après une interruption.
#### 2.1.2 États d'un processus
Un processus peut être dans l'un des cinq états suivants:
- **Nouveau**: Processus en création.
- **Prêt**: En attente d'exécution. Un processus est initialement dans cet état, puis passe à l'état élu lorsqu'il commence à s'exécuter. Il peut revenir à cet état si un autre processus utilise le processeur.
- **Élu**: Actuellement en cours d'exécution. Un processus peut passer de cet état à bloqué s'il ne peut être exécuté ou attend une opération d'E/S.
- **Bloqué**: En attente d'une opération d'E/S ou autre événement.
- **Fini**: Processus terminé.
#### 2.1.3 Mode noyau et mode utilisateur d'un processus
L'OS a un nombre limité d'appels système. Ces appels système se trouvent dans la table des processus - à travers les adresses des appels système. Un appel système peut être bloquant (peut faire passer un processus à l'état bloqué) ou non-bloquant (le cas contraire).

Le processus bascule entre le mode utilisateur et noyau - il est en mode utilisateur tant qu'il ne fait pas d'appels système.
#### 2.1.4 Espace d'adressage d'un processus
L'espace d'adressage virtuel comprend plusieurs segments, tels que le texte (code), les données, la pile et, parfois, des segments partagés ou de heap.
#### 2.1.5 API `Posix` pour les processus
Les processus sont organisés en arbre, avec `init` comme racine. Les processus parents peuvent gérer, mais pas renier, leurs processus fils. En cas de perte du processus père, le fils est adopté par `init`. Les processus partagent le même espace mémoire.
##### 2.1.5.1 Appels système `fork()`
```C
pid_t fork(void);
```
- **Description**: Crée un processus fils qui est une copie du processus parent.
- **Attributs/Valeurs**: Aucun attribut requis.
- **Retourne**:
	- `0` dans le processus fils.
	- Le PID (Process ID) du processus fils dans le processus parent.
	- `-1` en cas d'échec, avec une erreur définie dans `errno`.

Si le processus fils est terminé, il passe en mode zombie jusqu'à quand le processus père récupère son état de terminaison.
##### 2.1.5.2 Appels système `_exit()`
```C
void _exit(int status);
```
- **Description**: Termine immédiatement le processus appelant.
- **Attributs/Valeurs**:
	- `status`: Code de statut de terminaison du processus.
- **Retourne**: Ne retourne pas.
##### 2.1.5.3 Appels système `exec()`
Un processus peut remplacer son programme en cours (exécuté) par un autre grâce aux appels système `exec`. L'espace d'adressage du programme en cours sera remplacé par celui du nouvel exécutable.
```C
int execl(const char *path, const char *arg, ...);
```
- **Description**: Remplace le programme actuel par un nouveau programme.
- **Attributs/Valeurs**:
	- `path`: Chemin de l'exécutable.
	- `arg`: Arguments du programme, terminé par NULL.
- **Retourne**:
	- `-1` en cas d'échec, avec une erreur définie dans `errno`.
```C
int execv(const char *path, char *const argv[]);
```
- **Description**: Identique à `execl`, mais les arguments sont passés sous forme de tableau.
- **Attributs/Valeurs**:
	- `argv[]`: Tableau d'arguments, terminé par NULL.
- **Retourne**:
	- `-1` en cas d'échec.
```C
int execlp(const char *file, const char *arg, ...);
```
- **Description**: Identique à `execl`, mais recherche l'exécutable dans le `PATH`.
- **Attributs/Valeurs**:
	- `file`: Nom du fichier exécutable.
- **Retourne**:
	- `-1` en cas d'échec.
```C
int execvp(const char *file, char *const argv[]);
```
- **Description**: Combinaison de `execv` et `execlp`.
- **Attributs/Valeurs**:
	- `argv[]`: Tableau d'arguments, terminé par NULL.
- **Retourne**:
	- `-1` en cas d'échec.
```C
int execle(const char *path, const char *arg, ..., char * const envp[]);
```
- **Description**: Identique à `execl`, mais permet de spécifier l'environnement.
- **Attributs/Valeurs**:
	- `envp[]`: Tableau de variables d'environnement.
- **Retourne**:
	- `-1` en cas d'échec.
##### 2.1.5.4 Appels système `wait()` et `waitpid()`
```C
pid_t wait(int *status);
```
- **Description**: Attend la fin d'un processus fils.
- **Attributs/Valeurs**:
	- `status`: Stocke le statut de terminaison du processus fils.
- **Retourne**:
	- `PID` du fils terminé.
```C
pid_t waitpid(pid_t pid, int *status, int options);
```
- **Description**: Attend la fin d'un processus fils spécifique.
- **Attributs/Valeurs**:
	- `pid`: PID du processus fils à attendre.
	- `options`: Options pour le comportement de `waitpid`.
- **Retourne**:
	- `PID` du fils terminé
	- `-1` en cas d'échec.
---
- Si le fils est stoppé, les 8 bits de poids fort de `status` contiennent le numéro du signal qui a arrêté celui-ci, et les 8 autres ont la valeur `0177`.
- Si le fils s'est arrêté volontairement, les 8 bits de poids faible sont nuls et les 8 autres contiennent la valeur de l'argument `exit()`.
- Si le fils a eu une erreur, ou le processus n'a pas de père ou est en état zombie, cette valeur va être `-1`.
- Si le fils est terminé par un signal, les 8 bits de poids fort sont nuls et les 7 autres (1 vide ?) contiennent le numéro du signal qui a causé la fin du fils.
---
Pour interpréter la valeur de `status` retournée par `wait()` ou `waitpid()`, on utilise les macros suivantes:

1. **`WIFEXITED(status)`** : Cette macro vérifie si le processus fils s'est terminé normalement. Si elle renvoie vrai, cela signifie que le fils a appelé `exit()` ou a terminé son exécution.
   - **`WEXITSTATUS(status)`** : Si `WIFEXITED(status)` est vrai, cette macro renvoie la valeur de sortie que le processus fils a passée à `exit()`.

2. **`WIFSIGNALED(status)`** : Cette macro vérifie si le processus fils a été terminé par un signal. Si elle renvoie vrai, cela signifie que le fils a été terminé par un signal non intercepté.
   - **`WTERMSIG(status)`** : Si `WIFSIGNALED(status)` est vrai, cette macro renvoie le numéro du signal qui a terminé le processus fils.

3. **`WIFSTOPPED(status)`** : (Applicable seulement si `waitpid()` est appelé avec des options pour détecter les processus stoppés) Cette macro vérifie si le processus fils est actuellement stoppé. Si elle renvoie vrai, cela signifie que le fils est suspendu.
   - **`WSTOPSIG(status)`** : Si `WIFSTOPPED(status)` est vrai, cette macro renvoie le numéro du signal qui a stoppé le processus fils.

4. **`WIFCONTINUED(status)`** : (Applicable seulement si `waitpid()` est appelé avec des options pour détecter les processus qui ont repris après avoir été stoppés) Cette macro vérifie si le processus fils a repris son exécution après avoir été stoppé.
## 2.2 Threads
Un thread permet de diviser / partager l'exécution d'un processus en plusieurs parties, qui peuvent être exécutées en concurrence. Le processus principal est vu comme un ensemble de ressources que les threads partagent. Chaque thread possède sa propre pile d'exécution, son propre état, sa propre priorité, etc.

Un processus multithread présente plusieurs avantages:
- **Réactivité:** Des threads du processus peuvent s’exécuter meme si d'autres sont bloqués.
- **Partage de ressources:** Tous les threads du processus partagent le meme espace d'adressage, etc.
- **Economie:** Le partage fait épargner de l'espace mémoire et du temps.
#### 2.2.1 Threads utilisateur / noyau
Les threads peuvent être gérés ou ordonnancés par le noyau ou par une librairie de niveau utilisateur. Un processus peut donc être composé de plusieurs threads noyau ou utilisateur.

Le désavantage d'avoir les 2 est le fait que le blocage d'un thread utilisateur entraîne le blocage de tous les threads noyau, qui donc vont bloquer le reste des threads utilisateur liés au thread noyau.

Lorsqu'un processus est créé, un thread noyau est associé au thread principal de celui-ci. L'exécution de `pth_init()` transforme aussi le thread principal en thread utilisateur, puisque les threads utilisateur sont des threads `pth`.
#### 2.2.2 `pthread` et `pth`
```C
int pthread_create(pthread_t *thread, const pthread_attr_t *attr, void *(*start_routine)(void *), void *arg);
```
- **Description**: Crée un nouveau thread.
- **Attributs/Valeurs**:
	- `thread`: Pointeur vers l'identifiant du nouveau thread.
	- `attr`: Pointeur vers une structure `pthread_attr_t` spécifiant les attributs du thread. Peut être NULL pour les attributs par défaut.
	- `start_routine`: Fonction que le thread exécutera une fois créé.
	- `arg`: Argument unique passé à la fonction `start_routine`.
- **Retourne**:
	- `0` en cas de succès, ou un code d'erreur.
```C
pth_t pth_spawn(pth_attr_t attr, void *(*start_routine)(void *), void *arg);
```
- **Description**: Crée un nouveau thread utilisateur.
- **Attributs/Valeurs**:
	- `attr`: Attributs du thread utilisateur.
	- `start_routine`: Fonction que le thread exécutera.
	- `arg`: Argument passé à la fonction `start_routine`.
- **Retourne**:
	- Un identifiant de thread utilisateur (`pth_t`), ou `NULL` en cas d'échec.
```C
int pthread_join(pthread_t thread, void **retval);
```
- **Description**: Attend la fin d'un thread et récupère sa valeur de retour.
- **Attributs/Valeurs**:
	- `thread`: Identifiant du thread à attendre.
	- `retval`: Pointeur vers l'emplacement où stocker la valeur de sortie du thread.
- **Retourne**:
	- `0` en cas de succès, ou un code d'erreur.
```C
void pthread_exit(void *retval);
```
- **Description**: Termine le thread appelant et renvoie une valeur.
- **Attributs/Valeurs**:
	- `retval`: Valeur de retour que le thread en cours d'exécution va renvoyer.
- **Retourne**: Ne retourne pas.
```C
int pthread_cancel(pthread_t thread);
```
- **Description**: Envoie une demande d'annulation à un thread.
- **Attributs/Valeurs**:
	- `thread`: Identifiant du thread à annuler.
- **Retourne**:
	- `0` en cas de succès, ou un code d'erreur.
```C
int pthread_detach(pthread_t thread);
```
- **Description**: Détache un thread, libérant ses ressources à sa terminaison.
- **Attributs/Valeurs**:
	- `thread`: Identifiant du thread à détacher.
- **Retourne**:
	- `0` en cas de succès, ou un code d'erreur.

L'état de terminaison d'un thread est conservé jusqu'à ce qu'un autre thread le récupère via `pthread_join()`.
# 3: Communication interprocessus
Pour communiquer entre plusieurs processus, ils existent plusieurs systèmes mis en place:
## 3.1 Mémoire partagée
Chaque processus a son propre espace d'adressage prive partage avec ses threads, pour partager des donnes / fichier avec d'autres processus, il existe le concept d'espace de données commun.

La mémoire partagée permet d'avoir 2 processus qui utilisent les memes variables, qui peut être très utile dans le contexte des grandes applications, comme un jeu video, serveurs, etc.

Cependant, cette mémoire partagée peut poser un grand problème si elle n'est pas gérée correctement. Si plusieurs processus essayent d’accéder en meme temps a la meme mémoire partagée et essayent également de la modifier, cela va causer un *acces concurrent*, c'est-a-dire que la variable ne va pas changer comme on le souhaite, voir pire.
## 3.2 Signaux
Les signaux sont des valeurs envoyées par l'OS qui permettent de changer l’état d'un processus ou de plusieurs processus. Ceux-ci sont gérés par le signal handler, qui va donc dire ce que doit faire le programme quand un signal est reçu avant de faire quoi que ce soit.

Les signaux sont classifies par leur nom, type et numéro.

Ces signaux peuvent nous notifier si un processus veut arreter un autre (comme `SIGKILL`, `SIGTERM`) a cause d'une erreur, ou le mettre en pause `SIGSTOP` ou le continuer `SIGCONT`, etc.

Des signaux peuvent etre envoyes d'un processus a l'autre avec `kill(pid_t pid, int signum)`. On peut egalement creer un masque de signaux (qu'on va ignorer ou pas) - celui-ci sert a savoir les signaux a ignorer et mettre en attente jusqu'a la fin du processus.
## 3.3 Pipes
Pour transmettre des donnees entre deux processus, on utilise les tubes (pipes). Il y a les pipes normales ou anonymes (unnamed and named pipes). Les unnamed pipes peuvent stocker 5 Ko d'information, et elles sont unidirectionnelles. Elles sont utiles pour lier deux processus entre eux, comme par exemple envoyer l'output d'un vers l'input de l'autre.

Tous les enfants du processus pere qui fait un appel a pipe peuvent utiliser la pipe.

Les named pipes sont beaucoup plus performantes, elles peuvent stocker jusqu'a 40 Ko d'information et sont cette fois bidirectionnelles. Elles ne sont egalement pas detruites jusqu'a quand cela est explicitement precise.

Pour communiquer avec l'exterieur, les pipes utilisent `STDIN`, `STDOUT` et `STDERR`.

```C
int pipe(int filedes[2])
```
- **Description**: Crée un pipe anonyme utilisé pour la communication inter-processus.
- **Attributs/Valeurs** :
    - `filedes`: Un tableau de deux descripteurs de fichiers. `filedes[0]` est utilisé pour lire depuis le pipe, tandis que `filedes[1]` est utilisé pour écrire dans le pipe.
- **Retourne**:
    - `0` en cas de succès, `-1` en cas d'échec.
```C
int mkfifo(const char *pathname, mode_t mode)
```
- **Description**: Crée un pipe nommé (FIFO) avec un nom de fichier spécifié, permettant la communication entre processus qui ne sont pas liés par une relation parent-enfant.
- **Attributs/Valeurs**:
    - `pathname`: Chemin vers le fichier FIFO à créer.
    - `mode`: Les permissions pour le fichier FIFO. Utilisé de la même manière que dans `chmod()`.
- **Retourne**:
    - `0` en cas de succès, `-1` en cas d'échec.

Un avantage des pipes nommes est le fait que deux processus qui n'ont aucun lien de parente peuvent donc communiquer entre eux, pour transmettre des infos d'un a l'autre, ou l'inverse.
## 3.4 Sockets
Ils existent aussi les sockets, mais ceux-ci ne sont pas montres dans le livre. Les sockets permettent d'envoyer des infos entre des différentes machines, souvent a travers le Wi-Fi ou Bluetooth, etc.
# 4: Synchronisation des processus et interblocages
## 4.1 Synchronisation des processus
Plusieurs processus peuvent partager des objets ou variables. Si ce partage est fait sans précaution, cela peut induire a des résultats imprévisibles / non attendus.

Il faut donc empêcher les autres processus d’accéder a un objet partagé si cet objet est en cours d'utilisation par un autre - cela s'appelle **l'exclusion mutuelle**. Ces situations sont qualifiées **d'accès concurrents**.
#### 4.1.1 Objets / sections critiques
Les **objets critiques** sont des ressources ou des données partagées entre plusieurs processus, qui ne peuvent pas être accédées de manière sûre par plus d'un processus à la fois sans coordination. L'accès simultané à ces objets critiques peut entraîner des incohérences ou des erreurs.

Les **sections critiques** sont des portions de code où les processus accèdent ou modifient ces objets critiques. L'exécution simultanée de sections critiques par plusieurs processus peut mener à des conflits ou des résultats imprévisibles.

Pour assurer une **exclusion mutuelle** efficace, qui est essentielle pour éviter des problèmes d'accès concurrents aux objets critiques, quatre conditions doivent être respectées:

1. **Exclusion Mutuelle**: Aucun deux processus ne peuvent être simultanément dans leurs sections critiques.
2. **Progression**: Aucune hypothèse ne doit être faite sur la vitesse ou le nombre de processeurs des processus.
3. **Attente Limitée (Bounded Waiting)**: Aucun processus suspendu en dehors de sa section critique ne doit empêcher indéfiniment les autres processus d'accéder à leurs propres sections critiques.
4. **Absence de Famine (No Starvation)**: Chaque processus doit être en mesure d'accéder à sa section critique dans un temps raisonnable, évitant l'attente infinie.
#### 4.1.2 Masquage des interruptions
Le masquage des interruptions est une technique de gestion de la concurrence où un processus désactive les interruptions lorsqu'il entre dans une section critique et les réactive à sa sortie. Cette méthode garantit qu'un processus ne sera pas interrompu / suspendu pendant qu'il opère dans sa section critique, assurant ainsi l'exclusion mutuelle.

Cependant, si le processus ne réactive pas les interruptions avant de quitter la section critique, cela peut entraîner des problèmes graves, comme le gel du système.

Cette approche est limitée dans les environnements multiprocesseurs, car elle ne peut empêcher les autres processeurs d'intervenir et d'exécuter leurs propres interruptions. Ainsi, le masquage des interruptions n'est pas une solution viable pour les systèmes multiprocesseurs en ce qui concerne la gestion des accès concurrents aux sections critiques.
#### 4.1.3 Exclusion mutuelle par attente active
L'exclusion mutuelle par attente active utilise des **instructions atomiques** pour contrôler l'accès aux sections critiques. Une **instruction atomique** est une opération qui s'exécute entièrement sans être interrompue, garantissant qu'aucun autre processus ne peut modifier la ressource concernée pendant son exécution.

L'attente active signifie donc qu'un processus en attente d'accéder à une section critique vérifie continuellement si la condition d'entrée est remplie. Cela peut entraîner une consommation excessive de temps CPU, surtout si la section critique est longue.

De plus, il y a un risque que le processus en attente active ne puisse jamais accéder à la section critique, notamment si les autres processus occupent constamment la section critique, ce qui crée une situation d'attente infinie pour le processus en attente.
#### 4.1.4 Primitives `SLEEP` / `WAKEUP`
Un processus peut être mis en attente avec l'appel système `SLEEP` lorsqu'un autre accède à sa section critique. Une fois la section critique libérée, le processus en attente peut être réveillé avec `WAKEUP`.

Si le signal `WAKEUP` est émis avant que le processus destinataire ne soit effectivement en état de `SLEEP`, le processus risque de rester endormi indéfiniment, car il aura manqué le signal de réveil.

- **`pause()`**: Suspend le processus appelant jusqu'à la réception d'un signal.
- **`kill(pid, SIGCONT)`**: Envoie le signal `SIGCONT` au processus identifié par `pid`, utilisé pour réveiller un processus.

Conditions d'émission des signaux:
1. L'émetteur et le destinataire appartiennent au même parent.
2. L'émetteur est le super-utilisateur.
#### 4.1.5 Semaphores
Un **sémaphore** est un mécanisme de synchronisation utilisé pour contrôler l'accès aux ressources partagées et assurer l'exclusion mutuelle dans les environnements concurrents. Un sémaphore est représenté par une variable, souvent un entier, qui indique le nombre de processus autorisés à accéder simultanément à une section critique.

- **Opération `P(S)` (Wait)**: Lorsqu'un processus exécute `P(S)`, la valeur du sémaphore `S` est décrémentée. Si la valeur devient négative, cela signifie que le nombre de processus dans la section critique a atteint sa limite, et le processus appelant est mis en attente. L'opération `P(S)` doit être atomique pour éviter les conditions de course.
- **Opération `V(S)` (Signal)**: L'opération `V(S)` augmente la valeur du sémaphore `S`. Si `S` est égal à 0 ou négatif, cela indique qu'un ou plusieurs processus attendent l'accès à la section critique. L'augmentation de `S` peut potentiellement débloquer ces processus en attente.

```C
int sem_init(sem_t *sem, int pshared, unsigned int value)
```
- **Description**: Initialise un sémaphore.
- **Attributs/Valeurs**:
	- `sem`: Pointeur vers le sémaphore.
	- `pshared`: Si non nul, le sémaphore est partagé entre plusieurs processus.
	- `value`: Valeur initiale du sémaphore.
- **Retourne**:
	- `0` en cas de succès, `-1` en cas d'échec.
```C
int sem_wait(sem_t *sem)
```
- **Description**: Décrémente le sémaphore. Si le sémaphore vaut zéro, le processus appelant est bloqué.
- **Attributs/Valeurs**:
	- `sem`: Pointeur vers le sémaphore.
- **Retourne**:
	- `0` en cas de succès, `-1` en cas d'échec.
```C
int sem_post(sem_t *sem)
```
- **Description**: Incrémente le sémaphore. Si d'autres processus étaient bloqués sur ce sémaphore, ils peuvent être débloqués.
- **Attributs/Valeurs**:
	- `sem`: Pointeur vers le sémaphore.
- **Retourne**:
	- `0` en cas de succès, `-1` en cas d'échec.
```C
int sem_trywait(sem_t *sem)
```
- **Description**: Tente de décrémenter le sémaphore. Ne bloque pas si le sémaphore vaut zéro.
- **Attributs/Valeurs**:
	- `sem`: Pointeur vers le sémaphore.
- **Retourne**:
	- `0` en cas de succès, `-1` en cas d'échec avec `errno` défini à `EAGAIN` si le sémaphore vaut zéro.
```C
int sem_getvalue(sem_t *sem, int *sval)
```
- **Description**: Obtient la valeur actuelle du sémaphore.
- **Attributs/Valeurs**:
	- `sem`: Pointeur vers le sémaphore.
	- `sval`: Pointeur vers la variable où stocker la valeur du sémaphore.
- **Retourne**:
	- `0` en cas de succès, `-1` en cas d'échec.
```C
int sem_destroy(sem_t *sem)
```
- **Description**: Détruit un sémaphore.
- **Attributs/Valeurs**:
	- `sem`: Pointeur vers le sémaphore.
- **Retourne**:
	- `0` en cas de succès, `-1` en cas d'échec.
#### 4.1.6 `Mutex`
Dans la bibliothèque `pthread`, les **mutex** (ou verrous de mutual exclusion) sont des mécanismes de synchronisation utilisés pour l'exclusion mutuelle. Ils sont conceptuellement similaires aux sémaphores binaires, c'est-à-dire qu'ils ont seulement deux états: verrouillé et déverrouillé. Un mutex est utilisé pour contrôler l'accès à une ressource partagée, garantissant qu'un seul thread à la fois peut accéder à la ressource.

- **Verrouillage (`pthread_mutex_lock(&mutex)`)**: Cette fonction bloque le mutex spécifié. Si le mutex est déjà verrouillé par un autre thread, le thread appelant est mis en attente jusqu'à ce que le mutex soit disponible.
- **Déverrouillage (`pthread_mutex_unlock(&mutex)`)**: Cette fonction déverrouille le mutex. Si d'autres threads sont en attente du mutex, l'un d'entre eux (selon la politique de planification du système) peut alors acquérir le mutex.
## 4.2 Interblocages
Un interblocage (deadlock) est une situation dans un système informatique où deux processus ou plus sont bloqués car chacun attend une ressource détenue par un autre, créant ainsi un verrouillage mutuel. Pour qu'un interblocage se produise, quatre conditions doivent être réunies:

1. **Exclusion Mutuelle**: Au moins une ressource doit être en mode non partageable. Cela signifie que seulement un processus peut utiliser la ressource à un moment donné.
2. **Attente et Maintien**: Les processus détenant des ressources attendent d'autres ressources déjà détenues.
3. **Non-Préemption**: Les ressources ne peuvent pas être forcées à être libérées. Un processus doit libérer ses ressources volontairement.
4. **Attente Circulaire**: Il existe un ensemble de processus où chaque processus attend une ressource détenue par le prochain processus dans la séquence.
#### 4.2.1 Graphe d'allocation des ressources
Le **graphe d'allocation** est un outil utilisé dans la détection des interblocages. Il représente les processus, les ressources, et leurs relations. Les nœuds représentent les processus et les ressources, et les arcs représentent les demandes et les attributions de ressources. Un cycle dans ce graphe indique un interblocage potentiel.
#### 4.2.2 Detection / traitement / évitement / prevention des interblocages
Pour gérer et prévenir les interblocages, les systèmes peuvent utiliser plusieurs stratégies:

1. **Prévention**: Éliminer une des quatre conditions nécessaires pour qu'un interblocage se produise (mutual exclusion, hold and wait, no preemption, circular wait).
2. **Détection et récupération**: Le système détecte les interblocages et prend des mesures pour les résoudre, souvent en terminant ou en reprenant l'un des processus bloqués.
3. **Évitement**: Utiliser des algorithmes comme le banquier de Dijkstra pour allouer les ressources de manière à éviter les situations d'interblocage.

Des que le système détecte un interblocage, il doit généralement le supprimer, c'est-a-dire qu'il doit effectuer l'une des operations suivantes:

- **Retrait Temporaire de Ressources**: Retirer une ressource d'un processus pour la réattribuer à un autre.
- **Restauration de l’État Pré-Interblocage**: Revenir à un état système antérieur à l'interblocage pour le résoudre.
- **Termination de Processus**: En dernier recours, terminer un ou plusieurs processus impliqués dans l'interblocage pour libérer les ressources.

# 5: Ordonnancement des processus
La partie qui se charge de gérer l'allocation des processeurs aux processus / threads se nomme l'ordonnanceur. L'ordonnancement doit se faire selon une politique (pour répondre a des objectifs de performance).
## 5.1: Types d'ordonnanceurs
Ils existent 3 types d'ordonnanceurs:
1. **Long terme**: Gere l'admission des processus (passage a l’état prêt) selon la capacité du système (degré de multiprogrammation) et niveau de performance requis.
2. **Moyen terme**: Gere la selection des processus a retirer ou charger en mémoire.
3. **Court terme**: Gere la file des processus prêts et decide (en fonction d'une politique) de l'ordre d'execution de ceux-ci. Il effectue aussi le changement de contexte ainsi qu'implanter un ordonnancement preemptif, non preemptif ou cooperatif. Il est active par un événement: interruption du temporisateur, interruption d'un périphérique, appel système ou signal.
## 5.2: Objectifs de l'ordonnanceur (système multi-user)
Pour le système, l'ordonnanceur a ces objects:
- Maximiser le taux d'utilisation des processeurs / autres ressources du système
- Eviter le problème de famine
- Maximiser la capacité de traitement des systèmes de traitements par lots (nombre de processus executes par unite de temps)
- Minimiser le nombre et la durée des changements de contexte dans les systèmes en temps partage.
- Respecter les échéances (par rapport au temps) dans les systèmes en temps reel.

Pour l'utilisateur:
- Minimiser le temps de séjour des processus
- Minimiser le temps de réponse des processus
- Minimiser le temps d'attente d'execution
## 5.3 Ordonnanceurs non preemptifs
Dans un ordonnanceur non preemptif, il y a 2 politiques qui peuvent etre appliquees pour choisir le prochain processus a executer:
- **FCFS (First-Come First-Served)**: le prochain processus a traiter est celui qui est recu en premier d'apres la date d'arrivee.
- **SJF (Shortest Job First)**: le prochain processus a traiter depend du temps d'execution du processus (intervalle de temps entre la soumission et achevement), ou si plusieurs processus sont dans la file d'attente (d'apres les dates d'arrivee), celui avec le temps le plus court est choisi.

La formule pour calculer le temps moyen de sejour peut etre ecrite comme $\frac{4a + 3b + 2c + d}{4}$ - car le premier processus se termine apres le temps $a$, le deuxieme apres $a+b$, puis $a+b+c$ et $a+b+c+d$.

L'ordonnancement **SJF** est optimal que si les travaux sont recus simultanement.

- Le **temps de sejour** est obtenu en soustrayant la date d'arrivee du processus de la date de terminaison.
- Pour le **temps d'attente**, on soustraie le temps d'execution du temps de sejour.
---
*Exemple:*

| Processus     | Temps d'execution     | Date d'arrivee     |
|:----:|:----:|:----:|
| A     | 3     | 0     |
| B     | 6     | 1     |
| C     | 4     | 4     |
| D     | 2     | 6     |
| E     | 1     | 7     |
1. En **FCFS**:

| A | A | A | B | B | B | B | B | B | C | C | C | C | D | D | E |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  |  |  | 5 |  |  |  |  | 10 |  |  |  |  | 15 |  |
2. En **SJF**:

| A | A | A | B | B | B | B | B | B | E | D | D | C | C | C | C |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 |  |  |  | 5 |  |  |  |  | 10 |  |  |  |  | 15 |  |

---
Pour appliquer cette technique aux processus interactifs, il suffit de diviser le temps d'execution des commandes a chaque nouvelle commande emise par le processus interactif (/2, puis /4 puis /8 et que pour les commandes avant la nouvelle commande), mais un ordonnanceur non preemptif n'est pas interessant pour un systeme multi-user a cause des temps de reponse qui peuvent devenir longs et un processus peut monopoliser un processeur a cause d'une boucle infinie de calcul par exemple.
## 5.4 Ordonnanceurs preemptifs
Un ordonnanceur preemptif s'assure qu'aucun processus ne s'execute pendant trop longtemps en utilisant l'horloge electronique interne qui genere periodiquement une interruption, ou l'OS reprend la main et decide si le processus en cours doit continuer son execution ou etre suspendu pour laisser place a un autre.

Si le processus est suspendu, le systeme doit d'abord sauvegarder l'etat des registres avant de charger les donnees du processus a lancer dans les nouveaux registres. Cela se nomme le **changement de contexte**. Le systeme peut egalement suspendre un processus si un autre plus prioritaire arrive / devient pret.

Le processeur passe donc d'un processus a un autre en executant chaque processus pendant un **quantum** de temps (qui peut etre entre quelque dizaines ou centaines de millisecondes). La commutation doit etre donc plus courte que le **quantum**.

Cela a quelques problemes:
- Choix de la valeur du quantum
- Choix du prochain processus dans chaque situation:
	1. Le processus se bloque
	2. Le processus passe a l'etat pret
	3. Un processus passe a l'etat pret
	4. Le processus se termine ou cede le processeur
#### 5.4.1 Ordonnancement du plus petit temps d'execution
Le **SRT (Shortest Remaining Time)** est une version preemptive du **SJF**, ou l'ordonnanceur compare le temps d'execution estime du nouveau processus avec celui en execution. Si le temps du nouveau est plus court, il rentre en execution.
#### 5.4.2 Ordonnancement circulaire
Le **Round Robin** est un algorithme d'ordonnancement ou les processus a executer sont dans une liste **FIFO** et sont executes dans cet ordre. Un processus est a nouveau traite pendant un **quantum** de temps, mais s'il devient bloque ou se termine avant son **quantum** de temps, le processus est suspendu, mis en fin de liste et le prochain dans la liste est elu pour etre traite. Si le processus est toujours en traitement apres le **quantum** de temps, il est quand meme suspendu pour laisser place au prochain et passe egalement en fin de liste.

Pour resoudre le probleme du quantum de temps, on choisit une valeur qui n'est trop petite pour ne pas avoir trop de changements de contexte (et abaisser l'efficacite du processeur) ni trop grande car cela va augmenter le temps de reponse des courtes commandes (en mode interactif). En general, un quantum entre 20 et 50 ms est un bon compromis.
#### 5.4.3 Ordonnancement a base de priorites
Ce nouvel algorithme permet d'attribuer une priorite a chaque processus (si besoin critique ou autre) pour savoir lequel elire en 1er. Les processus de meme priorite seront dans une file FIFO, ou le nombre de files correspond au nombre de niveaux de priorite.

La priorite d'un processus en cours d'execution est diminuee regulierement par l'ordonnanceur. Cette priorite est comparee regulierement a celle du processus pret le plus prioritaire (en tete de file).
#### 5.4.4 Files multiples (quantum variable)
Pour reduire le nombre de commutations des processus qui consomment du temps CPU, il faut allouer un plus grand quantum. Quand un processus passe a l'etat elu pour la premiere fois, le processus lui est alloue pendant un quantum. Pour la 2nde fois, 2 quanta. Pour la $n^{ieme}$ fois, 2$^{(n-1)}$ quanta. Lorsqu'un processus est suspendu pour la nieme fois, sa priorite est recalculee ($2^n$) avant d'etre insere dans la file appropriee.

La priorite depend donc du nombre de quanta alloues lors de la prochaine activation du processus. Les processus dont le nombre de quanta est le plus petit seront les plus prioritaires.

Un processus qui consomme beaucoup de CPU va donc etre de moins en moins prioritaire et les processus interactifs vont etre les plus prioritaires.
## 5.5 Ordonnancement a deux niveaux
L'ordonnancement a deux niveaux deplace les processus elus entre la memoire et le disque (haut niveau) et choisit ceux a executer depuis la memoire (bas niveau). L'ordonnanceur de haut niveau va periodiquement retirer les processus qui restent assez longtemps (dans la memoire) de la memoire et les remplace par ceux qui sont restes trop longtemps sur le disque.
## 5.6 Ordonnancement des threads
Round robin et mode kernel tout le temps.

**Premier cas:**
Chaque processus a un thread ordonnanceur qui se charge d'ordonnancer les threads du processus. Ceux-ci sont ordonnances au niveau utilisateur et donc sont des threads utilisateur. L'ordonnanceur va utiliser une parmi les methodes d'ordonnancement mentionees plus tot.

La seule difference est l'absence d'une horloge pour suspendre l'execution d'un thread.

---
**Second cas:**
L'ordonnanceur choisit un thread parmi ceux qui sont prets (peu importe les processus), et les threads sont donc des threads noyau.
## 5.7 Ordonnanceur `Posix`
L'ordonnanceur Posix est un ordonnanceur preemptif a files multiples de threads, il classe les threads en au moins trois categories:
1. **FIFO temps reel** ou `SCHED_FIFO`: Les threads ici sont les plus prioritaires - ceux qui partagent cette priorite sont geres selon FCFS.
2. **Round Robin temps reel** ou `SCHED_RR`: Les threads qui partagent cette priorite sont geres selon Round Robin avec un quantum variable.
3. **Temps partage** ou `SCHED_OTHER`: Les threads ici sont les moins prioritaires (sont executes que si aucun thread des classes 1 et 2 ne sont prets) - ils sont aussi geres selon Round Robin avec un quantum variable.

Si un thread de classe 1 est elu, son execution est suspendue que si l'une des 3 situations arrive:
1. Un thread plus prioritaire de classe 1 est pret.
2. Il se bloque ou se termine.
3. Il cede volontairement le processeur avec `sched_yield()` sans se bloquer. Il est ensuite deplace a la fin de la file de sa classe.

A chaque top d'horloge, le quantum des threads de classes 2 ou 3 est decremente de 1. Si le thread est elu est le quantum est 0, il est suspendu.
# 6: Gestion de la mémoire
Espace d'adressage = Stack/Heap

Regroupe les instructions, les données et les piles d'execution du processus. Il est reference par des adresses relatives.

Memoire principale / physique = RAM

Espace de travail des processeurs. Les processeurs recuperent les instructions et les donnees necessaires a l'execution de processus. Elle est vue comme un tableau de mots de 1 octet chacun, ou chaque mot et reference par une adresse physique.

Memoire secondaire = Disques

--- info

## 6.1 Espace d'adressage d'un processus
Defini par l'ensemble des adresses accessibles au processus durant son execution, avec les adresses etant relatives. Il est structure en segments/regions/zones qui sont representes dans un meme espace contigu.

L'espace d'adressage d'un processus peut etre construit a partir de son executable.

*Un format commun est ELF (Executable and Linkable Format), qui contient de l'information sur les segments, les libraires dynamiques, l'adresse de la premiere instruction, etc.*

On peut creer/attacher/detacher un segment de donnees a l'espace d'adressage d'un processus. On peut egalement mapper des fichiers de donnees dans l'espace d'adressage d'un processus en utilisant `mmap()` - qui permet les acces directs aux donnees du fichier sans utiliser `read` ou `write` dans le fichier.

```C
void* mmap(void* addr, size_t len, int prot, int flags, int fd, off_t offset);
```
- **Description**: Attache/mappe un fichier de donnees a un espace d'adressage.
- **Attributs/Valeurs**:
	- `addr`: l'adresse virtuelle au debut du mappage - si `NULL`, le systeme choisit l'adresse qui est ensuite retournee dans `addr`.
	- `len`: nombre maximal d'octets du fichier a mapper.
	- `prot`: mode d'acces (`PROT_READ`, `PROT_WRITE`, `PROT_EXEC`) - doit etre compatible avec le mode d'ouverture du fichier.
	- `flags`: specifie si les modifications de la zone mappee sont visible ou non aux autres
		- `MAP_SHARED`: modifications affectent le fichier et sont visibles aux autres processus accedant au fichier
		- `MAP_PRIVATE`: modifications n'affectent pas le fichier - *copy-on-write*
		- `MAP_FIXED`: le fichier va etre projete exactement a l'adresse specifiee par le 1er param si != 0.
	- `fd`: descripteur du fichier a mapper.
	- `offset`: positiion dans le fichier au debut de la partie a projeter.
- **Retourne**:
	- Rien.
### 6.1.1 Segments de l'espace d'adressage (mode utilisateur)
1. Segment de code: Contient le code du processus et est stocke dans le fichier executable. Le fichier est read-only et peut etre partage entre plusieurs processus.
2. Segment de donnees: Compose de 2 parties - est read/write mais pas partage entre plusieurs processus.
	1. Donnees initialisees: Contient les variables globales initialisees.
	2. Donnees non-initialisees: Contient les autres variables globales.
3. Segment de pile: Gere les appels de fonctions, compose de sections alloues dynamiquement, ou chaque appel cree une section. Une section contient les variables locales, les arguments, un espace pour la valeur de retour et un espace pour la sauvegarde de certains registres (contenu du compteur ordinal, sommet de pile avant l'appel). Cette section est liberee en fin de fonction.
4. Segment de tas: Reserve aux allocations dynamiques d'espace. Il est situe juste apres le segment de donnees (avec le registre break contenant sa limite superieure).
## 6.2 Gestion de la memoire physique
La memoire est organisee en un nombre fixe/variable de partitions. Ou l'OS alloue une partition a un processus pour ensuite charger son espace d'adressage avant d'executer celui-ci. Ce processus peut rester sur la partition, ou faire des allers-retours entre la RAM et le disque.

Pour delimiter la plage d'adresses physiques accessibles au processus et realiser la conversion d'adresses relatives en adresses physiques, on utilise les registres de base et les registres limite.

Avant l'execution du processus, l'OS charge l'adresse physique du debut dans le registre de base et la limite superieure dans le registre limite. Pendant l'execution d'une instruction, chaque adresse relative referencee par l'instruction est comparee avec celle du registre limite. Si celle-ci est plus grande, l'acces est interdit, sinon, elle est convertie en adresse physique en ajoutant le contenu du registre de base dans l'adresse relative.

**La Fragmentation Interne a lieu lorsqu'un espace alloue n'est jamais utilise (l'unite d'allocation memoire etant une partition).**

Une solution a ceci est la creation dynamique des partitions a allouer aux processus en permettant le va-et-vient des processus durant leurs executions, ou l'OS cherche un espace memoire contigu assez grand pour contenir celui-ci. Si l'espace est trop grand, il est scinde en deux.

Cette solution peut conduire a l'apparition de trous trop petits qui ne peuvent etre alloues aux processus (**Fragmentation Externe**).

Une solution a la fragmentation externe est de **compacter** l'espace restant, mais cette solution prend enormement du temps a cause de la vitesse limitee des disques, une autre solution est de terminer le/les processus qui demadent de la memoire si celle-ci est saturee, en attedant un espace libre.

La memoire physique peut etre composee de plusieurs nodes memoire, comme par exemple dans Linux, ou chaque memory node peut contenir jusqu'a 3 zones, qui sont partitionnees en cases de meme taille. Un processus peut occuper plusieurs cadres pas forcement contigus.
## 6.3 Representation de l'etat de la memoire
bitmap - liste chainees - table de listes chainees
## 6.4 Allocation et liberation d'espace
Politique de remplacement (FIFO, LRU, Optimal, Working-Set)
Politique d'allocation d'espace (avant l'execution, durant l'execution avec/sans preallocation)
Politique de placement (First-Fit, Best-Fit, Worst-Fit)

Remplacement LRU
Remplacement FIFO
Remplacement Horloge

Segmentation pure
Segmentation paginee
# 7: Systèmes de fichiers et périphériques d'E / S
Le systeme de fichiers est la partie de l'OS qui gere l'organisation des donnees sur une unite de stockage. La gestion consiste en 5 parties:
- La creation;
- La suppression;
- Les acces en lecture / ecriture;
- Le partage des donnees et;
- Leur protection.
## 7.1 Les fichiers
Un fichier est une suite d'octets repartis dans des blocs de donnees de meme taille. Les utilisateurs peuvent donner des significations differentes au contenu d'un fichier.
Chaque fichier est identifie par un nom auquel est associe un ensemble d'attributs qui permettent de controller les acces, de localiser, de lire et d'ecrire (ou decrire?) les donnees dans le fichier.

*Le type des fichiers (donne par l'extension du fichier) peut etre necessaire dans certains cas.*
## 7.2 Accès aux fichiers
Pour acceder a un fichier, on a besoin du chemin d'acces qui peut etre absolu ou relatif. Les fichiers peuvent etre regroupes dans des repertoires ou sous-repertoires.
#### 7.2.1 Attributs des fichiers
Ils existent 3 categories d'attributs:
- Les attributs qui servent a controler les acces comme le code de protection, mot de passe, proprietaire.
- Les attributs qui definissent le type et l'etat courant du fichier: indicateur de type ASCII/binaire, taille courante, date de creation, date de la derniere modification.
- Les attributs qui permettent de localiser les donnes du fichier.
#### 7.2.2 i-nœuds
Dans les systemes GNU / Linux, les attributs d'un fichier sont rassembles dans des **i-nodes**. Les peripheriques et les pipes sont consideres comme des fichiers speciaux. Un **i-node** contient les informations suivantes:
1. Le type du fichier (ordinaire, repertoire, peripherique de type caractere, peripherique de type bloc ou pipe);
2. Le code de protection sur 9 bits;
3. Le compteur de references;
4. L'identificateur / groupe du proprietaire;
5. La taille;
6. Les dates de creation, du dernier acces et de la derniere modification;
7. Table d'index - composee de 13 numeros de blocs et pointeurs (ptr au bloc 0 -> 9 + ptr indirect simple, double et triple)
## 7.3 Services `Posix` sur les fichiers
Les principaux appels systeme relatifs aux fichiers sont:
- `open()`
- `close()`
- `read()`
- `write()`
- `lseek()` - pour deplacer le pointeur de fichier
- `stat()` - pour recuperer des informations d'un fichier
- `link()` - pour creer un autre chemin d'acces a un fichier physique represente par son i-node
- `unlink()` - pour supprimer ce chemin d'acces et egalement le fichier physique (si plus de chemin d'acces)
##### 7.3.1 `open()`
```C
int open(char* filename, int mode);
int open(char* filename, int mode, int permission);
```
Succes - retourne file descriptor
Echec - retourne -1

A l'ouverture du fichier, le pointeur de fichier poine sur le 1er element du fichier, sauf si `O_APPEND` a ete specifie. Les lectures / ecritures se font a partir de la position du pointeur et entrainent la modification de cette position.

Le `mode` peut correspondre a (ce sont des valeurs `int`):
- `O_RDONLY` - ouvrir en read only
- `O_WRONLY` - ouvrir en write only
- `O_RDWR` - ouvrir en read / write
- `O_CREAT` - creer le fichier s'il n'existe pas, puis l'ouvrir
- `O_EXCL` - ouvrir que si le fichier n'existe pas, si combine avec `O_CREAT`
- `O_TRUNC` - supprimer le contenu du fichier, si combine avec `O_WRONLY` ou `O_RDWR`

```C
int open(char* filename, O_RDONLY|O_WRONLY|O_RDWR|O_CREAT|O_EXCL|O_TRUNC, int permission); // RDWR correspond a RDONLY + WRONLY - toutes les options mises pour montrer
```

Les `permission` correspondent a:
- `S_IRUSR` / `00400` - Lecture pour le proprietaire
- `S_IWUSR` / `00200` - Ecriture pour le proprietaire
- `S_IXUSR` / `00100` - Execution pour le proprietaire
- `S_IRWXU` / `00700` - All of the above
- `S_IRGRP` / `00040` - Lecture pour le groupe
- `S_IROTH` / `00004` - Lecture pour tout le monde
- `S_IWOTH` / `00002` - Ecriture pour tout le monde
- `S_IXOTH` / `00001` - Execution pour tout le monde

```C
"S_IRUSR|S_IWUSR|S_IRGRP|S_IROTH" = 0644 = rw-r-r-
```
##### 7.3.2 `lseek()`
```C
int lseek(int fd, int offset, int origin);
```

Il retourne la nouvelle position du pointeur ou -1 en cas d'erreur, la position depend des parametres `offset` et `origin`:
- `SEEK_SET` - Nouvelle position = `offset`
- `SEEK_CUR` - Nouvelle position = Position courant + `offset`
- `SEEK_END` - Nouvelle position = Taille du fichier + `offset`

On peut donc utiliser ceux-ci comme cela:
```C
lseek(fd, 0, SEEK_CUR); // fd est un descripteur de fichier defini precedemment
```
##### 7.3.3 `dup()`
Chaque processus a une table de file descriptors (descripteurs de fichier). Cette table contient les file descriptors du processus ou chaque file descriptor pointe vers un fichier ouvert pour le processus. Des qu'un processus est cree, le systeme lui ouvre trois fichiers:
- L'entree standard - descriptor `0`
- La sortie standard - descriptor `1`
- La sortie standard - descriptor `2`
- + fichier(s) - descriptor `3..`

```C
int dup(int oldfd);
int dup2(int oldfd, int newfd);
```

L'appel `dup()` permet d'associer a un meme fichier plusieurs descriptors, en associant le plus petit descriptor libre au fichier pointe par `oldfd`. L'appel `dup2()` associe le descriptor `newfd` au fichier pointe par `oldfd`.
##### 7.3.4 `sendfile()`
Pour copier un fichier dans un autre, de maniere classique, on alloue un `buffer` de taille fixe, on lis des donnees du fichier a copier dans le `buffer` puis on ecrit dans le fichier copie le `buffer`. Ces operations sont repetees jusqu'a quand l'integralite des donnees du fichier sont copiees.

L'appel systeme `sendfile()` fournit un mecanisme pour copier sans utiliser le `buffer` (car celui-ci utilise du temps et de la memoire extra).

```C
sendfile(write_fd, read_fd, &offset, stat_buf.st_size);
```
- `write_fd` correspond au file descriptor de la copie du fichier
- `read_fd` correspond au file descriptor du fichier a copier
- `offset` correspond a la position a partir de laquelle commencer la copie
- `st_size` correspond au nombre d'octets a copier (on peut utiliser `fstat()` pour determiner cela)

La valeur retournée est le nombre d'octets copies.
## 7.4 Repertoires
Un repertoire est compose de fichiers et de sous repertoires, represente sous une structure arborescente, ou chaque branche est un repertoire et chaque feuille est un fichier. Dans GNU / Linux, chaque repertoire contient sa propre reference `.` et celle du repertoire superieur `..`.
## 7.5 Services `Posix` sur les repertoires
Les repertoires possedent une entree par fichier. Chaque entree contient au moins, le nom du fichier et son numero de i-node. On a les appels systeme suivants:
- `mkdir()`
- `rmdir()` - supprime un repertoire vide
- `opendir()`
- `closedir()`
- `readdir()`
- `rewinddir()` - place le pointeur au debut d'un repertoire
- `link()`
- `unlink()`
- `chdir()` - changer de repertoire de travail
- `rename()`
- `getcwd()` - obtenir le chemin d’accès du repertoire courant
## 7.6 Peripheriques d'entree / sortie

## 7.7 Le repertoire `/dev`
## 7.8 Les controleurs
