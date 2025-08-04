import sys
input = sys.stdin.readline

n = input().strip().split('-')
first = sum(map(int, n[0].split('+')))
rest = sum(sum(map(int, i.split('+'))) for i in n[1:])

print(first-rest)