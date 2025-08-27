import sys
input = sys.stdin.readline

n = int(input())
bag = []
for _ in range(n):
    w,v = map(int, input().split())
    bag.append((w,v))
    
