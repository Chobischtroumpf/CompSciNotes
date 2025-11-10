---
title: Chap 10 - slides_graphes_part1.pdf
authors: Alessandro Dorigo
tags:
  -
---

# Roy-Warshall
```python
def roy_warshall(G):
    assert isinstance(G, StaticGraph)
    M = [[int(e) for e in row] for row in G.adj]

    for i in range(G.n):
        M[i][i] = 1

    for k in range(G.n):
        for i in range(G.n):
            if M[i][k]:
                for j in range(G.n):
                    M[i][j] |= M[k][j]
        #print(f"{M}\n")

    return M
```
