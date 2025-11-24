---
title: INFO-F105 - Langages de Programmation 1
authors: Alessandro Dorigo
tags:
  - ULB
  - BA1
---
## Cours 7/2: Chapitre 1

- Prendre connaissance de plusieurs paradigmes de programmation
- Mieux connaitre liaison langage prog → langage machine

Algorithme: Methode efficace de resolution d’un probleme

Programme: Methode pour traduire cet algorithme pour un contexte materiel et logiciel donne (processeur, OS, lang de prog)

- Sequence d’op elementaires realisant un traitement souhaite pour une machine visee

Lang de prog: Convention d’ecriture lisible et comprehensible par un etre humain et traduisible de facon univoque en un code executable par une machine

Different lang de prog car applications diverses / contraintes / progres theoriques.

- Calcul scientifique, symbolique, app web, business…
- Vitesse d’exec, de dev, de maintenance
- Architectures materielles evoluent

Bon langage:

- Lisible, fiable, portable, peu couteux

Influences sur le design des langages:

- Architecture des ordis
- Progres theoriques, tendances
    - Couts materiels → couts logiciels

Langages imperatifs: Decrivent comment realiser qqch

Langages orientes objet: Element central est l’objet, defini par un ensemble de donnees et d’actions autorisees sur ces donnees

Langages fonctionnels: Paradigme declaratif → decrit ce qu’il faut realiser, mais pas comment, element central est la fonction, au sens mathematique

Langages script: Langages tres haut niveau, apprentissage et utilisation rapides

## Cours 8/2: Chapitre 1 & 2

**Chap 1:**

Les liens peuvent etre dynamiques ou statiques (dynamiques = durant l’exec)

Lang compiles = production du code source, production du code machine et execution sont des etapes distinctes

Lang interpretes = les trois etapes s’exec simultanement grace a un interpreteur

Compromis efficacite exec (lang compiles) vs facilite, interactivite au dev (lang interpretes)

**************Chap 2:**************

Toutes variables doivent etre declares.

## Cours 14/2: Chapitre 2 & 3

Defauts d’associativite → a + (b + c) == (a + b) + c ?

Effets de bords:

![Screenshot from 2023-02-14 16-30-16.png](INFO%20F-105%20Langages%20de%20Programmation%201%20e4660ebc33c9478e8d676120673b15d0/Screenshot_from_2023-02-14_16-30-16.png)

Inexistants dans les langages fonctionnels, se produisent lorsque l'exécution d'une fonction affecte l'état global de l'application, plutôt que de se limiter à la valeur de retour de la fonction.

Les effets de bord peuvent inclure des changements dans les variables globales, l'état du système de fichiers, l'interaction avec des périphériques externes, la modification de données en entrée ou la création de nouvelles données qui n'étaient pas là avant l'exécution de la fonction.

Les effets de bord peuvent rendre le code plus difficile à comprendre et à maintenir, car il n'est pas toujours évident de savoir quelles parties de l'application sont affectées par l'exécution d'une fonction.

Compromis efficacite / fiabilite

- Evite le cout en efficacite lie au passage de parametres
- Complique l’analyse du programme

Surcharge possible en C++ mais pas Java

Egalement moins naturelles:

- x = &y, x&y en C++
- & = l’adresse en memoire de y → x pointe vers la meme location, donc x contient l’adresse memoire de y
- On peut acceder / changer la valeur de y avec x en utilisant le deferencing operator (*x) → *x = 5, y = 5

Operations unaires: `++a` et `--a`, `a++` et `a--`

- Incrémentent ou décrémentent la valeur
- Valeur de `++a` est une référence à a après incrément
- Valeur de `a++` est une copie de a avant incrément

`++a` et `--a` modifient directement la valeur de la variable "a", tandis que `a++` et `a--` modifient la valeur de "a" après avoir renvoyé une copie ou une référence à la valeur avant la modification.

`x / y` = `double(x) / y` (convertir explicitement pour avoir float)

C++ a egalement les decalages:

- `a << k`, `a >> k` (decalage des bits de k positions vers la gauche ou vers la droite, avec ajout de bits)

AND = 1010&0101, a && b

OR = 1010|0101, a || b

XOR = 1010^0101

NOT = !a

Evaluations tronquees → Si l’opérande de gauche permet d’évaluer une expression booléenne, l’opérande de droite n’est pas évaluée

- false AND b
- true OR b

![Untitled](INFO%20F-105%20Langages%20de%20Programmation%201%20e4660ebc33c9478e8d676120673b15d0/Untitled.png)

