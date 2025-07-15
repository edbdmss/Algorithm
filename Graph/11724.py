n, m = map(int, input().split())
graph = [[] for i in range(n)]
graph.append([])
visited = [False] * (n+1)

for _ in range(m):      # graph 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v): 
    visited[v] = True   # 방문처리
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
count = 0   # 연결 요소의 개수 
for i in range(1,n+1):
    if not visited[i]:    # False이면
        dfs(i)
        count += 1
print(count)