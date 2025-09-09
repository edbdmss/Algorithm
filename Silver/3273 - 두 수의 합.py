import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
x = int(input())

num.sort(reverse=True)
ct = 0
start, end = 0, n-1

while (start < end):
    
    ans = num[start] + num[end]
    if ans == x:
        ct += 1
        start += 1
        end -= 1
    elif ans < x: end -= 1
    else: start += 1
    
print(ct)