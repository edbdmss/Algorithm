import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())    # 노드 개수 V, 간선 개수 E
K = int(input())    # 시작 노드
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(K):
    q = []
    heapq.heappush(q, (0, K))
    distance[K] = 0
    
    while q:
        dist, now_node = heapq.heappop(q)   #(노드, 거리)
        if distance[now_node] < dist:
                continue
        for i in graph[now_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])            