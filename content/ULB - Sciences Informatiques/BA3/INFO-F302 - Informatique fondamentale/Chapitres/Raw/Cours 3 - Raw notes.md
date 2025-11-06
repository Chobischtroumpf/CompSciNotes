---
title: Cours 3 - Raw notes
authors: Alessandro Dorigo
tags:
  -
---

> [!info]+ Fonction
> Soit $A$, $B$ deux ensembles. Une **fonction** $f$ de $A$ dans $B$ est une relation de $A$ ($f\subseteq A \times B$) telle que pour tout $a \in B$  il existe au moins plus un éléments $b \in B$ qu'on va noter $f(a)$, tel que $(a,b) \in f$
>
> - On notera $f: A -> B$ pour dire que la fonction est de $A$ dans $B$
> - On note donc $(f)$ son **domaine**, l'ensemble des éléments de $A$ qui est une image pour $f$
> - Le codomaine de $f$ noté codom(f), est l'ensemble des éléments de $B$ qui sont l'**image** d'au moins un élément de $A$ *pour* $f$
> - On note $B^A$ l'ensemble des fonctions de $A$ dans $B$
> - Pour tout $X \subseteq A$ , ont note $f|_x$ la fonction de $X$ dans $B$ définie pour tout $x \in B$
> Une fonction $f : A\rightarrow B$ est dite :
> - **injective**: si pour tout $a_{1}, a_{2} \in dom(f)$, si $f(a_{1})=f(a_{2})$ alors $a_{1}=a_{2}$
> - **surjective** si pour tout $b \in B$ il existe $a \in dom(f)$ tel que $f(a)=b$
> - **bijective** si elle est **injective** et **surjective**
> - **totale** si tout élément de $A$ possède une image pour $f$

>[!example]+ Exemple
>![[Pasted image 20250922083239.png]]

> [!abstract]- **Lemme des tiroirs/pigeons**
> Soient $A$, $B$ deux ensembles finis tels que #$A$ $>$ #$B$ (#A cardinalité, nbr d'éléments).  Alors il n'existe pas de fonction **totale** injective de $A$ dans $B$.
> Autrement dit, toute fonction **totale** devra envoyer au moins deux éléments de A vers le même élément de $B$.
> ![[Pasted image 20250922084340.png]]


> [!definition] Définition **Ensemble (IN)DÉNOMBRABLE**
> Un ensemble $X$ est **dénombrable** s'il existe une fonction injective de $X$ dans $\mathbb{N}$
> - Autrement dit il n'y a pas "plus" d'éléments dans $X$ que dans $\mathbb{N}$.

> [!example]+ Exemple les ensembles $\mathbb{Z}$ et $\mathbb{N}²$
> ![[Pasted image 20250922084823.png]]
> - $\mathbb{Q}$ l'ensemble des rationnels est **dénombrable** (car $\mathbb{Z}²$ est dénombrable)

> [!example]+ Indénombrable
> - L'ensemble des réels $\mathbb{R}$ est **indénombrable**. (sera démontré plus tard dans le chapitre sur l'indécidabilité).

L'ensemble des parties de $\mathbb{N}$ est **indénombrable**: **Preuve**: On doit démontrer qu'il n'existe aucune fonction injective de $2^{\mathbb{N}}$ dans $\mathbb{N}$
Preuve par l'absurde:
On suppose l'existence d'une fonction **totale injective** $f: 2^{\mathbb{N}} \rightarrow \mathbb{N}$
![[Pasted image 20250922091507.png]]


---

# Logique Propositionnelle : Introduction

>[!info]+ Langage logique
>Permet de décrire avec précision et rigueur des énoncés et des raisonnements, basés notamment sur des connecteurs Booléens (et, ou négation).

>Langage naturel peut mener à des paradoxes (pas assez rigoureux)
>- exemple détecteur de mensonges (fiables ou pas ?)

>[!note]+ Notations
>Vrai / Faux : $\top$, $\bot$
>Négation: $\neg p$
>Conjonction: $p \wedge q$
>Disjonction: $p \vee q$
>Implication: $p \to q$
>Equivalence: $p \leftrightarrow q$
