import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
total = road[0] * price[0]

min_price = price[0]
for i in range(1, n):
    min_price = min(min_price, price[i])
    total += (min_price * road[i])

print(total)