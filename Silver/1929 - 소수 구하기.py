import sys
import math
input = sys.stdin.readline

M, N = map(int, input().split())
num = [True] * (N+1)
num[0] = num[1] = False

for i in range(2, int(math.sqrt(N)+1)):
    if num[i]:
        for j in range(i*i, N+1, i):
            num[j] = False

for i in range(M, N+1):
    if num[i]:
        print(i) 