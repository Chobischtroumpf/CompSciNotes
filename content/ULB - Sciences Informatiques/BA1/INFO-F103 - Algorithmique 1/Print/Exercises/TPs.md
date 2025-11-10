---
title: TPs
authors: Alessandro Dorigo
tags:
  -
---

# Dynamic Programming
## Get Change
```python
def get_change(coins: list, value: int) -> list:
    # dynamic programming table that stores the minimum number of coins needed to make change for each value
    dp = [0] + [float('inf')] * value

    for i in range(1, value + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # if the value is not reachable, return an empty list
    if dp[value] == float('inf'):
        return []

    # reconstruct the coins used to make change
    res = [[0] * len(coins) for _ in range(dp[value])]

    i = value
    j = dp[value] - 1

    while i > 0:
        for k, coin in enumerate(coins):
            if i >= coin and dp[i] == dp[i - coin] + 1:
                res[j][k] += 1
                i -= coin
                break
    return res
```
## Longest Common Subsequence
```python
def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    res = ""

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            res = s1[i - 1] + res
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return res
```
# Sorting
## Quickselect
```python
def quickselect(arr, k):
    def partition(left, right, pivot_index):
        pivot = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        idx = left

        for i in range(left, right):
            if arr[i] < pivot:
                arr[i], arr[idx] = arr[idx], arr[i]
                idx += 1

        arr[right], arr[idx] = arr[idx], arr[right]
        return idx

    def select(left, right, k):
        if left == right:
            return arr[left]

        pivot_idx = partition(left, right, (left + right) // 2)

        if k == pivot_idx:
            return arr[k]
        elif k < pivot_idx:
            return select(left, pivot_idx - 1, k)
        else:
            return select(pivot_idx + 1, right, k)

    return select(0, len(arr) - 1, k)
```
## Quicksort with Key
```python
def quicksort(array, key=lambda x: x):
    def partition(low, high):
        pivot = key(array[high])
        i = low - 1

        for j in range(low, high):
            if key(array[j]) <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(array) - 1)

if __name__ == "__main__":
    data = [3, 6, 8, 10, 1, 2, 1]
    quicksort(data, key=lambda x: x)
    print(data)
```
# Graphs
## Friend Ranking System
```python
from Blueprints.Graph import StaticGraph

class Graph(StaticGraph):
    def __init__(self, V, vertices):
        super().__init__(V)
        self.vertices = vertices

    def ranking(self, d, v):
        visited = [False] * self.V
        visited[v] = True

        queue = [v]

        while d:
            next_queue = []

            for vertex in queue:
                for neighbor, weight in enumerate(self.adj[vertex]):
                    if weight and not visited[neighbor]:
                        visited[neighbor] = True
                        next_queue.append(neighbor)

            queue = next_queue
            d -= 1

        ranking = []

        for vertex in range(self.V):
            if visited[vertex]:
                ranking.append(self.vertices[vertex])

        print(ranking)

if __name__ == "__main__":
    vertices = [
        ("A", 100, [1, 2, 3]),
        ("B", 200, [0, 3, 4]),
        ("C", 300, [4, 7]),
        ("D", 400, [5, 6]),
        ("E", 500, [8, 10]),
        ("F", 600, [7, 9]),
        ("G", 700, [0, 9]),
        ("H", 800, []),
        ("I", 900, [1]),
        ("J", 1000, []),
        ("K", 1100, [])
    ]
    G_adj = [
        #A, B, C, D, E, F, G, H, I, J, K
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    ]

    G = Graph(11, vertices)
    G.adj = G_adj

    G.ranking(2, 0)
    G.ranking(2, 1)
    G.ranking(2, 2)
```
## Shortest Path
```python
from Blueprints.Graph import StaticGraph
from Blueprints.Queue import Queue

from Blueprints.Traversals.DFS import dfs_static
from Blueprints.Traversals.BFS import bfs_static

def shortest_path(G, start, dest):
    dist = [float('inf') for _ in range(G.V)]
    dist[start] = 0

    parent = [-1 for _ in range(G.V)]

    q = Queue()
    q.enqueue(start)

    while q:
        curr = q.dequeue()

        for neighbor, weight in enumerate(G.adj[curr]):
            if weight and dist[neighbor] > dist[curr] + weight:
                dist[neighbor] = dist[curr] + weight
                parent[neighbor] = curr
                q.enqueue(neighbor)

    path = []
    curr = dest

    while curr != -1:
        path.insert(0, curr)
        curr = parent[curr]

    return dist[dest], path
```
# Hashing
## XXHash
```python
def xxhash(t: tuple) -> int:
    L = len(t)

    X = 3527539
    P = 2870177450012600261
    N = 14029467366897019727
    M = 11400714785074694791

    x = P

    for k in t:
        x += (h(k, t) * N) % 2 ** 64
        x = rot_l(x, 31)
        x = (x * M) % 2 ** 64

    return x + (L ^ P ^ X) % 2 ** 64

def rot_l(x: int, n: int) -> int:
    return (x << n) | (x >> (64 - n))

def h(k: int, t: tuple) -> int:
    return k % len(t)
```
# Heaps
## Min-Max Heap
```python
class MinMaxHeap:
    def __init__(self, array):
        self.array = array

    def __len__(self):
        return len(self.array)

    def father(self, i):
        return (i - 1) // 2

    def depth(self, idx):
        ret = 0
        while idx > 0:
            idx = self.father(idx)
            ret += 1
        return ret

    def __str__(self):
        return str(self.array)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def insert(self, e):  # Each level alternates between max / min heaps
        idx = len(self)
        self.array.append(e)
        father_idx = self.father(idx)

        if self.depth(idx) % 2 == 0:    # Even depth: max heap
            if idx > 0 and self.array[idx] > self.array[father_idx]:
                self.swap(idx, father_idx)
                self.swim_max(father_idx)
            else:
                self.swim_min(idx)
        else:                           # Odd depth: min heap
            if idx > 0 and self.array[idx] < self.array[father_idx]:
                self.swap(idx, father_idx)
                self.swim_min(father_idx)
            else:
                self.swim_max(idx)

    def swim_max(self, idx):
        father_idx = self.father(idx)

        while father_idx > 0 and self.array[idx] > self.array[self.father(father_idx)]:
            self.swap(idx, self.father(father_idx))
            idx = self.father(father_idx)
            father_idx = self.father(idx)

    def swim_min(self, idx):
        father_idx = self.father(idx)

        while father_idx > 0 and self.array[idx] < self.array[self.father(father_idx)]:
            self.swap(idx, self.father(father_idx))
            idx = self.father(father_idx)
            father_idx = self.father(idx)
```
# BSTs
## Create BST with x as new root
```python
from Blueprints.Binary_Tree import BinaryTree

def find_x(root, x):
    if root is None:
        return None    elif root.get_root_val() == x:
        return root
    elif x < root.get_root_val():
        return find_x(root.get_left_child(), x)
    else:
        return find_x(root.get_right_child(), x)

def insert_bst(root, val):
    if root is None:
        return BinaryTree(val)
    if val < root.get_root_val():
        root.modify_left(insert_bst(root.get_left_child(), val))
    elif val > root.get_root_val():
        root.modify_right(insert_bst(root.get_right_child(), val))
    return root

def rebuild(root, new_root):
    if root is None:
        return    if root.get_root_val() != new_root.get_root_val():
        insert_bst(new_root, root.get_root_val())

    rebuild(root.get_left_child(), new_root)
    rebuild(root.get_right_child(), new_root)

def create_with_x(root, x):
    new_root = find_x(root, x)
    if not new_root:
        return None

	rebuild(root, new_root)
    return new_root
```
## BSTs Equivalent
```python
from Blueprints.Stack import Stack

def are_equiv(bst1, bst2):
    s1, s2 = Stack(), Stack()
    curr1, curr2 = bst1, bst2

    while (not s1.is_empty() or curr1) and (not s2.is_empty() or curr2):
        while curr1:
            s1.push(curr1)
            curr1 = curr1.get_left_child()
        while curr2:
            s2.push(curr2)
            curr2 = curr2.get_left_child()

        if s1.is_empty() or s2.is_empty():
            return False
        curr1 = s1.pop()
        curr2 = s2.pop()

        if curr1.get_root_val() != curr2.get_root_val():
            return False
        curr1 = curr1.get_right_child()
        curr2 = curr2.get_right_child()

    return not (not s1.is_empty() or curr1 or not s2.is_empty() or curr2)
```
## Is BST
```python
from Blueprints.Stack import Stack

def is_bst_rec(tree, lower=-float('inf'), upper=+float('inf')):
    if not tree:
        return True
    if not (lower <= tree.get_root_val() < upper):
        return False
    return is_bst_rec(tree.get_left_child(), lower, tree.get_root_val()) and is_bst_rec(tree.get_right_child(), tree.get_root_val(), upper)

def is_bst_iter(tree):
    stack = Stack()
    prev = None

    while not stack.is_empty() or tree:
        while tree:
            stack.push(tree)
            tree = tree.get_left_child()
        tree = stack.pop()

        if prev and tree.get_root_val() <= prev.get_root_val():
            return False
        prev = tree
        tree = tree.get_right_child()

    return True
```
# Binary Trees
## Trie
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        node = self.root
        # Iterating through the characters of the key and creating a new node for each character if it doesn't exist
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        # Marking the last node as the end of the key (because it needs to be a word)
        node.is_end = True

    def contains(self, key):
        node = self.root
        # Iterating through the characters of the key and returning False if a character doesn't exist
        for char in key:
            if char not in node.children:
                return False
            node = node.children[char]
        # Returning True if the last node is marked as the end of the key, which means it's the word we're looking for
        return node.is_end

    def delete(self, key):
        self._delete(self.root, key, 0)

    def _delete(self, node, key, index):
        if index == len(key):
            if not node.is_end:
                return False
            node.is_end = False

            return len(node.children) == 0

        char = key[index]

        if char not in node.children:
            return False
        to_delete = self._delete(node.children[char], key, index + 1)

        if to_delete:
            del node.children[char]
            return len(node.children) == 0

        return False

