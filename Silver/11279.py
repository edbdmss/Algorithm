import heapq
import sys
input = sys.stdin.readline

priority_queue = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if priority_queue:
            print(abs(heapq.heappop(priority_queue)))
        else:
            print("0")
    else:
        heapq.heappush(priority_queue, -x)