Registres / memoire NASM:

![Untitled](INFO%20F-105%20Langages%20de%20Programmation%201%20e4660ebc33c9478e8d676120673b15d0/Untitled%201.png)

Registres de base NASM:

![Untitled](INFO%20F-105%20Langages%20de%20Programmation%201%20e4660ebc33c9478e8d676120673b15d0/Untitled%202.png)

Huit registres généraux:

- Six registres de segments
- Registre de contrôle ou des flags servant notamment aux tests
- Instruction Pointer (eip), adresse de l’instruction suivante

![Untitled](INFO%20F-105%20Langages%20de%20Programmation%201%20e4660ebc33c9478e8d676120673b15d0/Untitled%203.png)

Expressions mixtes → par exemple a + b ou a = int b = float

Fonctionne avec des types distincts mais compatibles

- Les règles déterminant les conversions automatiques doivent être bien définies et bien utilisées
- Perte de capacités de correction par le compilateur

## Cours 15/2: Chapitre 3

Boucles a post conditions

Boucle a compteur → nombre d’iterations fixee a l’avance (sauf si compteur modifiable)

Boucle en assembleur

Programmation fonctionnelle: recursion

- Pas de var pour implementer cond / compteur
- Simuler boucle for avec fct recursive

Rupture de sequences (struc de ctrl sans instruc qui designe l’instruc suivante a executer)

- Sauts à une instruction étiquetée
- Sorties de structure de contrôle
- Gestion d’exceptions
- Appels et retours de routines

Sauts inconditionnels → jump en asm

Sorties de structure (break, continue, return, std::exit(code), std::abort())

Appel d’une fonction / routine / coroutine provoque un saut du code appelant vers le code de la fonction

→ Exceptions

Instructions declaratives → indiquent au compilateur comment traiter d’autres instructions et par tjr strictes (declaration d’un nom / type)

- Declaration : indiquer au compilateur comment traiter la variable i
- Définition : le compilateur génèrera du code machine pour stocker la variable en mémoire et pouvoir y accéder
- Initialisation : le compilateur stockera une valeur par défaut en mémoire

Définition vaut déclaration, mais l’inverse n’est pas vrai

La declaration est composee d’un specificateur / liste de declareurs

Specificateur:

- Spécificateur de type (obligatoire)
- Spécificateurs de stockage et liaison (optionnels)
- Spécificateurs de qualification (optionnels)
- Spécificateurs d’inclusion (optionnels, pour les fonctions)

**Types simples : void, char, short, int, long, float, double, signed, unsigned**

**Types élaborés : enum, union, struct**

![Untitled](INFO%20F-105%20Langages%20de%20Programmation%201%20e4660ebc33c9478e8d676120673b15d0/Untitled%204.png)

Declaration nom de type:

```cpp
typedef int T[], *PI, F(T);
typedef struct {double x, y;} Point;
Point p1;
```

Stockage / liaison:

- Allocation de mémoire / mode de stockage (variables statiques dans segment BSS/DATA)
- Durée de vie de la variable (bloc local ou processus)
- Portée et mode de liaison (visible dans le bloc local, l’unité de traduction, tout le programme)

Modes de stock / liaison:

**Par défaut (pas de spécificateur)**

- Si déclaration locale : durée de vie automatique (limitée au bloc local) et pas de liaison (portée limitée au bloc local)
- Si déclaration globale : durée de vie statique (durée de vie du processus) et liaison externe (visible dans tout le programme, pas juste le fichier)

**static**

- Si déclaration locale : stockage et durée de vie statique (e.g. valeur gardée entre appels fonction successifs)
- Si déclaration globale : idem plus mode de liaison interne (nom visible uniquement dans l’unité de traduction)

**extern : nom préservé jusqu’à l’édition des liens**

Qualification:

**const - variable constante**

- Permet au compilateur d’optimiser le code et détecter des modifications erronnées
- Doit être initialisée

**volatile**

- Mémoire suceptible de changer à cause de processus externes, car partagée entre plusieurs threads
- Interdit certaines optimisations au compilateur

## Cours 22/2: Chapitre 4

Types et systeme de typage

Le système de typage d'un langage de programmation définit les types de données manipulables et les règles de manipulation. Il peut être statique ou dynamique, explicite ou implicite.

- Un système de typage statique vérifie les types à la compilation, tandis qu'un système de typage dynamique les vérifie à l'exécution (C++ / C / Java).
- Un système de typage explicite nécessite une déclaration explicite des types, tandis qu'un système de typage implicite les infère du contexte (Python, Typescript).