if __name__ == '__main__':
    trie = Trie()

    trie.insert('algo')
    trie.insert('algorithmique')
    trie.insert('algorithm')

    print(trie.contains('algo'))
    print(trie.contains('algorithmique'))
    print(trie.contains('algorithm'))
```
## Mirror Tree
```python
from ARBRE_8_1 import *  #Binary Tree + Father

def mirror(tree):
    if tree is None:
        return None
    new_left = mirror(tree.get_right_child())
    new_right = mirror(tree.get_left_child())

    new_tree = BinaryTree(tree.get_root_val(), new_left, new_right)

    return new_tree

def mirror_father(tree):
    if tree is None:
        return None
    new_tree = BinaryTreeFather(tree.root)

    if tree.get_left_child() is not None:
        new_tree.modify_right(mirror_father(tree.left))
        new_tree.get_right_child().father = new_tree

    if tree.get_right_child() is not None:
        new_tree.modify_left(mirror_father(tree.right))
        new_tree.get_left_child().father = new_tree

    return new_tree
```
## Trees Equal
```python
def are_equal(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None or tree1.get_root_val() != tree2.get_root_val():
        return False
    return are_equal(tree1.get_left_child(), tree2.get_left_child()) and are_equal(tree1.get_right_child(), tree2.get_right_child())
```
## Tree Contains
```python
from Blueprints.Queue import Queue

def contains(tree, value):
    q = Queue()
    q.enqueue(tree)

    def level_search(queue):
        if queue.is_empty():
            return None
        node = queue.dequeue()

        if node is not None:
            if node.get_root_val() == value:
                return node

            queue.enqueue(node.get_left_child())
            queue.enqueue(node.get_right_child())

        return level_search(queue)
    return level_search(q)
```
## Binary Tree + Father
```python
from Blueprints.Binary_Tree import BinaryTree

class BinaryTreeFather(BinaryTree):
    def __init__(self, root, left=None, right=None, father=None):
        super().__init__(root, left, right)
        self._father = father

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, data):
        self._father = data


