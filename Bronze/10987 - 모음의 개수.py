import sys
input = sys.stdin.readline

m = ['a', 'e', 'i', 'o', 'u']
x = input()
ct = 0

for i in x:
    if i in m: ct += 1
        
print(ct)