'''import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    dp = [0] * 100001
    for l in range(2):
        sticker.append(list(map(int, input().split())))
    
    dp[0] = sticker[0] 
    for i in range(1, n):
        dp[i] = max(sticker[i-1][i], sticker[i][i-1], sticker[i][i])
        if dp[i] == sticker[i][i-1]:
            dp[i-1] = sticker[i][i-1]
    
    print(sum(dp))'''   