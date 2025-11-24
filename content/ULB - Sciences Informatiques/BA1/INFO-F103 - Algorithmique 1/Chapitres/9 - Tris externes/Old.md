---
title: Old
authors: Alessandro Dorigo
tags: []
---

Manipulation de fichiers très volumineux qui ne tiennent pas en mémoire:
- Les méthodes de tri externe manipulent des données sur fichiers, nécessitant des accès plus lents et souvent séquentiels;
- Il faut minimiser les accès aux fichiers pour optimiser les performances.
### Aspects système à considérer
- Minimiser les accès aux fichiers pour éviter les copies répétées entre disque et mémoire;
- Ignorer le coût du tri en mémoire par rapport aux copies disque/mémoire;
- Supposer que les fichiers sont sur des disques différents pour simplifier l’analyse.
## Méthode de tri externe
- Utilise des passes successives pour trier les données;
- Nous ignorerons le coût lié à la réalisation d’un tri en mémoire en comparaison avec le coût des copies vers et/ou depuis un fichier;
- Le coût est mesuré par le nombre de passes nécessaires.
### Hypothèse
- $N$ données à trier, mémoire centrale peut stocker $M < N$ données;
- Utilisation de plusieurs fichiers pour le tri, initialement les données sont dans le fichier 0.
## Tri-fusion (fusions multiples équilibrées)
- Première passe: divise le fichier en blocs de taille $M$ ou moins sur $P$ fichiers différents;
	- Le premier bloc est écrit, une fois trié, sur le fichier $0,\dots,$ le $P^{me}$ bloc est écrit, une fois trié, sur le fichier $P - 1$;
- Trie chaque bloc en mémoire et les sauvegarde sur plusieurs fichiers;
- Fusionne les blocs triés par passes successives jusqu’à ce que toutes les données soient triées.
## Exemple 1:
- Mémoire centrale de 3 données pour trier `ALGORITHMIQUEGENERALE`.
- $M = 3$, $N = 21$, $P = 3$ (6 fichiers au total).
### Processus
1. Découper les données en blocs de 3:
   - `ALG | ORI | THM | IQU | EGE | NER | ALE`
2. Trier et écrire les blocs sur les fichiers 0 à 2:
   - `fichier 0: AGL`
   - `fichier 1: IOR`
   - `fichier 2: HMT`
3. Si blocs restants, répéter le tri et écriture comme deuxième bloc sur les fichiers:
   - `fichier 0: AGL IQU AEL`
   - `fichier 1: IOR EEG`
   - `fichier 2: HMT ENR`
### Fusion $P$-fusion
1. Lire la première donnée du premier bloc de chaque fichier, écrire la plus petite sur le fichier $P$;
	- Le fichier $P$ contient alors un bloc d’au plus $MP$ données.
2. Lire la donnée suivante du fichier d’où provient la donnée écrite;
3. Répéter jusqu’à épuisement des blocs:
	- la mémoire contient `AIH` $\rightarrow$ on écrit `A` et on lit `G`
	- la mémoire contient `GIH` $\rightarrow$ on écrit `G` et on lit `L`
	- la mémoire contient `LIH` $\rightarrow$ on écrit `H` et on lit `M`
	- la mémoire contient `LIM` $\rightarrow$ on écrit `I` et on lit `O`
	- la mémoire contient `LOM` $\rightarrow$ on écrit `L` et on ne lit rien
	- la mémoire contient `OM` $\rightarrow$ on écrit `M` et on lit `T`
	- la mémoire contient `OT` $\rightarrow$ on écrit `O` et on lit `R`
	- la mémoire contient `RT` $\rightarrow$ on écrit `R` et on ne lit rien
	- la mémoire contient `T` $\rightarrow$ on écrit `T` et on ne lit rien
   - `fichier 3: AGHILMORT`
4. Fusionner les blocs restants sur les fichiers suivants:
   - `fichier 4: EEEGINQRU`
   - `fichier 5: AEL`
### Finalisation
- Fusion des fichiers 3 à 5 pour obtenir les données triées:
  - `fichier 0: AAEEEEGGHIILLMNOQRRTU`
