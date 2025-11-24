---
title: Méthodes directes pour la factorisation LU
authors: Alessandro Dorigo
tags:
  -
---

#### Méthode de Doolittle

D'abord la $k$-ième ligne de $U$, puis la $k$-ième colonne de $L$ :

```
for k=1:n
  for j=k:n
    u_{kj} = a_{kj} - \sum_{r=1}^{k-1} l_{kr}u_{rj}
  end
  for i=k+1:n
    l_{ik} = \frac{1}{u_{kk}}\left(a_{ik} - \sum_{r=1}^{k-1} l_{ir}u_{rk}\right)
  end
end
```

#### Méthode de Crout

D'abord la $k$-ième colonne de $L$, puis la $k$-ième ligne de $U$ :

```
for k=1:n
  for i=k:n
    l_{ik} = a_{ik} - \sum_{r=1}^{k-1} l_{ir}u_{rk}
  end
  for j=k+1:n
    u_{kj} = \frac{1}{l_{kk}}\left(a_{kj} - \sum_{r=1}^{k-1} l_{kr}u_{rj}\right)
  end
end
```
