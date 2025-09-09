import sys
input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n):
    x, y = map(int, input().split())
    room.append((x, y))

room.sort(key=lambda x: (x[1], x[0]))

ct = 1
start = 0
for i in range(1, n):
    if room[start][1] <= room[i][0]:
        ct += 1
        start = i
print(ct)