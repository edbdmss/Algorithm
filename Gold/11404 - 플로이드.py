import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        if x==y:
            graph[x][y] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


for k in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][k]+graph[k][y])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
    