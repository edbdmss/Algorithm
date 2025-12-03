from collections import deque 

n, m, v = map(int, input().split())
visited = [False] * (n+1)   # 방문정보 초기화
graph = [[] * i for i in range(n+1)]   # graph 초기화
result1 = []
result2 = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)   # 1번부터 시작
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()

def dfs(graph, v, visited):
    visited[v] = True   # 방문처리
    #print(v," ",end="")
    result1.append(v)
    for i in graph[v]:
        if not visited[i]:   # False인 경우 (방문한 적 x)
            dfs(graph, i, visited)
    return result1

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True    # 방문처리

    while (queue):
        v = queue.popleft()
        #print(v," ", end="")
        result2.append(v)
        for i in graph[v]:
            if not visited[i]:    # False인 경우 (방문한 적 x)
                queue.append(i)
                visited[i] = True
    return result2
                
                
print(*dfs(graph, v, visited))
visited.clear()
visited = [False] * (n+1)
print(*bfs(graph, v, visited))