import sys
input = sys.stdin.readline

N = int(input())
room = []
for _ in range(N):
    x, y = map(int, input().split())
    room.append((x,y))

room.sort(key=lambda x: (x[1], x[0]))

check = [0] * N
count = 0
start = 0

for start in range(N):
    if check[start] != 1: 
        count += 1
        for i in range(1, N):
            if room[start][1] <= room[i][0] and check[i] == 0:
                start = i
                check[i] = 1
            else:
                continue
print(count)