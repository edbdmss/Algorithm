import sys
import math
input = sys.stdin.readline

t = int(input())

def fac(x):
    return math.factorial(x)
        
for _ in range(t):
    n, m = map(int, input().split())
    if n == 1:
        print(m)
    else:
        print(fac(m) // (fac(n) * fac(m-n)))