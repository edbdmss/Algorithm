import sys
input = sys.stdin.readline

n = int(input())   #사람의 수
seat = list(input().rstrip())

ll = seat.count('L') // 2
holder = n+1 - ll

if holder==n:
    print(holder)
else:
    print(min(holder, n))