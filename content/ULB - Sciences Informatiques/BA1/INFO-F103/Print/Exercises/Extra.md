---
title: Extra
authors: Alessandro Dorigo
tags:
  -
---

# Data Structures
## Hash Table
```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.deleted = object()  # A marker for deleted elements

    def h1(self, key):
        # K&R hash function
        val = 0

        for char in key:
            val = (val * 31 + ord(char)) % self.size
        return val

    def h2(self, key):
        # DJB2 hash function
        val = 5381

        for char in key:
            val = (val * 33 + ord(char)) % self.size
        return val

    def h(self, key, j):
        return (self.h1(key) + j * self.h2(key)) % self.size

    def insert(self, key, value):
        for i in range(self.size):
            hash_idx = self.h(key, i)

            if self.table[hash_idx] is None or self.table[hash_idx] is self.deleted:
                self.table[hash_idx] = (key, value)
                return
        raise Exception("Hash table is full")

    def search(self, key):
        for i in range(self.size):
            hash_idx = self.h(key, i)

            if self.table[hash_idx] is None:
                return None
			if self.table[hash_idx] is not self.deleted and self.table[hash_idx][0] == key:
                return self.table[hash_idx][1]
        return None

    def delete(self, key):
        for i in range(self.size):
            hash_idx = self.h(key, i)

            if self.table[hash_idx] is None:
                return

            if self.table[hash_idx] is not self.deleted and self.table[hash_idx][0] == key:
                self.table[hash_idx] = self.deleted
                return
```
## List
```python
class List:
    def __init__(self):
        self._data = empty_list(1)
        self._count = 0
        self._capacity = 1

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, n):
        self.count = n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        self.capacity = n

    def __str__(self):
        return "[" + ", ".join(str(self._data[i]) for i in range(self.count)) + "]"

    def __len__(self):
        return self.count

    def __iter__(self):
        for i in range(self.count):
            yield self._data[i]

    def __getitem__(self, index):
        if index < 0:
            index += self.count

        if 0 <= index < self.count:
            return self._data[index]

        raise IndexError('Index out of range')

    def __setitem__(self, index, value):
        if index < 0:
            index += self.count

        if 0 <= index < self.count:
            self._data[index] = value
        else:
            raise IndexError('Index out of range')

    def __delitem__(self, index):
        if index < 0:
            index += self.count

        if 0 <= index < self.count:
            for i in range(index, self.count - 1):
                self._data[i] = self._data[i + 1]

            self._data[self.count - 1] = None
            self.count -= 1
        else:
            raise IndexError('Index out of range')

    def __contains__(self, item):
        for i in range(self.count):
            if self._data[i] == item:
                return True
        return False
    def __eq__(self, other):
        if isinstance(other, List) and self.count == other.count:
            for i in range(self.count):
                if self._data[i] != other._data[i]:
                    return False
            return True
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def _resize(self, new_capacity):
        new_data = empty_list(new_capacity)

        for i in range(self.count):
            new_data[i] = self._data[i]

        self._data = new_data
        self.capacity = new_capacity

    def append(self, item):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        self._data[self._count] = item
        self.count += 1

    def insert(self, index, item):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)

        if index < 0:
            index += self.count

        if 0 <= index <= self.count:
            for i in range(self.count, index, -1):
                self._data[i] = self._data[i - 1]

            self._data[index] = item
            self.count += 1
        else:
            raise IndexError('Index out of range')

    def pop(self, index=-1):
        if index < 0:
            index += self.count

        if 0 <= index < self.count:
            item = self._data[index]
            self.__delitem__(index)
            return item

        raise IndexError('Index out of range')

def empty_list(n):
    return [None] * n
```
# Lists
## Special Array (x values are >= x)
```python
def specialArray(nums: List[int]) -> int:
	nums.sort()
	n = len(nums)

	# Check potential x from 0 to n
	for x in range(n + 1):
		# Find the first index where nums[index] >= x
		low, high = 0, n

		while low < high:
			mid = (low + high) // 2

			if nums[mid] >= x:
				high = mid
			else:
				low = mid + 1
		# Check if the remaining elements are exactly x
		if n - low == x:
			return x
	return -1
```
# Stacks
## Infix to Postfix
```python
from Blueprints.Stack import Stack

def infix_to_postfix(str: str) -> str:
	weight = {'+': 1, '-': 1, '*': 2, '/': 2}
    op_stack = Stack()
    output = []
    chars = str.split()

    for c in chars:
        if c.isalpha() or c.isdigit():
            output.append(c)
        elif c == '(':
            op_stack.push(c)
        elif c == ')':
            while not op_stack.is_empty() and op_stack.peek() != '(':
                output.append(op_stack.pop())
            op_stack.pop()
        else:
            while not op_stack.is_empty() and weight.get(op_stack.peek(), 0) >= weight[c]:
                output.append(op_stack.pop())
            op_stack.push(c)

    while not op_stack.is_empty():
        output.append(op_stack.pop())

    return ' '.join(output)

def postfix_eval(str: str) -> (int, float):
    operand_stack = Stack()
    chars = str.split()

    for c in chars:
        if c.isalpha():
            raise NotImplemented
        if c.isdigit():
            operand_stack.push(int(c))
        else:
            b, a = operand_stack.pop(), operand_stack.pop()
            operand_stack.push(math(c, a, b))
    return operand_stack.pop()

def math(op: str, a: int, b: int) -> (int, float):
    if op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "+":
        return a + b
    else:
        return a - b
```
# Queues
## Hot Potato
```python
from Blueprints.Queue import Queue

def hot_potato(list, n: int) -> str:
    people_queue = Queue()

    for i in list:
        people_queue.enqueue(i)

    while people_queue.size() > 1:
        for i in range(n):
            people_queue.enqueue(people_queue.dequeue())
        people_queue.dequeue()

    return people_queue.dequeue()
```

