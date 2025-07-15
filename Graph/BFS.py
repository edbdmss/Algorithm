from collections import deque   
    
queue = deque()

N, M = map(int, input().split()) 
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input()))
    
    
def bfs(x, y):  # x: x좌표, y: y좌표
    
    queue = deque()  
    queue.append((x,y))  # 시작점 방문 처리
    dx=[1, -1, 0, 0]  # 위-아래로 이동
    dy=[0, 0, 1, -1]  # 왼쪽-오른쪽으로 이동
    
    while (queue):          # 큐가 빌때(False) 까지 
        x,y = queue.popleft()    # pop은 인자를 받지 않음.// 위치를 꺼냄.
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:   # 탐색이 성공할경우
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1     # 지금까지 온 거리 graph[x][y]에 1씩 더해서 총 거리 갱신
            else:
                continue
    return graph[N-1][M-1]
print(bfs(0, 0))


