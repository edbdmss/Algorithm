import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())

dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1] + a[i-1]

for _ in range(m):
    i, j = map(int, input().split()) 
    print(dp[j] - dp[i-1])