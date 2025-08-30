import sys
input = sys.stdin.readline

x = int(input())
dp = [0] * (x+1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1     # 조건 분기가 필요 없음. 그리디가 아님에 주의.
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[x])