def first(node):
    return node

def first_any(node):
    while node.father is not None:
        node = node.father
    return node

def next(node):
    if node.get_left_child():
        return node.get_left_child()
    if node.get_right_child():
        return node.get_right_child()

    found = False

    while not found:
        child = node
        node = node.father

        if node is None:
            found = True
        elif child is node.get_left_child() and node.get_right_child():
            node = node.get_right_child()
            found = True

    return node
```

# Backtracking
## BFS Maze
```python
from Blueprints.Deque import Deque

def is_valid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "_"

def valid_moves(x, y, board):
    moves = []

    move_x = [0, 1, 0, -1]
    move_y = [1, 0, -1, 0]

    for i in range(4):
        new_x = x + move_x[i]
        new_y = y + move_y[i]

        if is_valid(new_x, new_y, board):
            moves.append((new_x, new_y))

    return moves

def bfs(board):
    n, m = len(board), len(board[0])

    if n < 1 or m < 1 or board[0][0] == "x" or board[n - 1][m - 1] == "x":
        return False, "Invalid start or end position"

    queue = Deque()
    queue.add_rear((0, 0, 0))
    board[0][0] = "o"

    while not queue.is_empty():
        x, y, dist = queue.remove_front()

        if x == n - 1 and y == m - 1:
            return True, dist + 1

        for new_x, new_y in valid_moves(x, y, board):
            board[new_x][new_y] = "o"
            queue.add_rear((new_x, new_y, dist + 1))

    return False, "Solution does not exist"
