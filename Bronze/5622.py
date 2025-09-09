num = list(input())
time = 0
dial = [
    [], [], [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M','N', 'O'],
    ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']
] 

for i in num:
    for j in dial:
        if i in j:
            time += dial.index(j)
print(time)