## Performance
- Première phase: $\frac{N}{M}$ blocs triés;
- Nombre de passes pour tri complet: $1 + \left\lceil \log_P(\frac{N}{M}) \right\rceil$;

Trier $10^9$ éléments avec 6 fichiers et mémoire de $10^6$ éléments nécessite 8 passes.
- Si les fichiers sont sur même disque, plus $P$ est grand, moins il y a de passes mais plus il y a d'accès non séquentiels.

Nous pouvons généraliser la méthode de tri externe en utilisant un heap de grande taille pour trier les données élément par élément.
## Exemple 2:
1. La mémoire et le heap contiennent les 5 premières données à trier: `ALGOR`.
2. Extraction et insertion:
	- Extraire `A`, écrire sur le fichier 0, insérer `I`;
	- Réorganiser le heap si nécessaire;
	- Répéter jusqu'à ce que le tas soit réorganisé correctement.
### Gestion des ordres dans le heap
- Si l’élément inséré est plus petit que l’élément extrait, il est marqué pour le prochain bloc de fusion.
- Exemple avec `H` et `I`:
	- Si `H` est plus petit que `I`, marquer `H` et le considérer comme plus grand que les éléments actuels.
### Processus:
- **Étape 1:**
    - Extraire `A` (plus petit élément);
    - Écrire `A` sur le fichier 0;
    - Insérer `I`.
- **Étape 2:**
    - Extraire `G`;
    - Écrire `G` sur le fichier 0;
    - Insérer `T`.
- **Étape 3:**
    - Extraire `I`;
    - Écrire `I` sur le fichier 0;
    - Insérer `H` (plus petit que `I`);
    - Marquer `H` pour le prochain bloc.
- **Étape 4:**
    - Extraire `L`;
    - Écrire `L` sur le fichier 0;
    - Insérer `M`.
- **Étape 5:**
    - Extraire `M`;
    - Écrire `M` sur le fichier 0;
    - Insérer `O`.
- **Étape 6:**
    - Extraire `O`;
    - Écrire `O` sur le fichier 0;
    - Insérer `E` (plus petit que `O`);
    - Marquer `E` pour le prochain bloc.
- **Étape 7:**
    - Extraire `R`;
    - Écrire `R` sur le fichier 0;
    - Insérer `G`;
    - Marquer `G` pour le prochain bloc.
- **Étape 8:**
    - Extraire `T`;
    - Écrire `T` sur le fichier 0;
    - Insérer `U`.
- **Étape 9:**
	- Extraire `U`;
	- Écrire `U` sur le fichier 0;
	- Insérer `E`.
- Bloc fusionné sur fichier 0: `AGILMOQRTU`

Nous continuons en écrivant, sur le fichier 1, le nouveau bloc résultant d’une fusion:
- Nous extrayons du heap les données `E`, `E`, `E` et `G` et ce jusqu’à insérer dans le heap une donnée `A` plus petite que `G`;
- `A` est donc marquée comme appartenant au prochain bloc de fusion, nous extrayons `H` et `I`;
- Puis la donnée `E` juste insérée est aussi marquée et nous extrayons `L`, `N` et `R`.

Il ne reste alors que deux éléments marqués dans le heap.
- Le sommet de tête étant marqué, un nouveau bloc de fusion est complet, il est formé des 9 données `EEEGHILNR`.

Nous entamons la construction du troisième bloc de fusion sur le fichier 2.
- Ce bloc contiendra évidemment `A` et `E`.

Au cours de ces traitements, quand un élément est marqué et qu’il évolue dans le heap, lorsqu’il est comparé avec un autre élément déjà marqué, ces deux éléments doivent être comparés classiquement suivant leur priorité respective.

Nous obtenons donc après cette première phase, les fichiers suivants:
- `fichier 0: AGILMOQRTU`
- `fichier 1: EEEGHILNR`
- `fichier 2: AE`
## Technique de sélection-remplacement
- Engendre environ $\frac{N}{2M}$ blocs;
- Après l’extraction de $2M$ données depuis un heap de $M$ données, un nouveau bloc commence lorsque le sommet du tas est marqué.
## Passes de fusion
- Chaque passe de fusion divise le nombre de blocs par $P$;
	- Si $P^2 > \frac{N}{2M}$, deux passes suffisent pour réaliser le tri complet.
