n = int(input())

graph = []
node = [i for i in range(n)]
result = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result[i][j] = 1

for i in range(n):
    print(*graph[i], "", end="")