Avantages:

- Facilite la detection d’erreurs par le compilateur / programmeur
- Robustesse / lisibilite / modularisation des prog

Types elementaires:

- Entiers, booleens, characteres, complexes

Types complexes:

- Pointeurs / réference: accès indirect à un type de base
- Enumération: sous-type d'entiers avec une définition constante
- Tableaux: collection de valeurs du même type

Le type d’une variable definit les val que qu’elle peut prendre, son codage binaire et les op

Exemple:

`int i` - 3 fonctions:

- Déclaration: explique comment la variable i doit être traitée
- Définition: le compilateur crée du code machine pour stocker la variable en mémoire et y accéder
- Initialisation: le compilateur stocke une valeur par défaut en mémoire

Conversions implicites

Typage fort ou faible:

- Plus fort si:
    - Statique
    - Pas ou peu de conversions implicites
    - Memory-safe
- Fortement type si les erreurs de typage peuvent etre detectees lors de la compilation ou a l’execution

C - Typage faible / langage bas niveau:

- Déclaration explicite des variables avec typage statique
- Conversions explicites sans contraintes
- Nombreuses conversions implicites
- Accès arbitraire à la mémoire

C++ - Construction plus sûres (références vs pointeurs, conversions explicites)

Java - Typage fort (déclarations statiques, explicites, conversions limitées, mémoire protégée)

- Declarations obligatoires
- Types primitifs ou elementaires
- Types primitifs dédoublés par des classes enveloppantes (wrappers) de types “référence” (même opérateurs plus les méthodes communes à tous les objets)

Python - Typage dynamique

- Plupart des types sont immuables
    - Les types numeriques et char aussi
    - Exceptions: listes, ensembles, dict

Une analogie courante pour comprendre le polymorphisme est celle d'une maison et d'un appartement. Bien que les deux aient des caractéristiques similaires, telles qu'un toit, des murs et des portes, ils ont également des différences. Par exemple, une maison peut avoir un jardin et un garage, tandis qu'un appartement peut avoir un balcon et un ascenseur.

De même, dans la **programmation orientée objet**, une classe peut avoir des méthodes qui sont communes à toutes les instances de cette classe, mais chaque instance peut également avoir des méthodes qui lui sont propres.

Notations litterales:

- Decimale `123`
- Octale `0123`
- Hexadecimale `0x123`
- Binaire `0b123`
- Caractere `"123"` , peut avoir des escape codes `"\n"`

Types entiers C++:

- Entiers non signes
    - unsigned char
    - unsigned short int ou unsigned short
    - unsigned int ou unsigned
    - unsigned long int ou unsigned long
    - unsigned long long int ou unsigned long long
- Entiers signés
    - signed char
    - short int ou signed short int ou short
    - int ou signed int ou signed
    - long int ou signed long int ou long
    - long long int ou signed long long int ou signed long long ou long long


Pointeurs - type de var qui a pour valeur une adresse de mem ou null

- Adressage indirect
- Gestion mem dyn (stack)

Stockage dynamique:

- Code genere a la compilation pour gerer l’alloc en mem sur le **Runtime Stack**
- Utilise pour grosses donnees
- `malloc` en C, `new` en C++ / Java
- Memoire desallouee avec `free` ou `delete` ou bien avec le garbage collector

**Operations sur les pointeurs**

![Untitled](INFO%20F-105%20Langages%20de%20Programmation%201%20e4660ebc33c9478e8d676120673b15d0/Untitled%205.png)

## Cours 15/3: Chapitre 5

Sous-programmes - separer utilisation et implantation

Avantages

- Efficacite - code ecrit **qu’une seule** fois
- Abstraction / modularite - code peut etre remplace independamment

Variantes de fcts

- Procedure - bloc de code appelable, échangeant des informations via paramètres et variables globales
- Fonction
- Methode - fonction ou procédure définie au sein d’une classe, s’appliquant à un objet de cette classe
- Coroutine - généralisation du concept de fonction : à l’appel, l’exécution reprend au point de retour précédent
- Thread - s’exécute en parallèle du bloc appelant

**Effets de bord**

Au sens mathématique, une fonction s’applique à un élément du domaine et renvoie un élément du codomaine : pas de modification des paramètres ou autres variables

Dans beaucoup de langages, les fonctions ont de nombreux “effets de bord” : peuvent modifier les paramètres, ou même des cellules de mémoire arbitraires
