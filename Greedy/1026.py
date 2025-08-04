import sys

input = sys.stdin.readline

s = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bb = []

a.sort()
bb = sorted(b, reverse=True)
sum = 0

for i in range(s):
    sum += (a[i] * bb[i])

print(sum)