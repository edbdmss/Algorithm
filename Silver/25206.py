import sys
input = sys.stdin.readline

subject_list = []
subject_ct = 0
n = -1
for _ in range(20):
    
    x, y, z = input().split()
    
    if z == 'P':
        continue
    
    elif z == 'A+':
        n = 4.5
    elif z == 'A0':
        n = 4.0
    elif z == 'B+':
        n = 3.5    
    elif z == 'B0':
        n = 3.0
    elif z == 'C+':
        n = 2.5
    elif z == 'C0':
        n = 2.0        
    elif z == 'D+':
        n = 1.5
    elif z == 'D0':
        n = 1.0
    else:
        n = 0
        
    subject_ct += float(y)
    if n != -1:
        subject_list.append(float(y)*n)

print(sum(subject_list) / subject_ct)