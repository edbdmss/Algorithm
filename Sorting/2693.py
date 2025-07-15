import sys
T = int(sys.stdin.readline())

for i in range(T):
    
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    print(a[2])
