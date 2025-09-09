import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

start, end, ct = 0, 0, 0
total = 0

while True:
    if total >= M:
        if total == M:
            ct += 1
        total -= num[start]
        start += 1
    elif end == N:
        break
    else:
        total += num[end]
        end += 1        
          
print(ct)