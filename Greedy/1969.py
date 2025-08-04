import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
dna = []
hamming_distance = 0
hamming_sentence = []

for _ in range(n):
    dna.append(input().rstrip())

for i in zip(*dna):
    print(i)
    print(Counter(i), end='')