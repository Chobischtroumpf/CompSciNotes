---
title: Définitions à mémoriser
authors: Mihai Bors
tags:
  - InfoFond
---
## Chapitre 1: Logique propositionnelle

**Proposition** : Une proposition est un énoncé auquel on peut attribuer une valeur de vérité, vraie ou fausse.

**Interprétation / Valuation** : Une interprétation (ou valuation) est une fonction $V : P \to \{0,1\}$ qui associe à chaque proposition une valeur de vérité.

**Formule propositionnelle** : Une formule propositionnelle est construite à partir de propositions atomiques à l'aide de connecteurs logiques ($\neg$, $\land$, $\lor$, $\to$, $\leftrightarrow$).

**Satisfaisabilité** : Une formule $\varphi$ est satisfaisable s'il existe une interprétation $V$ telle que $V \models \varphi$.

**Validité** : Une formule $\varphi$ est valide si pour toute interprétation $V$, $V \models \varphi$.

**Théorème (lien validité/satisfaisabilité)** : Une formule $\varphi$ est valide si et seulement si sa négation $\neg\varphi$ n'est pas satisfaisable.

**Équivalence** : Deux formules $\varphi$ et $\psi$ sont équivalentes si $\varphi \leftrightarrow \psi$ est valide.

**Littéral** : Un littéral est une variable propositionnelle $x$ ou sa négation $\neg x$.

**Clause** : Une clause est une disjonction de littéraux $\ell_1 \lor \cdots \lor \ell_n$. Elle est satisfaite par une valuation $V$ s'il existe $i$ tel que $V(\ell_i)=1$.

**Clause vide** : La clause vide, notée $\bot$, est insatisfaisable.

**Satisfaction d'un ensemble de clauses** : Un ensemble de clauses $A = \{C_1, \ldots, C_n\}$ est satisfait par une valuation $V$, noté $V \models A$, si pour tout $i$, $V \models C_i$. En particulier, toute valuation satisfait l'ensemble vide $A = \emptyset$.

**Forme normale conjonctive (FNC / CNF)** : Une formule est en forme normale conjonctive (FNC) ssi c'est une conjonction de disjonctions de littéraux.

**Forme normale disjonctive (FND / DNF)** : Une formule est en forme normale disjonctive (FND) ssi c'est une disjonction de conjonctions de littéraux.

## Chapitre 2: Tableaux sémantiques

**Tableau sémantique** : Algorithme pour tester la satisfaisabilité d'une formule propositionnelle en construisant un arbre dont les nœuds sont des ensembles de formules, et les feuilles des ensembles de littéraux.

**$\alpha$-règles** : Règles de simplification des tableaux qui créent un seul fils (conjonction et formules équivalentes).

**$\beta$-règles** : Règles de simplification des tableaux qui créent deux fils (disjonction et formules équivalentes).

**Littéraux complémentaires** : Une paire de littéraux de la forme $x$ et $\neg x$.

**Feuille satisfaisable** : Une feuille d'un tableau sémantique est satisfaisable si elle ne contient pas de paire de littéraux complémentaires.

## Chapitre 3: Déduction naturelle

**Séquent** : Un séquent est une expression de la forme $\varphi_1, \ldots, \varphi_n \vdash \psi$ indiquant l'intention de montrer que $\psi$ peut être dérivée de $\varphi_1, \ldots, \varphi_n$.

**Prémisses** : Les formules $\varphi_1, \ldots, \varphi_n$ dans un séquent $\varphi_1, \ldots, \varphi_n \vdash \psi$ sont appelées prémisses (formules de départ).

**Conclusion** : La formule $\psi$ dans un séquent $\varphi_1, \ldots, \varphi_n \vdash \psi$ est appelée conclusion (formule à prouver).

**Règles de déduction** : Les règles de déduction formalisent la notion de dérivation syntaxique et permettent de faire le lien entre syntaxe et sémantique.

**Conséquence logique** : Le lien entre déduction syntaxique et sémantique : $\varphi_1, \ldots, \varphi_n \vdash \psi$ si et seulement si $\varphi_1, \ldots, \varphi_n \models \psi$.

**$\bot$e (ex falso quodlibet)** : Règle d'élimination de la contradiction : de $\bot$ on peut déduire n'importe quelle formule.

**Correction (soundness)** : Tout ce qui est prouvable est valide : si $\varphi_1, \ldots, \varphi_n \vdash \psi$ alors $\varphi_1, \ldots, \varphi_n \models \psi$.

**Complétude (completeness)** : Tout ce qui est valide est prouvable : si $\varphi_1, \ldots, \varphi_n \models \psi$ alors $\varphi_1, \ldots, \varphi_n \vdash \psi$.

