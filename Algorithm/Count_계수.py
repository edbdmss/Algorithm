# 특정한 조건을 만족하는 경우에만 사용 가능, 
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만
# 계수정렬은 직접 데이터의 값을 비교한 후 위치를 변경하는 정렬방식이 아님.
# 일반적으로 별도의 리스트를 선언해서 그 안에 정렬에 대한 정보를 담는다는 특징이 있다.


array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")