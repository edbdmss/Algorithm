import sys
input = sys.stdin.readline

k = int(input())
num = []

for _ in range(k):
    x = int(input())
    if x==0:
        num.pop()
    else:
        num.append(x)
print(sum(num))