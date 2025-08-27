'''import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

num = [str(i) for i in range(10, 1, -1)]
alpha = deque()

for _ in range(n):
    alpha.append(input().strip())
x = max(len(w) for w in alpha)   

alpha = ['@' * (x - len(w)) + w for w in alpha]

print(alpha)

for i in alpha:
    for j in i:
        if j '''
        
        
        
