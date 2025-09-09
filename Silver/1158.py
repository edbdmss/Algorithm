# 1. deque 사용

import sys
from collections import deque
input = sys.stdin.readline

def yose(n, k):
    
    queue = deque()
    for i in range(1, n+1):
        queue.append(i)
    result = []
    
    while (queue):
        for i in range(k-1):
            q = queue.popleft()
            queue.append(q)
        result.append(queue.popleft())
        
    return result
               
n, k = map(int, input().split())
y = yose(n,k)
print("<" + ", ".join(map(str, y)) + ">")