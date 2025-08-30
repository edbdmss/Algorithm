# 파라메트릭 서치 유형은 이진 탐색을 재귀적으로 구현하지 않고 반복문을 이용해 구현한다.
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

# 시작점은 0, 끝점은 가장 긴 떡의 길이로.
start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for x in array:         # 각각의 떡 길이 x
        if x > mid:
            total += x-mid
    if total < m:
        end = mid-1         # 끝점을 중간점-1로
    else:
        result=mid
        start = mid+1
print(result)