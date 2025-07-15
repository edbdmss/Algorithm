import sys

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    graph.append([x,y])

graph.sort(key=lambda x:(x[1],x[0]))
for i in graph:
    print(*i)