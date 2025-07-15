com = int(input())
link = int(input())

visited = [False] * (com+1)     # visited는 노드의 개수 +1로 
graph = [[] * i for i in range(com+1)]

for _ in range(link):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
    return visited

conta = dfs(graph, 1, visited)
print(conta.count(True)-1)