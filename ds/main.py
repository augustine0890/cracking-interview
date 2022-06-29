from graph import Graph
from queue import Queue


def bfs_traversal_helper(g, source, visited):
  result = ""
  queue = Queue()
  queue.enqueue(source)
  visited[source] = True # mark as visited
  # Traverse while queue is not empty
  while not queue.is_empty():
    # Dequeue a vertex/node from queue and add it to result
    curr = queue.dequeue()
    result += str(curr)
    # Get adjacent vertices to the current node from the list,
    # and if they are not already visited then enqueue them in the Queue
    temp = g.array[curr].head_node
    while temp is not None:
      if not visited[temp.data]:
        queue.enqueue(temp.data)
        visited[temp.data] = True # Visit the current node
      temp = temp.next_element
  
  return result, visited

# Breadth First Traversal of Graph g from source vertex
def bfs_traversal(g, source):
  # store already visited vertices
  result = ""
  num_of_vertices = g.vertices
  if num_of_vertices is 0:
    return result
  
  # A list to hold the history of visited nodes
  # Make a node visited whenever you enqueue it into queue
  visited = []
  for i in range(num_of_vertices):
    visited.append(False)
  # Start from source
  result, visited = bfs_traversal_helper(g, source, visited)
  # Visit remaining nodes
  for i in range(num_of_vertices):
    if not visited[i]:
      result_new, visited = bfs_traversal_helper(g, i, visited)
      result += result_new
  # For the above graph, it should return "01234" or "02143" etc
  return result

if __name__ == "__main__":
  g = Graph(5)
  g.add_edge(0, 2)
  g.add_edge(0, 1)
  g.add_edge(1, 4)
  g.add_edge(1, 3)

  g.print_graph()

  # print(g.array[1].get_head().data)
  print(bfs_traversal(g, 0))
