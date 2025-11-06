---
title: Chap 11 - slides_prog_dynamique_part1.pdf
authors: Alessandro Dorigo
tags:
  -
---

# Fibonacci récursif
[[Chap 02 - slides_recursivite.pdf#Fibonacci récursif|Défini au Chapitre 2]]
# Fibonacci itératif
[[Chap 02 - slides_recursivite.pdf#Fibonacci itératif|Défini au Chapitre 2]]
# Fibonacci memo descendant
### Slide 16
```python
class Fibonacci:
	def __init__(self, n):
		self.fib = {}
		print self.fibo(n)

	def fibo(self, n):
		if not self.fib.has_key(n):
			if n == 0:
				self.fib.setdefault(0,0)
			elif n == 1:
				self.fib.setdefault(1,1)
			else:
				temp = self.fibo(n - 1) + self.fibo(n - 2)
				self.fib.setdefault(n, temp)
		return self.fib[n]
```

# Bellman-Ford
### Slide 38 (63/80)
```C
Bellman-Ford(G = (S,A,w), s) // S = ensemble des sommets, A = ensemble des arretes, w = fonction de ponderation entre deux sommets, s = sommet de depart
	for (int i = 1 ; i <= ordre du graphe G(|S|) ; ++i)
		D_0[i] = +infty

	int k = 0

	while (k < ordre du graphe G)
		D_k[s] = 0

		for (v in S)
			D_k+1[v] = min{D_k[v],min{D_k[u] + w(u,v) | (u,v) in A}}

		if (D_k+1 == D_k)
			STOP
		else
			k += 1

	if (k == |S|)
		return -1 // Detection du circuit absorbant
	// D = tableau des distances depuis s (plus courts chemins)
return D
```

# Chap 11 - slides_prog_dynamique_part2.pdf
## Knapsack (Implementation naive)
### Slide 13
```python
def KP(weight, value, W, n):
    # Base case
    if n == 0 or W == 0:
        return 0

    # If weight of item n > W then item n is excluded
    if weight[n-1] > W:
        return KP(weight, value, W, n-1)

    # Else return max of item n included or not
    elif weight[n-1] <= W:
        return max(value[n-1] + KP(weight, value, W-weight[n-1], n-1),
                   KP(weight, value, W, n-1))

# Example call
# KP(weight, profit, W, n)
```
## Knapsack Memo
### Slide 17
```python
# Declaration and Init of T[][] at -1:
# n = number of distinct items, W = capacity of knapsack
T = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

def knapsack(weight, value, W, n):
    if n == 0 or W == 0: return 0
    # If computed, return already computed value
    if T[n][W] != -1: return T[n][W]
    # Otherwise
    elif weight[n - 1] <= W:  # item fitting & may be selected
        T[n][W] = max(knapsack(weight, value, W, n - 1),
                      value[n - 1] + knapsack(weight, value, W - weight[n - 1], n - 1))
        return T[n][W]
    elif weight[n - 1] > W:  # item not fitting
        T[n][W] = knapsack(weight, value, W, n - 1)
        return T[n][W]

# Exec: knapsack(weight, profit, W, n)
```
## Knapsack Tab
### Slide 21
```python
def knapsack_tab(weight, value, W, n):
    # Declaration and Init. of T[]:
    T = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Construct T[][] in ascending order
    for i in range(n + 1):  # Take i first items
        for w in range(W + 1):  # Ascending order
            if weight[i - 1] <= w:
                T[i][w] = max(T[i - 1][w], value[i - 1] + T[i - 1][w - weight[i - 1]])
            elif weight[i - 1] > w:  # item not fitting
                T[i][w] = T[i - 1][w]
    return T[n][W]

# Exec: knapsack_tab(weight, profit, W, n)
```
## Knapsack Tab v2
### Slide 24
```python
def knapsack_tab(weight, value, W, n):
    # Declaration and Init. of T[]:
    T = [0 for _ in range(W + 1)]

    # Construct T[] in ascending order
    for i in range(n + 1):  # Take i first items
        for w in range(W, 0, -1):  # Descending order
            if weight[i - 1] <= w:
                T[w] = max(T[w], value[i - 1] + T[w - weight[i - 1]])
    return T[W]

# Exec: knapsack_tab(weight, profit, W, n)
```
## UKP
### Slide 31
```python
def UKP(weight, value, W, index):
    # Base case
    if index == 0:
        return (W // weight[0]) * value[0]

    # Element (index) doesn’t occur even once in solution
    notTake = 0 + UKP(weight, value, W, index - 1)

    # Element occur at least once in solution
    take = -1e06
    if weight[index] <= W:
        take = value[index] + UKP(weight, value, W - weight[index], index)

    return max(take, notTake)
```
## UKP v2
### Slide 33
```python
def UKP_tab(weight, value, W, index):
    # Init array storing max value with w_i
    T = [0 for _ in range(W + 1)]

    # Recursion
    for w in range(W + 1):
        for j in range(index):
            if weight[j] <= w:
                T[w] = max(T[w], T[w - weight[j]] + value[j])

    return T[W]
```
## Knapsack Récursif
### Slide 36
```python
class Knapsack:
    def __init__(self, n):
        self.taille = n
        self.objet = []

        for i in range(self.taille):
            question = 'Volume objet ' + str(i + 1) + ' : '
            self.objet.append(eval(input(question)))

        volumeTotal = eval(input("Volume du sac : "))
        print(self.essai(volumeTotal))

    def essai(self, poids):
        max = 0

        for i in range(self.taille):
            s = poids - self.objet[i]

            if s >= 0:
                t = self.essai(s) + self.objet[i]
                if t > max:
                    max = t
        return max
```
## Knapsack Temp Saves
### Slide 37
```python
class Knapsack:
    def __init__(self, n):
        self.taille = n
        self.maxConnu = {}
        self.objet = []

        for i in range(self.taille):
            question = 'Volume objet ' + str(i + 1) + ' : '
            self.objet.append(eval(input(question)))

        volumeTotal = eval(input("Volume du sac : "))
        print(self.essai(volumeTotal))

    def essai(self, poids):
        max = 0

        if poids in self.maxConnu:
            return self.maxConnu[poids]

        for i in range(self.taille):
            s = poids - self.objet[i]

            if s >= 0:
                t = self.essai(s) + self.objet[i]
                if t > max:
                    max = t
        return self.maxConnu.setdefault(poids, max)
```
## Longest Common Subsequence (implementation Naive)
### Slide 41
```python
def LCS(C1, C2, m, n):
    if m == 0 or n == 0:
        return 0
    elif C1[m-1] == C2[n-1]:
        return 1 + LCS(C1, C2, m-1, n-1)
    elif C1[m-1] != C2[n-1]:
        return max(LCS(C1, C2, m, n-1), LCS(C1, C2, m-1, n))

# Example call
LCS(C1, C2, len(C1), len(C2))
```
## LCS Memo
### Slide 44
```python
# Init 2D-array T[][]
C1, C2 = "...", "..."
T = [[-1 for _ in range(len(C2) + 1)] for _ in range(len(C1) + 1)]

def LCS(C1, C2, m, n, T):
    if m == 0 or n == 0:
        return 0
    if T[m][n] != -1:
        return T[m][n]
    elif C1[m - 1] == C2[n - 1]:
        T[m][n] = 1 + LCS(C1, C2, m - 1, n - 1, T)
        return T[m][n]
    elif C1[m - 1] != C2[n - 1]:
        T[m][n] = max(LCS(C1, C2, m, n - 1, T), LCS(C1, C2, m - 1, n, T))
        return T[m][n]

# Example call
LCS(C1, C2, len(C1), len(C2), T)
```
## LCS Tab
### Slide 46
```Python
LCS : Longest Common Subsequence
def LCS_tab(C1,C2,m,n):

	# Declaration et init. du tableau T
	T = [[None]*(n+1) for _ in range(m+1)]
	# Construction ascendante de T[m][n]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				T[i][j] = 0
			elif C1[i-1] == C2[j-1]:
				T[i][j] = T[i-1][j-1]+1
			elif C1[i-1] != C2[j-1]:
				T[i][j] = max(T[i-1][j],T[i][j-1])
	return T[m][n]
```
## Impression de la LCS
### Slide 48
```python
# Appel LCS_tab : return T, T[m][n]
T, val = LCS_tab(C1, C2, m, n)

# Variable de sauvegarde de la chaine LCS
chain = ""

# Init. parcours de T
i = m
j = n

while i > 0 and j > 0:
    if C1[i - 1] == C2[j - 1]:
        chain += C1[i - 1]
        i -= 1
        j -= 1
    elif T[i - 1][j] > T[i][j - 1]:  # dir. i (valeur la plus grande)
        i -= 1
    elif T[i - 1][j] <= T[i][j - 1]:  # dir. j (valeur la plus grande)
        j -= 1

chain = chain[::-1]
print("LCS de " + C1 + " et " + C2 + " est " + chain)
```
