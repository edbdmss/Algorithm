import sys
input = sys.stdin.readline

A, B = map(int, input().split())

count = 1
while True:
    if B < A:
        count = -1
        break
    elif A == B:
        break
    
    if str(B)[-1] == '1':
        B -= 1
        B //= 10 
    elif B%2 != 0:
        count = -1
        break     
    else:
        B //= 2
    
    count += 1

print(count)