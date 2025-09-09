N = list(map(int, input()))
N.sort(reverse=True)
n = ''.join(map(str,N))
print(n)



''' join 메서드 → 리스트의 요소를 구분자로 연결해 하나의 문자열로 만듦.
    join은 문자열 리스트에만 사용 가능하므로, int형일 경우 map(str, ...)로 먼저 변경해야함.
'''