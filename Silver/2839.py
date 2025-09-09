import sys
input = sys.stdin.readline

n = int(input())
num = []
for i in range(1,n):
    if 5*i <= n:
        num.append(n-(5*i))
    
if n < 3 or n==4:
    print(-1)
    exit()

result = -1
for i in num:
    if i%3==0:
        five_index = num.index(i) + 1
        three_index = i//3
        result = five_index+three_index
if result == -1 and n%3==0:
    result = n//3
                        
print(result)