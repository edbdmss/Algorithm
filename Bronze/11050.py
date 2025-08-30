n, k = map(int, input().split())
m = 1
mm = 1
for i in range(k):
    m *= (n-i)
for i in range(1,k+1):
    mm *= (i)
    
print(m//mm)



'''
import math
n, k = map(int, input().split())
print(math.comb(n,k))
'''