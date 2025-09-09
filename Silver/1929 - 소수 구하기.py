import sys
import math
input = sys.stdin.readline

M, N = map(int, input().split())
num = [j for j in range(M, N+1)]

for j in range(N-M+1):
    r = True
    for i in range(2, int(math.sqrt(N))+1):
        if num[j] % i == 0 and num[j] != i :
            r = False
            continue
        if num[j] == 1:
            r = False
    if r:
        print(num[j])