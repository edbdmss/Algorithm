import sys
input = sys.stdin.readline

n = int(input())
x = []

for _ in range(n):
    x.append(int(input()))

ans = 0
while True:
    if len(x) == 1 or x[0] > max(x[1:]):
        break
    
    x[0] += 1
    i = x[1:].index(max(x[1:]))
    x[i+1] -= 1
    ans += 1
    
print(ans)