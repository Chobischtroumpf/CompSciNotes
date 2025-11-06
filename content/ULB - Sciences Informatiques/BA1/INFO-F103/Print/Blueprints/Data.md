---
title: Data
authors: Alessandro Dorigo
tags:
  -
---

# Data Types
## Node
```python
class Node:
    def __init__(self, data):
        self._data = data

    def __str__(self):
        return str(self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
		self._data = new_data

class ListNode(Node):
    def __init__(self, data, previous=None, next=None):
        super().__init__(data)
        self._previous = previous
        self._next = next

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @next.setter
    def next(self, new_next):
        self._next = new_next

    @previous.setter
    def previous(self, new_previous):
        self._previous = new_previous

class Edge:
    def __init__(self, vertex, weight, previous=None, next=None):
        self.node = ListNode(None, previous, next)  # ListNode to manage linked list connectivity
        self._dest = vertex
        self._weight = weight

    @property
    def dest(self):
        return self._dest

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

class TreeNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, new_left):
        self._left = new_left

    @right.setter
    def right(self, new_right):
        self._right = new_right
```
# Data Structures
## Linked List
```python
from Blueprints.Data_Structures import ListNode, Edge

class UnorderedLinkedList:
	def __init__(self):
        self.head = None
        self.count = 0

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    @property
    def is_empty(self) -> bool:
        return self.head is None

    def insert(self, item, *args):
        new_node = ListNode(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_after(self, base, item):
        base_node = self.search(base)

        if not base_node:
            return

        new_node = ListNode(item)
        new_node.next = base_node.next
        base_node.next = new_node
        self.count += 1

    def size(self) -> int:
        return self.count

    def remove(self, item):
        curr = self.search(item)

        if not curr:
            return
        if self.head == curr:
            self.head = curr.next
        else:
            prev = self.head

            while prev.next != curr:
                prev = prev.next

            prev.next = curr.next
        self.count -= 1

    def search(self, item):
        curr = self.head

        while curr:
            if curr.data == item:
                return curr
            curr = curr.next
        return None

class CircularUnorderedLinkedList(UnorderedLinkedList):
    def __init__(self):
        super().__init__()
        self.head = ListNode(-1)
        self.head.next = self.head

    def is_empty(self) -> bool:
        return self.head.next == self.head

    def insert(self, item, *args):
        new_node = ListNode(item)
        new_node.next = self.head.next
        self.head.next = new_node
        self.count += 1

    def insert_after(self, base, item):
        base_node = self.search(base)

        if not base_node:
            return

        new_node = ListNode(item)
        new_node.next = base_node.next
        base_node.next = new_node
        self.count += 1

    def search(self, item):
        curr = self.head.next

        while curr != self.head:
            if curr.data == item:
                return curr
            curr = curr.next
        return None

    def remove(self, base):
        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == base:
                prev.next = curr.next
                self.count -= 1
                return
            else:
	            prev = curr
                curr = curr.next

class UnorderedDoublyLinkedList(UnorderedLinkedList):
    def insert(self, item, *args):
        new_node = ListNode(item)
        new_node.next = self.head

        if self.head:
            self.head.previous = new_node

        self.head = new_node
        self.count += 1

    def insert_after(self, base, item):
        base_node = self.search(base)

        if not base_node:
            return

        new_node = ListNode(item)
        new_node.next = base_node.next
        new_node.previous = base_node
        base_node.next = new_node

        if new_node.next:
            new_node.next.previous = new_node
        self.count += 1

    def remove(self, item):
        curr = self.search(item)

        if not curr:
            return
        if curr.previous:
            curr.previous.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.previous = curr.previous
        self.count -= 1

class EdgeUnorderedLinkedList(UnorderedDoublyLinkedList):
    def insert(self, item, dest=None, weight=None):
        if dest is None or weight is None:
            raise ValueError("Both dest and weight must be provided")

        new_edge = Edge(dest, weight)
        new_edge.next = self.head

        if self.head:
            self.head.previous = new_edge

        self.head = new_edge
        self.count += 1

    def remove(self, vertex):
        e = self.head

        while e:
            if e.dest == vertex:
                if e.previous:
                    e.previous.next = e.next
                if e.next:
                    e.next.previous = e.previous
                self.count -= 1
                return

            e = e.next

    def search(self, vertex):
        e = self.head

        while e:
            if e.dest == vertex:
                return e
            e = e.next
        return None

    def weight(self, vertex):
        e = self.search(vertex)
        return e if e else None
```
## Stack
```python
from Blueprints.Data_Structures import ListNode

class Stack:
    def __init__(self):
		self.items = []

    def __len__(self) -> int:
        return len(self.items)

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


class NodeStack:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item):
        new_node = ListNode(item, previous=self.head)

        if self.head is not None:
            self.head.next = new_node

        self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        item = self.head.data
        self.head = self.head.previous

        if self.head is not None:
            self.head.next = None

        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data


class NodeStackNext:
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, item):
        new_node = ListNode(data=item, next=self.head)
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")

        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def peek(self):
		if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.head.data
```
## Queue
```python
from Blueprints.Data_Structures import ListNode

class Queue:
    def __init__(self):
        self.items = []

    def __len__(self) -> int:
        return len(self.items)

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.size() == 0

    def head(self):
        if self.is_empty():
            raise IndexError("head from empty queue")
        return self.items[-1]

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
		return self.items.pop()

class NodeQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.front is None

    def head(self):
        if self.is_empty():
            raise IndexError("head from empty queue")
        return self.front.data

    def enqueue(self, item):
        new_node = ListNode(item)

        if self.rear is not None:
            self.rear.next = new_node
            new_node.previous = self.rear

        self.rear = new_node

        if self.front is None:
            self.front = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        item = self.head()
        self.front = self.front.next

        if self.front is not None:
            self.front.previous = None
        else:
	        self.rear = None

        self._size -= 1
        return item

class NodeQueueNext:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.front is None

    def head(self):
        if self.is_empty():
            raise IndexError("head from empty queue")
        return self.front.data

    def enqueue(self, item):
        new_node = ListNode(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        item = self.head()
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        return item
```
## Deque
```python
from Blueprints.Data_Structures import ListNode

class Deque:
    def __init__(self):
        self.items = []

    def __len__(self) -> int:
        return len(self.items)

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.size() == 0

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
		if not self.is_empty():
            return self.items.pop()
        return None

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

class NodeDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.front is None

    def head(self):
        if self.is_empty():
            raise IndexError("head from empty deque")
        return self.front.data

    def tail(self):
        if self.is_empty():
            raise IndexError("tail from empty deque")
        return self.rear.data

    def add_front(self, item):
        new_node = ListNode(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front.previous = new_node
            self.front = new_node
        self._size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove_front from empty deque")

        item = self.head()
        self.front = self.front.next

        if self.front is not None:
            self.front.previous = None
        else:
	        self.rear = None

        self._size -= 1
        return item

    def add_rear(self, item):
        new_node = ListNode(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.previous = self.rear
            self.rear = new_node
        self._size += 1

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")

        item = self.tail()
        self.rear = self.rear.previous

        if self.rear is not None:
            self.rear.next = None
        else:
	        self.front = None

        self._size -= 1
        return item

class NodeDequeNext:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def size(self) -> int:
        return self.__len__()

    def is_empty(self) -> bool:
        return self.front is None

    def head(self):
        if self.is_empty():
            raise IndexError("head from empty deque")
        return self.front.data

    def tail(self):
        if self.is_empty():
            raise IndexError("tail from empty deque")
        return self.rear.data

    def add_front(self, item):
        new_node = ListNode(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node
        self._size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("remove_front from empty deque")

        item = self.head()
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self._size -= 1
        return item

    def add_rear(self, item):
        new_node = ListNode(item)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("remove_rear from empty deque")

        if self.front == self.rear:
            item = self.tail()
            self.front = None
            self.rear = None
        else:            current = self.front

            while current.next != self.rear:
                current = current.next

            item = self.tail()
            self.rear = current
            self.rear.next = None

        self._size -= 1
        return item
```
## Heap
```python
class Heap:
    def __init__(self, data=None):
        if data is None:
            self._array = []
        else:
            self._array = data

        for i in range(len(self._array) // 2 - 1, -1, -1):  # i goes from the last array element to the first
            self.heapify(i)

    def __str__(self) -> str:
        return str(self._array)

    @property
    def array(self):
        return self._array

    @property
    def depth(self) -> int:
        depth = 0
        while 2 ** depth - 1 < len(self._array):
            depth += 1
        return depth

    def insert(self, data):
        self._array.append(data)
        self.swim_up(len(self._array) - 1)

    def delete(self):
        if len(self._array) == 0:
            return None

        res = self._array[0]
        self._array[0] = self._array[-1]
        self._array.pop()
        self.swim_down(0)
        return res

    def heapify(self, idx):
        raise NotImplementedError("Please implement in subclass")

    def swim_up(self, idx):
        raise NotImplementedError("Please implement in subclass")

    def swim_down(self, idx):
        raise NotImplementedError("Please implement in subclass")

    @classmethod
    def heap_sort(cls, array):
        heap = cls(array)
        sorted_array = []

        while heap._array:
            sorted_array.append(heap.delete())
        # array[:] is used to modify the original array
        array[:] = sorted_array[::-1] if issubclass(cls, MaxHeap) else sorted_array  # Reverses the array if it's a MaxHeap, otherwise it's left as is (MinHeap)

class MinHeap(Heap):
    def __init__(self, data=None):
		super().__init__(data)

    def heapify(self, idx):
		smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self._array) and self._array[left] < self._array[smallest]:
            smallest = left

        if right < len(self._array) and self._array[right] < self._array[smallest]:
            smallest = right

        if smallest != idx:
            self._array[idx], self._array[smallest] = self._array[smallest], self._array[idx]
            self.heapify(smallest)

    def swim_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            if self._array[parent] > self._array[idx]:
                self._array[parent], self._array[idx] = self._array[idx], self._array[parent]
                idx = parent
            else:
                break

    def swim_down(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self._array) and self._array[left] < self._array[smallest]:
            smallest = left

        if right < len(self._array) and self._array[right] < self._array[smallest]:
            smallest = right

        if smallest != idx:
            self._array[idx], self._array[smallest] = self._array[smallest], self._array[idx]
            self.swim_down(smallest)

class MaxHeap(Heap):
    def __init__(self, data=None):
		super().__init__(data)

    def heapify(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self._array) and self._array[left] > self._array[largest]:
            largest = left

        if right < len(self._array) and self._array[right] > self._array[largest]:
            largest = right

        if largest != idx:
            self._array[idx], self._array[largest] = self._array[largest], self._array[idx]
            self.heapify(largest)

    def swim_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            if self._array[parent] < self._array[idx]:
                self._array[parent], self._array[idx] = self._array[idx], self._array[parent]
                idx = parent
            else:
                break

    def swim_down(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self._array) and self._array[left] > self._array[largest]:
            largest = left

        if right < len(self._array) and self._array[right] > self._array[largest]:
            largest = right

        if largest != idx:
            self._array[idx], self._array[largest] = self._array[largest], self._array[idx]
            self.swim_down(largest)
```
## Binary Tree
```python
from Blueprints.Data_Structures import TreeNode


class BinaryTree:
    def __init__(self, init_data, left=None, right=None):
        self._data = init_data
        self._left = left
        self._right = right

    def modify_left(self, item):
        self._left = BinaryTree(item)

    def modify_right(self, item):
        self._right = BinaryTree(item)

    def get_root_val(self):
        return self._data

    def set_root_val(self, item):
        self._data = item

    def get_left_child(self):
        return self._left

    def get_right_child(self):
        return self._right

class NodeBinaryTree:
    def __init__(self, init_data):
        self.root = TreeNode(init_data)

    def tree_get_root(self):
        return self.root

    def tree_set_left(self, base, item):
        base.left = TreeNode(item)

    def tree_set_right(self, base, item):
        base.right = TreeNode(item)

    def tree_get_left(self, base):
        return base.left

    def tree_get_right(self, base):
        return base.right
```
## BST
```python
class BinarySearchTree:
    def __init__(self, init_data):
        self.data = init_data
        self.left = None
        self.right = None
        self.parent = None

    def get_root_val(self):
        return self.data

    def set_root_val(self, value):
        self.data = value

    def get_global_root(self):
        curr = self
        while curr.parent is not None:
            curr = curr.parent
        return curr

    def get_next(self):
        if self.right is not None:
            curr = self.right

            while curr.left is not None:
                curr = curr.left
        else:
            child = self
            curr = self.parent

            while curr is not None and curr.right == child:
                child = curr
                curr = curr.parent
        return curr

    def get_previous(self):
        if self.left is not None:
            curr = self.left

            while curr.right is not None:
                curr = curr.right
        else:
            child = self
            curr = self.parent

            while curr is not None and curr.left == child:
                child = curr
                curr = curr.parent
        return curr

    def get_first(self):
        curr = self.get_global_root()
        while curr.left is not None:
            curr = curr.left
        return curr

    def get_last(self):
        curr = self.get_global_root()
        while curr.right is not None:
            curr = curr.right
        return curr

    def search(self, item):
        curr = self.get_global_root()

        while curr is not None and curr.data != item:
            if item < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def insert(self, item):
        curr = self.get_global_root()
        parent = None

        while curr is not None:
            parent = curr
            if item < curr.data:
                if curr.left is None:
                    break
				curr = curr.left
            else:
                if curr.right is None:
                    break
				curr = curr.right

        new_node = BinarySearchTree(item)
        new_node.parent = parent

        if item < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    def remove(self):
        if self.left is not None:
            predecessor = self.get_previous()
            self.data = predecessor.data
            predecessor.remove()
        elif self.right is not None:
            successor = self.get_next()
            self.data = successor.data
            successor.remove()
        else:
            if self.parent is not None:
                if self.parent.left == self:
                    self.parent.left = None
                else:
	                self.parent.right = None
            else:
	            self.data = None
                self.left = None
                self.right = None
```
## Graph
```python
from Blueprints.Data_Structures import EdgeUnorderedLinkedList

class Vertex:
	def __init__(self, vertex_idx):
        self._idx = vertex_idx
        self._edges = EdgeUnorderedLinkedList()

    def __str__(self):
        res = ', '.join(f"(to: {edge.dest}, weight: {edge.weight})" for edge in self.edges)
        return f"Vertex {self.idx} -> [{res}]"

    def __repr__(self):
        return self.__str__()

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def edges(self):
        return self._edges

    @property
    def out_edges(self):
        return self.edges

    def add_edge(self, dest, weight):
        self.edges.insert(dest, weight)

class StaticGraph:
    def __init__(self, n: int):
        self.V = n
        self.adj = [[0] * n for _ in range(n)]

    @property
    def n(self) -> int:
        return len(self.adj)

    def link(self, i: int, j: int, weight: int = 1):
        self.adj[i][j] = weight

    def unlink(self, i: int, j: int):
        self.adj[i][j] = 0

    def has_edge(self, i: int, j: int) -> bool:
        return self.adj[i][j] > 0

    def weight(self, i: int, j: int) -> int:
        return self.adj[i][j]

    def to_dynamic(self):
        G_dyn = DynamicGraph(self.n)

        for i in range(self.n):
            for j in range(self.n):
                weight = self.weight(i, j)

                if weight > 0:
                    G_dyn.link(i, j, weight)
        return G_dyn

class DynamicGraph:
    def __init__(self, n: int):
        self.neighbors = [Vertex(i) for i in range(n)]

    @property
    def n(self) -> int:
        return len(self.neighbors)

    def link(self, i: int, j: int, weight: int = 1):
        self.neighbors[i].add_edge(j, weight)

    def unlink(self, i: int, j: int):
        self.neighbors[i].edges.remove(j)

    def has_edge(self, i: int, j: int) -> bool:
        return self.neighbors[i].edges.search(j) is not None

    def weight(self, i: int, j: int) -> int:
        return self.neighbors[i].edges.weight(j)

    def to_static(self):
        G_stat = StaticGraph(self.n)

        for i in range(self.n):
            for e in self.neighbors[i].out_edges:
                G_stat.link(i, e.dest, e.weight)
        return G_stat
```

# Special
## Forest + Forest Node
```python
class ForestNode:
    def __init__(self, item):
        self._info = item
        self._child = None      # Child will be another ForestNode (subtree)
        self._brother = None    # Brother will be another ForestNode (sibling tree)

    def get_root_val(self):
        return self._info

    def set_root_val(self, item):
        self._info = item

    def get_child(self):
        return self._child

    def get_brother(self):
        return self._brother

    def set_child(self, new_node):
        self._child = ForestNode(new_node)

    def set_brother(self, new_node):
        self._brother = ForestNode(new_node)

class Forest:
    def __init__(self):
        self._trees = []

    def add_tree(self, tree):
        self._trees.append(tree)

    def get_trees(self):
        return self._trees
```
## $N$-ary Tree (via Forest)
```python
class NAryTree:
    def __init__(self, item):
        self._root = ForestNode(item)
        self._children = []

    def get_root(self):
        return self._root

    def get_children(self):
        return self._children

    def add_child(self, item):
        new_child = ForestNode(item)
        self._children.append(new_child)
        if not self._root.get_child():
            self._root.set_child(new_child)
        else:
            last_child = self._root.get_child()
            while last_child.get_brother():
                last_child = last_child.get_brother()
            last_child.set_brother(new_child)
```
