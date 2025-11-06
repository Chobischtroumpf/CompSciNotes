---
title: Code en bloc
authors: Alessandro Dorigo
tags:
  - ThInfo
---


> [!info]+ Définition
> Un **code en bloc** est un code où tous les mots ont la même longueur $\ell$.
> $$K : S \to C^\ell : s \mapsto c_1c_2...c_\ell$$

^b9336a

> [!abstract]- Propriétés
> - **Décodage "à la volée" facilité**: on peut découper la séquence par blocs de taille $\ell$
> - **Contrainte d'univocité**: $q \leq r^\ell$ si le code est univoque
> - **Simplicité d'implémentation**: structure régulière

**Avantages** :
 - Décodage simple et efficace
 - Synchronisation facile
 - Implémentation matérielle simple
 **Inconvénients** :
 - **Sous-optimal** dans beaucoup de contextes
 - Longueur fixe peut être inefficace si les symboles ont des fréquences très différentes
 - Peut gaspiller de l'espace de codage
