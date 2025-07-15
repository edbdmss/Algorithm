import sys

a,b,v = map(int, sys.stdin.readline().split())
day = 0
while True:
    v -= a
    day += 1
    if v == 0:
        break
    v += b
    
    
print(day)