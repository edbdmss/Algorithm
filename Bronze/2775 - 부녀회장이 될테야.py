import sys
input = sys.stdin.readline

'''T = int(input())
for _ in range(T):
    dp = [0] * 15
    k = int(input())
    n = int(input())
    dp[0] = n
    
    for i in range(1, 15):
        if i > 1:
            dp[i] = (n-1)*(k-i) + (n-2)*(k)
        else:
            dp[i] = dp[i-1] + i + i+1
    print(dp[k])
    '''
    
