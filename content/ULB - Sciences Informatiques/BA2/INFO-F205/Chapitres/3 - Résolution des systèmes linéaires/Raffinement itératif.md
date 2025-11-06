---
title: Raffinement itératif
authors: Alessandro Dorigo
tags:
  -
---

Le raffinement itératif permet d'améliorer la précision d'une solution approchée :

```
While (critère d'arrêt non satisfait) :
   r = b - Ax̂
   Ae = r
   x̂ = x̂ + e
End While
```

Cette méthode compense les erreurs d'absorption et est particulièrement efficace en arithmétique mixte (calcul du résidu en précision double).
