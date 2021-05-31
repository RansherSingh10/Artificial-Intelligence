visit = set()

def dfs(visit, graph, node):
    if node not in visit:
        print (node, end=" ")
        visit.add(node)
        for neighbour in graph[node]:
            dfs(visit, graph, neighbour)


visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

# Driver Code
print("BFS:", end = " ")
bfs(visited, graph, 'A')
print("\nDFS:", end = " ")
dfs(visit, graph, 'A')