## Chapitre 4: SAT et formes normales

**Problème SAT** : Le problème SAT consiste à décider si une formule propositionnelle (ou un ensemble de clauses) est satisfaisable.

**FNC et clauses (lien)** : Tout ensemble non-vide de clauses $A = \{C_1, \ldots, C_n\}$ est équivalent à la formule en FNC $\varphi_A = \bigwedge_{i=1}^{n} C_i$, au sens où pour toute valuation $V$ : $V \models A$ ssi $V \models \varphi_A$.

**Solveur SAT** : Un programme qui décide le problème SAT. Si la formule est satisfaisable, une interprétation qui la satisfait est retournée.

**Interprétation partielle $\varphi[x/b]$** : Formule obtenue en substituant toutes les occurrences de la variable $x$ par la valeur booléenne $b$ dans $\varphi$.

**Clause unitaire** : Clause qui ne contient qu'un seul littéral.

**Propagation de clauses unitaires** : Simplification consistant à substituer dans toutes les clauses la valeur de vérité qui rend vraie une clause unitaire.

**Proposition à polarité unique** : Variable qui apparaît toujours avec la même polarité (toujours positive ou toujours négative) dans toutes les clauses.

**Algorithme DPLL** : Algorithme de Davis-Putnam-Logemann-Loveland pour résoudre SAT, basé sur la simplification de clauses (propagation unitaire, polarité unique) et le backtracking.

**Transformation de Tseitin** : Transformation permettant de convertir une formule quelconque en FNC en temps polynomial en introduisant des variables auxiliaires.

**2-SAT** : Problème SAT restreint aux clauses contenant au plus 2 littéraux. Décidable en temps polynomial.

**QSAT (Quantified SAT)** : Extension de SAT avec des quantificateurs universels et existentiels sur les variables.

**MAX-SAT** : Problème d'optimisation consistant à trouver une interprétation qui satisfait le maximum de clauses possible.

**WEIGHTED-MAX-SAT** : Variante de MAX-SAT où chaque clause a un poids, et on cherche à maximiser la somme des poids des clauses satisfaites.

**3-SAT** : Problème SAT restreint aux clauses contenant exactement 3 littéraux. Problème $NP$-complet.

## Chapitre 5: Théorie de la complexité

**Alphabet** : Un alphabet $\Sigma$ est un ensemble fini de symboles.

**Mot** : Un mot sur un alphabet $\Sigma$ est une suite finie de symboles de $\Sigma$ (élément de $\Sigma^*$).

**Mot vide** : Le mot vide, noté $\varepsilon$, est le mot de longueur zéro.

**Langage** : Un langage sur un alphabet $\Sigma$ est un sous-ensemble de $\Sigma^*$.

**Problème de décision** : Un problème de décision est un langage $P \subseteq \Sigma^*$ dont la réponse est oui ou non.

**Problème d'optimisation** : Un problème où l'on veut maximiser ou minimiser une certaine quantité.

**Algorithme de décision** : Un algorithme $A$ décide un problème $P \subseteq \Sigma^*$ si pour tout mot $u \in \Sigma^*$, $A$ termine et retourne 1 si $u \in P$, et 0 sinon.

**Algorithme de vérification** : Un algorithme qui, étant donnée une solution candidate à un problème de décision, décide si cette solution est valide.

**Certificat** : Pour un problème $P$ et une entrée $u$, un certificat est un mot $v$ tel qu'un algorithme de vérification $A$ satisfait $A(u,v) = 1$, prouvant ainsi que $u \in P$.

**Classe $P$** : La classe $P$ est l'ensemble des problèmes de décision qui peuvent être résolus par un algorithme déterministe en temps polynomial.

**Classe $NP$** : La classe $NP$ est l'ensemble des problèmes de décision pour lesquels une solution candidate peut être vérifiée en temps polynomial (i.e., il existe un algorithme de vérification polynomial et un certificat de taille polynomiale).

**Réduction polynomiale** : Un problème $A$ se réduit en temps polynomial à un problème $B$ (noté $A \leq_p B$) s'il existe une fonction calculable en temps polynomial qui transforme toute instance de $A$ en une instance de $B$ préservant les solutions.

**$NP$-dur** : Un problème de décision $P$ est $NP$-dur si tout problème $P'$ de $NP$ se réduit à $P$ en temps polynomial.

**$NP$-complet** : Un problème est $NP$-complet s'il appartient à $NP$ et s'il est $NP$-dur (i.e., tout problème de $NP$ se réduit à lui en temps polynomial).

**Théorème de Cook** : SAT est $NP$-complet. Premier problème démontré $NP$-complet (1971).