## Printer
```python
import random
from Blueprints.Queue import Queue

class Printer:
    def __init__(self, ppm: int):
        self.rate = ppm
        self.task = None
        self.time = 0

    def tick(self):
        if self.task is not None:
            self.time -= 1
            if self.time <= 0:
                self.task = None

    def busy(self) -> bool:
        if self.task is not None:
            return True
		else:
			return False

    def start_next(self, new: 'Task'):
        self.task = new
        self.time = new.pages * 60 / self.rate

class Task:
	def __init__(self, time: int):
        self._timestamp = time
        self._pages = random.randrange(1, 21)

    @property
    def timestamp(self) -> int:
        return self._timestamp

    @property
    def pages(self) -> int:
        return self._pages

    def wait_time(self, current_time: int) -> int:
        return current_time - self.timestamp

def simulation(seconds: int, ppm: int):
    printer = Printer(ppm)
    print_queue = Queue()
    waiting_times = []

    for curr in range(seconds):
        if new_task():
            task = Task(curr)
            print_queue.enqueue(task)

        if (not printer.busy()) and (not print_queue.is_empty()):
            next = print_queue.dequeue()
            waiting_times.append(next.wait_time(curr))
            printer.start_next(next)

        printer.tick()

    average = sum(waiting_times) / len(waiting_times)
    print("Average Wait: %6.2f secs, %3d tasks remaining." % (average, print_queue.size()))

def new_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
	else:
		return False

for i in range(10):
    simulation(3600, 5)
```
# Heaps
## Taxicab
```python
class Heap:
    def __init__(self, key=lambda x, y: x > y):
        self.heapList = []
        self.size = 0
        self.key = key

    def parent(self, index):
        return (index - 1) // 2

    def leftChild(self, index):
        return (index * 2) + 1

    def rightChild(self, index):
        return (index * 2) + 2

    def exists(self, index):
        return index < self.size

    def swap(self, index1, index2):
        self.heapList[index1], self.heapList[index2] = self.heapList[index2], self.heapList[index1]

    def priorityUp(self, index):
        while index > 0 and self.key(self.heapList[index], self.heapList[self.parent(index)]):
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def priorityChild(self, index):
        if not self.exists(self.leftChild(index)):
            return -1
        elif not self.exists(self.rightChild(index)):
            return self.leftChild(index)
        else:
            if self.key(self.heapList[self.leftChild(index)], self.heapList[self.rightChild(index)]):
                return self.leftChild(index)
            else:
                return self.rightChild(index)

    def priorityDown(self, index):
        while self.exists(self.leftChild(index)):
            mc = self.priorityChild(index)

            if mc == -1 or not self.key(self.heapList[mc], self.heapList[index]):
	            break

            self.swap(index, mc)
            index = mc

    def insert(self, item):
        self.heapList.append(item)
        self.size += 1
        self.priorityUp(self.size - 1)

    def delete(self):
        if self.size == 0:
            return None

        retval = self.heapList[0]
        self.heapList[0] = self.heapList[self.size - 1]
        self.size -= 1
        self.heapList.pop()
        self.priorityDown(0)
        return retval

def taxicab(k, N):
    limit = int(N ** (1/3)) + 1
    sums = dict()
    h = Heap(lambda x, y: x[0] < y[0])  # Min-heap based on cube sum

    for a in range(1, limit):
        for b in range(a, limit):
            cubes = a ** 3 + b ** 3

            if cubes <= N:
                if cubes not in sums:
                    sums[cubes] = []
                sums[cubes].append((a, b))
            if cubes > N:
                break

    for cubes, pairs in sums.items():
        if len(pairs) >= k:
            h.insert((cubes, pairs))

    while h.size > 0:
        smallest = h.delete()
        print(f"Sum: {smallest[0]}, Pairs: {smallest[1]}")
```
## Take Gifts From the Richest Pile
```python
def pickGifts(gifts: List[int], k: int) -> int:
    # idea is to convert the gifts array to a max heap, pop k times, square root the values popped
    # add the new values to a new heap
    # repeat until done
    heap = [-x for x in gifts]
    heapq.heapify(heap)

    for i in range(k):
        val = heapq.heappop(heap)
        val = -val
        val = int(val ** 0.5)
        heapq.heappush(heap, -val)

    return -sum(heap)
```
## Delete Greatest Value in Each Row
```python
def deleteGreatestValue(grid: List[List[int]]) -> int:
    # given an m*n matrix, delete the greatest value in each row, and return the sum of the greatest values taken
    # the logic would be to make a heap of each row, and pop the greatest value from each row
    # then sum the greatest values taken
    temp = []
    res = 0

    while any(grid):
        for row in grid:
            heap = []

            for val in row:
                heapq.heappush(heap, -val)

            temp.append(-heapq.heappop(heap))

            if temp[-1] in row:
                row.remove(temp[-1])

        res += max(temp)
        temp = []

    return res
```
## Furthest Building
```python
def furthestBuilding(heights, bricks, ladders):
    heap = []

    for i in range(len(heights) - 1):
	    if heights[i + 1] <= heights[i]:
		    continue

        diff = heights[i + 1] - heights[i]

        if diff > 0:
	        heapq.heappush(heap, diff)

            if len(heap) > ladders:
	            bricks -= heapq.heappop(heap)
			if bricks < 0:
				return i

    return len(heights) - 1
```
## Pythagorean Triples
```python
from Blueprints.Heap import MinHeap

def alpha(a, b, c):
    return a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c

def beta(a, b, c):
    return 2 * a + b + 2 * c, a + 2 * b + 2 * c, 2 * a + 2 * b + 3 * c

def gamma(a, b, c):
    return -2 * a + b + 2 * c, -a + 2 * b + 2 * c, -2 * a + 2 * b + 3 * c

def triples(n):
    root = (3, 4, 5)

    heap = MinHeap()
    heap.insert(root)

    seen = set()
    seen.add(root)

    while heap.array:
        triplet = heap.delete()

        if triplet[2] > n:
            continue
		yield triplet

        for f in (alpha, beta, gamma):
            new = f(*triplet)

            if new not in seen and new[2] <= n:
                seen.add(new)
                heap.insert(new)
    return
```
# Trees
## Sorted List to Balanced BST
```python
def middle(head):
	slow = head
	fast = head
	prev = None

	while fast and fast.next:
		prev = slow
		slow = slow.next
		fast = fast.next.next
	if prev:
		prev.next = None
	return slow

def sortedListToBST(head: ListNode) -> TreeNode:
	if not head:
		return None
	mid = middle(head)
	root = TreeNode(mid.val)

	if head == mid:
		return root

	root.left = sortedListToBST(head)
	root.right = sortedListToBST(mid.next)

	return root
```
## N-Tree Preorder/Postorder + Iter/Recursive
```python
def ppr(tree: list):
    if not tree:
        return

	print(tree[0])

    for child in tree[1:]:
        ppr(child)

def psr(tree: list):
    if not tree:
        return

	for child in tree[1:]:
        psr(child)

    print(tree[0])

def ppi(tree: list):
    if not tree:
        return

	stack = [tree]

    while stack:
        current = stack.pop()
        print(current[0])
        stack.extend(reversed(current[1:]))

def psi(tree: list):
    if not tree:
        return

	stack = [tree]
    done = []

    while stack:
        current = stack[-1]

        if current in done:
            stack.pop()
            print(current[0])
        else:
            done.append(current)
            for child in reversed(current[1:]):
                stack.append(child)
```
## Remove Duplicates from BST
```python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)

def inorder(tree, res):
    if tree:
        inorder(tree.left, res)
        res.append(tree.val)
        inorder(tree.right, res)

def remove_duplicates(tree: BinaryTree) -> BinaryTree:
    values = []
    inorder(tree.root, values)

    unique_values = list(set(values))
    unique_values.sort()

    new_tree = BinaryTree()
    for value in unique_values:
        new_tree.insert(value)

    return new_tree
```
## Reverse Path in BST
```python
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reverse_path(root, data):
    # Trouver le chemin et collecter les valeurs
    path = []
    curr = root

    while curr is not None:
        path.append(curr)
        if data < curr.value:
            curr = curr.left
        elif data > curr.value:
            curr = curr.right
        else:
            break
    # Inverser les valeurs le long du chemin
    values = [node.value for node in path]
    values.reverse()

    # Réaffecter les valeurs inversées aux nœuds sur le chemin
    for i, node in enumerate(path):
        node.value = values[i]
```
# Sorts
## Mergesort Linked Lists w/out Duplicates
```python
class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

def mergesort_ll(head: Node) -> Node:
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    # Split the list into two halves
    middle.next = None

    left = mergesort_ll(head)
    right = mergesort_ll(next_to_middle)

    sorted_list = merge(left, right)
    return sorted_list

def get_middle(head: Node) -> Node:
    if head is None:
        return head

    slow = head
    fast = head.next

    while fast is not None:
        fast = fast.next
        if fast is not None:
            slow = slow.next
            fast = fast.next

    return slow

def merge(left: Node, right: Node) -> Node:
    if left is None:
        return right
    if right is None:
        return left

    if left.key < right.key:
        result = left
        result.next = merge(left.next, right)
    elif left.key > right.key:
        result = right
        result.next = merge(left, right.next)
    else:
        # Skip the duplicate
        result = left
        result.next = merge(left.next, right.next)

    return result
```
# Recursive
## Get Subtree with Given Sum
```python
class Node:
    def __init__(self, weight: int, *children: 'Node'):
        self.weight = weight
        self.children = list(children)

    def add_node(self, node: 'Node'):
        self.children.append(node)

def get_subtree(root: 'Node', x: int) -> Node | None:
    if root is None:
        return None

    def helper(node: 'Node', current_sum: int, target_sum: int) -> Node | None:
        if node is None:
            return None

        current_sum += node.weight
        new_node = Node(node.weight)

        for child in node.children:
            sub_node = helper(child, current_sum, target_sum)

            if sub_node is not None:
                new_node.add_node(sub_node)

        if current_sum == target_sum or new_node.children:
            return new_node
        else:
            return None

    return helper(root, 0, x)
```
## Longest Sequence
```python
def longest_sequence(n: int):
    # if '0' not in s
    # return 0 cause no distance
    # else separate each '1'
    # get max of lengths
    binary_str = bin(n)[2:]

    def helper(s: str):
        if '0' not in s:
            return 0
        else:
            zeros = s.split('1')
            lengths = [len(z) for z in zeros]
            return max(lengths)

    return helper(binary_str)
```
# Backtracking
## Eccentricity
```python
def excentricite(v, G):
    from collections import deque

    # BFS pour calculer la distance de v à tous les autres sommets
    queue = deque([v])
    distances = {v: 0}

    while queue:
        current = queue.popleft()

        for neighbor in G.neighbors[current].edges:
            if neighbor.dest not in distances:
                queue.append(neighbor.dest)
                distances[neighbor.dest] = distances[current] + neighbor.weight  # Utiliser le poids ici, bien que ce soit toujours 1

    # L'excentricité de v est la plus grande valeur dans distances
    return max(distances.values())

def rayon(G):
    excentricites = {i: excentricite(i, G) for i in range(G.n)}
    return min(excentricites.values())
```
### Complexité du calcul du rayon
La complexité de calculer l'excentricité d'un sommet à l'aide de BFS est $O(V + E)$, où $V$ est le nombre de sommets et $E$ est le nombre d'arêtes dans le graphe, car chaque sommet et chaque arête est explorée une fois. Pour calculer le rayon, nous devons calculer l'excentricité de chaque sommet, ce qui nécessite un BFS pour chaque sommet.

