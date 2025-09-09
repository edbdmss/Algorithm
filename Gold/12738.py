# bisect 라이브러리로 구현
import sys
import bisect
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
temp = []

def lis(a):
    for i in a:
        if not temp or i > temp[-1]:
            temp.append(i)
        elif i <= temp[-1]:
            x = bisect.bisect_left(temp, i)
            temp[x] = i
    return len(temp)
    
print(lis(a))