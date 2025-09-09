# 탑다운
import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 100

dp[1] = 1
dp[2] = 2
dp[3] = 4

def DP(n):
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = DP(n-1) + DP(n-2) + DP(n-3)
        return dp[n]

for _ in range(T):
    n = int(input())
    print(DP(n))
    
    
    
    
# 바텀업
import sys
input = sys.stdin.readline

T = int(input())
dp = [0] * 100
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(T):
    n = int(input())
    
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])