```
## Shortest Path (no BFS)
```python
def is_valid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "_"

def valid_moves(x, y, board):
    moves = []

    move_x = [0, 1, 0, -1]
    move_y = [1, 0, -1, 0]

    for i in range(4):
        new_x = x + move_x[i]
        new_y = y + move_y[i]

        if is_valid(new_x, new_y, board):
            moves.append((new_x, new_y))

    return moves

def solve(x, y, board, n, m):
    if x == n - 1 and y == m - 1:
        return True

    for new_x, new_y in valid_moves(x, y, board):
        board[new_x][new_y] = "o"

        if solve(new_x, new_y, board, n, m):
            return True
        board[new_x][new_y] = "_"
    return False

def maze_route(board):
    n, m = len(board), len(board[0])

    if n < 1 or m < 1 or board[0][0] == "x" or board[n - 1][m - 1] == "x":
        return False, "Invalid start or end position"

    board[0][0] = "o"

    if solve(0, 0, board, n, m):
        return True, board
    else:
        return False, "Solution does not exist"
```
## Knight Route
```python
def is_valid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == -1

def valid_moves(x, y, board):
    moves = []

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        new_x = x + move_x[i]
        new_y = y + move_y[i]

        if is_valid(new_x, new_y, board):
            moves.append((new_x, new_y))

    return moves

def solve(x, y, move_i, board, n, m, end_cell):
    if move_i == n * m:
        return x == end_cell[0] and y == end_cell[1]

    for new_x, new_y in valid_moves(x, y, board):
        board[new_x][new_y] = move_i

        if solve(new_x, new_y, move_i + 1, board, n, m, end_cell):
            return True
        board[new_x][new_y] = -1
    return False

