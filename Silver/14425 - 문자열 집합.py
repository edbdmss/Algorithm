import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = []
for _ in range(n):
    s.append(input())
ct = 0
for i in range(m):
    x = input()
    if x in s:
        ct += 1
print(ct)