INF = int(1e9)

n = int(input())        # 노드의 개수
m = int(input())        # 간선의 개수

# 2차원 그래프 무한 값으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
           

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())         
    graph[a][b] = c
   
           
# 플로이드 워셜 점화식            
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('infinity', end='')
        else:
            print(graph[a][b], end='')
    print()
    
