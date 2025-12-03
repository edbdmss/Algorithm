# 집합 자료형 활용
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hear = set()
for i in range(N):
    hear.add(input().rstrip())

see = set()
for i in range(M):
    see.add(input().rstrip())

result = sorted(list(see&hear))
print(len(result))
for j in result:
    print(j)