import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]            # 노드 연결 그래프
degree = [1]*(n+1)    # 진입 차수
queue = deque()

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    