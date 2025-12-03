def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)   #end를 mid-1로 변경해서 재귀 호출
    else:
        return binary_search(array, target, mid+1, end)     #start를 mid+1로 변경해서 재귀 호출
    

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)     
if result == None:
    print("존재하지 않는 원소")
else:
    print(result+1)             # 인덱스 출력 (mid)