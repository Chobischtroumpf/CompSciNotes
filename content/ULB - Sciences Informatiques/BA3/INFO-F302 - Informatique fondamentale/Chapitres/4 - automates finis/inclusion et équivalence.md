---
title: inclusion et équivalence
authors: Mihai Bors
tags: []
---

# inclusion et équivalence
- Soient $A_1,A_2$ deux automates sur un alphabet $\Sigma$
- $A_1,A_2$ sont équivalens si $L(A_1) = L(A_2)$

## théorème
- Soient $A_1,A_2$ deux automates sur un alphabet $\Sigma$
- il est décidable en temps polynomial
	- si $L(A_1) \subseteq L(A_2)$
	- si $L(A_1) = L(A_2)$

### algorithme
- idée
	- double inclusion : $L(A_1) = L(A_2) \Leftrightarrow L(A_1) \subseteq L(A_2), L(A_2) \subseteq L(A_1)$
- Si $A_1, A_2$ pas complets
	- → commencer par les compléter
	- → on a $L(A_1) \subseteq  L(A_2) \Leftrightarrow L(A_1) \cap \overline{L(A_2)} = \emptyset$
- étapes
	1. construire $A_c : L(A_c) = \overline{L(A_2)}$ (temps poly)
	2. construire $I : L(I) = L(A_1) \cap L(A_c)$ avec $A_1 \otimes A_c$ (temps poly)
	3. tester le vide de $I$ (temps poly )

**exemple**
![[c17159efa2ea3d27e0dfd98139ca47db.png]]
### autre méthode
Soient $A_1, A_2$ deux automates complets
![[830401ef98fe8d89623153f39d721c75.png]]
![[c58f9facc632c7560044851bf7c58005.png]]
