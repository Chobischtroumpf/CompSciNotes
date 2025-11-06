---
title: Traversals
authors: Alessandro Dorigo
tags:
  -
---

# DFS
```python
def dfs_static(graph, start):
    visited = [False] * graph.n
    result = []

    def dfs(vertex):
        visited[vertex] = True
        result.append(vertex)

        for i in range(graph.n):
            if graph.adj[vertex][i] > 0 and not visited[i]:
                dfs(i)

    dfs(start)
    return result

def dfs_dynamic(graph, start):
    visited = [False] * graph.n
    result = []

    def dfs(vertex_idx):
        vertex = graph.neighbors[vertex_idx]
        visited[vertex.idx] = True
        result.append(vertex.idx)

        for edge in vertex.out_edges:
            if not visited[edge.dest]:
                dfs(edge.dest)

    dfs(start)
    return result
```
# BFS
```python
from Blueprints.Deque import Deque

def bfs_static(graph, start):
    visited = [False] * graph.n
    queue = Deque()
    queue.add_rear(start)
    result = []

    while not queue.is_empty():
        vertex = queue.remove_front()

        if not visited[vertex]:
            visited[vertex] = True
            result.append(vertex)

            for i in range(graph.n):
                if graph.adj[vertex][i] > 0 and not visited[i]:
                    queue.add_rear(i)
    return result

def bfs_dynamic(graph, start):
    visited = [False] * graph.n
    queue = Deque()
    queue.add_rear(start)
    result = []

    while not queue.is_empty():
        vertex_idx = queue.remove_front()

        if not visited[vertex_idx]:
            vertex = graph.neighbors[vertex_idx]
            visited[vertex_idx] = True
            result.append(vertex.idx)

            for edge in vertex.out_edges:
                if not visited[edge.dest]:
                    queue.add_rear(edge.dest)
    return result
```
# Inorder
```python
from Blueprints.Data_Structures import Stack

def inorder_rec_tree(tree: "BinaryTree"):
	if tree is not None:
        inorder_rec_tree(tree.get_left_child())
        print(tree.get_root_val())
        inorder_rec_tree(tree.get_right_child())


def inorder_iter_tree(tree: "BinaryTree"):
    stack = Stack()
    curr = tree

    while not stack.is_empty() or curr is not None:
        if curr is not None:
            stack.push(curr)
            curr = curr.get_left_child()
        else:
            curr = stack.pop()
            print(curr.get_root_val())
            curr = curr.get_right_child()


def inorder_node_tree(tree: "NodeBinaryTree"):
	def inorder_node(node: "TreeNode"):
        if node is not None:
            inorder_node(tree.tree_get_left(node))
            print(node.data)
            inorder_node(tree.tree_get_right(node))

    inorder_node(tree.tree_get_root())


def inorder_iter_node_tree(tree: "NodeBinaryTree"):
    stack = Stack()
    curr = tree.tree_get_root()

    while not stack.is_empty() or curr is not None:
        if curr is not None:
            stack.push(curr)
            curr = tree.tree_get_left(curr)
        else:
            curr = stack.pop()
            print(curr.data)
            curr = tree.tree_get_right(curr)
```
# Postorder
```python
from Blueprints.Data_Structures import Stack

def postorder_rec_tree(tree: "BinaryTree"):
    if tree is not None:
        postorder_rec_tree(tree.get_left_child())
        postorder_rec_tree(tree.get_right_child())
        print(tree.get_root_val())

def postorder_iter_tree(tree: "BinaryTree"):
    if tree is None:
        return

    stack = Stack()
    out = Stack()
    stack.push(tree)

    while not stack.is_empty():
        curr = stack.pop()
        out.push(curr)

        if curr.get_left_child() is not None:
            stack.push(curr.get_left_child())
        if curr.get_right_child() is not None:
            stack.push(curr.get_right_child())

    while not out.is_empty():
        curr = out.pop()
        print(curr.get_root_val())

def postorder_node_tree(tree: "NodeBinaryTree"):
    def postorder_node(node: "TreeNode"):
        if node is not None:
            postorder_node(tree.tree_get_left(node))
            postorder_node(tree.tree_get_right(node))
            print(node.data)

    postorder_node(tree.tree_get_root())

def postorder_iter_node_tree(tree: "NodeBinaryTree"):
    if tree.tree_get_root() is None:
        return

    stack = Stack()
    out = Stack()
    stack.push(tree.tree_get_root())

    while not stack.is_empty():
        curr = stack.pop()
        out.push(curr)

        if curr.left is not None:
            stack.push(curr.left)
        if curr.right is not None:
            stack.push(curr.right)

    while not out.is_empty():
        curr = out.pop()
        print(curr.data)

def postorder_forest(forest: "ForestNode"):
    while forest is not None:
        postorder_forest(forest.get_child())
        print(forest.get_root_val())
        forest = forest.get_brother()
```
# Preorder
```python
from Blueprints.Data_Structures import Stack

def preorder_rec_tree(tree: "BinaryTree"):
    if tree is not None:
        print(tree.get_root_val())
        preorder_rec_tree(tree.get_left_child())
        preorder_rec_tree(tree.get_right_child())

def preorder_iter_tree(tree: "BinaryTree"):
    if tree is None:
        return

    stack = Stack()
    stack.push(tree)

    while not stack.is_empty():
        curr = stack.pop()
        print(curr.get_root_val())

        if curr.get_right_child() is not None:
            stack.push(curr.get_right_child())
        if curr.get_left_child() is not None:
            stack.push(curr.get_left_child())


def preorder_node_tree(tree: "NodeBinaryTree"):
    def preorder_node(node: "TreeNode"):
        if node is not None:
            print(node.data)
            preorder_node(tree.tree_get_left(node))
            preorder_node(tree.tree_get_right(node))

    preorder_node(tree.tree_get_root())

def preorder_iter_node_tree(tree: "NodeBinaryTree"):
    if tree.tree_get_root() is None:
        return

    stack = Stack()
    stack.push(tree.tree_get_root())

    while not stack.is_empty():
        curr = stack.pop()
        print(curr.data)

        if curr.right is not None:
            stack.push(curr.right)
        if curr.left is not None:
            stack.push(curr.left)

def preorder_forest(forest: "ForestNode"):
    while forest is not None:
        print(forest.get_root_val())
        preorder_forest(forest.get_child())
        forest = forest.get_brother()
```
# Level
```python
from Blueprints.Data_Structures import Queue

def level_order_tree(tree: "BinaryTree"):
    if tree is None:
        return

    queue = Queue()
    queue.enqueue(tree)

    while not queue.is_empty():
        curr = queue.dequeue()

        if curr:
            print(curr.get_root_val())
            queue.enqueue(curr.get_left_child())
            queue.enqueue(curr.get_right_child())

def level_order_node_tree(tree: "NodeBinaryTree"):
    if tree.tree_get_root() is None:
        return

    queue = Queue()
    queue.enqueue(tree.tree_get_root())

    while not queue.is_empty():
        curr = queue.dequeue()

        if curr:
            print(curr.data)
            if curr.left is not None:
                queue.enqueue(curr.left)
            if curr.right is not None:
                queue.enqueue(curr.right)

def level_order_forest(forest: "ForestNode"):
    if forest is None:
        return

    queue = Queue()
    queue.enqueue(forest)

    while not queue.is_empty():
        curr = queue.dequeue()

        while curr:
            print(curr.get_root_val())
            queue.enqueue(curr.get_child())
            curr = curr.get_brother()
```
