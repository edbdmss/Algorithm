import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

arr = [0] * (n+1)
for i in range(1, n+1):
    arr[i] = num[i-1] + arr[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i-1])
    