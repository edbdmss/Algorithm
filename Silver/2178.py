from collections import deque

N,M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    
    queue = deque()
    queue.append((x,y))
    while (queue):
        
        x,y = queue.popleft()    #위치중요. for문안에 넣으면 안된다? → 상하좌우를 모두 살펴보기전에 popleft해서 큐가 너무 일찍 비게 됨.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
            else:
                continue
    return graph[N-1][M-1]

print(bfs(0,0))