**PSPACE** : Classe des problèmes décidables en espace (mémoire) polynomial.

**EXPTIME** : Classe des problèmes décidables en temps exponentiel.

## Chapitre 6: Indécidabilité

**Problème décidable** : Un problème de décision $P$ est décidable s'il existe un algorithme qui, pour toute entrée, termine et répond correctement.

**Problème indécidable** : Un problème de décision $P$ est indécidable s'il n'existe aucun algorithme qui le résout pour toutes les entrées.

**Réduction (pour indécidabilité)** : Pour montrer qu'un problème $P_1$ est indécidable, on construit un algorithme qui transforme toute instance d'un problème indécidable connu $P_2$ en une instance de $P_1$ préservant les solutions. Si $P_1$ était décidable, alors $P_2$ le serait aussi (contradiction).

**Problème de l'arrêt** : Étant donné un programme $P$ et une entrée $x$, le problème de l'arrêt consiste à décider si $P$ s'arrête sur $x$.

**Indécidabilité du problème de l'arrêt** : Le problème de l'arrêt est indécidable (Turing, 1936).

**Problème de la Correspondance de Post (PCP)** : Étant donné $n$ paires de mots $(u_1, v_1), \ldots, (u_n, v_n)$, décider s'il existe une séquence d'indices $i_1, \ldots, i_k$ telle que $u_{i_1} \cdots u_{i_k} = v_{i_1} \cdots v_{i_k}$. Ce problème est indécidable.

## Chapitre 7: Automates finis

**$\Sigma^*$** : Ensemble de tous les mots (finis) sur l'alphabet $\Sigma$, incluant le mot vide $\varepsilon$.

**Automate fini** : Un automate fini est un quintuplet $A = (Q, \Sigma, \delta, q_0, F)$, où $Q$ est un ensemble fini d'états, $\Sigma$ un alphabet, $\delta$ une fonction de transition, $q_0$ l'état initial et $F$ l'ensemble des états acceptants.

**Fonction de transition $\delta$** : Fonction qui détermine l'état suivant de l'automate : $\delta : Q \times \Sigma \to Q$ pour un automate déterministe, ou $\delta : Q \times \Sigma \to \mathcal{P}(Q)$ pour un automate non-déterministe.

**État initial** : L'état de départ de l'automate, noté $q_0$, représenté graphiquement par une flèche sans source.

**État acceptant (ou final)** : Un état dans lequel l'automate accepte le mot lu. Représenté graphiquement par un double cercle.

**Exécution (run)** : Une exécution d'un automate est une suite d'états correspondant à la lecture d'un mot.

**Acceptation** : Un mot est accepté par un automate si, après sa lecture complète, l'automate se trouve dans un état acceptant.

**Langage reconnu** : Le langage reconnu (ou accepté) par un automate $A$, noté $L(A)$, est l'ensemble des mots qu'il accepte.

**Automate fini non-déterministe (AFN)** : Un automate où l'on peut avoir plusieurs destinations possibles pour un même couple (état, lettre). Un mot est accepté s'il existe au moins une exécution acceptante.

**Automate complet** : Un automate est complet si pour tout état $q$ et tout symbole $a \in \Sigma$, il existe au moins une transition depuis $q$ étiquetée par $a$.

**État puits** : État non acceptant depuis lequel aucune transition ne mène à un état acceptant. Utilisé pour compléter un automate.

**État atteignable** : Un état $q$ est atteignable s'il existe un mot $w$ tel qu'il existe une exécution de l'automate sur $w$ qui atteint $q$.

**Facteur** : Un mot $u$ est un facteur d'un mot $v$ s'il existe deux mots $v_1, v_2$ tels que $v = v_1 u v_2$ (i.e., $u$ est une sous-séquence de lettres consécutives de $v$).

## Chapitre 8: Expressions rationnelles

**Expression rationnelle** : Une expression rationnelle sur un alphabet $\Sigma$ est définie par la grammaire : $E ::= \varepsilon \mid a \mid \emptyset \mid (E+E) \mid (E \cdot E) \mid E^*$, où $a \in \Sigma$.

**Concaténation de langages** : Pour deux langages $L_1, L_2$, leur concaténation est $L_1 \cdot L_2 = \{u_1 u_2 \mid u_1 \in L_1 \land u_2 \in L_2\}$.

**Étoile de Kleene** : Pour un langage $L$, on définit $L^* = \{u_1 \cdots u_k \mid k \geq 0, u_i \in L\}$ (en particulier $\varepsilon \in L^*$).

