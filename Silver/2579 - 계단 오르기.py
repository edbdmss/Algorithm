import sys
input = sys.stdin.readline

T = int(input())

stairs = []
for _ in range(T):
    stairs.append(int(input()))

stairs.reverse()
dp = []

    
print(sum(dp))