from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())

degree = [0] * (n+1)    # 진입차수 리스트 0으로 초기화
graph = [[] for _ in range(n+1)]   # 노드 간 연결정보 
queue = deque()   # 노드 삽입 큐
ki = []    # 결과 리스트

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b) 
    degree[b] += 1

for i in range(1, n+1):          # 한 번만 실행
    if degree[i] == 0:
        queue.append(i)

while(queue):
    x = queue.popleft()
    ki.append(x)
    
    for i in graph[x]:          # x와 연결된 다음 노드들에 대해
        degree[i] -= 1          # 진입차수를 줄이고
        if degree[i] == 0:          # 차수=0이 되면 큐에 삽입
            queue.append(i)
        
print(*ki)
