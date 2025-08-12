'''import sys
input = sys.stdin.readline

def search(num, x, count, start, end):
    if start > end:
        return count
    mid = (start+end)//2
    
    if num[mid] == x:
        count += 1
        if num[mid] > num[mid-1]:
            return search(num, x, count, mid+1, end)
        else:
            return search(num, x, count, start, mid-1)
    elif num[mid] > x:
        return search(num, x, count, start, mid-1)
    else:
        return search(num, x, count, mid+1, end)        
    
    
n = int(input())
num = list(map(int, input().split()))
num.sort()

m = int(input())
target = list(map(int, input().split()))

for i in target:
    print(search(num, i, 0, 0, n-1), end=" ")'''
    
