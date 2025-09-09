# 이분 탐색 직접 구현 
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
temp = []

def LIS(a):
    for i in a:
        if not temp or temp[-1] < i:
            temp.append(i)
        elif temp[-1] >= i:
            x = bisect(temp, i, 0, len(temp))    # temp배열과 i를 전달하여 위치 x반환
            temp[x] = i
    return len(temp)

def bisect(temp, i, start, end):
    while (start < end):
        mid = (start+end)//2
        if i > temp[mid]:
            start = mid+1
        else:
            end = mid    # 배열에 i가 없더라도 i가 들어갈 정확한 위치를 반환해야함.
    return start

print(LIS(a))
