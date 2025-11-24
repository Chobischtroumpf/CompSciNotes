---
title: Pathfinders
authors: Alessandro Dorigo
tags:
  -
---

# Roy-Warshall
```python
def roy_warshall(graph):
    # Initialize the matrix M with the same values as the graph's adjacency matrix
    M = [[int(e) for e in row] for row in graph.adj]

    # Set the diagonal elements to 1 (self-loops)
    for i in range(graph.n):
        M[i][i] = 1

    # Update the matrix M to include paths found via intermediate vertices
    for k in range(graph.n):
        for i in range(graph.n):
            if M[i][k]:
                for j in range(graph.n):
                    M[i][j] |= M[k][j]

    return M
```
# Floyd-Warshall
```python
def floyd_warshall(graph):
    # Initialize distance and predecessor matrices
    D = [[float('inf')] * graph.n for _ in range(graph.n)]
    P = [[None] * graph.n for _ in range(graph.n)]

    # Set initial distances based on the adjacency matrix
    for i in range(graph.n):
        for j in range(graph.n):
            if i == j:
                D[i][j] = 0
            elif graph.adj[i][j] != 0:
                D[i][j] = graph.adj[i][j]
                P[i][j] = i
            else:
                D[i][j] = float('inf')
                P[i][j] = None

    # Update distances using intermediate vertices
    for k in range(graph.n):
        for i in range(graph.n):
            for j in range(graph.n):
                if D[i][k] != float('inf') and D[k][j] != float('inf'):
                    new_distance = D[i][k] + D[k][j]
                    if new_distance < D[i][j]:
                        D[i][j] = new_distance
                        P[i][j] = P[k][j]

    # Check for negative-weight cycles
    for i in range(graph.n):
        if D[i][i] < 0:
            raise ValueError("Graph contains a negative-weight cycle")

    return D, P
```
# Djikstra
```python
from Blueprints.Graph import DynamicGraph
from Blueprints.Graph import StaticGraph

def dijkstra(graph, src):
    V = graph.n
    dist = [float('inf')] * V
    dist[src] = 0
    spt_set = [False] * V

    def print_solution(dist):
        print("Vertex \t Distance from Source")
        for i in range(V):
            print(f"{i} \t\t {dist[i]}")

    def min_distance(dist, spt_set):
        min_val = float('inf')
        min_idx = -1

        for v in range(V):
            if dist[v] < min_val and not spt_set[v]:
                min_val = dist[v]
                min_idx = v
        return min_idx

    # Main loop of Dijkstra's algorithm
    for _ in range(V - 1):
        u = min_distance(dist, spt_set)

        if u == -1:  # No more vertices are reachable
            break

        spt_set[u] = True

        # Get edges (neighbors) based on graph type
        if isinstance(graph, DynamicGraph):
            edges = graph.neighbors[u].out_edges
        elif isinstance(graph, StaticGraph):
            edges = [(v, graph.weight(u, v)) for v in range(V) if graph.has_edge(u, v)]
        else:
            raise ValueError("Graph type not supported")

        for edge in edges:
            if isinstance(graph, DynamicGraph):
                v, weight = edge.dest, edge.weight
            else:
                v, weight = edge

            if not spt_set[v] and dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight

    print_solution(dist)
```
# Moore
```python
from Blueprints.Graph import DynamicGraph
from Blueprints.Graph import StaticGraph
from Blueprints.Queue import Queue

def moore(graph, start, end):
    # Initialize index with infinity and parent with -1
    index = [float('inf')] * graph.n
    index[start] = 0
    parent = [-1] * graph.n
    shortest_path = []

    # Initialize the queue and enqueue the start vertex
    q = Queue()
    q.enqueue(start)

    # BFS to find shortest path
    while not q.is_empty():
        u = q.dequeue()

        # Get neighbors based on graph type
        if isinstance(graph, DynamicGraph):
            neighbors = [edge.dest for edge in graph.neighbors[u].edges]
        elif isinstance(graph, StaticGraph):
            neighbors = [v for v in range(graph.n) if graph.has_edge(u, v)]
        else:
            raise ValueError("Graph type not supported")

        # Update index and parent for each neighbor
        for i in neighbors:
            if index[i] == float('inf'):
                q.enqueue(i)
                index[i] = index[u] + 1
                parent[i] = u

    # Reconstruct shortest path if end is reachable
    if index[end] != float('inf'):
        k = index[end]
        shortest_path = [end]

        while k > 0:
            shortest_path.insert(0, parent[shortest_path[0]])
            k -= 1

    return shortest_path
```
