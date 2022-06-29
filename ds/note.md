# Graph
- Degree of a Vertex: total number of edges incident on a vertex
- Parallel Edges: two undirected edges are parallel if they have the same end vertices. Two directed edges are parallel if they have the same starting and ending vertices.
- Self Loop: this occurs when an edge starts and ends on the same vertex.
- Adjacency: two vertices are said to be adjacent if there is an edge between them directly.
- Directed Graph: $$n(n-1) \ possible \ edges$$
- Undirected Graph: $$(n*(n-1))/2 \ maximum \ possible \ edges$$
- The two most common ways to represent a graph are:
  - Adjacency Matrix: for a directed graph, the usual convention is to think of the rows as sources and the columns as destination.
  - Adjacency List

## Bipartite Graph
- The vertices of this graph are divided into two disjoint parts in such a way no two vertices in the same part are adjacent to each other.
- All the acyclic graphs can be bi-partite, but in the case of cyclic graphs, they must contain an even number of vertices.

## Graph Traversal Algorithms
1. Breadth first search
- The BFS algorithm earns its name because it grows breadth-wise. All the nodes at a certain level are traversed before moving on to the next level.
2. Depth first search
- The DFS algorithm is the opposite of BFS in the sense that it grows depth-wise