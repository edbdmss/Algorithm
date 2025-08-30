# 삽입 정렬은 두번째 데이터부터 시작한다. -> 첫번째 데이터는 그 자체로 정렬되어 있다고 판단하므로
# 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추게 된다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:           # 현재 위치보다 그 왼쪽 원소가 더 크면
            array[j], array[j-1] = array[j-1], array[j]         # 자리 바꾸기
        else:
            break
print(array)