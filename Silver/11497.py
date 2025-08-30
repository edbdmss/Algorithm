# 1
import sys
input = sys.stdin.readline

t = int(input())

def make_list(wood):
    
    left.append(wood[0])
    right.append(wood[1])
    del wood[0:2]
    
    x=0
    y=0
    for i in wood:
        if i-left[x] <= i-right[y]:
            right.append(i)
            y+=1
        else:
            left.append(i)
            x+=1
    right.sort(reverse=True) 
    
    left_plus_right = left+right
    return left_plus_right


while (t > 0):
    t -= 1
    
    left = []
    right = []
    
    n = int(input())
    wood = list(map(int, input().split()))
    wood.sort()
    
    left_plus_right = make_list(wood)
    
    difference = []
    for i in range(n-1):
        difference.append(abs(left_plus_right[i+1] - left_plus_right[i]))
    print(max(difference))
    wood.clear()
    
    
    
# 2
T = int(input())

for _ in range(T):
    N = int(input())
    height = sorted(list(map(int, input().split())))
    
    x = 0
    
    for i in range(2, N):
        x = max(x, abs(height[i] - height[i-2]))
    
    print(x)