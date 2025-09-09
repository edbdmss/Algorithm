from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))
    
queue = deque()        
for i in range(m):    # 익어있는 토마토 큐에 삽입
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))   
                                     
def bfs():
            
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while (queue):
         
        x, y = queue.popleft()     # x가 행(m), y가 열(n)
        
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and graph[x][y] != -1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1     
            else:
                continue 
            
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                print(-1)
                return
            
    ct = max(max(i) for i in graph)    # 이중 max → 각 행에서 max 구하고, 그 안에서 다시 max
    print(ct-1)
            
bfs()