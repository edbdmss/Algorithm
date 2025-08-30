s = int(input())
n = 1

while True:
    if (n*n + n <= 2*s):
        n+=1
    else:
        break     
print(n-1)