import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())
day1= (V-B) / (A-B)
day2 = (B+V) / (A-B)
print(min(math.ceil(day1), math.ceil(day2)))    