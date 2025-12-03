# 개선된 다익스트라 알고리즘은 힙 자료구조를 사용한다.

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())    # 노드의 개수 n, 간선의 개수 m
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기 
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))     # (노드, 비용) 형태
    

def dijkstra(start):
    q = []
    
    # 첫번째 노드로 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now_node = heapq.heappop(q)
        if distance[now_node] < dist:  # 현재까지 노드에 적립된 비용이 새 거리보다 작으면
            continue
        for i in graph[now_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) 
                
# 실행
dijkstra(start)     #distance 리스트 업데이트

for i in range(1, n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
    