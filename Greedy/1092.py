'''import sys
input = sys.stdin.readline

n = int(input())
weight = sorted(list(map(int, input().split())))
m = int(input())
box = sorted(list(map(int, input().split())))


def binarySearch(i, start, end):
    
    while (start <= end):
        mid = (start+end)//2
        
        if i >= box[mid]:
            start = mid+1
        else:
            end = mid-1
    return mid


count = 0
for i in weight:
    index = binarySearch(i, 0, m)
    box.remove(box[index])
    m -= 1
count+=1

print(count)'''



import sys
import bisect
input = sys.stdin.readline

n = int(input())
weight = sorted(list(map(int, input().split())))
m = int(input())
box = sorted(list(map(int, input().split())))


if weight[-1] < box[-1]:
    print(-1)
    exit()
    
count = 0
while(box):
    for i in weight:
        if not box:
            break
        index = bisect.bisect_right(box, i, lo=0, hi=len(box)) - 1
        if index >= 0:
            box.pop(index)
    count+=1

print(count)