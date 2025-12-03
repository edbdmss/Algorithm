 # 코딩테스트의 이진탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는 문제가 많다. 
 # 따라서 탐색범위가 2000만을 넘어가면 이진 탐색으로 문제에 접근한다.
 
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않음")
else:
    print(result-1)
    