def knight_route(n, m, end_cell):
    if n < 1 or m < 1:
        return False, "Board is too small"

    board = [[-1 for _ in range(m)] for _ in range(n)]
    board[0][0] = 0  # Start position

    if solve(0, 0, 1, board, n, m, end_cell):
        return True, board
    else:
        return False, "Solution does not exist"
```
## Linear Equation Solver
```python
def sol_eq_lin_rec(a, y, b, n, sol):
    # Base case: if solution's length equals n, check if the dot product of a and sol equals y
    if len(sol) == n:
        if sum(a[i] * sol[i] for i in range(n)) == y:
            print(sol)  # Print solution if it solves the equation
        return

    # Recursive step: try adding each possible value of x (from 0 to b) to the solution
    for x in range(b + 1):
        sol_eq_lin_rec(a, y, b, n, sol + [x])  # add each x from 0 to b

def sol_eq_lin_iter(a, y, b, n):
    sol = [0] * n  # Initialize solution with all coefficients set to 0

    while True:
        # Check if the current combination of coefficients solves the equation
        if sum(a[i] * sol[i] for i in range(n)) == y:
            print(sol)

        # Increment coefficients to generate the next combination
        for i in range(n):
            sol[i] += 1  # Increment coefficient at position i

            if sol[i] > b:  # If coefficient exceeds the bound, reset it
                sol[i] = 0

                if i == n - 1:  # If all coefficients have been reset, terminate
                    return
            else:
	            break  # New combination
```
## N subsets of size K
```python
def generate_subsets_size(k, n):
    if k > n:
        return []

    temp = []
    result = []

    def helper(start, current_size):
        # Only add to result when the current size of temp matches k
        if current_size == k:
            result.append(tuple(temp))
            return

        for i in range(start, n + 1):
            temp.append(i)
            helper(i + 1, current_size + 1)
            temp.pop()

    helper(1, 0)
    return [list(subset) for subset in result]
```
## Generate Subsets
```python
def generate_subsets(arr):
    temp = []
    result = set()

    def helper(idx):
        if idx == len(arr):
            # if 0 < len(temp) < len(arr):  removes empty and the initial arr
            result.add(tuple(temp))
            return
        else:            # Include the current element
            temp.append(arr[idx])
            helper(idx + 1)

            # Exclude the current element (backtrack)
            temp.pop()
            helper(idx + 1)

    helper(0)
    return [list(subset) for subset in result]
```
# Recursive
## AGM
```python
def recursive_agm(x, y, eps):
    def helper(a_n, g_n, eps):
        if abs(a_n - g_n) < eps:
            return (a_n + g_n) / 2
        else:
            return helper((a_n + g_n) / 2, (a_n * g_n) ** 0.5, eps)

    return helper(x, y, eps)

def agm(x, y, eps):
    a_n, g_n = x, y

    while abs(a_n - g_n) >= eps:
        a_n, g_n = (a_n + g_n) / 2, (a_n * g_n) ** 0.5

    return (a_n + g_n) / 2
```
## Hanoi
```python
from Blueprints.Stack import Stack

def hanoi(n: int):
    tower_a = Stack()
    tower_b = Stack()
    tower_c = Stack()

    for i in range(n, 0, -1):
        tower_a.push(i)

    def helper(n: int,
               source: Stack, auxiliary: Stack, destination: Stack,
               s: str, a: str, d: str):
        # If only one disk, move from source to dest
        if n == 1:
            destination.push(source.pop())
            print(f"Déplacer un disque de {s} à {d}")
            return
        # Move n - 1 disks from source to aux (B), using dest as temp storage
        helper(n - 1, source, destination, auxiliary, s, d, a)
        # Move nth disk from source to dest
        destination.push(source.pop())
        print(f"Déplacer un disque de {s} à {d}")
        # Move n - 1 disks from aux to dest, using source as temp storage
        helper(n - 1, auxiliary, source, destination, a, s, d)

    helper(n, tower_a, tower_b, tower_c, 'A', 'B', 'C')
