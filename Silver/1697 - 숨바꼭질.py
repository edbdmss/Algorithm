import sys
input = sys.stdin.readline

n, k = map(int, input().split())
time = 0

while True:
    if n==k: break
    
    if k > n and k%2==0:
        k//=2
        time+=1
    else:
        if k > n: k -= 1
        else: k += 1
        time+=1

print(time)