**Langage d'une expression rationnelle** : Le langage $L(E)$ d'une expression rationnelle $E$ est défini inductivement selon sa structure :
- $L(\varepsilon) = \{\varepsilon\}$
- $L(a) = \{a\}$
- $L(\emptyset) = \emptyset$
- $L(E_1 + E_2) = L(E_1) \cup L(E_2)$
- $L(E_1 \cdot E_2) = L(E_1) \cdot L(E_2)$
- $L(E^*) = L(E)^*$

**Théorème de Kleene** : Un langage est reconnaissable par un automate fini si et seulement si il est définissable par une expression rationnelle.

## Chapitre 9: Logique des prédicats

**Arité** : Nombre d'arguments d'un prédicat ou d'une fonction. On note $p^n$ ou $f^n$ pour indiquer l'arité $n$.

**Symbole de relation (prédicat)** : Symbole utilisé pour exprimer des relations entre objets, noté $p, q, r, \ldots$ Chaque prédicat a une arité (nombre d'arguments).

**Symbole de fonction** : Symbole utilisé pour construire des termes, noté $f, g, h, \ldots$ Chaque fonction a une arité.

**Symbole de constante** : Symbole représentant un élément fixe, noté $c, d, e, \ldots$

**Terme** : Expression construite à partir de variables, constantes et symboles de fonctions. Défini inductivement : toute variable ou constante est un terme, et si $f$ est une fonction d'arité $n$ et $t_1, \ldots, t_n$ sont des termes, alors $f(t_1, \ldots, t_n)$ est un terme.

**Terme clos** : Un terme sans variable.

**Formule atomique** : Formule de la forme $p(t_1, \ldots, t_n)$ où $p$ est un prédicat d'arité $n$ et $t_1, \ldots, t_n$ sont des termes.

**Quantificateur universel** : Noté $\forall x$, exprime "pour tout $x$".

**Quantificateur existentiel** : Noté $\exists x$, exprime "il existe $x$".

**Langage du premier ordre** : Un langage logique caractérisé par des symboles de relations (prédicats), de fonctions et de constantes, ainsi que des quantificateurs.

**Occurrence d'une variable** : Position effective d'une variable dans une formule (qui ne suit pas un quantificateur).

**Variable libre** : Une variable $x$ est libre dans une formule $\varphi$ si elle a au moins une occurrence qui ne se trouve dans aucune sous-formule commençant par $\forall x$ ou $\exists x$.

**Variable liée** : Une variable dont l'occurrence se trouve dans une sous-formule quantifiée par cette variable.

**Formule close** : Une formule sans variable libre.

**Libres($\varphi$)** : L'ensemble des variables libres de la formule $\varphi$.

**Domaine** : Ensemble non vide $M$ dans lequel on interprète les formules d'une structure.

**Structure** : Une structure $\mathcal{M}$ pour un langage $L$ se compose d'un domaine $M$ non vide et d'interprétations des symboles de $L$ : relations pour les prédicats, fonctions totales pour les symboles de fonctions, et éléments pour les constantes.

**Valuation (pour variables)** : Une fonction $v : V \to M$ qui attribue à chaque variable $x$ une valeur $v(x)$ dans le domaine $M$.

**Interprétation d'un terme** : L'interprétation d'un terme $t$ dans une structure $\mathcal{M}$ selon une valuation $v$, notée $t^{\mathcal{M},v}$, est un élément du domaine calculé inductivement.

**Satisfaction d'une formule** : Une structure $\mathcal{M}$ et une valuation $v$ satisfont une formule $\varphi$, noté $\mathcal{M}, v \models \varphi$, si $\varphi$ est vraie dans $\mathcal{M}$ pour la valuation $v$.

**Modèle** : Une structure $\mathcal{M}$ est un modèle d'une formule close $\varphi$ si $\mathcal{M} \models \varphi$ (i.e., $\varphi$ est vraie dans $\mathcal{M}$, indépendamment de la valuation puisque $\varphi$ est close).

**Formule valide (en logique des prédicats)** : Une formule $\varphi$ est valide si pour toute structure $\mathcal{M}$ et toute valuation $v$, on a $\mathcal{M}, v \models \varphi$.

**Formule satisfaisable (en logique des prédicats)** : Une formule $\varphi$ est satisfaisable s'il existe une structure $\mathcal{M}$ et une valuation $v$ telles que $\mathcal{M}, v \models \varphi$.

**Équivalence de formules (en logique des prédicats)** : Deux formules $\varphi$ et $\psi$ sont équivalentes si pour toute structure $\mathcal{M}$ et toute valuation $v$, on a $\mathcal{M}, v \models \varphi$ si et seulement si $\mathcal{M}, v \models \psi$.

**Théorème de la validité en logique du premier ordre** : Le problème de validité en logique du premier ordre est indécidable.
