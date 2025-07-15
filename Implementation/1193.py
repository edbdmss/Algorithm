x = int(input())
temp = x
num = [i for i in range(1,x+1)]

for i in num:
    temp -= i
    if temp < 0 or temp == 0:
        temp += i
        break

num2 = []
if x%2 == 0:
    for i in range(1,temp+1):
        a = i
        b = temp-i+1
        num2.append((a,'/',b))
else:
    for i in range(1,temp+1):
        a = temp-i+1
        b = i
        num2.append((a,b))
        
r = list(num2[temp-1])
print(*r)