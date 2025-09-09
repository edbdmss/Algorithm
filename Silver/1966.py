'''import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    n, m = map(int, input().split())
    docs = []
    p =list(map(int, input().split()))
    for i in range(1, n+1):
        heapq.heappush(docs, (-p[i-1], i))       # (우선순위, 데이터값) 구조
    
    ct = 1
    for i in range(m-1):
        heapq.heappop(docs)
        ct += 1
    print(ct)'''
    
    
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    queue = deque(map(int, input().split()))
    stack = []
    
    while (queue):
        index = max(queue)

        stack.append(index)
    
            
        
    
    