## Fusion multiphasée (polyphase)
La fusion multiphasée répartit de manière irrégulière les blocs triés obtenus après une première phase sur plusieurs fichiers, laissant un fichier disponible pour les opérations de fusion.
- Les fusions s'arrêtent lorsqu'un des fichiers est vidé.
## Exemple 3:
Dans un système ayant une mémoire centrale de deux éléments et pouvant potentiellement manipuler 3 fichiers, notre ensemble de données `ALGORITHMIQUEGENERALE` peut se répartir de
la manière suivante:
- `fichier 0: AL IR IM EG ER AL E`
- `fichier 1: GO HT QU EN`
- `fichier 2:`
### Processus:
**Première fusion**:
- Fusionner les quatre premiers blocs des fichiers 0 et 1.
	- `fichier 0: ER   AL   E`
	- `fichier 1:`
	- `fichier 2: AGLO HIRT IMQU EEGN`
**Deuxième fusion**:
- Fusionner les trois premiers blocs des fichiers 0 et 2.
	- `fichier 0:`
	- `fichier 1: AEGLOR AHILRT EIMQU`
	- `fichier 2: EEGN`
**Troisième fusion**:
- Fusionner le premier bloc du fichier 1 avec l'unique bloc du fichier 2.
	- `fichier 0: AEEEEGGLNOR`
	- `fichier 1: AHILRT        EIMQU`
	- `fichier 2:`
**Quatrième fusion**:
- Fusionner le premier bloc du fichier 1 avec l'unique bloc du fichier 0.
	- `fichier 0:`
	- `fichier 1: EIMQU`
	- `fichier 2: AAEEEGGHILLNORRT`
**Cinquième fusion**:
- Fusionner les deux derniers blocs.
	- `fichier 0: AAEEEEGGHIILLMNOQRRTU`
	- `fichier 1:`
	- `fichier 2:`
## Distribution optimisée des blocs
Pour optimiser les fusions, il est crucial de bien répartir les blocs initialement:
- **Approche "à reculons"**
    - Commencer par déterminer la répartition des blocs après la dernière fusion;
    - Travailler à rebours pour déterminer la répartition initiale.

Les valeurs indiquées représentent le nombre de blocs sur chaque fichier et une même colonne de valeurs représente la situation des fichiers après une fusion.
- L’évolution des fusions dans le temps se comprend en lisant la figure de droite à gauche.
### Exemple avec 3 fichiers:
- `fichier 0: 1 | 0 | 1 | 3 | 0 | 5  | 13 | ...`
- `fichier 1: 0 | 1 | 2 | 0 | 3 | 8  | 0  | ...`
- `fichier 2: 0 | 1 | 0 | 2 | 5 | 0  | 8  | ...`
- `Total:     1 | 2 | 3 | 5 | 8 | 13 | 21 | ...`

Le nombre total de blocs après chaque fusion suit la suite de Fibonacci. La plus grande valeur de la colonne courante est mise à zéro après l’avoir additionnée aux autres valeurs dans la même colonne pour obtenir la colonne suivante.
### Généralisation pour 4 fichiers:
- `fichier 0: 1 | 0 | 1 | 3 | 7  | 0  | ...`
- `fichier 1: 0 | 1 | 2 | 4 | 0  | 7  | ...`
- `fichier 2: 0 | 1 | 2 | 0 | 4  | 11 | ...`
- `fichier 3: 0 | 1 | 0 | 2 | 6  | 13 | ...`
- `Total:     1 | 3 | 5 | 9 | 17 | 31 | ...`

La séquence des totaux suit une forme généralisée de la suite de Fibonacci.
### Optimisation des fusions
Pour optimiser les fusions et l'utilisation des fichiers, il faut répartir les blocs initiaux selon les configurations basées sur les séquences de Fibonacci généralisées. Si le nombre total de blocs n'est pas un nombre de Fibonacci, il faut ajouter des blocs fictifs pour obtenir la configuration souhaitée.
