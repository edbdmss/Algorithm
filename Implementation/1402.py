'''import sys

T = int(sys.stdin.readline())
for i in range(T):
    num = []
    ans = []
    a, b = map(int, sys.stdin.readline().split())
    for j in range(1,a+1):
        if a%j == 0:
            num.append(j)
    l = len(num)
    
    for k in range(l):
        if (num[k] + num[l-k-1] == b):
           ans.append(1)
        else:
            ans.append(0)
    if 1 in ans:
        print("yes")
    else:
        print("no")   
      '''
      

# 19532.py  (zerodivisionerror)
a, b, c, d, e, f = map(int, input().split())
if a != 0 and d !=0 and (b-2) != 0:
    b1 = b
    c1 = c
    b//=a
    c//=a   
    e//=d
    f//=d
    y= (c-f)//(b-e)
    x= (c1 - b1*y)//a
    print(x, y)
else:
    exit
