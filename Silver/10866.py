from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

n = int(input())
for i in range(n):
    order = input().rstrip().split()
    o = order[0]
    if o == 'push_front':
        queue.appendleft(order[1])
    elif o == 'push_back':
        queue.append(order[1]) 
    elif o == 'pop_front':
        if queue:
            x = queue.popleft()
            print(x)
        else:
            print(-1)
    elif o == 'pop_back':
        if queue:
            x = queue.pop()
            print(x)
        else:
            print(-1)
    elif o == 'size':
        print(len(queue))
    elif o == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif o == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif o == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)