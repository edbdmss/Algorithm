import sys

s = sys.stdin.readline().strip()

num1 = 0
num0 = 0
if s[0] == '0':
    num0 += 1
else:
    num1 += 1
    
for i in range(1, len(s)):
      
    if s[i] != s[i-1]:
        if s[i] == '0':
            num0 += 1
        else:
            num1 += 1
    else:
        continue

if num0 < num1:
    print(num0)
else:
    print(num1)
    
    
    
    ## 로직(알고리즘)도 맞고, 테스트케이스도 전부 정답이 나오지만 이상하게 틀렸다고 나왔던 문제, 구현이 미숙했던 문제 
    ## 왜 그리디 일까?
    