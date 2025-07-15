import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]            # 노드 연결 그래프
degree = [1]*(n+1)    # 진입 차수
visited = [False]*(n+1)  # 방문 여부

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            if degree[v] >= degree[i]:
                degree[i] += degree[v]
            dfs(i)    

dfs(1)
print(*degree[1:])         