import sys

N = int(sys.stdin.readline().rstrip())
a = []

for _ in range(N):
    x, y = map(int, input().split())
    a.append([x,y]) 
a.sort()

for i in range(N):   #출력
    print(*a[i])
    
    
    
# a.append([x,y])  → 리스트를 요소로 갖는 리스트. 2차원 리스트