import sys
input = sys.stdin.readline

n = int(input())
rank = []
for _ in range(n):
    rank.append(int(input()))
rank.sort()

angry = 0
for i in range(n):
    if rank[i] != i+1:
        angry += abs((i+1 - rank[i]))

print(angry)      