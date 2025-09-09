import sys
input = sys.stdin.readline

n = int(input())
loap = []
for _ in range(n):
    x = int(input())
    loap.append(x)

loap.sort()
total = 0
for i in range(n):
    total = max(total, loap[i] * (n-i))
print(total)