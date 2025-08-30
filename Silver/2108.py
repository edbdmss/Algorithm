import sys
import statistics

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()


    
print(round(sum(num)/n))  # 산술평균
print(num[(n-1)//2])    # 중앙값
print()   # 최빈값
print(num[n-1]-num[0])   # 범위