```
## Strassen Determinant
```python
def split(matrix):
    row = len(matrix)
    col = len(matrix[0]) if matrix else 0
    row2, col2 = row // 2, col // 2

    return [
        [row[:col2] for row in matrix[:row2]],
        [row[col2:] for row in matrix[:row2]],
        [row[:col2] for row in matrix[row2:]],
        [row[col2:] for row in matrix[row2:]]
    ]

def add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def sub_matrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def strassen(a, b):
    if len(a) == 1:
        return [[a[0][0] * b[0][0]]]

    a1, a2, a3, a4 = split(a)
    b1, b2, b3, b4 = split(b)

    m1 = strassen(add_matrix(a1, a4), add_matrix(b1, b4))
    m2 = strassen(add_matrix(a3, a4), b1)
    m3 = strassen(a1, sub_matrix(b2, b4))
    m4 = strassen(a4, sub_matrix(b3, b1))
    m5 = strassen(add_matrix(a1, a2), b4)
    m6 = strassen(sub_matrix(a1, a3), add_matrix(b1, b2))
    m7 = strassen(sub_matrix(a2, a4), add_matrix(b3, b4))

    c11 = sub_matrix(add_matrix(m1, m4), add_matrix(m5, m7))
    c12 = add_matrix(m3, m5)
    c21 = add_matrix(m2, m4)
    c22 = add_matrix(sub_matrix(m1, m2), add_matrix(m3, m6))

    top = [c11[i] + c12[i] for i in range(len(c11))]
    bottom = [c21[i] + c22[i] for i in range(len(c21))]

    return top + bottom
```
# Stacks
## Balanced Paranthesis
```python
from Blueprints.Stack import Stack

def is_open(char: str, tokens: list) -> bool:
    for array in tokens:
        if array[0] == char:
            return True
	return False

def matches(open: str, close: str, tokens: list) -> bool:
    for array in tokens:
        if array[0] == open:
            return array[1] == close
    return False

def is_balanced() -> bool:
    tokens = [['(', ')'], ['[', ']'], ['{', '}']]
    stack = Stack()

    while True:
        c = input("Enter char (or '#' to end input): ")
        if c == '#':
            break
        if is_open(c, tokens):
            stack.push(c)
        else:
            if stack.is_empty() or not matches(stack.pop(), c, tokens):
                return False
    return stack.is_empty()
```
## Min Stack
```python
from Blueprints.Stack import Stack

class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, item):
        self.stack.push(item)

        if self.min_stack.is_empty() or item <= self.min_stack.peek():
            self.min_stack.push(item)

    def pop(self):
        elem = self.stack.pop()

        if elem == self.min_stack.peek():
            self.min_stack.pop()

        return elem

    @property
    def peek(self):
        return self.stack.peek() if not self.stack.is_empty() else None

    @property
    def get_min(self):
        return self.min_stack.peek() if not self.min_stack.is_empty() else None
```
## Max Decreasing Subsequence Sum
```python
from Blueprints.Stack import Stack

def max_decreasing_subsequence_sum():
    stack = Stack()
    number = int(input("Enter number (or '-1' to end input): "))
    max_sum = 0

    while number != -1:
        while not stack.is_empty() and stack.peek() < number:
            stack.pop()

        stack.push(number)
        max_sum = max(max_sum, sum(stack.items))

    return max_sum, stack
```
## Reverse Stack
```python
from Blueprints.Stack import Stack

def reverse_stack(stack: Stack):
    n = len(stack)
    temp = Stack()

    for i in range(n, 1, -1):
        item = stack.pop()

        for j in range(1, i):
            temp.push(stack.pop())
        stack.push(item)

        for j in range(1, i):
            stack.push(temp.pop())
```