Ainsi, la complexité totale pour calculer le rayon est $O(V \times (V + E))$. Cela peut être potentiellement coûteux pour de grands graphes, mais c'est la méthode directe sans optimisations supplémentaires.
## New Hope (color graph)
```python
class NouvelEspoir:
    def __init__(self, G, k):
        self.G = G
        self.k = k
        self.coloring = [-1] * G.n  # -1 indicates that the planet is yet unassigned

    def save_galaxy(self):
        if self.color_graph(0):
            return self.coloring
        else:
            return "No solution found, galaxy not saved :("

    def color_graph(self, node):
        if node == self.G.n:
            return True  # All nodes colored successfully

        for color in range(1, self.k + 1):
            if self.is_valid_color(node, color):
                self.coloring[node] = color

                if self.color_graph(node + 1):
                    return True
				self.coloring[node] = -1  # Backtrack

        return False

    def is_valid_color(self, node, color):
        for neighbor in self.G.neighbors[node].edges:
            if self.coloring[neighbor.dest] == color:
                return False
		return True
```
## All Paths from Source Target
```python
def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    def dfs(node, path):
        path.append(node)
        # If the current node is the last node in the graph
        if node == len(graph) - 1:
            res.append(path.copy())
        else:
            # Recur for all the nodes that can be visited from the current node
            for neighbor in graph[node]:
                dfs(neighbor, path)
        path.pop()

    res = []
    dfs(0, [])
    return res
```
## Number of Queens
```python
def n_queens(n):
    res = []
    solve(n, 0, [], res)
    return res

def is_valid(col_placements):
    row_id = len(col_placements) - 1

    for i in range(row_id):
        diff = abs(col_placements[i] - col_placements[row_id])

        if diff == 0 or diff == row_id - i:
            return False
    return True

def solve(n, row, col_placements, res):
    if row == n:
        res.append(col_placements.copy())
    else:
        for col in range(n):
            col_placements.append(col)

            if is_valid(col_placements):
                solve(n, row + 1, col_placements, res)

            col_placements.pop()
```
## N Queens Problem
```python
def solveNQueens(n):
	res = []
	self.solve(n, 0, [], res)
	return res

def is_valid(col_placements):
	row_id = len(col_placements) - 1

	for i in range(row_id):
		diff = abs(col_placements[i] - col_placements[row_id])

		if diff == 0 or diff == row_id - i:
			return False
	return True

def solve(self, n, row, col_placements, res):
	if row == n:
		board = self.create_board(col_placements)
		res.append(board)
	else:
		for col in range(n):
			col_placements.append(col)

			if self.is_valid(col_placements):
				self.solve(n, row + 1, col_placements, res)

			col_placements.pop()

def create_board(self, col_placements):
	n = len(col_placements)
	board = []

	for i in range(n):
		row = ["."] * n
		row[col_placements[i]] = "Q"
		board.append("".join(row))

	return board
```
## Tour (traveler problem)
```python
class Graph:
    def __init__(self, n: int):
        ...
    def voisins_de(self, v: int) -> list[int]:
        # retourne la liste des indices des sommets reliés à v
        ...

    def nombre_de_fans_dans(self, v: int) -> int:
        # retourne le nombre de fans dans v
        ...

    def cout_concert_dans(self, v: int) -> int:
        # retourne le cout de l’organisation d’un concert dans v
        ...

    def cout_trajet_entre(self, v: int, w: int) -> int:
        # retourne le cout du trajet entre v et w
        ...

    def __len__(self) -> int:
        # retourne le nombre de sommets du graphe
        ...

class Tournee:
    def __init__(self, G, depart, longueur_tournee, budget):
        self.G = G
        self.depart = depart
        self.longueur_tournee = longueur_tournee
        self.budget = budget
        self.best_fans = 0
        self.best_itineraire = []
        self.best_cost = 0

    def dfs(self, v, days, budget, fans, path):
        if days == self.longueur_tournee:
            if v == self.depart and fans > self.best_fans:
                self.best_fans = fans
                self.best_itineraire = path[:]
                self.best_cost = self.budget - budget
            return

        for w in self.G.voisins_de(v):
            travel_cost = self.G.cout_trajet_entre(v, w)
            concert_cost = self.G.cout_concert_dans(w)
            total_cost = travel_cost + (concert_cost if w not in path else 0)

            if budget >= total_cost and (w not in path or w == self.depart):
                path.append(w)
                self.dfs(w, days + 1, budget - total_cost, fans + (self.G.nombre_de_fans_dans(w) if w not in path else 0), path)
                path.pop()

    def trouver_itineraire(self):
        self.dfs(self.depart, 0, self.budget, 0, [self.depart])
        return self.best_itineraire, self.best_fans, self.best_cost, self.longueur_tournee
```
## Distance Matrix
```python
class Arete:
    def __init__(self, poids, destination):
        self.poids = poids
        self.destination = destination

class Sommet:
    def __init__(self, idx, areteParent = None):
        self.idx = idx
        self.areteParent = areteParent
        self.aretesEnfants= []

def distances_sommets(racine, n):
    M = [[float('inf')] * n for _ in range(n)]

    def dfs(noeud, parent, poids):
        for arete in noeud.aretesEnfants:
            enfant = arete.destination

            if enfant == parent:
                continue

			poids_enfant = poids + arete.poids
            M[noeud.idx][enfant.idx] = poids_enfant
            M[enfant.idx][noeud.idx] = poids_enfant
            dfs(enfant, noeud, poids_enfant)

    # Start DFS from the root
    dfs(racine, None, 0)

    # Set distance from each node to itself as 0
    for i in range(n):
        M[i][i] = 0

    return M
```
## Maze 2.0 (A* + Constraints + Shortest Path)
```python
from Blueprints.Heap import MinHeap

def is_near_mine(x, y, board):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == "x":
            return True
	return False

def is_valid(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == "_" and not is_near_mine(x, y, board)

def find_start_end_points(board):
    start_points = [(x, 0) for x in range(len(board)) if is_valid(x, 0, board)]
    end_points = [(x, len(board[0]) - 1) for x in range(len(board)) if is_valid(x, len(board[0]) - 1, board)]
    return start_points, end_points

def manhattan_distance(x, y, goals):
    return min(abs(x - gx) + abs(y - gy) for gx, gy in goals)

def a_star_search(board, start, valid_ends):
    queue = MinHeap([(0 + manhattan_distance(start[0], start[1], valid_ends), 0, start[0], start[1])])
    visited = {start}
    parent = {start: None}

    while queue.array:
        _, dist, x, y = queue.delete()

        if (x, y) in valid_ends:
            path = []

            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]

            path.append(start)
            path.reverse()
            return dist, path

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if (nx, ny) not in visited and is_valid(nx, ny, board):
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.insert((dist + 1 + manhattan_distance(nx, ny, valid_ends), dist + 1, nx, ny))

    return float('inf'), []

def print_solution(board):
    for row in board:
        print(" ".join(str(cell).rjust(2, ' ') for cell in row))

if __name__ == "__main__":
    import random

    def generate_large_board(size, mine_probability=0.13):
        board = []
        for _ in range(size):
            row = ['x' if random.random() < mine_probability else '_' for _ in range(size)]
            board.append(row)
        return board

    size = 20
    board = generate_large_board(size)
    start_points, end_points = find_start_end_points(board)
    end_set = set(end_points)
    shortest_path = float('inf')
    best_path = []

    for start in start_points:
        dist, path = a_star_search(board, start, end_set)

        if dist < shortest_path:
            shortest_path = dist
            best_path = path

    if best_path:
        for x, y in best_path:
            board[x][y] = 'o'
        print(f"Shortest path length is {shortest_path} steps")
        print_solution(board)
    else:
        print("No solution found")
```
## Optimal BST
```python
import numpy as np

def optimal_bst(keys, freq):
    n = len(keys)
    cost = np.zeros((n, n))
    root = np.zeros((n, n))

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                c = 0

                if r > i:
                    c += cost[i][r - 1]
                if r < j:
                    c += cost[r + 1][j]

                c += sum(freq[i:j + 1])

                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r
    return cost, root

def construct(root, keys, start, end, parent, bool):
    if start > end:
        if bool:
            print(f"NULL <- {keys[parent]}")
        else:
            print(f"{keys[parent]} -> NULL")
        return

    node = int(root[start][end])

    if parent == -1:
        print(f"Root: {keys[node]}")
    elif bool:
        print(f"{keys[node]} <- {keys[parent]}")
    else:
        print(f"{keys[parent]} -> {keys[node]}")

    construct(root, keys, start, node - 1, node, True)
    construct(root, keys, node + 1, end, node, False)

if __name__ == '__main__':
    keys = [1, 2, 3, 4]
    values = [10, 20, 30, 40]
    freq = [2, 9, 3, 7]

    cost, root = optimal_bst(keys, freq)
    print(f"The optimal BST cost is: {int(cost[0][len(keys) - 1])}\n")
    construct(root, values, 0, len(keys) - 1, -1, True)
```
# Dynamic Programming
## Max Profit (greedy - 1 day)
```python
def maxProfit(self, prices: List[int]) -> int:
    dp = float('inf')
    profit = 0

    for price in prices:
        # Update the minimum price so far if a lower price is found
        if price < dp:
            dp = price

        # Calculate potential profit
        curr = price - dp

        # Modify if better profit is found
        if curr > profit:
            profit = curr

    return profit
```
## Max Profit (top-down - i days)
```python
def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)
    dp = [0] * n
    # max_diff tracks the maximum of dp[j - 1] - prices[j] seen so far; initialized with the first day
    max_diff = -prices[0]

    for i in range(1, n):
        # Calculate maximum profit for day i by either not selling (dp[i - 1]) or selling on day i
        # prices[i] + max_diff effectively means considering selling on day i where max_diff incorporates
        # the maximum profitable buy price from previous days
        dp[i] = max(dp[i - 1], prices[i] + max_diff)
        # Update max_diff to include the current day's buy potential
        # dp[i - 1] - prices[i] calculates the potential profit if buying on day i and selling later
        max_diff = max(max_diff, dp[i - 1] - prices[i])

    # The last element in dp array will have the maximum profit achievable with the given stock prices
    return dp[n - 1]
```
## All Possible Full Binary Trees
```python
def allPossibleFBT(n: int) -> List[Optional[TreeNode]]:
    def count(n, dp={}):
        if n in dp:
            return dp[n]
        # Base case: the only full binary tree with 1 node is a single root node with no children
        if n == 1:
            return [TreeNode(0)]
        # A full binary tree cannot have an even number of nodes !!!
        if n % 2 == 0:
            return []

        res = []
        # Iterate through all odd numbers less than n to split the nodes
        # between the left and right subtrees
        for x in range(1, n, 2):
            left_trees = count(x, dp)  # Recursively find all possible left subtrees with x nodes
            right_trees = count(n - 1 - x, dp)  # Recursively find all possible right subtrees with n - 1 - x nodes

            # Combine each pair of left and right trees to form a full binary tree            # and append to the result list
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(0)  # New root for each combination
                    root.left = left
                    root.right = right
                    res.append(root)
        # Memoize the result for n nodes
        dp[n] = res
        return res
    return count(n, {})
```
