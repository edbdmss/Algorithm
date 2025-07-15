import sys

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    a,b = sys.stdin.readline().split()
    a = int(a)
    graph.append([a, b])
    
graph.sort(key=lambda x:x[0])
for i in graph:
    print(*i)
 