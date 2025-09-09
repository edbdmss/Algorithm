import sys
input = sys.stdin.readline

n = int(input())
city = sorted(list(map(int, input().split())))
max_budget = int(input())

start = 0
end = city[n-1]

ans = 0
while (start <= end):
    budget = 0
    mid = (start+end)//2
    
    for i in city:
        if mid > i:
            budget += i
        else:
            budget += mid
    
    if budget <= max_budget:
        start = mid+1
        ans = max(ans, mid)   
    else:
        end = mid-1
    
print(ans)