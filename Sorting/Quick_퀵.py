# 기준 데이터를 설정하고 큰 수와 작은 수를 교환한 후 리스트를 반으로 나눈다.
''' 
왼쪽은 pivot보다 큰 데이터, 오른쪽은 pivot보다 작은 데이터를 선택
엇갈렸으면 pivot과 작은데이터(right)를 교환
엇갈리지 않았으면 left와 right 교환.
''' 
# 분할 정복이기 때문에 속도가 빠른것. 일반적인 시간복잡도는 O(NlogN). 그러나 최악의 경우 O(n²)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
