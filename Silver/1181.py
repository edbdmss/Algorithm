n = int(input())
word = []
for i in range(n):
    word.append(input())
    
word = list(set(word))
word.sort()
word.sort(key=lambda x: len(x), )
for i in word:
    print(i)